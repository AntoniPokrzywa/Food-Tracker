import React, { useState } from 'react';

const DEFAULT_MACRO_TARGETS = {
  calories: 2000,
  protein: 50,
  carbohydrates: 275,
  fat: 70,
};

const macroLabels = {
  calories: 'Calories (kcal)',
  protein: 'Protein (g)',
  carbohydrates: 'Carbs (g)',
  fat: 'Fat (g)',
};

const DailySummary = ({ meals }) => {
  const [macroTargets, setMacroTargets] = useState(DEFAULT_MACRO_TARGETS);
  const [showModal, setShowModal] = useState(false);

  const calculateDailyTotals = () => {
    return meals.reduce((totals, meal) => ({
      calories: totals.calories + (meal.calories || 0),
      protein: totals.protein + (meal.protein || 0),
      carbohydrates: totals.carbohydrates + (meal.carbohydrates || 0),
      fat: totals.fat + (meal.fat || 0)
    }), { calories: 0, protein: 0, carbohydrates: 0, fat: 0 });
  };

  const totals = calculateDailyTotals();

  const handleSlider = (macro, value) => {
    setMacroTargets((prev) => ({ ...prev, [macro]: Number(value) }));
  };

  return (
    <div className="daily-summary">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h2>Daily Summary</h2>
        <button className="macro-settings-btn" onClick={() => setShowModal(true)} title="Set daily goals">
          <span role="img" aria-label="settings">⚙️</span>
        </button>
      </div>
      <div className="nutrition-cards">
        {Object.entries(totals).map(([nutrient, value]) => (
          <div key={nutrient} className="nutrition-card">
            <h3>{nutrient.charAt(0).toUpperCase() + nutrient.slice(1)}</h3>
            <p>{value}g</p>
          </div>
        ))}
      </div>
      <div className="macro-bars">
        {Object.entries(macroTargets).map(([macro, target]) => {
          const value = totals[macro] || 0;
          const percent = Math.min((value / target) * 100, 100);
          return (
            <div key={macro} className="macro-bar-row">
              <div className="macro-bar-label">
                {macroLabels[macro]}: {value} / {target}{macro === 'calories' ? ' kcal' : 'g'}
              </div>
              <div className="macro-bar-outer">
                <div className="macro-bar-inner" style={{ width: `${percent}%` }} />
              </div>
            </div>
          );
        })}
      </div>
      {showModal && (
        <div className="macro-modal-overlay" onClick={() => setShowModal(false)}>
          <div className="macro-modal" onClick={e => e.stopPropagation()}>
            <h3>Set Daily Goals</h3>
            {Object.entries(macroTargets).map(([macro, value]) => (
              <div key={macro} className="macro-slider-row">
                <label>{macroLabels[macro]}</label>
                <input
                  type="range"
                  min={macro === 'calories' ? 1000 : 0}
                  max={macro === 'calories' ? 5000 : macro === 'protein' ? 300 : macro === 'carbohydrates' ? 600 : 200}
                  step={macro === 'calories' ? 10 : 1}
                  value={value}
                  onChange={e => handleSlider(macro, e.target.value)}
                />
                <span className="macro-slider-value">{value}{macro === 'calories' ? ' kcal' : 'g'}</span>
              </div>
            ))}
            <button className="btn-primary" style={{marginTop: 18}} onClick={() => setShowModal(false)}>Done</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default DailySummary; 