import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { TemperatureDisplay } from './components/TemperatureDisplay/TemperatureDisplay'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>

      <TemperatureDisplay />

    </>
  )
}

export default App
