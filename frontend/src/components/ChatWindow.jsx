import SourceList from "./SourceList";

function ChatWindow() {
  return (
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

          <SourceList />
        </div>
      </div>
    </section>
  );
}

export default ChatWindow;