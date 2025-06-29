import React, { useState } from 'react';

const MealForm = ({ onAddMeal, loading, error }) => {
  const [mealForm, setMealForm] = useState({
    name: '',
    food_weight: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddMeal(mealForm);
    setMealForm({ name: '', food_weight: '' });
  };

  return (
    <div className="meal-form-section">
      <h2>Add New Meal</h2>
      {error && <div className="error-message">{error}</div>}
      
      <form onSubmit={handleSubmit} className="meal-form">
        <div className="form-row">
          <div className="form-group">
            <label>Food Name:</label>
            <input
              type="text"
              value={mealForm.name}
              onChange={(e) => setMealForm({...mealForm, name: e.target.value})}
              placeholder="e.g., Chicken Breast"
              required
            />
          </div>
          
          <div className="form-group">
            <label>Weight (g):</label>
            <input
              type="number"
              value={mealForm.food_weight}
              onChange={(e) => setMealForm({...mealForm, food_weight: e.target.value})}
              placeholder="100"
              required
            />
          </div>
        </div>
        
        <button type="submit" disabled={loading} className="btn-primary">
          {loading ? 'Adding...' : 'Add Meal'}
        </button>
      </form>
    </div>
  );
};

export default MealForm; 