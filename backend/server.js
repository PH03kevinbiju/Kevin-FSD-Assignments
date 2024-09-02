const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB Atlas connection
const uri = "mongodb+srv://kevinbiju000:kevinbiju12345@cluster0.xhpdm.mongodb.net/"; // Replace with your actual connection string
mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("Connected to MongoDB Atlas"))
    .catch(err => console.error("Could not connect to MongoDB Atlas", err));

// User Schema
const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
});

const User = mongoose.model('User', userSchema);

// API Route for signup
app.post('/api/signup', async (req, res) => {
    const { name, email, password } = req.body;

    try {
        // Check if the user already exists
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ message: "User already exists" });
        }

        // Create a new user
        const newUser = new User({ name, email, password });
        await newUser.save();

        res.status(201).json({ message: "User created successfully" });
    } catch (err) {
        console.error("Error during signup:", err);
        res.status(500).json({ message: "Server error" });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
