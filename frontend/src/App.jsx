import React, { useState } from "react";
import axios from "axios";

function App() {
  const [jd, setJd] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    try {
      const res = await axios.post("http://localhost:8000/generate", { jd });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Backend error. Check if backend is running.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>JD Project Generator</h1>

      <textarea
        rows="10"
        cols="50"
        value={jd}
        onChange={(e) => setJd(e.target.value)}
      />

      <br />
      <button onClick={handleSubmit}>Generate</button>

      {result && result.projects && result.projects.map((p, i) => (
        <div key={i} style={{ marginTop: "20px" }}>
          <h2>{p.name}</h2>
          <p>{p.description}</p>
          <p>{(p.tech_stack || []).join(", ")}</p>

          <ul>
            {(p.resume_points || []).map((pt, idx) => (
              <li key={idx}>{pt}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default App;