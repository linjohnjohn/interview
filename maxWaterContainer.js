class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        const m = heights.length;
        let l = 0, r = m - 1, mx = 0;

        while (l < r) {
            const lower = Math.min(heights[l], heights[r]);
            mx = Math.max(mx, lower * (r - l));

            if (lower === heights[l]) {
                l++;
            } else {
                r--;
            }
        }
        return mx;
    }
}
