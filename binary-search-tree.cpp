/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* searchBST(struct TreeNode* root, int val) {
    if (!root) {
        return NULL;
    }
    if (root->val == val) {
        return root;
    }    
    if (root->val < val) {
        return searchBST(root->right, val);
    } else {
        return searchBST(root->left, val);
    }
    
}
