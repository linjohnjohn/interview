/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
    const jumpableArr = new Array(nums.length).fill(false);
    jumpableArr[nums.length - 1] = true;

    for (let i = nums.length - 2; i >= 0; i--) {
        const jumpsAllowed = nums[i];

        for (let j = i + 1; j <= i + jumpsAllowed; j++) {
            if (j < nums.length && jumpableArr[j]) {
                jumpableArr[i] = true;
                continue;
            }
        }
    }

    return jumpableArr[0];
};