# Definition for singly-linked list:
# class ListNode
#   attr_accessor :value, :next
#   def initialize(val)
#     @value = val
#     @next = nil
# end
#
def removeKFromList(l, k)
    newList = ListNode.new(0)
    newListCopy = newList
    while l
        if l.value != k
            addedNode = ListNode.new(l.value)
            newList.next = addedNode
            newList = newList.next
        end
        l = l.next
    end
    newListCopy = newListCopy.next
    newListCopy
            
end
