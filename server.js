
const WebSocket = require('ws');




// Create a WebSocket server

const wss = new WebSocket.Server({ port: 8080 });




console.log('WebSocket server started');

// Handle incoming WebSocket connections

wss.on('connection', (ws) => {

    console.log('WebSocket connection established');




    ws.on('message', (message) => {
        try {
            console.log('Received message:', JSON.parse(message.toString()).event);

        } catch(e) {
            console.log(`Received message: ${message.toString()}`)
        }


    });

    ws.on('close', () => {

        console.log('WebSocket connection closed');

    });

});




const client = new WebSocket('ws://localhost:8080');




client.on('open', () => {

    console.log('WebSocket client connected');

    client.send('Hello from WebSocket client');

});




