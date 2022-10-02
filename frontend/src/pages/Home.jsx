import { Box, Typography, Button } from '@mui/material';
import { styled } from '@mui/material/styles';
import Plyr from "plyr-react";
import "plyr-react/plyr.css";
import React, { useState } from 'react';

const axios = require("axios");

const StyledButton = styled(Button)({
    '&:hover': {
        backgroundColor: '#5671FF',
        boxShadow: 'none',
    },
    'background-color': '#6981FF',
})

const StyledBox = styled(Box)({
    flex: 2,
    border: 'dashed #6981FF',
    borderWidth: '2px',
    position: 'relative'


})


const CenteredBox = styled(Box) ({
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
})

const CenteredButton = styled(StyledButton) ({
    position: 'absolute',
    top: '120%',
    left: '50%',
    transform: 'translate(-50%, 0%)',
})



const ContainerBox = styled(Box) ({
    height: '100vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
})

const Home = () => {

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
      console.log(videoSrc)
      setVideoSrc(response.data.path);
    }
    
    return (
        <ContainerBox>
            <Box sx={{ height: '30vh', padding: '40px', display: 'flex' }}>
                <Box sx={{ flex: 2}}>
                    <Typography variant="h2">We make video editing easy</Typography>
                    <Typography variant="h4" sx={{color: '#939393'}}>Automatically generated background music and high-quality captions for any video</Typography>
                </Box>
                <StyledBox sx={{flex: 2, marginLeft: '200px'}}>
                    {videoSrc ? <Plyr  {
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
                    /> :
                        <CenteredBox>
                            {/* <form
                            action="http://0.0.0.0:8000/add-music"
                            method="POST"
                            encType="multipart/form-data"
                        >
                            <CenteredButton type="file" name="file" component="label" variant="contained">Upload<input type="file" hidden onChange={'form.submit()'}></input></CenteredButton>
                        </form> */}
                            <form onSubmit={handleSubmit}>
                                {/* <input type="file" id="video" name="video" accept="video/*" />
                            <input type="submit" value="Submit" /> */}
                                <CenteredButton type="file" name="file" component="label" variant="contained">Upload<input type="file" hidden onChange={'form.submit()'}></input></CenteredButton>
                            </form>

                            <Typography sx={{ top: '40%', textAlign: 'center' }} variant="h4">Drop files or upload files here</Typography>
                        
                        </CenteredBox>
                    }
                </StyledBox>
            </Box>
        </ContainerBox>
    )
}

export default Home