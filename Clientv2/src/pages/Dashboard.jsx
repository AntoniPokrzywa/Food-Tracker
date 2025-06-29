import React from 'react';
import Header from '../components/Header/Header';
import DateSelector from '../components/Dashboard/DateSelector';
import MealForm from '../components/Meals/MealForm';
import DailySummary from '../components/Dashboard/DailySummary';
import MealsList from '../components/Meals/MealsList';

const Dashboard = ({ 
  currentUser, 
  onLogout, 
  selectedDate, 
  onDateChange, 
  meals, 
  onAddMeal, 
  loading, 
  error 
}) => {
  return (
    <div className="app">
      <Header currentUser={currentUser} onLogout={onLogout} />
      
      <main className="main-content">
        <DateSelector 
          selectedDate={selectedDate} 
          onDateChange={onDateChange} 
        />

        <div className="dashboard">
          <MealForm 
            onAddMeal={onAddMeal} 
            loading={loading} 
            error={error} 
          />
          <DailySummary meals={meals} />
        </div>

        <MealsList meals={meals} />
      </main>
    </div>
  );
};

export default Dashboard; 