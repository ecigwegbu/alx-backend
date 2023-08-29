// Node redis Client
import { createClient } from 'redis';
// import { promisify } from 'util';

const client = createClient();
// const connectStatus = await client.connect();
client.on('error', (err) => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => {
  console.log('Redis client connected to the server');
  // Now we're ready, subscribe to the channel
  client.subscribe('holberton school channel');
});

// And now listen for the messages
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
