import React, { useState } from "react";
import "./good_video.mp4";
import Plyr from "plyr-react";
import "plyr-react/plyr.css";
import Dropzone from "dropzone";

const axios = require("axios");

function App() {
  const [videoSrc, setVideoSrc] = useState(null);

  async function handleSubmit(event) {
    event.preventDefault();
    const video = event.target.video.files[0];
    console.log(video);
    setVideoSrc(video);

    const response = await axios.post(
      "http://localhost:8000/add-music",
      { file: video },
      { headers: { "Content-Type": "multipart/form-data" } }
    );
    console.log(response);
    console.log(response.data.path);
    setVideoSrc(response.path);
  }

  return (
    <div className="App">
      {true && (
        <>
          <Plyr  {
          ...{
            source: {
              type: 'video',
              title: 'Example title',
              sources: [
                {
                  src: videoSrc,
                  type: 'video/mp4',
                  size: 720,
                }
              ]
            }
          }}
          />
        </>
      )}
      <form onSubmit={handleSubmit}>
        <input type="file" id="video" name="video" accept="video/*" />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default App;
