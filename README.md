#  AI Study Planner

An intelligent, AI-powered study planner that generates personalized, concise study schedules based on your subjects, exam date, available study hours, and weak topics. Built with FastAPI, Groq AI, and modern web technologies with stunning Aceternity-style animations.

## ✨ Features

- **AI-Powered Planning** — Uses Groq's LLaMA model to generate smart, summarized study plans
- **Personalized Schedules** — Input subjects, exam date, daily study hours, and weak topics to get tailored recommendations
- **Concise Output** — Summarized study plans (10-15 lines max) with actionable insights, not long daily breakdowns
- **Beautiful UI** — Dark theme with glassmorphism, animated starfield background, smooth transitions
- **Responsive Design** — Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Generation** — Instant plan generation with loading indicators and error handling
- **Free & Fast** — Powered by free Groq API with no credits required

## 🚀 Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **AI API**: Groq (LLaMA-3.1-8B-Instant)
- **Environment**: Python 3.11+, Uvicorn

### Frontend
- **HTML5, CSS3, Vanilla JavaScript**
- **Canvas API** for animated starfield background
- **CSS Animations** for glassmorphism and smooth effects
- **Responsive Grid Layout**

## 📋 Prerequisites

- Python 3.11 or higher
- Node.js (optional, for frontend deployment)
- Groq API Key (free tier available at [groq.com](https://groq.com))
- Git

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-study-planner.git
cd ai-study-planner
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your Groq API key
echo GROQ_API_KEY=your_api_key_here > .env
```

Get your free Groq API key from [console.groq.com](https://console.groq.com)

### 3. Start the Backend Server

```bash
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at `http://localhost:8000`

### 4. Frontend Setup

Open `frontend/index.html` in your browser or serve it locally:

```bash
cd ../frontend

# Using Python's built-in server
python -m http.server 8001

# Or using Node.js
npx serve .
```

Frontend will be available at `http://localhost:8001` (or as shown in your local server output)

## 📖 Usage

### Step 1: Open the Application
Navigate to the frontend URL in your browser (e.g., `http://localhost:8001/index.html`)

### Step 2: Fill in Study Details
- **Subjects**: Enter subjects you need to study (e.g., "Math, Physics, Chemistry")
- **Exam Date**: Pick your exam date
- **Hours per Day**: How many hours per day can you study (1-24)
- **Weak Topics**: Specify topics you find difficult (e.g., "Integration, Thermodynamics")

### Step 3: Generate Plan
Click **"Generate Plan"** — the AI will create a personalized, concise study strategy in 10-15 seconds

### Step 4: Review Your Plan
The study plan will include:
- Key topics to focus on
- Daily study focus areas
- Time allocation per subject
- Special focus for weak topics
- Recommended revision strategy

## 📁 Project Structure

```
ai-study-planner/
├── backend/
│   ├── app.py                 # FastAPI application
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # Environment variables (Groq API key)
├── frontend/
│   └── index.html             # Single-page HTML application
└── README.md                  # This file
```

## 🌐 Deployment

### Deploy Backend to Render (Recommended)

1. Sign up at [render.com](https://render.com)
2. Create new **Web Service**
3. Connect your GitHub repository
4. Configure the service:
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `uvicorn backend.app:app --host 0.0.0.0 --port 8000`
5. Add Environment Variables:
   - **GROQ_API_KEY**: `gsk_your_api_key_here`
6. Click **Deploy**

Your backend will be available at `https://your-app-name.onrender.com`

### Deploy Frontend to Vercel (Recommended)

1. Push your repository to GitHub
2. Go to [vercel.com](https://vercel.com) and sign in with GitHub
3. Click **New Project** and import your repository
4. Configure the project:
   - Set **Root Directory** to `frontend/`
5. Add Environment Variables:
   - **VITE_API_URL**: `https://your-backend-url.onrender.com`
6. Click **Deploy**

Your frontend will be available at `https://your-project.vercel.app`

### Alternative: Deploy Backend to Fly.io

```bash
cd backend

# Install flyctl: https://fly.io/docs/getting-started/installing-flyctl/

# Login and create app
flyctl auth login
flyctl launch --name ai-study-planner-backend --region ord --no-deploy

# Set your Groq API key as a secret
flyctl secrets set GROQ_API_KEY=your_api_key_here

# Deploy
flyctl deploy
```

Your backend will be available at `https://ai-study-planner-backend.fly.dev`

## 🔑 Environment Variables

### Backend (.env file)
```
GROQ_API_KEY=gsk_your_api_key_here
```

Get your free API key from [Groq Console](https://console.groq.com)

## 🎨 Customization

### Change AI Model
Edit `backend/app.py` line 55:
```python
model="llama-3.1-8b-instant",  # Change to another Groq model
```

Available models:
- `llama-3.1-8b-instant` (default, fastest)
- `mixtral-8x7b-32768`
- `gemma-7b-it`

### Adjust Output Length
Edit `backend/app.py` line 60:
```python
max_tokens=1000,  # Increase for longer plans
```

### Customize Theme Colors
Edit `frontend/index.html` CSS variables (lines 210-250):
- Primary color: `#00d4ff` (cyan)
- Secondary color: `#0099ff` (blue)
- Background: `#0a0e1a` (dark)

## 🐛 Troubleshooting

### "GROQ_API_KEY not set" Error
- Ensure `.env` file exists in `backend/` folder
- Check your API key is valid at [console.groq.com](https://console.groq.com)
- Restart the backend server after adding the key

### Frontend can't connect to backend
- Ensure backend is running on `http://localhost:8000`
- Check browser console (F12) for CORS errors
- Update frontend API URL if deployed

### Output appears incomplete
- Increase `max_tokens` in `backend/app.py`
- Check Groq API status at [status.groq.com](https://status.groq.com)

## 📊 API Endpoints

### POST `/generate-plan`
Generates a personalized study plan.

**Request:**
```json
{
  "subjects": "Math, Physics",
  "exam_date": "2026-02-15",
  "hours_per_day": 5,
  "weak_topics": "Integration, Thermodynamics"
}
```

**Response:**
```json
{
  "plan": "**Study Plan for Math & Physics**\n\n- Focus on: Integration techniques and thermodynamic laws\n- Daily 5-hour strategy: 2.5h Math, 2.5h Physics\n- Weak topics: 40% of study time\n- Revision: Final 2 days before exam\n..."
}
```

### GET `/`
Health check endpoint.

**Response:**
```json
{
  "message": "✅ AI Study Planner API is running"
}
```

## 📝 System Prompt (How AI Generates Plans)

The AI is instructed to:
- Generate **concise, summarized** study plans (10-15 lines max)
- Focus on **actionable insights** rather than hour-by-hour breakdowns
- Highlight **weak topics** and **revision strategy**
- Use **bullet points** for clarity
- Provide **time allocation** per subject

Modify the prompt in `backend/app.py` (lines 37-41) to change AI behavior.

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas to contribute:
- Additional AI models support
- Mobile app wrapper
- Study progress tracking
- Export plans to PDF/Excel
- Multiple languages support
- Database integration

## 📄 License

This project is licensed under the MIT License — see the LICENSE file for details.

## 🙏 Acknowledgments

- **Groq AI** — For the fast, free LLaMA API
- **Aceternity UI** — For animation inspiration
- **FastAPI** — Excellent Python web framework
- **Community** — For feedback and support


## 🚀 Future Roadmap

- [ ] User authentication & plan history
- [ ] Collaborative study planning
- [ ] Integration with Google Calendar
- [ ] Mobile app (React Native)
- [ ] Study timer with notifications
- [ ] Performance analytics
- [ ] Multiple language support
- [ ] Offline mode

---
