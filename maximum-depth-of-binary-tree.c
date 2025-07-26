/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if (root == NULL) return 0;
    int left_max = maxDepth(root->left);
    int right_max = maxDepth(root->right);
    return 1 + (left_max > right_max ? left_max : right_max);
    
}
