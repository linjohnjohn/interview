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