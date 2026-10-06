/*
 * Problem: Find the Duplicate Number
 * An array of n+1 integers contains values in 1..n and exactly one distinct repeated number,
 * possibly repeated more than twice. Find it without modifying the array and with constant
 * extra space.
 *
 * Expected input/output: nums=[1,3,4,2,2] -> 2; nums=[3,3,3,3,3] -> 3
 */

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


/*
 * Key insight:
 * View each value as a next-index pointer and use Floyd's cycle detection to find the cycle
 * entry. Subtracting the expected sum only works under stronger assumptions.
 */
