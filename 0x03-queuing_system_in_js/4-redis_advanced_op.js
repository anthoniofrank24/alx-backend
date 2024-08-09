import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
    setHolbertonSchools();
});

client.on('ready', () => {
    console.log('Redis client is ready to use');
});

function setHolbertonSchools() {
    const schools = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2
    };

    for (const [city, value] of Object.entries(schools)) {
        client.hset('HolbertonSchools', city, value, (err, res) => {
            if (err) {
                console.error(`Error setting value for ${city}: ${err.message}`);
            } else {
                console.log(`Reply: ${res}`);
            }
        });
    }

    displayHolbertonSchools();
}

function displayHolbertonSchools() {
    client.hgetall('HolbertonSchools', (err, result) => {
        if (err) {
            console.error(`Error fetching data: ${err.message}`);
        } else {
            console.log(result);
        }
    });
}
