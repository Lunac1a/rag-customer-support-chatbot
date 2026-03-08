function MessageInput({ input, setInput, loading, onSend }) {
  const handleSubmit = () => {
    if (!input.trim() || loading) return;
    onSend();
  };

  return (
    <div className="chat-input-area">
      <input
        type="text"
        placeholder="Type your question here..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSubmit();
          }
        }}
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Sending..." : "Send"}
      </button>
    </div>
  );
}

export default MessageInput;