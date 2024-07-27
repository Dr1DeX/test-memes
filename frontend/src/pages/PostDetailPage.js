import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Box, Typography, Button, CircularProgress } from '@mui/material';

const PostDetail = () => {
    const { id } = useParams();
    const [post, setPost] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchPost = async () => {
            try {
                const response = await axios.get(`/api/v1/memes/${id}`);
                setPost(response.data);
            } catch (error) {
                console.error('Error fetching post:', error);
            } finally {
                setIsLoading(false);
            }
        };
        fetchPost();
    }, [id]);

    const handleEdit = () => {
        navigate(`/edit-post/${id}`);
    };

    const handleDelete = async () => {
        await axios.delete(`/api/v1/memes/${id}`);
        navigate('/');
    };

    if (isLoading) {
        return <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}><CircularProgress /></Box>;
    }

    if (!post) {
        return <Typography>Post not found</Typography>;
    }

    return (
        <Box sx={{ padding: 2 }}>
            {post.image_url && (
                <Box sx={{ marginBottom: 2, textAlign: 'center' }}>
                    <img src={post.image_url} alt={post.text} style={{ maxWidth: '100%', height: 'auto' }} />
                </Box>
            )}
            <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                <Typography variant="h4" component="h1" gutterBottom>
                    {post.text}
                </Typography>
                <Box sx={{ marginTop: 2, display: 'flex', justifyContent: 'center' }}>
                    <Button variant="contained" color="primary" onClick={handleEdit} sx={{ marginRight: 1 }}>
                        Редактировать мемес
                    </Button>
                    <Button variant="contained" color="secondary" onClick={handleDelete} sx={{ marginLeft: 1 }}>
                        Удалить мемес
                    </Button>
                </Box>
            </Box>
        </Box>
    );
};

export default PostDetail;
