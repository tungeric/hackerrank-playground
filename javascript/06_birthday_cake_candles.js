// Birthday cake candles - show row of candles that person will blow out next (next tallest row)
// Input: n = 4, ar = [3, 2, 1, 3]
// Output: 2

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

function birthdayCakeCandles(n, ar) {
  // Complete this function
  let counter = {};
  let max = 0;
  ar.forEach((height) => {
    if (counter[height] == undefined) {
      counter[height] = 1;
    } else {
      counter[height] += 1;
    }
    if (height > max) {
      max = height;
    }
  })
  return counter[max];
}

function main() {
  var n = parseInt(readLine());
  ar = readLine().split(' ');
  ar = ar.map(Number);
  var result = birthdayCakeCandles(n, ar);
  process.stdout.write("" + result + "\n");

}
