# Definition for singly-linked list:
# class ListNode
#   attr_accessor :value, :next
#   def initialize(val)
#     @value = val
#     @next = nil
# end
#

def removeKFromList(l, k)
  # Removes any element in l that has a value of k
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

# Is List Palindrome
#
def isListPalindrome(l)
    array=[]
    while l
        array << l.value
        l = l.next
    end
    return array == array.reverse
end

# Add two huge numbers
# Input: a = [9876, 5432, 1999]
#        b = [1, 8001]
# Output: [9876, 5434, 0]
# Input: a = [123, 4, 5]
#        b = [100, 100, 100]
# Output: [223, 104, 105]

def addTwoHugeNumbers(a, b)
    a_num = ""
    b_num = ""
    while a
        a_num += '%04d' % a.value
        a = a.next
    end
    puts a_num
    while b
        b_num += '%04d' % b.value
        b = b.next
    end
    puts b_num
    total = a_num.to_i + b_num.to_i
    result = []
    return [0] if total == 0
    while total > 0
        result.unshift(total%10000)
        total /= 10000
    end
    result
end

