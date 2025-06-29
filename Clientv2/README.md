# Food Tracker Frontend

A modern React-based frontend for the Food Tracker application.

## Features

- **User Authentication**: Register and login functionality
- **Meal Tracking**: Add meals with food name and weight
- **Nutrition Analysis**: Automatic calculation of calories, protein, carbs, and fats
- **Daily Summary**: View daily nutrition totals
- **Date Selection**: Track meals for different dates
- **Responsive Design**: Works on desktop and mobile devices

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open your browser to `http://localhost:5173`

## Backend Requirements

Make sure the Flask backend is running on `http://localhost:5000` with the following endpoints:

- `POST /register` - User registration
- `POST /login` - User login
- `POST /logout` - User logout
- `GET /user` - Get current user info
- `POST /meals` - Add a new meal
- `GET /meals/<date>` - Get meals for a specific date

## Environment Setup

The backend requires a PostgreSQL database. Create a `.env` file in the Server directory with:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=food_tracker
SECRET_KEY=your-secret-key-here
```

## Usage

1. **Register/Login**: Create an account or login with existing credentials
2. **Add Meals**: Enter food name and weight, the system will automatically calculate nutrition values
3. **View Daily Summary**: See your total nutrition intake for the selected date
4. **Track Progress**: Switch between dates to view your meal history

## Technologies Used

- React 18
- Vite
- Modern CSS with Grid and Flexbox
- Fetch API for backend communication
