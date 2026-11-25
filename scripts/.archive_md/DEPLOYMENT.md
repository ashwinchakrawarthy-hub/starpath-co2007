# Free Cloud Deployment & Access Guide for STARPath

This guide provides step-by-step instructions for deploying and accessing **STARPath** on **100% free cloud hosting services** without requiring credit card details or recurring fees.

---

## Deployment Options Summary

| Platform | Your Free Clean Address | Cost | Credit Card Needed? | Setup Time |
|---|---|---|---|---|
| **1. Vercel Cloud (User Choice)** | **`https://starpath-uclan.vercel.app`** | **100% Free** | **No** | 2 minutes |
| **2. Hugging Face Spaces** | `https://starpath.hf.space` | **100% Free** | **No** | 3 minutes |
| **3. Render (Free Web Service)** | `https://starpath-uclan.onrender.com` | **100% Free** | **No** | 4 minutes |
| **4. Localhost / Campus Lab PC** | `http://127.0.0.1:8000` | **Free** | **No** | 10 seconds |

---

## Option 1: Vercel Cloud (Fastest & Cleanest — `*.vercel.app`)

Vercel provides blazing-fast serverless cloud hosting for FastAPI applications with clean addresses like `https://starpath-uclan.vercel.app`.

### Pre-Configured Files in This Repository:
- **`vercel.json`**: Root configuration routing all traffic (`/(.*)`) to the serverless function.
- **`api/index.py`**: Serverless ASGI entry point exposing FastAPI `app`.
- **`requirements.txt`**: Standard dependencies automatically installed during Vercel builds.

### Step-by-Step Instructions:

#### Method A: Deploy via GitHub (Recommended — 2 Minutes):
1. **Push this folder to a GitHub repository:**
   - Create a free GitHub repository named `starpath-uclan` (or `starpath`).
   - Push your code to GitHub (or drag-and-drop the files on github.com).
2. **Log into Vercel:**
   - Go to [https://vercel.com/signup](https://vercel.com/signup) and click **Continue with GitHub** (no credit card required).
3. **Import the Project:**
   - On the Vercel dashboard, click **Add New... $\rightarrow$ Project**.
   - Find your `starpath-uclan` repository and click **Import**.
   - Project Name: `starpath-uclan` (this determines your URL: `starpath-uclan.vercel.app`).
   - Framework Preset: Leave as **Other**.
   - Root Directory: `./` (default).
4. **Environment Variables (Optional):**
   - If you have a free Google Gemini key from [Google AI Studio](https://aistudio.google.com/), add:
     - `LLM_PROVIDER`: `gemini`
     - `GEMINI_API_KEY`: *(your key)*
   - *(If omitted, STARPath automatically runs in the built-in offline grounded mode with zero API keys!)*
5. **Click Deploy:**
   - Within 60 seconds, your site is live with a permanent address:  
     **`https://starpath-uclan.vercel.app`** (or your chosen name)!

#### Method B: Deploy from Terminal (Using Vercel CLI):
1. Open PowerShell in `c:\Users\ELCOT\Desktop\AGILE- Project`.
2. Run:
   ```powershell
   npx vercel
   ```
3. Follow the 4 interactive prompts:
   - *Set up and deploy?* Type `y` and press Enter.
   - *Which scope?* Press Enter (your personal account).
   - *Link to existing project?* Type `n` and press Enter.
   - *What’s your project’s name?* Type `starpath-uclan` and press Enter.
   - *In which directory is your code located?* Press Enter (`./`).
4. Vercel builds and outputs your live production URL: **`https://starpath-uclan.vercel.app`**.

---

## Option 1: Hugging Face Spaces (Recommended — Easiest & 100% Free)

Hugging Face Spaces allows you to host Python Docker applications for free with a permanent public web link.

### Step-by-Step Instructions:
1. **Create a Free Account:** Sign up at [https://huggingface.co/join](https://huggingface.co/join) (no credit card required).
2. **Create a New Space:**
   - Go to [https://huggingface.co/new-space](https://huggingface.co/new-space).
   - Enter Space Name: `starpath-assistant` (or your preferred name).
   - License: Select **MIT** or **Apache 2.0**.
   - Space SDK: Select **Docker** -> **Blank**.
   - Space Hardware: Select **CPU Basic · 2 vCPU · 16 GB · Free**.
   - Visibility: **Public**.
   - Click **Create Space**.
3. **Upload the STARPath Code:**
   - On your Space page, click the **Files** tab -> **Add file** -> **Upload files**.
   - Drag and drop all files from this folder (`app/`, `data/`, `docs/`, `scripts/`, `tests/`, `Dockerfile`, `requirements.txt`, `README.md`).
   - Click **Commit changes to main**.
4. **(Optional) Add Free Google Gemini API Key:**
   - In your Space, click **Settings** -> **Variables and secrets**.
   - Under **Secrets**, click **New secret**:
     - Key: `GEMINI_API_KEY`
     - Value: *(Paste your free key from [Google AI Studio](https://aistudio.google.com/))*
   - Under **Variables**, click **New variable**:
     - Key: `LLM_PROVIDER`
     - Value: `gemini`
   *(If you omit this, STARPath runs in the built-in `offline` mode automatically with zero keys!)*
5. **Access Your Live Assistant:**
   - Within 2 minutes, the container builds and your app will be live at:
     `https://<your-username>-starpath-assistant.hf.space`

---

## Option 2: Render Free Web Service

Render offers free web application hosting directly from a GitHub repository.

### Step-by-Step Instructions:
1. **Push your code to a GitHub repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial STARPath commit"
   git remote add origin https://github.com/<your-username>/starpath-uclan.git
   git push -u origin main
   ```
2. **Sign up on Render:** Visit [https://render.com/](https://render.com/) and sign in with GitHub.
3. **Create Web Service:**
   - Click **New +** -> **Web Service**.
   - Select your `starpath-uclan` repository.
   - Name: `starpath-uclan`.
   - Environment: **Python 3**.
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Plan: Select **Free**.
4. **Environment Variables:**
   - Under the **Environment Variables** tab, you can optionally add:
     - `LLM_PROVIDER`: `gemini` (or `offline`)
     - `GEMINI_API_KEY`: *(your free key)*
5. **Deploy:** Click **Deploy Web Service**. Your public URL will be `https://starpath-uclan.onrender.com`.

---

## Option 3: Instant Free Cloud URL via Cloudflare Tunnel (Quick Sharing)

If you have the server running locally on your computer and want to immediately test it on your mobile phone or share it with team members in your lab session:

1. **Start the local server:**
   Double-click `run_local.bat` (or run `python -m uvicorn app.main:app --port 8000`).
2. **Open a second terminal and run Cloudflare's free quick tunnel:**
   ```powershell
   winget install Cloudflare.cloudflared
   cloudflared tunnel --url http://127.0.0.1:8000
   ```
3. Cloudflare will output an instant, secure public HTTPS URL (e.g., `https://random-words.trycloudflare.com`). Anyone can open this link on their phone or tablet to use the assistant!

---

## Option 4: Local Execution (For Campus Network Demonstration)

As required by the assignment brief, your implementation must run reliably on the University network:

1. Double-click `run_local.bat` in this folder.
2. The script starts the FastAPI server and automatically opens your web browser to:
   **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
3. No internet connection or API keys are required when running in default `offline` mode!
