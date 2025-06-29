import React from 'react';

const DateSelector = ({ selectedDate, onDateChange }) => {
  return (
    <div className="date-selector">
      <label>Select Date:</label>
      <input
        type="date"
        value={selectedDate}
        onChange={(e) => onDateChange(e.target.value)}
      />
    </div>
  );
};

export default DateSelector; 