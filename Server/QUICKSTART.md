# Quick Start Guide - Food Tracker Backend

## 🚀 Start the Backend (No Database Setup Required!)

1. **Install Python dependencies:**
```bash
cd Server
pip install -r requirements.txt
```

2. **Start the backend server:**
```bash
python start_dev.py
```

That's it! The backend will:
- ✅ Use SQLite database (no PostgreSQL needed)
- ✅ Create test data automatically
- ✅ Start on http://localhost:5000
- ✅ Enable CORS for frontend communication

## 👤 Test Credentials

- **Email:** test@example.com
- **Password:** password123

## 📊 Test Data Included

The system automatically creates:
- 1 test user
- 5 sample meals (today and yesterday)
- Mock nutrition data for common foods

## 🔧 What's Included

- **Authentication:** Register, login, logout
- **Meal Tracking:** Add meals with automatic nutrition calculation
- **Mock LLM:** Nutrition data for common foods (chicken, rice, salmon, etc.)
- **SQLite Database:** No external database required
- **CORS Enabled:** Frontend can communicate with backend

## 🌐 API Endpoints

- `POST /register` - Create new account
- `POST /login` - User login
- `POST /logout` - User logout
- `GET /user` - Get current user info
- `POST /meals` - Add new meal
- `GET /meals/<date>` - Get meals for specific date

## 🎯 Next Steps

1. Start the frontend: `cd Clientv2 && npm run dev`
2. Open http://localhost:5173
3. Login with test credentials
4. Start tracking your meals!

## 🔄 Production Setup

For production, you can:
1. Set up PostgreSQL database
2. Create `.env` file with database credentials
3. Set `SECRET_KEY` environment variable
4. Add `GEMINI_API_KEY` for real nutrition data 