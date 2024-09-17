#include <math.h>
#include <stdlib.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 struct ListNode* create0Node(struct ListNode* head) {
    struct ListNode* newnode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newnode->next = NULL;
    newnode->val = 0;
    head->next = newnode;
    return newnode;
 }
 
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head1=l1;
    struct ListNode* head2=l2;
    while(head1 || head2) {
        int output = head1->val + head2->val;
        if (output > 9) {
            if (!head1->next) create0Node(head1);
            head1->next->val += (int)(output / 10);
            output = output % 10;
        }
        head1->val = output;
        printf("%d\n", output);
        if (!head1->next && head2->next) create0Node(head1);
        if (!head2->next && head1->next) create0Node(head2);
        head1 = head1->next;
        head2 = head2->next;
    }
    return l1;
}
