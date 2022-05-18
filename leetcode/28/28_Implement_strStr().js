/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for (let i = 0; i < haystack.length; i++) {
        let flag = false;
        
        for (let j = 0; j < needle.length; j++) {
            if(haystack[i + j] !== needle[j]) {
                flag = true;
            } 
        }
        
        if (flag == false) {
            return i;
        }
    }
    
    return -1;
};
