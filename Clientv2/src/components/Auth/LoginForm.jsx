import React, { useState } from 'react';

const LoginForm = ({ onAuth, loading, error, isLoginMode, onToggleMode }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onAuth(formData);
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h1>Food Tracker</h1>
        <h2>{isLoginMode ? 'Login' : 'Register'}</h2>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit} className="auth-form">
          <div className="form-group">
            <label>Email:</label>
            <input
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({...formData, email: e.target.value})}
              required
            />
          </div>
          
          <div className="form-group">
            <label>Password:</label>
            <input
              type="password"
              value={formData.password}
              onChange={(e) => setFormData({...formData, password: e.target.value})}
              required
            />
          </div>
          
          <button type="submit" disabled={loading} className="btn-primary">
            {loading ? 'Loading...' : (isLoginMode ? 'Login' : 'Register')}
          </button>
        </form>
        
        <button 
          onClick={onToggleMode}
          className="btn-secondary"
        >
          {isLoginMode ? 'Need an account? Register' : 'Have an account? Login'}
        </button>
      </div>
    </div>
  );
};

export default LoginForm; 