import React, { useState } from "react";
import Home from "./pages/Home";
import Video from "./pages/Video";
import "@fontsource/oxygen";

function App() {
  const [video, setVideo] = useState(null);

  console.log(video);

  return video ? (
    <Video url={`/data/${video}`} />
  ) : (
    <Home onUpload={setVideo} />
  );
}

export default App;
