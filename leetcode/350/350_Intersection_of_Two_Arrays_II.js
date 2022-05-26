/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    let answer = [];
    
    for(let i = 0; i < nums2.length; i++){
           let val = nums2[i];
           if (nums1.includes(val)) {
               let temp = nums1.splice(nums1.indexOf(val), 1);
               final.push(val);
           }
    }
    return answer;
};
