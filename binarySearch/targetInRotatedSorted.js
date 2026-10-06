/*
 * Problem: Search in Rotated Sorted Array
 * An ascending array of distinct values has been rotated. Return target's index or -1 in
 * O(log n).
 *
 * Expected input/output: nums=[4,5,6,7,0,1,2], target=0 -> 4; same nums, target=3 -> -1
 */

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0, r = nums.length;

        while (l < r) {
            const m = l + Math.floor((r - l) / 2);

            if (target === nums[m]) return m;

            // left sorted
            if (nums[m] > nums[l]) {
                if (target > nums[m]) {
                    l = m + 1;
                } else if (target < nums[m]) {
                    if (target < nums[l]) {
                        l = m + 1;
                    } else {
                        r = m;
                    }
                }
            } else {
                if (target < nums[m]) {
                    r = m;
                } else if (target > nums[m]) {
                    if (target > nums[r - 1]) {
                        r = m;
                    } else {
                        l = m + 1
                    }
                }
            }
        }

        return -1;
    }
}



const s = new Solution();
console.log(s.search([3, 1], 3));
console.log(s.search([1, 2, 3, 4, 5, 6, 7], 3));
console.log(s.search([3], 3));
console.log(s.search([5, 1, 2, 3, 4], 1));
console.log(s.search([2, 3, 4, 5, 1], 5));


/*
 * Key insight:
 * At least one half around the midpoint is sorted. Check whether target lies in that half's
 * value range to decide which half to retain.
 */
