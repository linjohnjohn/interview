/*
 * Problem: Two Sum
 * Return indices of two different array elements whose sum equals target. Assume exactly one
 * solution; either index order is acceptable.
 *
 * Expected input/output: nums=[2,7,11,15], target=9 -> [0,1]; nums=[3,3], target=6 -> [0,1]
 */

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const visited = new Map();

        for (let i = 0; i < nums.length; i++) {
            const v = nums[i];
            if (visited.get(target - v) != undefined) {
                return [visited.get(target - v), i];
            } else {
                visited.set(v, i);
            }
        }
    }
}

console.log(new Solution().twoSum([5, 6, 1, 3], 6));

/*
 * Key insight:
 * As you scan, look for target minus the current value in a map of earlier values to indices
 * before storing the current value.
 */
