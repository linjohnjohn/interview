/*
 * Problem: LRU Cache
 * Build a fixed-capacity cache with get and put in O(1). Reading or updating a key makes it
 * most recently used; evict the least recently used key when full. Missing keys return -1.
 *
 * Expected input/output: capacity=2; put(1,10), put(2,20), get(1), put(3,30), get(2) -> 10,
 * -1
 */

class LRUCache {
    keyValue = new Map();
    forward = new Map();
    backward = new Map();
    head;
    tail;
    capacity;

    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        this.head = -1
        this.tail = 1001;
        this.forward.set(this.head, this.tail);
        this.backward.set(this.tail, this.head);
        this.capacity = capacity;
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        const v = this.keyValue.get(key);
        if (v !== undefined) {
            this.llRemove(key);
            this.llAppend(key);
            return v;
        } else {
            return -1;
        }


    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        if (this.keyValue.has(key)) {
            this.keyValue.set(key, value);
            this.llRemove(key);
            this.llAppend(key);
        } else if (this.capacity > 0) {
            this.capacity--;
            this.llAppend(key);
            this.keyValue.set(key, value);
        } else {
            const LRU = this.forward.get(this.head);
            this.llRemove(LRU);
            this.keyValue.delete(LRU);
            this.llAppend(key);
            this.keyValue.set(key, value);
        }
    }

    llRemove(key) {
        const next = this.forward.get(key);
        const prev = this.backward.get(key);
        this.forward.set(prev, next);
        this.backward.set(next, prev);
    }

    llAppend(key) {
        const last = this.backward.get(this.tail);
        this.forward.set(last, key);
        this.backward.set(key, last);
        this.forward.set(key, this.tail);
        this.backward.set(this.tail, key);
    }

}

const c = new LRUCache(2);


c.put(1, 1);
c.put(2, 2);
c.put(3, 3);

c.get(1);
c.get(2);
c.put(3, 33);
c.get(3);


// Test 1: Not full LRU and set a new value
// Test 1: Not full LRU and set an existing value
// Test 1: Full LRU and set a new value
// Test 1: Full LRU and Set something that already exists
// Test 1: Full LRU and set the key about to be evicted


/*
 * Key insight:
 * Combine a hash map for lookup with a doubly linked list for usage order; move accessed
 * keys to the newest end.
 */
