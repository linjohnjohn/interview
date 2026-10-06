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