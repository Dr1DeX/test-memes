// src/pages/HomePage.js
import axios from "axios"
import React, { useEffect, useState } from 'react';
import api from '../api';
import PostCard from '../components/PostCard';

const HomePage = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const fetchPosts = async () => {
            const response = await axios.get('http://localhost:8001/memes');
            setPosts(response.data);
        };
        fetchPosts();
    }, []);

    const handleEdit = (id) => {
        // Implement edit functionality
    };

    const handleDelete = async (id) => {
        await api.delete(`/${id}`);
        setPosts(posts.filter(post => post.id !== id));
    };

    return (
        <div>
            {posts.map((post) => (
                <PostCard key={post.id} post={post} onEdit={handleEdit} onDelete={handleDelete} />
            ))}
        </div>
    );
};

export default HomePage;
