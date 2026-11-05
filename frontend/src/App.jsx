import { useState } from 'react'
import HomePage from './pages/HomePage'
import VerityNavBar from './Components/VerityNavBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <VerityNavBar />
      <HomePage />
    </>
  )
}

export default App
