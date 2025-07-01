import React from 'react';

const MealCard = ({ meal }) => {
  return (
    <div className="meal-card">
      <h3>{meal.name}</h3>
      <p><strong>Weight:</strong> {meal.food_weight}g</p>
      <div className="meal-nutrition">
        <span>Calories: {meal.calories || 0}</span>
        <span>Protein: {meal.protein || 0}g</span>
        <span>Carbs: {meal.carbohydrates || 0}g</span>
        <span>Fats: {meal.fat || 0}g</span>
      </div>
    </div>
  );
};

export default MealCard; 