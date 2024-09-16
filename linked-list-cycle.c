/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if (head==NULL || head->next==NULL) return false;
    struct ListNode* s = head;
    struct ListNode* f = head;
    while (f != NULL && f->next != NULL) {
        s = s->next;
        f = f->next->next;
        if (s == f) return true;
    }
    return false;
    
}
