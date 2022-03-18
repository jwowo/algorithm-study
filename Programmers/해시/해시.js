function solution(participant, completion) {
  var answer = '';
  // let runner = participant.filter(person => !completion.includes(person)); // 동명이인 처리 문제

  participant.sort();
  completion.sort();
  console.log(participant);
  console.log(completion);

  for (const index of completion.keys()) {
    if (participant[index] != completion[index]) {
      answer = participant[index];
      break;
    }
  }
  if (answer === '') {
    answer = participant[participant.length - 1];
  }

  return answer;
}
