import React from 'react';
import MealCard from './MealCard';

const MealsList = ({ meals }) => {
  if (meals.length === 0) {
    return (
      <div className="meals-section">
        <h2>Today's Meals</h2>
        <p className="no-meals">No meals recorded for this date.</p>
      </div>
    );
  }

  return (
    <div className="meals-section">
      <h2>Today's Meals</h2>
      <div className="meals-grid">
        {meals.map((meal) => (
          <MealCard key={meal.id} meal={meal} />
        ))}
      </div>
    </div>
  );
};

export default MealsList; 