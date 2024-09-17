/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    // code here
    struct ListNode* temp = head;
    while (temp) {    
        if (temp->next && temp->next->val == temp->val) {
            temp->next = temp->next->next;                
        } else {
            temp = temp->next;
        }
    }
    return head;
}
