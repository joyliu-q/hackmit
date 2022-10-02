import React, { useState } from "react";
import "./App.css";
import Video from "./pages/Video";

const axios = require("axios");

function App() {
  const [video, setVideo] = useState(null);

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

  return <Video />;
}

export default App;
