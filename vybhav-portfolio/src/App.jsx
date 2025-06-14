import './index.css';

import Navbar from './components/Navbar';
import About from './components/About';
import Education from './components/Education';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Footer from './components/Footer';
import Skills from './components/Skills';
import Contact from './components/Contact';
import Certifications from './components/Certifications';

function App() {
  return (
    <div className="font-sans text-gray-900 bg-white min-h-screen">
      <Navbar />

      <main className="p-6 space-y-12">
        <About />
        <Contact />
        <Education />
        <Experience />
        <Certifications />
        <Projects />
        <Skills />
      </main>

      <Footer />
    </div>
  );
}

export default App;