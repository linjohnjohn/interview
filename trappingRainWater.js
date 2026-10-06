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
