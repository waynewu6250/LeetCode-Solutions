#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LinkedNode(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
    
    # put the node at last
    def push_back(self, node):
        
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    # kick the current node and put it at last
    def kick(self, prev):
        current = prev.next
        if current == self.tail:
            return
        
        # remove the node in the middle
        prev.next = current.next
        self.key_to_prev[current.next.key] = prev
        current.next = 0
        
        # put it at last
        self.push_back(current)
    
    # pop front node
    def pop_front(self):
        # remove head
        head = self.dummy.next
        del self.key_to_prev[head.key]
        
        # add head.next as head
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return
        
        self.push_back(LinkedNode(key, value))
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

