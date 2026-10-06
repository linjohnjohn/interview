/**
 * @param {number[]} nums
 * @return {boolean}
 */
var jumpDP = function (nums) {
    const jumpCount = new Array(nums.length).fill(Infinity);
    jumpCount[nums.length - 1] = 0;

    for (let i = nums.length - 2; i >= 0; i--) {
        const jumpsAllowed = nums[i];

        for (let j = i + 1; j <= i + jumpsAllowed && j < nums.length; j++) {
            jumpCount[i] = Math.min(jumpCount[i], jumpCount[j] + 1);
        }
    }

    return jumpCount[0];
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {
    if (nums.length === 1) return 0;
    let jumpsTaken = 1, jumpsLeft = nums[0], candidate = 0;

    for (let i = 1; i < nums.length - 1; i++) {
        jumpsLeft -= 1;
        candidate -= 1;

        if (nums[i] > jumpsLeft && nums[i] > candidate) {
            candidate = nums[i];
        }

        if (jumpsLeft === 0) {
            // if candidate, the best backup option, is 0, then we're stuck
            if (candidate <= 0) return -1;
            jumpsTaken++;
            jumpsLeft = candidate;
        }
    }

    return jumpsTaken;
};


console.log(jump([2, 1]))
console.log(jump([2, 3, 1, 1, 4]));
console.log(jump([2, 2, 0, 0, 4]));