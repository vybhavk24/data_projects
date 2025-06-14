import './index.css';

import Navbar from './components/Navbar';
import About from './components/About';
import Education from './components/Education';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Footer from './components/Footer';

function App() {
  return (
    <div className="font-sans text-gray-900 bg-white min-h-screen">
      <Navbar />

      <main className="p-6 space-y-12">
        <About />
        <Education />
        <Experience />
        <Projects />
      </main>

      <Footer />
    </div>
  );
}

export default App;