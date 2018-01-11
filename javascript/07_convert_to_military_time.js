// Convert time to military time
// Input: 07:05:45PM
// Output: 19:05:45

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

function timeConversion(s) {
  // Complete this function
  let sCopy = s.slice();
  let sRemainder = sCopy.substring(2, sCopy.length - 2)
  let hour = sCopy.substring(0, 2);
  let amPm = sCopy.substring(sCopy.length - 2, sCopy.length)
  if (amPm === "AM") {
    if (hour === '12') {
      hour = '00';
    }
  } else {
    if (hour !== '12') {
      hour = (parseInt(hour) + 12).toString();
    }
  }
  return `${hour}${sRemainder}`;
}

function main() {
  var s = readLine();
  var result = timeConversion(s);
  process.stdout.write("" + result + "\n");

}
