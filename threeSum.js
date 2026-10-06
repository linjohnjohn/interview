/*
 * Problem: 3Sum
 * Return all unique value triplets summing to zero, using three different indices. Triplet
 * and result order do not matter.
 *
 * Expected input/output: nums=[-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]; nums=[0,0,0] ->
 * [[0,0,0]]
 */

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {

        // twoSum on each element where target = nums[i] and the array is the elements other than i,
        // twoSum is O(n) and requires O(n) space, this would be O(n^2) and require O(n) space as well
    }
}


/*
 * Key insight:
 * Sort, fix one number, and use two pointers to find pairs summing to its negative. Skip
 * duplicate choices at every step.
 */
