/*
 * Problem: Lowest Common Ancestor of a Binary Search Tree
 * Given a BST and two nodes in it, return their lowest shared ancestor. A node can be its
 * own ancestor. Tree arrays below use level order with null for missing children.
 *
 * Expected input/output: root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8 -> node 6; p=2, q=4 ->
 * node 2
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


/*
 * Key insight:
 * If both values are smaller, go left; if both are larger, go right. The first split or
 * matching node is their lowest common ancestor.
 */
