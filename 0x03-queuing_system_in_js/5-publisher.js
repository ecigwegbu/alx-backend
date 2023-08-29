// Node redis Client
import redis from 'redis';
// import { promisify } from 'util';

const client = redis.createClient();

const channel = 'holberton school channel';
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish(channel, message);
  }, time);
}

function publishMessages() {
  publishMessage('Holberton Student #1 starts course', 100);
  publishMessage('Holberton Student #2 starts course', 200);
  publishMessage('KILL_SERVER', 300);
  publishMessage('Holberton Student #3 starts course', 400);
}

// const connectStatus = await client.connect();
client.on('error', (err) => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => {
  console.log('Redis client connected to the server');
  // Now that we're ready, publish messages!
  publishMessages();
});
