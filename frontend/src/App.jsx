import React, { useState } from 'react';
import LineChart from './LineChart';
import SimulacionForm from './SimulacionForm';
import './App.css';
import useManageData from './useManageData';


function App() {


  const { datasets, simular, isLoading, hayDatosCargados } = useManageData();


  return (
    <div className="App">
      <SimulacionForm simular={simular} />
      {isLoading && <p>Cargando...</p>}

      {hayDatosCargados ? (
        <>
          <LineChart datasets={datasets.unidadesTotales} title={"Unidades totales"} />
          <LineChart datasets={datasets.autoparte1} title={"Autopartes 1"} />
          <LineChart datasets={datasets.autoparte2} title={"Autopartes 2"} />
        </>
      ): (
        <p>No hay datos para mostrar</p>
      )}
    </div>
  );
}

export default App;
