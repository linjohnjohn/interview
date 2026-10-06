/*
 * Problem: Binary Search
 * Given an ascending array of distinct integers, return target's zero-based index or -1 when
 * absent in O(log n).
 *
 * Expected input/output: nums=[-1,0,3,5,9,12], target=9 -> 4; same nums, target=2 -> -1
 */

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0, r = nums.length;

        while (r > l) {
            const m = Math.floor((l + r) / 2);
            if (nums[m] === target) return m;
            else if (nums[m] > target) {
                r = m;
            } else {
                l = m + 1;
            }
        }

        return -1;
    }
}


/*
 * Key insight:
 * Compare with the middle value and discard the half that cannot contain target; keep
 * interval endpoints consistent.
 */
