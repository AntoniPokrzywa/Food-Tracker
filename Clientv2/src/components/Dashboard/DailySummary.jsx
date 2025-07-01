import React from 'react';

const MACRO_TARGETS = {
  calories: 2000,
  protein: 50,
  carbohydrates: 275,
  fat: 70,
};

const DailySummary = ({ meals }) => {
  const calculateDailyTotals = () => {
    return meals.reduce((totals, meal) => ({
      calories: totals.calories + (meal.calories || 0),
      protein: totals.protein + (meal.protein || 0),
      carbohydrates: totals.carbohydrates + (meal.carbohydrates || 0),
      fat: totals.fat + (meal.fat || 0)
    }), { calories: 0, protein: 0, carbohydrates: 0, fat: 0 });
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
      <div className="macro-bars">
        {Object.entries(MACRO_TARGETS).map(([macro, target]) => {
          const value = totals[macro] || 0;
          const percent = Math.min((value / target) * 100, 100);
          return (
            <div key={macro} className="macro-bar-row">
              <div className="macro-bar-label">
                {macro.charAt(0).toUpperCase() + macro.slice(1)}: {value} / {target}{macro === 'calories' ? ' kcal' : 'g'}
              </div>
              <div className="macro-bar-outer">
                <div className="macro-bar-inner" style={{ width: `${percent}%` }} />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default DailySummary; 