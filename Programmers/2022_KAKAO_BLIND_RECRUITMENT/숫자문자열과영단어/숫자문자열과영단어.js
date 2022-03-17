function solution(s) {
  let numObj = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };

  for (num of Object.keys(numObj)) {
    if (s.includes(num)) {
      let regexAllCase = new RegExp(num, 'gi');
      s = s.replace(regexAllCase, numObj[num]);
    }
  }

  return parseInt(s);
}
