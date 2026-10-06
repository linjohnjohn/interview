
class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Solution {
    /**
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        const valToInorderIndex = inorder.reduce((map, v, i) => {
            map.set(v, i);
            return map;
        }, new Map());
        let pStart = 0;

        function buildTreeHelper(iStart, iEnd) {
            if (iStart === iEnd) return null;
            const nodeVal = preorder[pStart++];
            const idx = valToInorderIndex.get(nodeVal);
            const n = new TreeNode(nodeVal, buildTreeHelper(iStart, idx), buildTreeHelper(idx + 1, iEnd));

            return n;
        }

        return buildTreeHelper(0, inorder.length);
    }
}

// Function to find the height of the binary tree
function findHeight(root) {
    if (!root) {
        return -1;
    }

    let leftHeight = findHeight(root.left);
    let rightHeight = findHeight(root.right);

    return Math.max(leftHeight, rightHeight) + 1;
}


// Helper function to perform inorder traversal 
// and populate the 2D matrix
function inorder(root, row, col, height, ans) {
    if (!root) {
        return;
    }

    // Calculate offset for child positions
    let offset = Math.pow(2, height - row - 1);

    // Traverse the left subtree
    if (root.left) {
        inorder(root.left, row + 1, col - offset,
            height, ans);
    }

    // Place the current node's value in the matrix
    ans[row][col] = root.val.toString();

    // Traverse the right subtree
    if (root.right) {
        inorder(root.right, row + 1, col + offset,
            height, ans);
    }
}


// Function to convert the binary tree to a 2D matrix
function treeToMatrix(root) {

    // Find the height of the tree
    let height = findHeight(root);

    // Rows are height + 1; columns are 2^(height+1) - 1
    let rows = height + 1;
    let cols = Math.pow(2, height + 1) - 1;

    // Initialize 2D matrix with empty strings
    let ans = Array.from({ length: rows }, () =>
        Array(cols).fill(""));

    // Populate the matrix using inorder traversal
    inorder(root, 0, Math.floor((cols - 1) / 2),
        height, ans);

    console.log(ans);
    return ans;
}

const s = new Solution();

treeToMatrix(s.buildTree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]))

