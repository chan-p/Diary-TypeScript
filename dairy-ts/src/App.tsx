import React from 'react';
// import { Diary } from './Diary'
import Calendar from 'react-calendar'
import './App.css';

// const initialState: Diary[] = [
//   {
//       id: 1,
//       date: '2020-8-22',
//       title: '調子がよかった'
//   }
// ]

const App: React.FC = () => {

  return (
    <div>
      <Calendar locale="ja-JP" calendarType="US" value={new Date()} />
    </div>
  )
}

export default App;
