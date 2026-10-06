/*
 * Problem: Longest Consecutive Sequence
 * Return the length of the longest run of consecutive integer values, regardless of input
 * order. Duplicates do not extend the run; aim for O(n) time.
 *
 * Expected input/output: nums=[100,4,200,1,3,2] -> 4; nums=[1,1,2] -> 2
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
    // bucket numbers in a hashmap of <value, 0> at first
    /**
     * then iterate through the keys of the hashmap, if its value is 0,
     * it means the key hasn't been visited yet and we need to check for it's longest
     * increasing/decreasing sequence
     * */

    const numMap = nums.reduce((m, v) => m.set(v, 0), new Map());

    const getHelper = (v) => {
        const chain = numMap.get(v);
        if (chain !== 0) return chain;
        const previousChain = getHelper(v - 1) || 0;
        numMap.set(v, previousChain + 1);
        return previousChain + 1;
    }

    let maxChain = 0;
    for (k of numMap.keys()) {
        maxChain = Math.max(getHelper(k), maxChain);
    }

    return maxChain;
};

console.log(longestConsecutive([1, 2, 3, 4, 5, 6]));
console.log(longestConsecutive([3, 1, 2, 0, 5, 6, 4]));

/*
 * Key insight:
 * Use a set and expand only from numbers without a predecessor, or memoize each number's
 * chain length as this file does.
 */
