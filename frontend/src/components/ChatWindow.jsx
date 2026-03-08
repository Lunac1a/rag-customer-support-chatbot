import SourceList from "./SourceList";

function ChatWindow({ messages }) {
  return (
    <section className="chat-section">
      <div className="chat-messages">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${
              message.role === "user" ? "user-message" : "bot-message"
            }`}
          >
            <p>{message.text}</p>

            {message.role === "assistant" && message.sources?.length > 0 && (
              <SourceList sources={message.sources} />
            )}
          </div>
        ))}
      </div>
    </section>
  );
}

export default ChatWindow;