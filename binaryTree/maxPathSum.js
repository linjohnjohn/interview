/*
 * Problem: Binary Tree Maximum Path Sum
 * Return the largest sum along any nonempty path of connected nodes, with no node repeated.
 * The path may start and end anywhere. Trees below use level order with null for missing
 * children.
 *
 * Expected input/output: root=[-10,9,20,null,null,15,7] -> 42; root=[-3] -> -3
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
     * @return {number}
     */
    maxPathSum(root) {
        return this.maxLeftRightHelper(root)[0];
    }

    maxLeftRightHelper(root) {
        if (root === null) return [0, 0, 0]
        const [lMax, lOneSided] = this.maxLeftRightHelper(root.left);
        const [rMax, rOneSided] = this.maxLeftRightHelper(root.right);

        return [Math.max(lMax, rMax, root.val + lOneSided + rOneSided), Math.max(lOneSided + root.val, rOneSided + root.val, 0)];
    }
}


/*
 * Key insight:
 * Return only the best one-sided gain to the parent, but evaluate a full path using both
 * children locally. Ignore negative child gains and keep the global answer nonempty.
 */
