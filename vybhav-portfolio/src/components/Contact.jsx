import React from 'react';

function Contact() {
  return (
    <section id="contact" className="p-6">
      <h2 className="text-2xl font-bold mb-4">📞 Contact</h2>
      <p><strong>Name:</strong> Vybhav K</p>
      <p><strong>Email:</strong> vybhavkvviet@gmail.com</p>
      <p><strong>Phone:</strong> +91 7349402665</p>
      <div className="mt-4 space-x-4">
        <a href="https://github.com/vybhavk24" target="_blank" className="text-blue-600 underline">GitHub </a> |
        <a href="https://www.linkedin.com/in/vybhav-k-0b02891b9" target="_blank" className="text-blue-600 underline"> LinkedIn</a>
      </div>
    </section>
  );
}

export default Contact;