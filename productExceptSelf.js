/*
 * Problem: Product of Array Except Self
 * For each index, return the product of all other elements. Solve in O(n) without division,
 * including inputs containing zeros.
 *
 * Expected input/output: nums=[1,2,3,4] -> [24,12,8,6]; nums=[2,3,0,4] -> [0,0,24,0]
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    const m = nums.length;
    const prefixProduct = new Array(m), suffixProduct = new Array(m);

    prefixProduct[0] = 1;
    suffixProduct[m - 1] = 1;

    for (let i = 0; i < m - 1; i++) {
        prefixProduct[i + 1] = prefixProduct[i] * nums[i];
    }

    for (let i = m - 1; i > 0; i--) {
        suffixProduct[i - 1] = suffixProduct[i] * nums[i];
    }

    const result = new Array(m);
    for (let i = 0; i < m; i++) {
        result[i] = prefixProduct[i] * suffixProduct[i];
    }

    return result;
};

console.log(productExceptSelf([2, 3, 0, 4]));
console.log(productExceptSelf([2, 3, 4]));

/*
 * Key insight:
 * Multiply the product strictly to the left by the product strictly to the right of each
 * index.
 */
