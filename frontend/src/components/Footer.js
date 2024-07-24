import React from "react";
import { Box, Typography } from "@mui/material";

const Footer = () => {
    return (
        <Box component="footer" sx={{ textAlign: 'center', padding: '20px', marginTop: 'auto'}}>
            <Typography variant="body2" color="textSecondary">
                &copy; 2024 Смешнявка. Все права защищены.
            </Typography>
        </Box>
    )
}

export default Footer;