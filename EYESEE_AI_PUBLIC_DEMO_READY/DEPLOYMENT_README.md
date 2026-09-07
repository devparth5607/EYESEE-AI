# EYESEE-AI Public Demo Deployment

Recommended host: Render Web Service.

1. Put this folder in a GitHub repository.
2. In Render, create a **New Web Service** from that repository.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `python server.py`
5. Deploy. Render will provide a public URL such as `https://eyesee-ai.onrender.com`.
6. Paste that URL into the PPT as **Live Demo**.

The app uses SQLite for the prototype database. On free/ephemeral hosting, local database data may reset when the service is redeployed/restarted.

The current AI grading logic is a prototype/demo safeguard, not a clinically validated diagnostic model.
