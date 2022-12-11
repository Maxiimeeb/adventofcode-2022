const fs = require('fs');

// Read the contents of the input file.
const input = fs.readFileSync('input.txt', 'utf8');

// Parse the input into an array of integers, where each element
// represents the number of Calories in a food item.
const elves = input.split('\r\n\r\n').map((elf) => elf.split('\r\n').map(Number));

console.log(elves);

// Sort the array in descending order.
const elfCalories = elves.map((elf) => elf.reduce((sum, c) => sum + c, 0));

// Find the sum of the top three Elves carrying the most Calories.
const topThree = elfCalories.sort((a, b) => b - a).slice(0, 3).reduce((sum, c) => sum + c, 0);

// Print the result.
console.log(topThree);