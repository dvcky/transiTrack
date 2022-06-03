const https = require('https');
    https.get(
      "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
      { headers: { "x-api-key": 'PTdOahGWGZ3fmscVAZQYf9Z3HwwX1VZl9tSZgTKk'}
      },
      (resp) => {
        resp.on('data', (chunk) => {
          console.log("Receiving Data");
        });
        resp.on('end', () => {
          console.log("Finished receiving data");
console.log(resp.body);
        });
      }).on("error", (err) => {
        console.log("Error: " + err.message);
      });