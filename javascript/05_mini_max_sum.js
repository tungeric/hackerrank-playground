// MINI MAX SUM
// input: 1, 2, 3, 4, 5
// output: 10 14

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
  input_stdin += data;
});

process.stdin.on('end', function () {
  input_stdin_array = input_stdin.split("\n");
  main();
});

function readLine() {
  return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function miniMaxSum(arr) {
  // Complete this function
  let total = arr.reduce(add, 0);
  partial = arr.map((el) => total - el);
  console.log(`${Math.min(...partial)} ${Math.max(...partial)}`);
}

function add(a, b) {
  return a + b;
}

function main() {
  arr = readLine().split(' ');
  arr = arr.map(Number);
  miniMaxSum(arr);

}
