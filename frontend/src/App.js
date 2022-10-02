import React, { useEffect, useState } from "react";
import Home from "./pages/Home";
import Video from "./pages/Video";
import "@fontsource/oxygen";

function App() {
  const [video, setVideo] = useState(null);

  return video ? <Video video={video} /> : <Home onUpload={setVideo} />;
}

export default App;
