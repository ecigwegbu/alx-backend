// Can I have a seat?
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

// Redis
const client = redis.createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => console.log('Redis client connected to the server'));

// reserve 'number' of seats in redis
function reserveSeat(number) {
  client.set('available_seats', number, redis.print);
}

// retrieve number of available seats from redis
const reservationEnabled = true;
async function getCurrentAvailableSeats() {
  // use try/catch when calling it
  const asyncGet = promisify(client.get).bind(client);
  const result = await asyncGet('available_seats');
  return result;
}

// Kue Queue
const queue = kue.createQueue();

// Server
const app = express();
const hostname = '127.0.0.1';
const port = 1245;

// Server
// Get available seats
app.get('/available_seats', async (req, res) => {
  try {
    const available_seats = await getCurrentAvailableSeats();
    return res.status(200).send({numberOfAvailableSeats: available_seats});
  } catch (err) {
    // throw err
    return res.status(500).json({Error: 'Redis Error'});
  }
});

// reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.status(503).send({ status: 'Reservation are blocked' });
  }
  const jobData = {
    jobId: 1,
    message: 'Reserve a seat for me',
  };
  const job = queue.create('reserve_seat', jobData).save((err) => {
    if (err) {
      res.status(500).send({ status: 'Reservation failed' });
    }
    res.status(200).send({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    // throw err;
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

function processQueue() { // helper function
  queue.process('reserve_seat', (job, done) => {
    done();
  });
}

// Process the jobs on the queue
app.get('/process', async (req, res) => {
  let available_seats;
  try {
    available_seats = await getCurrentAvailableSeats();
  } catch (err) {
    res.status(500).json({ Error: 'Redis Error' });
    res.end();
    return;
  }
  available_seats -= 1;
  if (available_seats < 0) {
    res.status(503).json('Error: Not enough seats available');
    res.end();
    return;
  } else if (available_seats === 0) {
    reservationEnabled = false;
  }
  processQueue();
  reserveSeat(available_seats);
  res.status(200).send({ status: 'Queue processing' });
  return;
});

reserveSeat(50); // initialise available_seats
app.listen(port, hostname);
