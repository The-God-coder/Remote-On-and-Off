const connectionString = '<Database URI>';
const express = require('express')
const { Client } = require('pg');
app = express()
const http = require('http').Server(app)
const io = require('socket.io')(http);

const path = require('path')
const PORT = process.env.PORT || 5000


const client = new Client({
  connectionString: connectionString,
  ssl: { rejectUnauthorized: false }
});

client.connect();

app.get('/', (req, res) => res.sendFile(path.join(__dirname, 'index.html')))
http.listen(PORT, function() {
    console.log('listening on *:'+PORT);
 });

 io.on('connection', function(socket) {
    console.log('A user connected');
 
    socket.on('on', () => {
        console.log('on') 
        
            client.query("INSERT INTO onoff(onoff)VALUES('on')", (err, res) => {
                 if(err) throw err;
             })
         
     })
    
     socket.on('off', () => {
         console.log('off')
        
            client.query("INSERT INTO onoff(onoff)VALUES('off')", (err, res) => {
                if(err) throw err;
            })
        
    })
 });

