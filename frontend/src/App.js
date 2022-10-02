import './App.css';
import React, { useState } from 'react';
import './good_video.mp4';

function App() {
  const [video, setVideo] = useState(null);

  function handleSubmit(event) {
    const video = event.target.video.value;
    console.log(video)
    setVideo(video)

    // TODO: send it over to backend server, which makes a new video, puts the file in s3 bucket, and returns file path
    event.preventDefault();
  }

  return (
    <div className="App">
      {video && <>
        <video width="750" height="500" controls >
          <source src="https://media.w3.org/2010/05/sintel/trailer_hd.mp4" type="video/mp4"/>
        </video>
      </>}
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <input type="file" id="video" name="video" accept="video/*" />
          <input type="submit" value="Submit" />
        </form>
      </header>
    </div>
  );
}

export default App;
