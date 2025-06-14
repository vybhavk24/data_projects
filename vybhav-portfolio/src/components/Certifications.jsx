import React from 'react';

function Certifications() {
  return (
    <section id="certifications" className="p-6">
      <h2 className="text-2xl font-bold mb-4">📜 Certifications</h2>

      <h3 className="text-xl font-semibold mb-2 mt-4">✅ Completed</h3>
      <ul className="list-disc pl-6">
        <li>IBM Data Analyst Professional Certificate</li>
        <li>Mathematics for ML by DeepLearning.AI</li>
        <li>Stanford's Machine Learning Professional Certificate</li>
        <li>Learn SQL Basics for Data Science Specialization</li>
      </ul>

      <h3 className="text-xl font-semibold mb-2 mt-4">⏳ Actively Pursuing</h3>
      <ul className="list-disc pl-6">
        <li>Gooogle's Advanced Data Analytics Professional Certificate</li>
        <li>Microsoft's Power BI for data analysis</li>
      </ul>
    </section>
  );
}

export default Certifications;