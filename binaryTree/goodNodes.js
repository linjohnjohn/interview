/*
 * Problem: Count Good Nodes in Binary Tree
 * Count nodes with no larger value on the path from the root to that node, including the
 * node itself. Trees below use level order with null for missing children.
 *
 * Expected input/output: root=[3,1,4,3,null,1,5] -> 4; root=[1] -> 1
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


/*
 * Key insight:
 * Carry the maximum value seen along each root-to-node path; count a node when its value is
 * at least that maximum.
 */
