/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const count = {};
    
    for (let num of nums) {
        if (count[num]) {
            return true
        } else {
            count[num] = 1;
        }
    }
    
    return false;
};
