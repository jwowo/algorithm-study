/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = {};
    
    for (let num of nums) {
        if (count[num]) {
            count[num] += 1;
        } else {
            count[num] = 1;
        }
    }
    
    let maxCount = 0;
    let answer = 0;
    
    for (let key of Object.keys(count)) {
        if (maxCount < count[key]) {
            maxCount = count[key];
            answer = key;
        }
    }
    
    return answer;
};
