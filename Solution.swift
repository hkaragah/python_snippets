/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        guard let l1 = l1, let l2 = l2 else { return nil }
        var currentNode: ListNode? = l1
        var totalVal1 = ""
        while(currentNode != nil){
            print("in the first while loop")
            totalVal1 = "\(totalVal1)\(currentNode!.val)"
            currentNode = currentNode!.next
        }
        totalVal1 = String(totalVal1.reversed())

        currentNode = l2
        var totalVal2 = ""
        while(currentNode != nil){
            print("in the second while loop")
            totalVal2 = "\(totalVal2)\(currentNode!.val)"
            currentNode = currentNode!.next
        }
        totalVal2 = String(totalVal2.reversed())
        
        print("\(totalVal1) \(totalVal2)")

        var totalValString = String((String(((Int(totalVal1) ?? 0) + (Int(totalVal2) ?? 0))) ?? "").reversed())
        print("almostdone \(totalValString)")
        var parentNode: ListNode? = ListNode()
        currentNode = parentNode
        for character in totalValString {
            print("in last loop \(currentNode!.val)")
            currentNode!.val = Int(String(character)) ?? 0
            totalValString.removeFirst()
            currentNode!.next = totalValString.count > 0 ? ListNode() : nil
            currentNode = currentNode!.next
        }
        return parentNode
    }
}