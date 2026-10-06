/*
 * Problem: Invert Binary Tree
 * Swap left and right children at every node and return the resulting root. Trees below use
 * level order with null for missing children.
 *
 * Expected input/output: root=[4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]; root=[] -> []
 */

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Solution {
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    invertTree(root) {
        if (root === null) return root;
        this.invertTree(root.left);
        this.invertTree(root.right);
        [root.left, root.right] = [root.right, root.left];
        return root;
    }
}


/*
 * Key insight:
 * Each subtree is inverted the same way: invert its children and swap them.
 */
