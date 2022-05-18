/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let count = {};
    
    for (let num of nums) {
        if (count[num]) {
            count[num] += 1;
        } else {
            count[num] = 1;
        }
    }
    
    for (let k of Object.keys(count)) {
        if(count[k] === 1) {
            return k;
        }
    }
    
};
