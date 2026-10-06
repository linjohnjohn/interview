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