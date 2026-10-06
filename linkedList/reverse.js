/*
 * Problem: Reverse Linked List
 * Reverse a singly linked list and return the new head. Arrays below list node values in
 * traversal order.
 *
 * Expected input/output: head=[1,2,3] -> [3,2,1]; head=[] -> []
 */

class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        let prev = null, cur = head;

        while (cur != null) {
            const next = cur.next;
            cur.next = prev;
            [prev, cur] = [cur, next];
        }

        return prev;
    }
}

const s = new Solution();

const l0 = null;
const l1 = new ListNode(1);
const l3 = new ListNode(1, new ListNode(2, new ListNode(3)));
console.log(s.reverseList(l0));
console.log(s.reverseList(l1));
const rl3 = s.reverseList(l3);
console.log(rl3);
console.log(s.reverseList(rl3));


/*
 * Key insight:
 * Save the next node before redirecting each node's next pointer to the previous node.
 */
