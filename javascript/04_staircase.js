// STAIRCASE
// Input: 6
// Output:      #
        //     ##
        //    ###
        //   ####
        //  #####
        // ######

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

function staircase(n) {
  // Complete this function
  for (i = 1; i <= n; i++) {
    let row = ""
    for (j = 0; j < n; j++) {
      if (j <= n - 1 - i) {
        row += " ";
      } else {
        row += "#";
      }
    }
    console.log(row)
  }
}

function main() {
  var n = parseInt(readLine());
  staircase(n);

}
