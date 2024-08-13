const fs = require('fs');
fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) throw err;
    const rows = parseInt(data.trim());
    let diamond = '';
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < rows - i - 1; j++) {
            diamond += " ";
        }
        for (let j = 0; j <= i; j++) {
            diamond += "* ";
        }
        diamond += '\n';
    }
    for (let i = 0; i < rows - 1; i++) {
        for (let j = 0; j <= i; j++) {
            diamond += " ";
        }
        for (let j = 0; j < rows - i - 1; j++) {
            diamond += "* ";
        }
        diamond += '\n';
    }
    fs.writeFile('output.txt', diamond, (err) => {
        if (err) throw err;
        console.log('Diamond');
    });
});
