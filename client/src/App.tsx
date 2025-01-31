import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('https://project-it.onrender.com/info')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <textarea
        readOnly
        value={data ? JSON.stringify(data, null, 2) : 'Loading...'}
        rows={20}
        cols={80}
      />
    </div>
  );
}

export default App;
