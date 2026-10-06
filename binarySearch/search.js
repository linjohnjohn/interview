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
