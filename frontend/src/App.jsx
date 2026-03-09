import { useState } from "react";
import "./App.css";
import UploadPanel from "./components/UploadPanel";
import ChatWindow from "./components/ChatWindow";
import MessageInput from "./components/MessageInput";
import { API_BASE_URL } from "./config/api";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    const question = input.trim();
    if (!question || loading) return;

    const userMessage = {
      role: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch response from backend.");
      }

      const data = await response.json();

      const botMessage = {
        role: "assistant",
        text: data.answer,
        sources: data.sources || [],
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        role: "assistant",
        text: "Failed to connect to the backend.",
        sources: [],
      };

      setMessages((prev) => [...prev, errorMessage]);
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>RAG Customer Support Bot</h1>
        <p>Ask questions based on your uploaded documents.</p>
      </header>

      <main className="app-main">
        <UploadPanel />

        <div className="chat-layout">
          <ChatWindow messages={messages} />
          <MessageInput
            input={input}
            setInput={setInput}
            loading={loading}
            onSend={handleSend}
          />
        </div>
      </main>
    </div>
  );
}

export default App;
