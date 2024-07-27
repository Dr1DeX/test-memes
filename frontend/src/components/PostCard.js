import React from "react";
import { Card, CardContent, CardMedia, Typography, CardActions, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";

const PostCard = ({ post, onEdit, onDelete }) => {
    const navigate = useNavigate();

    const handleCardClick = () => {
        navigate(`/memes/${post.id}`);
    };
    
    return (
        <Card sx={{ maxWidth: 345, margin: '20px auto', display: 'flex', flexDirection: 'column',cursor: 'pointer' }} onClick={handleCardClick}>
            {post.image_url && (
                <CardMedia
                    component="img"
                    sx={{ height: 'auto', maxHeight: 350, objectFit: 'contain' }}
                    image={post.image_url}
                    alt="post image"
                />
            )}
            <CardContent sx={{ flexGrow: 1 }}>
                <Typography gutterBottom variant="h6" component="div">
                    {post.text}
                </Typography>
            </CardContent>
            <CardActions>
                <Button size="small" color="primary" onClick={() => onEdit(post.id)}>
                    Редактировать мемес
                </Button>
                <Button size="small" color="secondary" onClick={() => onDelete(post.id)}>
                    Удалить мемес
                </Button>
            </CardActions>
        </Card>
    );
};

export default PostCard;