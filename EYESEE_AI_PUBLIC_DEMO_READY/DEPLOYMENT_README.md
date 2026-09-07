EYESEE-AI

Explainable AI for Diabetic Retinopathy Screening in Rural India

EYESEE-AI is an explainable AI-based diabetic retinopathy screening platform designed to make early eye screening more accessible in rural and low-connectivity healthcare settings.

The project combines retinal image analysis, explainability, patient management, referral support, multilingual interaction, and an offline-first workflow in a single platform.

💡 Project Overview

Diabetic Retinopathy (DR) can progress silently and may lead to vision loss when it is not detected early.

EYESEE-AI is designed to support frontline healthcare workers by providing a simple digital workflow:

Register Patient → Capture / Upload Retinal Image → Screen with AI → View Explanation → Generate Referral → Track History

The platform is intended to support screening and prioritization. It is not designed to replace ophthalmologists or professional medical diagnosis.

🎯 Objectives

Enable accessible retinal screening in rural areas

Provide an easy workflow for frontline healthcare workers

Add explainability instead of showing only an AI prediction

Support low-connectivity and offline-first usage

Simplify patient registration and screening history

Generate referral recommendations for cases needing further evaluation

Support multiple Indian languages and voice interaction

Create a foundation for lightweight mobile and edge deployment

🔄 End-to-End Workflow

Patient Registration
        ↓
Retinal Image Capture / Upload
        ↓
Image Quality Check & Preprocessing
        ↓
AI-Based DR Screening
        ↓
Grad-CAM Explainability
        ↓
Screening Result
        ↓
Referral Recommendation
        ↓
Patient History & Follow-up

🧠 Explainable AI

A core feature of EYESEE-AI is explainability.

Instead of presenting only a severity prediction, the system uses Grad-CAM to generate a visual heatmap showing retinal regions associated with the model's decision.

This is intended to improve:

Transparency

Interpretability

User trust

Understanding of AI-assisted screening results

⚙️ Technical Approach

1. Image Acquisition

The platform supports retinal image capture/upload as the starting point of the screening workflow.

2. Image Preprocessing

The proposed preprocessing pipeline includes:

Image quality assessment

Noise reduction

Contrast enhancement using CLAHE

Resizing and normalization

3. AI Classification

The project uses a CNN / transfer-learning approach based on EfficientNet-B0 for diabetic retinopathy severity grading.

The target grading categories are:

No DR

Mild NPDR

Moderate NPDR

Severe NPDR

Proliferative DR

4. Explainability

Grad-CAM is used to generate the visual explanation associated with the model output.

5. Screening & Referral

The platform records screening results and supports referral recommendations and follow-up history.

⭐ Key USP

Explainable AI

Shows why a case is flagged through a Grad-CAM visualization.

Offline-First

Designed for environments with limited or intermittent internet connectivity.

Multilingual Support

Designed to support multiple Indian languages with voice interaction.

Rural-Focused Design

The workflow is intended to be simple and practical for frontline healthcare workers.

End-to-End Workflow

Covers patient registration, screening, explanation, referral and history in one platform.

Lightweight / Edge-Ready

The architecture considers deployment on resource-constrained devices using lightweight inference technologies.

🏥 Rural Healthcare Workflow

A typical use case can be:

Frontline Healthcare Worker

→ Register patient
→ Capture retinal image
→ Run screening
→ View result + Grad-CAM
→ Identify cases needing attention
→ Generate referral
→ Maintain digital history

This brings an initial screening workflow closer to the patient.


📊 Expected Impact

EYESEE-AI is designed to help:

Increase access to early diabetic retinopathy screening

Reduce dependence on specialist availability for initial screening

Prioritize potentially high-risk cases for specialist evaluation

Improve transparency of AI-assisted screening

Support healthcare workers in low-connectivity locations

Maintain digital screening and referral records

🌱 Accessibility & Sustainability

The platform is designed around lightweight digital workflows, offline-first operation, edge-friendly inference, and digital reporting.

This can help reduce unnecessary travel for initial screening, enable local processing where appropriate, and support efficient digital record keeping.

🔒 Responsible AI

EYESEE-AI is a screening and decision-support prototype, not a clinical diagnostic system.

AI outputs should be reviewed by qualified healthcare professionals before clinical decisions are made.

Before real-world medical deployment, the model and workflow would require appropriate clinical validation, representative datasets, performance evaluation, and regulatory/safety review.

🚀 Vision

Screen Early. See Clearly. Healthier Tomorrow.

EYESEE-AI aims to make diabetic retinopathy screening more accessible, explainable, practical, multilingual and rural-ready.
