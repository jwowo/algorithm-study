function solution(numbers) {
  let answer = 0;
  const list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  for (n of list) {
    if (!numbers.includes(n)) {
      answer += n;
    }
  }

  return answer;
}
