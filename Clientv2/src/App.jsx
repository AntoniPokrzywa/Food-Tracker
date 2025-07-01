import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import { useMeals } from './hooks/useMeals';
import Auth from './pages/Auth';
import Dashboard from './pages/Dashboard';
import './App.css';

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? children : <Navigate to="/auth" replace />;
};

const AppRoutes = () => {
  const { 
    isAuthenticated, 
    currentUser, 
    isLoginMode, 
    loading, 
    error, 
    handleAuth, 
    handleLogout, 
    toggleMode 
  } = useAuth();

  const [selectedDate, setSelectedDate] = useState(new Date().toISOString().split('T')[0]);
  const { meals, loading: mealsLoading, error: mealsError, addMeal } = useMeals(selectedDate);
  console.log(meals);
  if (!isAuthenticated) {
    return (
      <Routes>
        <Route 
          path="/auth" 
          element={
            <Auth 
              onAuth={handleAuth}
              loading={loading}
              error={error}
              isLoginMode={isLoginMode}
              onToggleMode={toggleMode}
            />
          } 
        />
        <Route path="*" element={<Navigate to="/auth" replace />} />
      </Routes>
    );
  }

  return (
    <Routes>
      <Route 
        path="/" 
        element={
          <ProtectedRoute>
            <Dashboard 
              currentUser={currentUser}
              onLogout={handleLogout}
              selectedDate={selectedDate}
              onDateChange={setSelectedDate}
              meals={meals}
              onAddMeal={addMeal}
              loading={mealsLoading}
              error={mealsError}
            />
          </ProtectedRoute>
        } 
      />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
};

function App() {
  return (
    <Router>
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </Router>
  );
}

export default App;
