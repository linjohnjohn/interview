/*
 * Problem: Container With Most Water
 * Choose two vertical lines whose heights are given. Return the maximum water area: distance
 * between them times the shorter height.
 *
 * Expected input/output: heights=[1,8,6,2,5,4,8,3,7] -> 49; heights=[1,1] -> 1
 */

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


/*
 * Key insight:
 * Start with the widest pair and move the shorter side inward; moving the taller side cannot
 * improve the area while the shorter side stays.
 */
