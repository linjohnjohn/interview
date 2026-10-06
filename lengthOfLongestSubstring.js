
class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let l = 0, r = 0, max = 0, charSet = new Set();

        while (r < s.length) {
            const rChar = s.charAt(r)
            if (charSet.has(rChar)) {
                max = Math.max(max, r - l);
                while (charSet.has(rChar)) {
                    charSet.delete(s.charAt(l++));
                }
            } else {
                r++;
                charSet.add(rChar);
            }
        }

        max = Math.max(max, r - l);
        return max;
    }
}


const s = new Solution();
console.log(s.lengthOfLongestSubstring('abcd'));
console.log(s.lengthOfLongestSubstring('aaa'));
console.log(s.lengthOfLongestSubstring(''));
console.log(s.lengthOfLongestSubstring('abcdabcde'));
console.log(s.lengthOfLongestSubstring('abcab'));