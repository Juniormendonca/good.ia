import React, { useState } from 'react';

export default function TimerConfigScreen() {
  const [frequency, setFrequency] = useState('1h');

  const handleChange = (e) => setFrequency(e.target.value);
  const handleSave = () => {
    alert(`Frequência salva: ${frequency}`);
  };

  return (
    <div style={{ padding: '1rem', fontFamily: 'sans-serif' }}>
      <h1>Timer de Elogios</h1>
      <p>Escolha a frequência das mensagens:</p>
      <select value={frequency} onChange={handleChange}>
        <option value="1h">A cada 1 hora</option>
        <option value="3h">A cada 3 horas</option>
        <option value="6h">A cada 6 horas</option>
        <option value="24h">Uma vez por dia</option>
      </select>
      <div style={{ marginTop: '1rem' }}>
        <button onClick={handleSave}>Salvar</button>
      </div>
    </div>
  );
}
