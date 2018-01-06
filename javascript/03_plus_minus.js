// input: arr = [-4 3 -9 0 4 1]
// output: console log
            // 0.500000
            // 0.333333
            // 0.166667

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

function plusMinus(arr) {
  // Complete this function
  let negCount = 0;
  let posCount = 0;
  let zeroCount = 0;
  let totalCount = arr.length;
  arr.forEach((el) => {
    char = el.toString()[0]
    switch (char) {
      case '-':
        negCount += 1;
        break;
      case '0':
        zeroCount += 1;
        break;
      default:
        posCount += 1;
    }
  })
  console.log((posCount / totalCount).toFixed(6));
  console.log((negCount / totalCount).toFixed(6));
  console.log((zeroCount / totalCount).toFixed(6));
}

function main() {
  var n = parseInt(readLine());
  arr = readLine().split(' ');
  arr = arr.map(Number);
  plusMinus(arr);

}
