import { createClient} from 'redis';

const client = createClient({
    url: 'redis://localhost:6379'
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Reids client not connected to the server: ${err.message}`);
});

client.on('ready', () => {
    console.log('Redis client is ready to use');
});

client.connect().catch((err) => {
    console.log(`Redis client connection error: ${err.message}`);
});
