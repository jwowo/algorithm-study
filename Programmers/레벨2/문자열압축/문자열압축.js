function solution(s) {
  let answer = s.length;

  for (let i = 1; i <= parseInt(s.length / 2); i++) {
    let compressLength = i;
    let currentCompressStr = '';
    let compareCompressStr = '';
    let count = 1;
    let compressResult = '';
    let startIdx = 0;
    let endIdx = i;

    while (endIdx <= s.length) {
      currentCompressStr = s.substring(startIdx, endIdx);
      compareCompressStr = s.substring(endIdx, endIdx + compressLength);

      startIdx += compressLength;
      endIdx += compressLength;

      if (currentCompressStr === compareCompressStr) {
        count += 1;
      } else {
        if (count == 1) compressResult += currentCompressStr;
        else compressResult += count + currentCompressStr;
        count = 1;
      }
    }

    if (endIdx - compressLength < s.length) {
      compressResult += s.substring(endIdx - compressLength, s.length + 1);
    }

    // console.log(`compress Length : ${compressLength}`);
    // console.log(`compress Result : ${compressResult}`);
    // console.log(`compress Result Length : ${compressResult.length}`);
    // console.log('');

    answer = Math.min(answer, compressResult.length);
  }

  return answer;
}

// 문제 풀이 걸린 시간 : 47분 31초
