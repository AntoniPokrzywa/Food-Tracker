import React from 'react';

const DailySummary = ({ meals }) => {
  const calculateDailyTotals = () => {
    return meals.reduce((totals, meal) => ({
      calories: totals.calories + (meal.calories || 0),
      protein: totals.protein + (meal.protein || 0),
      carbs: totals.carbs + (meal.carbs || 0),
      fats: totals.fats + (meal.fats || 0)
    }), { calories: 0, protein: 0, carbs: 0, fats: 0 });
  };

  const totals = calculateDailyTotals();

  return (
    <div className="daily-summary">
      <h2>Daily Summary</h2>
      <div className="nutrition-cards">
        {Object.entries(totals).map(([nutrient, value]) => (
          <div key={nutrient} className="nutrition-card">
            <h3>{nutrient.charAt(0).toUpperCase() + nutrient.slice(1)}</h3>
            <p>{value}g</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DailySummary; 