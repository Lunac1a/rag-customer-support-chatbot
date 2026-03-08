function SourceList({ sources }) {
  return (
    <div className="sources">
      <h3>Sources</h3>

      {sources.map((source, index) => (
        <div className="source-card" key={index}>
          <p>
            <strong>File:</strong> {source.source}
          </p>
          <p>
            <strong>Chunk:</strong> {source.chunk_index}
          </p>
          <p>{source.text}</p>
        </div>
      ))}
    </div>
  );
}

export default SourceList;