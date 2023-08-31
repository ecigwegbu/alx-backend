// Test for the Kue job creation module
import kue from 'kue';

const queue = kue.createQueue();

export default function createPushNotificationsJobs(jobs, queue) {
  // creates push notification jobs based on a given list of jobData and a queue
  jobs.forEach((jobData) => {
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
    const job = queue.create('push_notification_code_3', jobData).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}
