class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        const sArr = [], results = [], stack = [[n, 0, true]];

        while (stack.length) {
            const candidate = stack.pop();
            if (candidate === 'pop') {
                sArr.pop();
                continue;
            }
            const [openQuota, closeQuota, shouldOpen] = candidate;

            if (!shouldOpen && openQuota === 0 && closeQuota === 0) {
                results.push(sArr.join(''));
                continue;
            };

            if (shouldOpen) {
                if (openQuota <= 0) continue;
                sArr.push('(');
                stack.push('pop');
                stack.push([openQuota - 1, closeQuota + 1, true]);
                stack.push([openQuota - 1, closeQuota + 1, false]);
            } else {
                if (closeQuota <= 0) continue;
                sArr.push(')');
                stack.push('pop');
                stack.push([openQuota, closeQuota - 1, true]);
                stack.push([openQuota, closeQuota - 1, false]);

            }
        }

        return results;
    }
}

const s = new Solution();
console.log(s.generateParenthesis(2));
console.log(s.generateParenthesis(3));
console.log(s.generateParenthesis(4));