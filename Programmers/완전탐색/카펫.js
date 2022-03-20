function solution(brown, yellow) {
  var answer = [];

  for (let row = 1; row <= yellow; row++) {
    column = yellow / row;
    if (!Number.isInteger(column)) {
      continue;
    }

    if (2 * row + 2 * column + 4 == brown) {
      answer = [row + 2, column + 2];
    }
  }
  return answer;
}
