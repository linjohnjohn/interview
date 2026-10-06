/*
 * Problem: Search a 2D Matrix
 * Each row is sorted and each row's first value exceeds the previous row's last. Decide
 * whether target exists in O(log(rows*columns)).
 *
 * Expected input/output: matrix=[[1,3,5],[7,9,11]], target=9 -> true; same matrix, target=6
 * -> false
 */

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

/*
 * Key insight:
 * Treat the matrix as one sorted array; index i maps to row i//columns and column i%columns.
 */
