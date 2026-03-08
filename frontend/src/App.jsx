import "./App.css";
import UploadPanel from "./components/UploadPanel";
import ChatWindow from "./components/ChatWindow";
import MessageInput from "./components/MessageInput";

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>RAG Customer Support Bot</h1>
        <p>Ask questions based on your uploaded documents.</p>
      </header>

      <main className="app-main">
        <UploadPanel />

        <div className="chat-layout">
          <ChatWindow />
          <MessageInput />
        </div>
      </main>
    </div>
  );
}

export default App;