/*
 * Problem: Remove Nth Node from End
 * Remove the nth node counting backward from a linked list's end and return its head. n is
 * valid. Arrays below list node values in traversal order.
 *
 * Expected input/output: head=[1,2,3,4,5], n=2 -> [1,2,3,5]; head=[1], n=1 -> []
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
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        const dummy = new ListNode(0, head);
        let slow = dummy, fast = head;

        for (let i = 1; i <= n; i++) {
            fast = fast.next;
        }

        while (fast !== null) {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;

        return dummy.next;
    }
}

const s = new Solution();

const l1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));

printLL(s.removeNthFromEnd(l1, 4));
printLL(s.removeNthFromEnd(l1, 2));
function printLL(list) {
    const res = [];
    while (list) {
        res.push(list.val);
        list = list.next;
    }

    console.log(res);
}


/*
 * Key insight:
 * Use a dummy head and two pointers separated by n nodes; when the fast pointer ends, the
 * slow pointer is just before the node to remove.
 */
