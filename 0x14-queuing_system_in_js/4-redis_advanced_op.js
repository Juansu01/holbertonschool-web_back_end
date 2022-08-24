import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => console.log('Redis client connected to the server'));

function main() {
  const key = 'HolbertonSchools';
  const keyNames = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
  const values = [50, 80, 20, 20, 40, 2];

  keyNames.forEach((k, i) => {
    client.hset(key, k, values[i], redis.print);
  });

  client.hgetall(key, (err, value) => {
    console.log(value);
  })
}

main();
