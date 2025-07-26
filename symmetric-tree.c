/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool symmetric(struct TreeNode* left, struct TreeNode* right) {
    if (!left || !right) return left == right;
    return left->val == right->val && symmetric(left->left, right->right) && symmetric(left->right, right->left);
}

bool isSymmetric(struct TreeNode* root) {
    return symmetric(root, root);    
}
