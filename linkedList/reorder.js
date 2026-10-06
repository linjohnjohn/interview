/*
 * Problem: Reorder List
 * Rearrange nodes in place from L0,L1,...,Ln to L0,Ln,L1,Ln-1,... without changing their
 * values. Arrays below show node order after mutation.
 *
 * Expected input/output: head=[1,2,3,4] -> [1,4,2,3]; head=[1,2,3,4,5] -> [1,5,2,4,3]
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
     * @return {void}
     */
    reorderList(head) {
        const median = this.findMedian(head);
        const list2 = this.reverseList(median.next);
        median.next = null;
        return this.mergeList(head, list2);
    }

    findMedian(head) {
        let slow = head, fast = head.next;
        while (fast !== null && fast.next !== null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

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

    mergeList(l1, l2) {
        let dummy = new ListNode(), tail = dummy;
        while (l1 !== null && l2 !== null) {
            tail.next = l1;
            tail = tail.next;
            l1 = l1.next;
            tail.next = l2;
            tail = tail.next;
            l2 = l2.next;
        }

        if (l1) {
            tail.next = l1;
        } else if (l2) {
            tail.next = l2;
        }

        return dummy.next;
    }
}
const s = new Solution();


const l1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));

printLL(s.reorderList(l1));
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
 * Find the middle with slow/fast pointers, reverse the second half, then weave the two
 * halves together.
 */
