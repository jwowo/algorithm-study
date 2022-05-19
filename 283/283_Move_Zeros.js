/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let count = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            nums.splice(i, 1);
            i -= 1;
            count += 1;
        }
    }
    
    while (count > 0) {
        nums.push(0);
        count -= 1;
    }
    
    return nums;
};
