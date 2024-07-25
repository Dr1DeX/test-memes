import axios from "axios"
import React, { useEffect, useState } from 'react';
import api from '../api';
import PostCard from '../components/PostCard';
import { useNavigate } from "react-router-dom"
import { Box, Pagination, Typography, CircularProgress } from "@mui/material";

const HomePage = () => {
    const [posts, setPosts] = useState([]);
    const [page, setPage] = useState(1);
    const [pageSize] = useState(6);
    const [isLoading, setIsLoading] = useState(false);
    const [totalPosts, setTotalPosts] = useState(0);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchPosts = async () => {
            setIsLoading(true);
            try {
                const response = await axios.get(`/api/v1/memes`, {
                    params: {
                        page:page,
                        page_size: pageSize
                    }
                });
                setPosts(response.data[0]);
                setTotalPosts(response.data[1]);
            } catch (error) {
                console.error('Error fetching posts:', error);
            } finally {
                setIsLoading(false);
            }
        };
        fetchPosts();
    }, [page, pageSize]);

    const totalPages = Math.ceil(totalPosts / pageSize);
    
    const handlePageChange = (event, newPage) => {
        setPage(newPage);
    }

    const handleEdit = (id) => {
        navigate(`/edit-post/${id}`);
    };

    const handleDelete = async (id) => {
        await api.delete(`/api/v1/memes/${id}`);
        setPosts(posts.filter(post => post.id !== id));
    };

    return (
        <Box>
            {posts.map((post) => (
                <PostCard key={post.id} post={post} />
            ))}
            <Box sx={{ display: 'flex', justifyContent: 'center', marginTop: 2}}>
                <Pagination
                    count={totalPages}
                    page={page}
                    onChange={handlePageChange}
                    color="primary"
                />
            </Box>
        </Box>
    );
};

export default HomePage;