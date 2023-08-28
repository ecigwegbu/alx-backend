// Node redis Client
import redis from 'redis';
// import { createClient } from 'redis';

const client = redis.createClient();
// const connectStatus = await client.connect();
client.on('error', (err) => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => console.log('Redis client connected to the server'));

// await client.set('key', 'value');
// const value = await client.get('key');
// await client.disconnect();
