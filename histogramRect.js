class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights) {
        const left = this.createAtLeastAsTallArr(heights);
        heights.reverse();
        const right = this.createAtLeastAsTallArr(heights);
        right.reverse();
        heights.reverse();


        let max = 0;
        for (const i of heights) {
            max = Math.max(max, heights[i] * (1 + left[i] + right[i]));
        }

        return max;
    }

    createAtLeastAsTallArr(heights) {
        const left = new Array(heights.length).fill(0);
        const monoIncStack = [];
        for (const i in heights) {
            const h = heights[i];
            let top = monoIncStack.pop();
            while (top !== undefined && heights[top] >= h) {
                top = monoIncStack.pop();
            }

            if (top && heights[top] < h) {
                left[i] = i - top + left[top];
            }

            if (top !== undefined) {
                monoIncStack.push(top);
            }

            if (monoIncStack.length && monoIncStack[monoIncStack.length - 1] >= h) {
                left[i] = streak;
                streak++;
            } else {
                left[i] = 0;
                streak = 1;
            }
            allTallerThan = h;
        }

        return left;
    }
}


const s = new Solution();

console.log(s.largestRectangleArea([7, 1, 7, 2, 2, 4]));
console.log(s.largestRectangleArea([1, 3, 7]));