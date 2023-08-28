// Node redis Client
import redis from 'redis';
// import { promisify } from 'util';

const client = redis.createClient();
// const connectStatus = await client.connect();
client.on('error', (err) => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => console.log('Redis client connected to the server'));

client.hset('4-redis_advanced_op.js', 'Portland', '50', redis.print);
client.hset('4-redis_advanced_op.js', 'Seattle', '80', redis.print);
client.hset('4-redis_advanced_op.js', 'New York', '20', redis.print);
client.hset('4-redis_advanced_op.js', 'Bogota', '20', redis.print);
client.hset('4-redis_advanced_op.js', 'Cali', '40', redis.print);
client.hset('4-redis_advanced_op.js', 'Paris', '2', redis.print);

client.hgetall('4-redis_advanced_op.js', (err, object) => {
  // test for error
  if (err) {
    console.log('Error', err);
    return;
  }
  console.log(object);
});
