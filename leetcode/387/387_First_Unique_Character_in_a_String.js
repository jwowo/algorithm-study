/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let count = {};
    
    for (let i = 0; i < s.length; i++) {
        if (count[s[i]]) {
            count[s[i]] += 1;
        } else {
            count[s[i]] = 1;
        }
    }
    
    let answer = -1;
    let nonRepeatChar = '';
    let nonRepeatIndex = 100001;
    
    for (let key of Object.keys(count)) {
        if (count[key] < 2) {
            nonRepeatChar = key;
            nonRepeatIndex = Math.min(nonRepeatIndex, s.indexOf(key));
        }
    }
    
    if (nonRepeatIndex !== 100001) {
        answer = nonRepeatIndex;
    }
    
    return answer;
};
