import { Box, Typography, Button } from "@mui/material";
import { styled } from "@mui/material/styles";
import axios from "axios";
import "./Home.css";

const StyledButton = styled(Button)({
  "&:hover": {
    backgroundColor: "#5671FF",
    boxShadow: "none",
  },
  "background-color": "#6981FF",
});

const StyledBox = styled(Box)({
  flex: 2,
  border: "dashed #6981FF",
  borderWidth: "2px",
  position: "relative",
});

const CenteredBox = styled(Box)({
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
});

const CenteredButton = styled(StyledButton)({
  position: "absolute",
  top: "120%",
  left: "50%",
  transform: "translate(-50%, 0%)",
});

const ContainerBox = styled(Box)({
  height: "100vh",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
});

const Home = ({ onUpload }) => {
  const handleSubmit = async (e) => {
    // get the file from the input
    const video = e.target.files[0];

    axios
      .post(
        "http://localhost:8000/add-music",
        {
          file: video,
        },
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          timeout: 1000_000,
        }
      )
      .then((res) => {
        console.log("asdjfklsadjf klsajfd ksd");
        console.log(video.name);
        onUpload(video.name);
      })
      .catch((err) => {
        console.log(err);
      });

    e.preventDefault();
  };

  return (
    <ContainerBox>
      <video className='videoTag' autoPlay loop muted>
        <source src={"sample.mp4"} type='video/mp4' />
      </video>
      <Box sx={{ height: "30vh", padding: "40px", display: "flex" }}>
        <Box sx={{ flex: 2 }}>
          <Typography variant="h2">We make video editing easy</Typography>
          <Typography variant="h4" sx={{ color: "#939393" }}>
            Automatically generated background music and high-quality captions
            for any video
          </Typography>
        </Box>
        <StyledBox sx={{ flex: 2, marginLeft: "200px", backgroundColor: "#F5F5F5" }}>
          <CenteredBox>
            <form onSubmit={handleSubmit}>
              <CenteredButton
                type="file"
                name="file"
                component="label"
                variant="contained"
              >
                Upload
                <input
                  type="file"
                  hidden
                  onChange={(e) => {
                    handleSubmit(e);
                  }}
                />
              </CenteredButton>
            </form>

            <Typography sx={{ top: "40%", textAlign: "center" }} variant="h4">
              Drop files or upload files here
            </Typography>
          </CenteredBox>
        </StyledBox>
      </Box>
    </ContainerBox>
  );
};

export default Home;
