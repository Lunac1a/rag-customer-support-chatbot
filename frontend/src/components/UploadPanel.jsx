import { useState } from "react";

function UploadPanel() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile || null);
    setStatus("");
  };

  const handleUpload = async () => {
  if (!file) {
    setStatus("Please choose a file first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    setStatus("Uploading...");

    const response = await fetch("http://127.0.0.1:8001/api/ingest", {
      method: "POST",
      body: formData,
    });

    console.log("upload response status:", response.status);

    const text = await response.text();
    console.log("upload response body:", text);

    if (!response.ok) {
      throw new Error(`Upload failed: ${response.status} ${text}`);
    }

    const data = JSON.parse(text);
    setStatus(`Uploaded: ${data.filename} (${data.num_chunks} chunks)`);
    setFile(null);
  } catch (error) {
    console.error("upload error:", error);
    setStatus(String(error));
  }
};

  return (
    <aside className="sidebar">
      <h2>Knowledge Base</h2>

      <div className="upload-box">
        <input type="file" accept=".txt" onChange={handleFileChange} />

        {file && <p>Selected: {file.name}</p>}

        <button onClick={handleUpload}>Upload</button>

        {status && <p>{status}</p>}
      </div>
    </aside>
  );
}

export default UploadPanel;