/*
 * Problem: Trapping Rain Water
 * Given unit-width bar heights, return the total water trapped between bars after rain.
 *
 * Expected input/output: height=[0,1,0,2,1,0,1,3,2,1,2,1] -> 6; height=[3,0,3] -> 3
 */

class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        const m = height.length;
        const largestToRight = new Array(m);
        let max = 0;
        for (let i = m - 1; i >= 0; i--) {
            largestToRight[i] = max;
            max = Math.max(max, height[i]);
        }

        let sum = 0;
        max = 0;
        for (let i = 0; i < m; i++) {
            const water = Math.min(max, largestToRight[i]) - height[i];
            max = Math.max(height[i], max)
            if (water >= 0) sum += water;
        }

        return sum;
    }
}

const s = new Solution();

console.log(s.trap([1, 2, 3, 0, 0, 4, 2, 4]));


/*
 * Key insight:
 * Water above each bar is max(0, min(highest left, highest right) - height). Precompute one
 * side and scan while tracking the other.
 */
