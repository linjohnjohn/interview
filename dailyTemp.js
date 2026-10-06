/*
 * Problem: Daily Temperatures
 * For each temperature, return how many days until a strictly warmer day. Use 0 when no
 * warmer day follows.
 *
 * Expected input/output: temperatures=[73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
 */

class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const deStack = [], res = new Array(temperatures.length);

        for (let i = temperatures.length - 1; i >= 0; i--) {
            let top = deStack.pop();
            while (top !== undefined && temperatures[top] <= temperatures[i]) {
                top = deStack.pop();
            }

            if (top !== undefined) {
                deStack.push(top);
                res[i] = top - i;
            } else {
                res[i] = 0
            }

            deStack.push(i);
        }

        return res;
    }
}

const s = new Solution();

console.log(s.dailyTemperatures([1, 2, 3]));
console.log(s.dailyTemperatures([3, 2, 1]));
console.log(s.dailyTemperatures([3, 2, 4]));
console.log(s.dailyTemperatures([3, 2, 4, 5]));

/*
 * Key insight:
 * A monotonic stack keeps useful candidate indices; discard days that cannot be the next
 * warmer day.
 */
