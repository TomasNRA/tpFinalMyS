import React, { useEffect, useState } from 'react';
import LineChart from './LineChart';
import SimulacionForm from './SimulacionForm';
import './App.css';
import useManageData from './useManageData';
import LoadingSpinner from './LoadingSpinner';

function App() {

  const { datasets, simular, isLoading, hayDatosCargados } = useManageData();
  const [cantidadDatos, setCantidadDatos] = useState(0);

  useEffect(() => {
    setCantidadDatos(datasets?.unidadesTotales[0]?.data.length || 36);
  }, [datasets]) 

  return (
    <div className="App">
      <SimulacionForm simular={simular} />
      {isLoading && <LoadingSpinner />}

      {!hayDatosCargados && !isLoading && <p className='no-data'>-- No hay datos para mostrar --</p>}

      {hayDatosCargados && (
        <section className='chart-container'>
          <LineChart datasets={datasets.unidadesTotales} title={"Unidades totales producidas mensualmente"} cantidadDatos={cantidadDatos}/>
          <LineChart datasets={datasets.autoparte1} title={"Cantidad de autoparte 1 en stock"} cantidadDatos={cantidadDatos}/>
          <LineChart datasets={datasets.autoparte2} title={"Cantidad de autoparte 2 en stock"} cantidadDatos={cantidadDatos}/>
          <LineChart datasets={datasets.promedioEsperaMensual} title={"Promedio de espera mensual"} cantidadDatos={cantidadDatos}/>
          <LineChart datasets={datasets.tiemposSinStock} title={"Tiempo promedio sin stock (anual)"} cantidadDatos={3}/>  
        </section>
      )}
      
    </div>
  );
}

export default App;
