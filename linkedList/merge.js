class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}


class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        const head = new ListNode();
        let cur = head, a = list1, b = list2;

        while (a != null || b != null) {
            const aVal = a === null ? Infinity : a.val;
            const bVal = b === null ? Infinity : b.val;
            if (aVal <= bVal) {
                cur.next = a;
                cur = a;
                a = a.next;
            } else {
                cur.next = b;
                cur = b;
                b = b.next;
            }
        }

        return head.next;
    }
}

const s = new Solution();


const l1 = new ListNode(1, new ListNode(3, new ListNode(5)));
const l2 = new ListNode(1, new ListNode(4));

console.log(s.mergeTwoLists(l1, l2));