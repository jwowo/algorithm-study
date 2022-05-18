/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let answer = 0;
    
    let sum = {0 : 1};
    let acc = 0;
    
    for (const num of nums) {
        acc += num;
        
        if(sum[acc - k]) {
            answer += sum[acc - k];
        }
        
        if (sum[acc]) {
            sum[acc] += 1;
        } else {
            sum[acc] = 1
        }
    }
    
    console.log(sum);
    
    return answer;
};

//     let answer = 0;
//     let acc = 0;
    
//     const prefix = new Map();
//     prefix.set(0, 1);
    
//     for (const num of nums) {
//         acc += num;
        
//         if (prefix.has(acc-k)) {
//             answer += prefix.get(acc - k);
//         }
        
//         if (prefix.has(acc)) {
//             prefix.set(acc, prefix.get(acc) + 1);
//         } else {
//             prefix.set(acc, 1);
//         }
//     }
    
//     return answer;
// };
