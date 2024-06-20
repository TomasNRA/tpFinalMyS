
import React, { useEffect } from 'react'

import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function LineChart({datasets, title}) {

  useEffect(() => {
    console.log(datasets)
  }, [datasets])
  

  
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: title,
      },
    },
  };

  const data = {
    labels: Array.from({ length: 36 }, (_, i) => i + 1),
    datasets: datasets,
  };

  return (
    <Line data={data} options={options} />
  )
}
