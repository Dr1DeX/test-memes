import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Grid, Card, CardMedia, Typography } from '@material-ui/core';
import { io } from 'socket.io-client';

const socket = io("http://localhost:8001");

const App = () => {
  const [memes, setMemes] = useState([]);
  const [image, setImage] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8001/memes")
      .then(response => setMemes(response.data))
      .catch(error => console.error(error));

    socket.on("connect", () => {
      console.log("Connected to WebSocket");
    });

    socket.on("new_image", data => {
      setImage(data);
    });

    return () => {
      socket.off("new_image");
    };
  }, []);

  return (
    <Container>
      <Grid container spacing={3}>
        {memes.map(meme => (
          <Grid item xs={12} sm={6} md={4} key={meme.id}>
            <Card>
              <CardMedia
                component="img"
                alt={meme.text}
                height="140"
                image={meme.image}
                title={meme.text}
              />
              <Typography variant="h5" component="h2">
                {meme.text}
              </Typography>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default App;
