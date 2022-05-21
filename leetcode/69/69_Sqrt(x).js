/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let start = 0;
    let end = x;
    
    if (x === 0 || x === 1) {
        return x;
    }
    
    while (start <= end) {
        let mid = parseInt((start + end) / 2);
        let squared = mid * mid;
        
        if (squared === x) {
            return mid;
        } else if (squared > x) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    
    return end;
};
