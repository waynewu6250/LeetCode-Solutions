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
    ListNode* swapPairs(ListNode* head) {
        
        if(head == NULL || head->next == NULL)
            return head;
        
        ListNode* dummy = new ListNode(0);
        ListNode* prev = dummy;
        ListNode* ptr = head;
        
        while(ptr != NULL && ptr->next != NULL){
            
            ListNode* nxt = ptr->next;
            ptr->next = nxt->next;
            nxt->next = ptr;
            prev->next = nxt;
            
            prev = ptr;
            ptr = ptr->next;
            
            
        }
        return dummy->next;