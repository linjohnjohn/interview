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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {
        if (subRoot === null) return true;
        if (root === null) return false;

        return this.isSameTree(root, subRoot) || this.isSubtree(root.left, subRoot) || this.isSubtree(root.right, subRoot)
    }

    isSameTree(p, q) {
        if (p === null && q === null) return true;
        if (p === null || q === null) return false;

        return p.val === q.val && this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
    }
}
