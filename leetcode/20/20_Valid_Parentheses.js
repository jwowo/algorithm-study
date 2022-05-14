/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  pares = [];

  for (let i = 0; i < s.length; i++) {
    console.log(pares);

    if (s[i] === '(') {
      pares.push('(');
      continue;
    }
    if (s[i] === '{') {
      pares.push('{');
      continue;
    }
    if (s[i] === '[') {
      pares.push('[');
      continue;
    } else {
      if (pares.length === 0) {
        return false;
      } else {
        if (s[i] === ')' && pares[pares.length - 1] !== '(') {
          return false;
        }
        if (s[i] === ']' && pares[pares.length - 1] !== '[') {
          return false;
        }
        if (s[i] === '}' && pares[pares.length - 1] !== '{') {
          return false;
        }
        pares.pop();
      }
    }
  }
  console.log(pares);

  if (pares.length === 0) {
    return true;
  } else {
    return false;
  }
};
