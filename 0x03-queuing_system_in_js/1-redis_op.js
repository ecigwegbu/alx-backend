// Node redis Client
import redis from 'redis';

const client = redis.createClient();
// const connectStatus = await client.connect();
client.on('error', (err) => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  // Sets the redis value and displays a confirmation message
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  // gets the redis value and displays a confirmation message
  client.get(schoolName, (error, value) => {
    if (error) {
      console.log('Get Error', error);
    } else {
      console.log(value);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
