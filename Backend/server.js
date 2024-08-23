const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 3000;

// Middleware to parse form data
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files from 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Login route
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    
    // Simple validation (you can replace this with actual database checks)
    if (username === 'testuser' && password === 'password123') {
        res.send('Login successful!');
    } else {
        res.send('Invalid username or password.');
    }
});

// Registration route
app.post('/register', (req, res) => {
    const { username, email, password, confirmPassword } = req.body;
    
    // Simple validation
    if (!username || !email || !password || !confirmPassword) {
        return res.send('All fields are required.');
    }
    
    if (password !== confirmPassword) {
        return res.send('Passwords do not match.');
    }

    // You can replace this with actual database storage
    res.send('Registration successful!');
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
