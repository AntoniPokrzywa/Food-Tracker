import { useState, useEffect } from 'react';

const API_BASE_URL = 'http://localhost:5000';

export const useMeals = (selectedDate) => {
  const [meals, setMeals] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchMeals = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/meals/${selectedDate}`, {
        credentials: 'include'
      });
      if (response.ok) {
        const mealsData = await response.json();
        setMeals(mealsData);
      }
    } catch (error) {
      console.error('Error fetching meals:', error);
    }
  };

  const addMeal = async (mealData) => {
    setLoading(true);
    setError('');

    try {
      const response = await fetch(`${API_BASE_URL}/meals`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
          ...mealData,
          date: selectedDate
        })
      });

      const data = await response.json();

      if (response.ok) {
        await fetchMeals();
        setError('');
      } else {
        setError(data.detail || 'Failed to add meal');
      }
    } catch (error) {
      setError('Network error. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMeals();
  }, [selectedDate]);

  return {
    meals,
    loading,
    error,
    addMeal,
    refetch: fetchMeals
  };
}; 