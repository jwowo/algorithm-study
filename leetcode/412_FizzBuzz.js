/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let answer = [];
    const fizzBuzzObj = { 3: 'Fizz', 5: 'Buzz' }
    
    for (let num = 1; num <= n; num++) {
        let word = '';
        
        for (let key of Object.keys(fizzBuzzObj)) {
            if (num % key === 0) {
                word += fizzBuzzObj[key];
            }
        }
        
        if (!word) {
            word = num.toString();
        }
        
        answer.push(word);
    }
    
    return answer;
};
