const express = require('express');
const app = express();
const port = 3000;
const connectDB = require('./config/db');

// connect database

connectDB();

app.get('/', (req, res) => res.send("Hello world!"));

app.listen(port, ()=>{
    console.log(`App.js listening on port ${port}`)
})