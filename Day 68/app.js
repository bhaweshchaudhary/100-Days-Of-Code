const fs = require('fs');
// creating server
const port = 3000;
// 1. http module
const http = require('http');
const server = http.createServer((req, res) => {
    console.log("Request has been made from browser to server");
    // console.log(req);
    // console.log(req.method);
    // console.log(req.url)

    let path = './views';
    switch(req.url){
        case '/':
            path += '/index.html'
            res.statusCode = 200;
            break;
        case '/about':
            path += '/about.html'
            res.statusCode = 200;
            break;
        case '/about-me':
            res.statusCode=301;
            res.setHeader('Location', '/about');
            res.end()
        default:
            path += '/404.html'
            res.statusCode = 404;
            break;
    };

    fs.readFile(path, 'UTF-8', (err, fileData)=>{
        if(err){
            console.log(err);
        } else {
            res.end(fileData);
        }
    })
});

server.listen(port, 'localhost', ()=>{
    console.log(`Server is listening on port ${port}`)
}); // it accepts 3 arguments , port, host, callback function
