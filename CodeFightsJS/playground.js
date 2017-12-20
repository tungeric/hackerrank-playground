// ARRAYS
function firstNotRepeatingCharacter(s) {
  let counter = {};
  s.split('').forEach((char) => {
    if (counter[char] === undefined) {
      counter[char] = 1;
    } else {
      counter[char] += 1;
    }
  });
  let firstNotRepeatedChar = '_';
  for (i = 0; i < Object.keys(counter).length; i++) {
    let key = Object.keys(counter)[i];
    if (counter[key] === 1) {
      firstNotRepeatedChar = key;
      break;
    }
  }
  return firstNotRepeatedChar;
}

//---

function rotateImage(a) {
  const n = a.length;
  const updated = new Array();
  for (i = 0; i < n; i++) {
    updated[i] = new Array();
    for (j = 0; j < n; j++) {
      updated[i][j] = false;
    }
  }
  let tempOldData = null;
  let tempNewData = null;
  let iOld = null;
  let jOld = null;
  let iNew = null;
  let jNew = null;
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      if (updated[i][j] === false) {
        iOld = i;
        jOld = j;
        iNew = j;
        jNew = n - 1 - i;
        while (updated[iNew][jNew] === false) {
          tempNewData = a[iNew][jNew];
          a[iNew][jNew] = tempOldData || a[iOld][jOld];
          updated[iNew][jNew] = true;
          iOld = iNew;
          jOld = jNew;
          iNew = jOld;
          jNew = n - 1 - iOld;
          tempOldData = tempNewData;
        }
        tempOldData = null;
        tempNewData = null;
      }
    }
  }
  return a;
}

// --- sudoku

function sudoku2(grid) {
  let isValid = true;
  for (i = 0; i < 9; i++) {
    for (j = 0; j < 9; j++) {
      if (grid[i][j] !== '.') {
        // check rows, columns
        for (m = 0; m < 9; m++) {
          if (m !== j && grid[i][m] === grid[i][j]) {
            isValid = false;
            break;
          }
          if (m !== i && grid[m][j] === grid[i][j]) {
            isValid = false;
            break;
          }
        }

        // check subgrid
        for (m = i - (i % 3); m < i - (i % 3) + 3; m++) {
          for (n = j - (j % 3); n < j - (j % 3) + 3; n++) {
            if (m !== i && n !== j && grid[m][n] === grid[i][j]) {
              isValid = false;
              break;
            }
          }
        }

      }
    }
  }
  return isValid;
}
