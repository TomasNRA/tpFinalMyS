
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

export default function LineChart({datasets, title, cantidadDatos = 36}) {

  
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
    scales: {
      y: {
        beginAtZero: true,
        min: 0,
      },
    },
  };

  const data = {
    labels: Array.from({ length: cantidadDatos }, (_, i) => i + 1),
    datasets: datasets,
  };

  return (
    <section>
      <Line data={data} options={options} />
    </section>
  )
}
