// Node redis Client
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
// const connectStatus = await client.connect();
client.on('error', (err) => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  // Sets the redis value and displays a confirmation message
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  // gets the redis value and displays a confirmation message
  try {
    const asyncGet = promisify(client.get).bind(client);
    const result = await asyncGet(schoolName);
    console.log(result);
  } catch (err) {
    console.log('Get Error', err);
  }
}

displaySchoolValue('Holberton')
  .then(() => setNewSchool('HolbertonSanFrancisco', '100'))
  .then(() => displaySchoolValue('HolbertonSanFrancisco'));
