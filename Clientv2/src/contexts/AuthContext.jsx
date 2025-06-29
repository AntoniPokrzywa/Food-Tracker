import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);
  const [isLoginMode, setIsLoginMode] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const API_BASE_URL = 'http://localhost:5000';

  const checkAuthStatus = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/user`, {
        credentials: 'include'
      });
      if (response.ok) {
        const userData = await response.json();
        setCurrentUser(userData);
        setIsAuthenticated(true);
      }
    } catch (error) {
      console.log('Not authenticated');
    }
  };

  const handleAuth = async (formData) => {
    setLoading(true);
    setError('');

    const endpoint = isLoginMode ? '/login' : '/register';
    
    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(formData)
      });

      const data = await response.json();

      if (response.ok) {
        if (isLoginMode) {
          setIsAuthenticated(true);
          await checkAuthStatus();
        } else {
          setIsLoginMode(true);
        }
        setError('');
      } else {
        setError(data.detail || 'An error occurred');
      }
    } catch (error) {
      setError('Network error. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    try {
      await fetch(`${API_BASE_URL}/logout`, {
        method: 'POST',
        credentials: 'include'
      });
      setIsAuthenticated(false);
      setCurrentUser(null);
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  const toggleMode = () => {
    setIsLoginMode(!isLoginMode);
    setError('');
  };

  useEffect(() => {
    checkAuthStatus();
  }, []);

  const value = {
    isAuthenticated,
    currentUser,
    isLoginMode,
    loading,
    error,
    handleAuth,
    handleLogout,
    toggleMode
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}; 