class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums) {
        const sum = nums.reduce((s, n) => {
            return s + n;
        }, 0);

        const n = nums.length - 1;
        const nSums = n * (n + 1) / 2;
        return sum - nSums;
    }
}

const s = new Solution();

s.findDuplicate([1, 2, 3, 2]);
s.findDuplicate([1, 2, 3, 1]);
s.findDuplicate([1, 1]);
