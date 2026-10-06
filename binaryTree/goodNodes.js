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
     * @return {number}
     */
    goodNodes(root, max = -Infinity) {
        if (root === null) return 0;
        max = Math.max(root.val, max);
        let gnodes = this.goodNodes(root.left, max) + this.goodNodes(root.right, max);

        if (root.val >= max) {
            gnodes++;
        }

        return gnodes;
    }
}
