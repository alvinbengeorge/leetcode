/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head) {
    int final_value = 0;
    while (head) {
        final_value = (final_value << 1) + head->val;
        head = head->next;
    }
    return final_value;
}
