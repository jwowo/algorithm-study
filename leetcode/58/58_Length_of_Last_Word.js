/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    // console.log(s.trim());
    // console.log(s.trim().split(' '));
    // console.log(s.trim().split(' ').slice(-1));
    // console.log(s.trim().split(' ').slice(-1)[0]);
    
    return s.trim().split(' ').slice(-1)[0].length;
};
