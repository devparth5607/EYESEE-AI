import json, sqlite3, webbrowser, os
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8788"))
DB = ROOT / 'data' / 'eyesee.db'
INDEX = ROOT / 'index.html'
DB.parent.mkdir(exist_ok=True)

def init_db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    c.execute('''CREATE TABLE IF NOT EXISTS patients(
      id TEXT PRIMARY KEY,name TEXT NOT NULL,age TEXT,gender TEXT,phone TEXT,diabetesStatus TEXT,diabetes TEXT,
      village TEXT,phc TEXT,district TEXT,state TEXT,pin TEXT,landmark TEXT,lat TEXT,lng TEXT,accuracy TEXT,notes TEXT,createdAt TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS screenings(
      id INTEGER PRIMARY KEY AUTOINCREMENT,patient_id TEXT,grade TEXT,confidence TEXT,referral TEXT,explainability TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS referrals(
      id INTEGER PRIMARY KEY AUTOINCREMENT,patient_id TEXT,grade TEXT,status TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    c.commit(); c.close()

def send_json(h, obj, status=200):
    raw=json.dumps(obj,ensure_ascii=False).encode('utf-8')
    h.send_response(status); h.send_header('Content-Type','application/json; charset=utf-8'); h.send_header('Cache-Control','no-store'); h.send_header('Content-Length',str(len(raw))); h.end_headers(); h.wfile.write(raw)

def read_json(h):
    n=int(h.headers.get('Content-Length','0') or 0)
    raw=h.rfile.read(n) if n else b'{}'
    return json.loads(raw.decode('utf-8') or '{}')

class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args): print(fmt % args)
    def do_GET(self):
        p=urlparse(self.path).path
        q=parse_qs(urlparse(self.path).query)
        if p=='/api/health': return send_json(self, {'ok':True,'backend':'Python','database':'SQLite','port':PORT})
        c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
        try:
            if p=='/api/patients':
                rows=[dict(r) for r in c.execute('SELECT * FROM patients ORDER BY rowid DESC')]
                return send_json(self, {'patients':rows})
            if p=='/api/screenings':
                pid=q.get('patient_id',[None])[0]
                if pid: rows=[dict(r) for r in c.execute('SELECT * FROM screenings WHERE patient_id=? ORDER BY id DESC',(pid,))]
                else: rows=[dict(r) for r in c.execute('SELECT * FROM screenings ORDER BY id DESC')]
                return send_json(self, {'screenings':rows})
            if p=='/api/referrals':
                rows=[dict(r) for r in c.execute('SELECT * FROM referrals ORDER BY id DESC')]
                return send_json(self, {'referrals':rows})
            if p=='/api/dashboard':
                patients=c.execute('SELECT COUNT(*) n FROM patients').fetchone()['n']
                screenings=c.execute('SELECT COUNT(*) n FROM screenings').fetchone()['n']
                referrals=c.execute('SELECT COUNT(*) n FROM referrals').fetchone()['n']
                return send_json(self, {'patients':patients,'screenings':screenings,'referrals':referrals})
            if p=='/api/analytics':
                return send_json(self, {'patients':c.execute('SELECT COUNT(*) n FROM patients').fetchone()['n'],'screenings':c.execute('SELECT COUNT(*) n FROM screenings').fetchone()['n'],'referrals':c.execute('SELECT COUNT(*) n FROM referrals').fetchone()['n']})
        finally: c.close()
        # Any non-API path serves the SPA. This fixes 404s from old filename URLs too.
        if p.startswith('/api/'):
            return send_json(self, {'error':'Not found'}, 404)
        if INDEX.exists():
            raw=INDEX.read_bytes(); self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.send_header('Cache-Control','no-store'); self.send_header('Content-Length',str(len(raw))); self.end_headers(); self.wfile.write(raw); return
        self.send_error(500,'index.html missing')
    def do_POST(self):
        p=urlparse(self.path).path; data=read_json(self); c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
        try:
            if p=='/api/patients':
                fields=['id','name','age','gender','phone','diabetesStatus','diabetes','village','phc','district','state','pin','landmark','lat','lng','accuracy','notes','createdAt']
                vals=[data.get(k,'') for k in fields]
                sets=','.join(f'{k}=excluded.{k}' for k in fields[1:])
                c.execute(f"INSERT INTO patients ({','.join(fields)}) VALUES ({','.join(['?']*len(fields))}) ON CONFLICT(id) DO UPDATE SET {sets}", vals)
                c.commit(); return send_json(self, {'ok':True,'patient':data})
            if p=='/api/screenings':
                c.execute('INSERT INTO screenings(patient_id,grade,confidence,referral,explainability) VALUES(?,?,?,?,?)',(data.get('patient_id',''),data.get('grade',''),data.get('confidence',''),data.get('referral',''),data.get('explainability','')))
                c.commit(); return send_json(self, {'ok':True})
            if p=='/api/referrals':
                c.execute('INSERT INTO referrals(patient_id,grade,status) VALUES(?,?,?)',(data.get('patient_id',''),data.get('grade',''),data.get('status','Pending')))
                c.commit(); return send_json(self, {'ok':True})
        finally: c.close()
        return send_json(self, {'error':'Not found'}, 404)

if __name__=='__main__':
    init_db()
    server=ThreadingHTTPServer(('0.0.0.0',PORT),Handler)
    url=f'http://127.0.0.1:{PORT}/'
    print('EYESEE-AI running at',url,flush=True)
    # Only auto-open a browser for local desktop launches.
    if os.environ.get('PORT') is None:
        try: webbrowser.open(url)
        except Exception: pass
    server.serve_forever()
