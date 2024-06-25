import React from 'react'

export default function Simulaciones({simulaciones}) {
  return (
    <section className='simulaciones-container'>
      {simulaciones.map((simulacion, index) => (
        <div key={index} className='simulacion'>
          <h3>Simulación #{index + 1}</h3>
          <span><span className='title'>Autoparte 1:</span> {simulacion.cantidadAutopartes1}</span>
          <span><span className='title'>Autoparte 2:</span> {simulacion.cantidadAutopartes2}</span>
          <span><span className='title'>Cantidad operarios:</span> {simulacion.cantidadOperarios}</span>
          <span><span className='title'>Dias produccion:</span> {simulacion.diasProduccion}</span>
        </div>
      ))}
    </section>
  )
}
