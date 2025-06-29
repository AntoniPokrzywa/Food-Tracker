import React from 'react';

const Header = ({ currentUser, onLogout }) => {
  return (
    <header className="header">
      <h1>Food Tracker</h1>
      <div className="user-info">
        <span>Welcome, {currentUser?.email}</span>
        <button onClick={onLogout} className="btn-logout">Logout</button>
      </div>
    </header>
  );
};

export default Header; 