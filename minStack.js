/*
 * Problem: Min Stack
 * Implement push, pop, top, and getMin, each in O(1). Queries and pop are made only when the
 * stack is nonempty.
 *
 * Expected input/output: push(-2), push(0), push(-3), getMin(), pop(), top(), getMin() ->
 * -3, 0, -2 for the three queries
 */

class MinStack {
    stack = [];
    mds = [];

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if (this.mds.length === 0 || this.mds[this.mds.length - 1] >= val) {
            this.mds.push(val);
        }
    }

    /**
     * @return {void}
     */
    pop() {
        const v = this.stack.pop();
        if (this.mds[this.mds.length - 1] === v) {
            this.mds.pop();
        }

        return v;
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack.slice(-1);
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.mds[this.mds.length - 1];
    }
}

const ms = new MinStack()
ms.push(1);
ms.push(2);
ms.push(0);

console.log(ms.getMin());
ms.pop();
console.log(ms.getMin());

/*
 * Key insight:
 * Keep a second stack of minima, including duplicate minima, so popping a minimum restores
 * the previous one.
 */
