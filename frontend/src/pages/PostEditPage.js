import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Box, Button, TextField, Typography, CircularProgress } from '@mui/material';

const EditPostPage = () => {
  const { id } = useParams();
  const [post, setPost] = useState({ text: '', image_url: '' });
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPost = async () => {
      try {
        const response = await axios.get(`/api/v1/memes/${id}`);
        setPost(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching post:', error);
        setLoading(false);
      }
    };
    fetchPost();
  }, [id]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setPost((prev) => ({ ...prev, [name]: value }));
  };

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('text', post.text);
    if (image) {
      formData.append('image', image);
    }

    try {
      await axios.put(`/api/v1/memes/${id}`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
    } catch (error) {
      console.error('Error updating post:', error);
    }
  };

  if (loading) {
    return <CircularProgress />;
  }

  return (
    <Box
      component="form"
      sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: 2 }}
      onSubmit={handleSubmit}
    >
      <Typography variant="h6" gutterBottom>Редактирование поста</Typography>
      <TextField
        label="Text"
        name="text"
        value={post.text}
        onChange={handleChange}
        variant="outlined"
        fullWidth
        margin="normal"
      />
      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
        style={{ marginBottom: '16px' }}
      />
      <Button type="submit" variant="contained" color="primary">Сохранить изменения</Button>
    </Box>
  );
};

export default EditPostPage;
