/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function (s, t) {
  let sArray = [];
  let tArray = [];

  let shortLength = s.length > t.length ? t.length : s.length;

  for (let i = 0; i < shortLength; i++) {
    // s 값 확인
    if (s[i] === '#' && sArray) {
      sArray.pop();
    } else {
      sArray.push(s[i]);
    }

    // t 값 확인
    if (t[i] === '#' && tArray) {
      tArray.pop();
    } else {
      tArray.push(t[i]);
    }
  }

  if (s.length > t.length) {
    for (let i = shortLength; i < s.length; i++) {
      if (s[i] === '#' && sArray) {
        sArray.pop();
      } else {
        sArray.push(s[i]);
      }
    }
  } else if (s.length < t.length) {
    for (let i = shortLength; i < t.length; i++) {
      if (t[i] === '#' && tArray) {
        tArray.pop();
      } else {
        tArray.push(t[i]);
      }
    }
  }

  let sResult = sArray.join('');
  let tResult = tArray.join('');

  // return
  if (sResult === tResult) return true;
  else return false;
};

// 개선점 1 : 배열과 문자열 변수 사용하지 않고 풀 수 있을 것 같다.
// 개선점 2 : for문을 2 * N 만큼 도는데 N 으로 줄이기
