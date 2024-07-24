import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { Link } from "react-router-dom";

const Header = () => {
    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1}}>
                    <Link to="/" style={{ textDecoration: 'none', color: 'inherit'}}>Смешнявка</Link>
                </Typography>
                <Button color='inherit' component={Link} to="/create-post">Создать мемес</Button>
            </Toolbar>
        </AppBar>
    )
}

export default Header;