import React from 'react';
import { createRoot } from 'react-dom/client';
import TimerConfigScreen from './TimerConfigScreen.jsx';

const rootElement = document.getElementById('root');
const root = createRoot(rootElement);
root.render(<TimerConfigScreen />);
