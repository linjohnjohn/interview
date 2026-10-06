class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let l = 0, r = nums.length;

        if (nums.length === 1 || nums[nums.length - 1] > nums[0]) return nums[0];

        while (r > l) {
            const mid = l + Math.floor((r - l) / 2);

            if (nums[mid] < nums[0]) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return nums[l];
    }
}


const s = new Solution();
console.log(s.findMin([5, 1, 2, 3, 4]));
console.log(s.findMin([1, 2, 3, 4]));
console.log(s.findMin([1]));
console.log(s.findMin([2, 1]));
