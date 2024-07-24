// src/pages/CreatePostPage.js
import React, { useState } from 'react';
import api from '../api';
import { Box, Button, TextField, Typography } from '@mui/material';

const CreatePostPage = () => {
    const [title, setTitle] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        await api.post('/', { title});
        setTitle('');
    };

    return (
        <Box
            component="form"
            sx={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                '& .MuiTextField-root': { m: 1, width: '25ch' },
                margin: '20px auto',
                maxWidth: 500
            }}
            onSubmit={handleSubmit}
        >
            <Typography variant="h6" gutterBottom>Create New Post</Typography>
            <TextField
                label="Title"
                variant="outlined"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
            />
           
            <Button type="submit" variant="contained" color="primary">Submit</Button>
        </Box>
    );
};

export default CreatePostPage;
