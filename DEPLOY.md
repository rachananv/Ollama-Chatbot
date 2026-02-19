# Cloud Deployment Guide - Render

Follow these steps to deploy your chatbot permanently to the cloud (both mobile & desktop):

## Step 1: Get Groq API Key (Free)

1. Go to https://console.groq.com/
2. Sign up for free
3. Create an API key
4. Copy it (you'll need it in Step 3)

## Step 2: Push to GitHub

```powershell
cd "c:\Users\USER\OneDrive\New folder\ollama"
git add .
git commit -m "Prepare for cloud deployment with Groq API"
git push origin main
```

## Step 3: Deploy to Render (Free)

1. Go to https://render.com/
2. Sign up and connect your GitHub account
3. Click "New +" → "Web Service"
4. Select your `Ollama-Chatbot` repository
5. Fill in settings:
   - **Name**: ollama-chatbot
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python web_chatbot_cloud.py`
   - **Instance Type**: Free (you can upgrade later)

6. Click "Advanced" and add Environment Variable:
   - **Key**: `GROQ_API_KEY`
   - **Value**: (paste your Groq API key from Step 1)

7. Click "Create Web Service"
8. Wait 2-3 minutes for deployment
9. Render will give you a URL like: `https://ollama-chatbot.onrender.com`

## Step 4: Update GitHub Pages

Once deployed, the Render URL will be permanent. I'll update your `index.html` to redirect to the Render deployment URL.

Just provide the Render URL from Step 3, and I'll push the update!

---

## Alternative: Deploy to Railway (Also Free)

If Render doesn't work:
1. Go to https://railway.app/
2. Connect GitHub, import repo
3. Add `GROQ_API_KEY` environment variable
4. Deploy
5. Get the public URL

---

**Benefits of this approach:**
- ✅ No local server needed
- ✅ Works on mobile & desktop
- ✅ Permanent public URL
- ✅ Free tier available
- ✅ Always online

**Duration:** Render free tier is fine for personal use. If you need production, upgrade to paid plan.
