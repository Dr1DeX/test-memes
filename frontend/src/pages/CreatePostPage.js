import React, { useState } from 'react';
import api from '../api';
import { Box, Button, TextField, Typography } from '@mui/material';

const CreatePostPage = () => {
    const [text, setText] = useState('');
    const [image, setImage] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append('text', text);
        if (image) {
            formData.append('image', image);
        }

        try {
            const response = await api.post('/memes', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log('Post created:', response.data);
            setText('');
            setImage(null);
        } catch (error) {
            console.error('Error creating post:', error);
        }
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
                maxWidth: 500,
            }}
            onSubmit={handleSubmit}
        >
            <Typography variant="h6" gutterBottom>Create New Post</Typography>
            <TextField
                label="Text"
                variant="outlined"
                value={text}
                onChange={(e) => setText(e.target.value)}
                required
            />
            <input
                type="file"
                onChange={(e) => setImage(e.target.files[0])}
                accept="image/*"
                style={{ margin: '10px 0' }}
            />
            <Button type="submit" variant="contained" color="primary">Submit</Button>
        </Box>
    );
};

export default CreatePostPage;
