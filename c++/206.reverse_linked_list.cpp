/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        return reverse(head);
        
    }
    
    ListNode* reverse(ListNode* head) {
        if(head == NULL or head->next == NULL){
            return head;
        }
        ListNode* ptr = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return ptr;
    }
    
    
};