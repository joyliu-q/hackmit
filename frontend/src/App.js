<<<<<<< HEAD
=======
import './App.css';
import React, { useState } from 'react';
import './good_video.mp4';
const axios = require('axios');

>>>>>>> ac9dfbf92e2fdb4dc058170061c2ba9be6eb504d
function App() {
  const [video, setVideo] = useState(null);

  async function handleSubmit(event) {
    const video = event.target.video.value;
    console.log(video)
    setVideo(video)

    // TODO: send it over to backend server, which makes a new video, puts the file in s3 bucket, and returns file path
    const response = await axios.post('http://localhost:8000/add-music', {file: video}, {headers: {'Content-Type': 'multipart/form-data'}});
    console.log(response)
    event.preventDefault();
  }

  return (
    <div className="App">
<<<<<<< HEAD
      <form
        action="http://0.0.0.0:8000/add-music"
        method="POST"
        encType="multipart/form-data"
      >
        <input type="file" name="file" />
        <button type="submit">Submit</button>
      </form>
=======
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
>>>>>>> ac9dfbf92e2fdb4dc058170061c2ba9be6eb504d
    </div>
  );
}

export default App;
