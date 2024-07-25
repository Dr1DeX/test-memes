import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import CreatePostPage from './pages/CreatePostPage';
import EditPostPage from './pages/PostEditPage';

const App = () => {
    return (
        <Router>
            <Header />
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/create-post" element={<CreatePostPage />} />
                <Route path="/edit-post/:id" element={<EditPostPage />} />
            </Routes>
            <Footer />
        </Router>
    );
};

export default App;
