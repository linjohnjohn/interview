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