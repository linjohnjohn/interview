class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}



class Solution {
    /**
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        const dummy = new ListNode(0);
        let current = dummy, carry = 0;

        while (l1 || l2) {
            const l1Val = l1 ? l1.val : 0;
            const l2Val = l2 ? l2.val : 0;
            const sum = l1Val + l2Val + carry;
            current.next = new ListNode(sum % 10);
            carry = Math.floor(sum / 10);
            current = current.next;

            l1 = l1 ? l1.next : null;
            l2 = l2 ? l2.next : null;
        }

        if (carry === 1) {
            current.next = new ListNode(1);
        }

        return dummy.next;
    }
}

const s = new Solution();

const l1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
const l2 = new ListNode(1, new ListNode(9, new ListNode(9, new ListNode(6))));
const l0 = new ListNode(0);

printLL(s.addTwoNumbers(l1, l2));
printLL(s.addTwoNumbers(l1, l0));

function printLL(list) {
    const res = [];
    while (list) {
        res.push(list.val);
        list = list.next;
    }

    console.log(res);
}
