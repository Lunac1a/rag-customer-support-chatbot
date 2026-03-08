import "./App.css";

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>RAG Customer Support Bot</h1>
        <p>Ask questions based on your uploaded documents.</p>
      </header>

      <main className="app-main">
        <aside className="sidebar">
          <h2>Knowledge Base</h2>

          <div className="upload-box">
            <p>No file uploaded yet.</p>
            <button>Choose File</button>
            <button>Upload</button>
          </div>
        </aside>

        <section className="chat-section">
          <div className="chat-messages">
            <div className="message user-message">
              <p>How long does shipping take?</p>
            </div>

            <div className="message bot-message">
              <p>
                Standard shipping takes 3 to 7 business days. Express shipping
                takes 1 to 3 business days.
              </p>

              <div className="sources">
                <h3>Sources</h3>
                <div className="source-card">
                  <p><strong>File:</strong> store_policy.txt</p>
                  <p><strong>Chunk:</strong> 0</p>
                  <p>
                    Shipping Policy... Standard shipping takes 3 to 7 business
                    days...
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="chat-input-area">
            <input
              type="text"
              placeholder="Type your question here..."
            />
            <button>Send</button>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;