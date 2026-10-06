class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const m = matrix.length, n = matrix[0].length;

        let l = 0, r = m * n;

        while (r > l) {
            const mid = l + Math.floor((r - l) / 2);
            const c = mid % n, row = Math.floor(mid / n);
            if (matrix[row][c] > target) {
                r = mid;
            } else if (matrix[row][c] < target) {
                l = mid + 1;
            } else {
                return true;
            }
        }

        return matrix[l] === target;
    }
}

const s = new Solution();
// console.log(s.searchMatrix([[1, 2, 3], [3, 5, 7], [9, 9, 9]], 5));
console.log(s.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15))