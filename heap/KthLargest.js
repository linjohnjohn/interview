/*
 * Problem: Kth Largest Element in a Stream
 * Initialize with k and an array, then add values one at a time. Each add returns the kth
 * largest value seen so far, counting duplicates; assume at least k values after a query.
 *
 * Expected input/output: k=3, nums=[4,5,8,2]; add(3) -> 4; add(5) -> 5; add(10) -> 5
 */

const { MinPriorityQueue } = require('@datastructures-js/priority-queue');


class KthLargest {
    /**
     * @param {number} k
     * @param {number[]} nums
     */
    constructor(k, nums) {
        this.minHeap = new MinPriorityQueue();
        this.k = k;

        for (const num of nums) {
            this.minHeap.enqueue(num);
        }

        while (this.minHeap.size() > k) {
            this.minHeap.dequeue();
        }
    }

    /**
     * @param {number} val
     * @return {number}
     */
    add(val) {
        this.minHeap.enqueue(val);
        if (this.minHeap.size() > this.k) {
            this.minHeap.dequeue();
        }
        return this.minHeap.front();
    }
}

const s = new KthLargest();

/*
 * Key insight:
 * Keep a min-heap containing only the largest k values; its root is the kth largest.
 */
