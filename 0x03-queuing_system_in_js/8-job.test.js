// Tests for the Kue job creation module
import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('add jobs to queue', () => {
    const jobs = [
      { phoneNumber: '+1-234-8039799', message: 'He is alive!' },
      { phoneNumber: '+44-800-2678971', message: 'The Eagle has landed' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({ phoneNumber: '+1-234-8039799', message: 'He is alive!' });
  });

  it('throws error when not an array', () => {
    expect(() => {
      createPushNotificationsJobs('notAnArray', queue);
    }).to.throw('Jobs is not an array');
  });
});
