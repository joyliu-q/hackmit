import React, { useEffect, useRef } from "react";
import { Typography } from "@mui/material";
import { Box } from "@mui/system";
import Plyr from "plyr-react";
import "plyr-react/plyr.css";

const Video = ({ video }) => {
  const ref = useRef(null);

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        minHeight: "100vh",
      }}
    >
      <Box>
        <Plyr
          ref={ref}
          controls={undefined}
          source={{
            type: "video",
            title: "Elephants Dream",
            sources: [
              {
                src: `http://localhost:8000/data/${video}`,
                type: "video/mp4",
              },
            ],
          }}
        />
      </Box>
    </Box>
  );
};

export default Video;
