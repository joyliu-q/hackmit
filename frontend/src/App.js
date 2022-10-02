function App() {
  return (
    <div className="App">
      <form
        action="http://0.0.0.0:8000/add-music"
        method="POST"
        encType="multipart/form-data"
      >
        <input type="file" name="file" />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
