
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
