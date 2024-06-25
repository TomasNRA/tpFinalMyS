import React from 'react'
import {CubeSpinner} from 'react-spinners-kit'

export default function LoadingSpinner() {
  return (
    <div className='spinner-container'>
      <CubeSpinner size={50} frontColor="#5aa1f3" backColor="#3d6ea6" loading={true} />
      <span>Simulando...</span>
    </div>
  )
}
