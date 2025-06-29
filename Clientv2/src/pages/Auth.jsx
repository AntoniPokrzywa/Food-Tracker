import React from 'react';
import LoginForm from '../components/Auth/LoginForm';

const Auth = ({ onAuth, loading, error, isLoginMode, onToggleMode }) => {
  return (
    <LoginForm 
      onAuth={onAuth}
      loading={loading}
      error={error}
      isLoginMode={isLoginMode}
      onToggleMode={onToggleMode}
    />
  );
};

export default Auth; 