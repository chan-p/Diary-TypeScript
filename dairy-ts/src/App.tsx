import React from 'react';
import { Diary } from './Diary'
import './App.css';

const initialState: Diary[] = [
  {
      id: 1,
      date: '2020-8-22',
      title: '調子がよかった'
  }
]

const App: React.FC = () => {

  return (
      <div>
          <input type="date"/>
      </div>
  )
}

export default App;
