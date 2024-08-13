const fs = require('fs');
fs.writeFile('input.txt', "hellljhcbaucjzcgvugvgvcugdsvugvugv", (err) => {
    if (err) {
        console.error('Error writing to input.txt:', err);
        return;
    }
    fs.readFile('input.txt', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading input.txt:', err);
            return;
        }
        fs.writeFile('output.txt', data, (err) => {
            if (err) {
                console.error('Error writing to output.txt:', err);
            } else {
                console.log('Data successfully written to output.txt');
            }
        });
    });
});
