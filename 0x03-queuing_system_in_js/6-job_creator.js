// create a single Kue job
const kue = require('kue');

const queue = kue.createQueue();

const notification = {
  phoneNumber: '+1-222-555-7777',
  message: 'He is alive!',
};

const job = queue.create('push_notification_code', notification).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
