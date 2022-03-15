import React, {useState} from 'react';
import {Grid, Box, TextField, Button, InputAdornment} from "@mui/material"
import {AccountBoxOutlined, LockOutlined} from "@mui/icons-material";


const App: React.FC = () => {
    
    const [password, setPassword] = useState('');
    const [username, setUsername] = useState('');
    
  return (
    <div>
      <Grid container style={{minHeight: "100vh"}}>
        <Grid item xs={12} sm={6}>
            <Box
              sx={{
                width: 1,
                height: 1,
                backgroundColor: 'primary.dark',
              }}
            />
        </Grid>
        <Grid container item xs={12} sm={6} style={{padding: "10"}}>
            <div />
            <Grid container justifyContent="center" alignItems="center" direction="column">
                <Grid container justifyContent="center" alignItems="center" direction="column">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="logo" width={100}/>
                </Grid>
                <TextField 
                    required
                    label="Username" 
                    margin="normal" 
                    value={username}
                    onChange={(event) => {setUsername(event.target.value)}}
                    InputProps={{ 
                        startAdornment: (
                            <InputAdornment position="start">
                                <AccountBoxOutlined />
                            </InputAdornment>
                        )
                    }}
                />
                <TextField
                    required    
                    label="Password" 
                    margin="normal" 
                    type="password"
                    value={password}
                    autoComplete="current-password"
                    onChange={(event) => {setPassword(event.target.value)}}
                    InputProps={{ 
                    startAdornment: (
                        <InputAdornment position="start">
                            <LockOutlined />
                        </InputAdornment>
                    )
                }}
                />
                <div style={{ height: 20}} />
                <Button 
                    color="primary" 
                    variant="contained"
                >
                    Log in
                </Button>
                <div style={{ height: 20}} />
                <Button 
                    onClick={() => {
                        alert('redirect to contacts page');
                    }}
                >
                    Interested in a Demo?
                </Button>
            </Grid>
            <Grid container justifyContent="center" alignItems="center" spacing={2}>
                <Grid item>
                    <Button
                        onClick={() => {
                            alert('go to github page');
                    }}
                    >
                    Interested in the Source Code?
                    </Button>
                </Grid>
                <Grid item>
                    <Button 
                        variant="outlined"
                        onClick={() => {
                            alert('go to forgot password page');
                    }}
                    >
                    Forgot Password?
                    </Button>
                </Grid>
            </Grid>
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
