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

function diagonalDifference(a) {
  // Complete this function
  let primSum = 0;
  let secSum = 0;
  let idx = 0;
  while (idx < a.length) {
    primSum += a[idx][idx];
    secSum += a[idx][a.length - 1 - idx];
    idx += 1;
  }
  return Math.abs(primSum - secSum);
}

function main() {
  var n = parseInt(readLine());
  var a = [];
  for (a_i = 0; a_i < n; a_i++) {
    a[a_i] = readLine().split(' ');
    a[a_i] = a[a_i].map(Number);
  }
  var result = diagonalDifference(a);
  process.stdout.write("" + result + "\n");

}
