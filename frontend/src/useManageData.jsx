import { useState } from "react";

export default function useManageData() {


  const [hayDatosCargados, setHayDatosCargados] = useState(false);
  const [datasetsUnidadesTotales, setDatasetsUnidadesTotales] = useState([]);
  const [datasetsAutoparte1, setDatasetsAutoparte1] = useState([]);
  const [datasetsAutoparte2, setDatasetsAutoparte2] = useState([]);

  const [isLoading, setIsLoading] = useState(false);

  const colores = [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
  ]

  const datasets = {
    unidadesTotales: datasetsUnidadesTotales,
    autoparte1: datasetsAutoparte1,
    autoparte2: datasetsAutoparte2,
  }

  const createDatasets = (data) => {

    const nroSimulacion = datasetsUnidadesTotales.length + 1;

    const nuevoDatasetUnidadesTotales = {
      label: `Simulacion ${nroSimulacion}`,
      data: data.unidades_totales_por_mes,
      borderColor: colores[nroSimulacion - 1],
      backgroundColor: colores[nroSimulacion - 1],
      fill: false,
    }

    setDatasetsUnidadesTotales([...datasetsUnidadesTotales, nuevoDatasetUnidadesTotales]);

    const nuevoDatasetAutoparte1 = {
      label: `Simulacion ${nroSimulacion}`,
      data: data.stock_auto_parte1_por_mes,
      borderColor: colores[nroSimulacion - 1],
      backgroundColor: colores[nroSimulacion - 1],
      fill: false,
    }

    setDatasetsAutoparte1([...datasetsAutoparte1, nuevoDatasetAutoparte1]);

    const nuevoDatasetAutoparte2 = {
      label: `Simulacion ${nroSimulacion}`,
      data: data.stock_auto_parte2_por_mes,
      borderColor: colores[nroSimulacion - 1],
      backgroundColor: colores[nroSimulacion - 1],
      fill: false,
    }

    setDatasetsAutoparte2([...datasetsAutoparte2, nuevoDatasetAutoparte2]);

  }

  const simular = async (cantidadAutopartes1, cantidadAutopartes2, diasProduccion, cantidadOperarios) => {
    try {
      setIsLoading(true);
      const request = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "cantidad_operarios": cantidadOperarios,
          "produccion_diaria_autoparte1": cantidadAutopartes1,
          "produccion_diaria_autoparte2": cantidadAutopartes2,
          "dias_produccion": diasProduccion
        })
      }

      const response = await fetch('http://localhost:8000/random', request);
      const data = await response.json();

      createDatasets(data)
      setHayDatosCargados(true);
      
    } catch (error) {
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  }

  return { datasets, simular, isLoading, hayDatosCargados }
}