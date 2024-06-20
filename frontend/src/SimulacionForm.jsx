import React, { useState } from "react";

export default function SimulacionForm({simular}) {
  const [cantidadAutopartes1, setCantidadAutopartes1] = useState(0);
  const [cantidadAutopartes2, setCantidadAutopartes2] = useState(0);
  const [diasProduccion, setDiasProduccion] = useState(0);
  const [cantidadOperarios, setCantidadOperarios] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    simular(cantidadAutopartes1, cantidadAutopartes2, diasProduccion, cantidadOperarios);
  };

  return (
    <form onSubmit={handleSubmit} className="simulacionForm">
      <h1>Simulación de producción de autopartes</h1>

      <div>
        <fieldset>
          <label htmlFor="cantidadAutopartes1">Cantidad de autopartes 1</label>
          <input
            type="number"
            id="cantidadAutopartes1"
            value={cantidadAutopartes1}
            onChange={(e) => setCantidadAutopartes1(e.target.value)}
            min={0}
          />
        </fieldset>

        <fieldset>
          <label htmlFor="cantidadAutopartes2">Cantidad de autopartes 2</label>
          <input
            type="number"
            id="cantidadAutopartes2"
            value={cantidadAutopartes2}
            onChange={(e) => setCantidadAutopartes2(e.target.value)}
            min={0}
          />
        </fieldset>

        <fieldset>
          <label htmlFor="diasProduccion">Días de producción</label>
          <input
            type="number"
            id="diasProduccion"
            value={diasProduccion}
            onChange={(e) => setDiasProduccion(e.target.value)}
            min={0}
          />
        </fieldset>

        <fieldset>
          <label htmlFor="cantidadOperarios">Cantidad de operarios</label>
          <input
            type="number"
            id="cantidadOperarios"
            value={cantidadOperarios}
            onChange={(e) => setCantidadOperarios(e.target.value)}
            min={0}
          />
        </fieldset>
      </div>

      <button type="submit">Simular</button>
    </form>
  );
}
