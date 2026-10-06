/*
 * Problem: Jump Game
 * Start at index 0. Each nonnegative value is the maximum forward jump from that index.
 * Decide whether you can reach the last index.
 *
 * Expected input/output: nums=[2,3,1,1,4] -> true; nums=[3,2,1,0,4] -> false
 */

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

/*
 * Key insight:
 * Keep the farthest reachable index; an index beyond that boundary cannot be visited.
 * Backward DP can also mark positions that reach the end.
 */
