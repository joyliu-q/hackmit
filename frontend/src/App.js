import './App.css';
import React, { useState } from 'react';
import './good_video.mp4';
import Plyr from "plyr-react"
import "plyr-react/plyr.css"
import Dropzone from "dropzone";

const axios = require('axios');

function App() {
  const [video, setVideo] = useState(null);

  React.useEffect(() => {
    let myDropzone = new Dropzone("#dropzone");
    myDropzone.on("addedfile", async (video) => {
      console.log(`File added: ${video.name}`);
      setVideo(video)
      await addMusic()
      // TODO: await resp
    });
  }, [])

  async function addMusic() {
    // TODO: send it over to backend server, which makes a new video, puts the file in s3 bucket, and returns file path
    const response = await axios.post('http://localhost:8000/add-music', {file: video}, {headers: {'Content-Type': 'multipart/form-data'}});
    console.log(response)
  }

  async function handleSubmit(event) {
    const video = event.target.video.value;
    console.log(video)
    setVideo(video)
    await addMusic()
    event.preventDefault();
  }

  return (
    <div className="App">
      <div className="convert-container">
        <h1>[Title Here]</h1>
        <form action="/target" id="dropzone">
          LMAO
        </form>
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
      {true && <>
        <Plyr  {
          ...{
            source: {
              type: 'video',
              title: 'Example title',
              sources: [
                {
                  src: "https://media.w3.org/2010/05/sintel/trailer_hd.mp4",
                  type: 'video/mp4',
                  size: 720,
                }
              ]
            }
          }}
          />
      </>}
    </div>
  );
}

export default App;
