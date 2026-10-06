/*
 * Problem: Subtree of Another Tree
 * Decide whether root contains a node whose entire subtree matches subRoot in both structure
 * and values. Trees below use level order with null for missing children.
 *
 * Expected input/output: root=[3,4,5,1,2], subRoot=[4,1,2] -> true; subRoot=[4,1,3] -> false
 */

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


/*
 * Key insight:
 * Try an exact tree comparison at every node of root; matching just the root value is
 * insufficient.
 */
