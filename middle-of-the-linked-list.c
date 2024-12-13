/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* rabbit = head;
    struct ListNode* tortoise = head;
    while (rabbit != NULL && rabbit->next != NULL) {
        rabbit = rabbit->next->next;
        tortoise = tortoise->next;
    }
    return tortoise;    
}
