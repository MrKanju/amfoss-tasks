const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the number of rows: ', (answer) => {
    const rows = parseInt(answer);

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < rows - i - 1; j++) {
            process.stdout.write(" ");
        }
        for (let j = 0; j <= i; j++) {
            process.stdout.write("* ");
        }
        console.log();
    }
    for (let i = 0; i < rows - 1; i++) {
        for (let j = 0; j <= i; j++) {
            process.stdout.write(" ");
        }
        for (let j = 0; j < rows - i - 1; j++) {
            process.stdout.write("* ");
        }
        console.log();
    }

    rl.close();
});
