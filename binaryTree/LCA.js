/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {
        let candidate = root;
        const upper = Math.max(p.val, q.val);
        const lower = Math.min(p.val, q.val);
        while (candidate !== null) {
            if (candidate.val > upper) {
                candidate = candidate.left;
            } else if (candidate.val < lower) {
                candidate = candidate.right;
            } else {
                return candidate;
            }
        }
    }
}
