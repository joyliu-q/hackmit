import React, { useState } from "react";
import "./good_video.mp4";
import Plyr from "plyr-react";
import "plyr-react/plyr.css";
import Dropzone from "dropzone";

const axios = require("axios");

function App() {
  const [video, setVideo] = useState(null);
  Dropzone.autoDiscover = false;

  React.useEffect(() => {
    let myDropzone = new Dropzone("div.my-dropzone", { url: "/file/post" });
    myDropzone.on("addedfile", async (video) => {
      console.log(`File added: ${video.name}`);
      setVideo(video);
      // TODO: await resp
    });
  }, []);

  async function handleSubmit(event) {
    const video = event.target.video.files[0];
    console.log(video);
    setVideo(video);

    const response = await axios.post(
      "http://localhost:8000/add-music",
      { file: video },
      { headers: { "Content-Type": "multipart/form-data" } }
    );
    console.log(response);
    event.preventDefault();
  }

  return (
    <div className="App">
      {video && (
        <>
          <video width="750" height="500" controls>
            <source
              src="https://media.w3.org/2010/05/sintel/trailer_hd.mp4"
              type="video/mp4"
            />
          </video>
        </>
      )}
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
