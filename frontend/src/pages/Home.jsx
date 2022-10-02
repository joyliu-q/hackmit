import { Box, Typography, Button } from '@mui/material';
import { styled } from '@mui/material/styles';


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


    return (
        <ContainerBox>
            <Box sx={{ height: '30vh', padding: '40px', display: 'flex' }}>
                <Box sx={{ flex: 2}}>
                    <Typography variant="h2">We make video editing easy</Typography>
                    <Typography variant="h4" sx={{color: '#939393'}}>Automatically generated background music and high-quality captions for any video</Typography>
                </Box>
                <StyledBox sx={{flex: 2, marginLeft: '200px'}}>
                    <CenteredBox>
                         <form
                            action="http://0.0.0.0:8000/add-music"
                            method="POST"
                            encType="multipart/form-data"
                        >
                            <CenteredButton type="file" name="file" component="label" variant="contained">Upload<input type="file" hidden onChange={'form.submit()'}></input></CenteredButton>
                        </form>

                        <Typography sx={{top: '40%', textAlign: 'center'}}variant="h4">Drop files or upload files here</Typography>
                        
                    </CenteredBox>
                </StyledBox>
            </Box>

        </ContainerBox>
    )
}

export default Home