import axios from "axios"
import React, { useEffect, useState } from 'react';
import api from '../api';
import PostCard from '../components/PostCard';
import { useNavigate } from "react-router-dom"

const HomePage = () => {
    const [posts, setPosts] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchPosts = async () => {
            const response = await axios.get('/api/v1/memes');
            setPosts(response.data);
        };
        fetchPosts();
    }, []);

    const handleEdit = (id) => {
        navigate(`/edit-post/${id}`);
    };

    const handleDelete = async (id) => {
        await api.delete(`/api/v1/memes/${id}`);
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
