/*
 * Problem: Reverse Nodes in k-Group
 * Reverse each full group of k linked-list nodes; leave a final group with fewer than k
 * nodes unchanged. Change links rather than values. Arrays below show node order.
 *
 * Expected input/output: head=[1,2,3,4,5], k=2 -> [2,1,4,3,5]; k=3 -> [3,2,1,4,5]
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
     * @param {number} k
     * @return {ListNode}
     */
    reverseKGroup(head, k) {
        let kth = this.findKth(head, k);

        if (kth === null) {
            return head;
        }

        const afterK = kth.next;
        const tail = this.reverseKGroup(afterK, k);

        kth.next = null;
        this.reverse(head);
        head.next = tail;

        return kth;
    }

    /**
     * @param {ListNode} head
     * @param {number} k
     * @return {ListNode}
     */
    reverseKGroupIterative(head, k) {
        const dummy = new ListNode(0, head);
        let groupPrev = dummy;
        while (true) {
            let kth = this.findKth(groupPrev.next, k);
            if (kth === null) {
                break;
            }
            const afterK = kth.next;
            kth.next = null;

            this.reverse(groupPrev.next);
            const last = groupPrev.next;
            last.next = afterK;
            groupPrev.next = kth;
            groupPrev = last;
        }

        return dummy.next;
    }

    reverse(head) {
        let prev = null, current = head;

        while (current) {
            const next = current.next;
            current.next = prev;
            [prev, current] = [current, next];
        }

        return prev;
    }

    findKth(current, k) {
        for (let i = 1; i < k; i++) {
            if (current === null) break;
            current = current.next;
        }

        return current;
    }
}

const s = new Solution();

const l0 = null;
const l1 = new ListNode(1);
const l3 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6, new ListNode(7)))))));
printLL(s.reverseKGroupIterative(l0, 1));
printLL(s.reverseKGroupIterative(l1, 1));
const rl3 = s.reverseKGroupIterative(l3, 3);
printLL(rl3);
printLL(s.reverseKGroupIterative(rl3, 3));
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
 * Confirm k nodes exist before reversing a group; reconnect its new head and tail with the
 * neighboring groups.
 */
