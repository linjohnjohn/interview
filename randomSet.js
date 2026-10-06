/*
 * Problem: Insert Delete GetRandom O(1)
 * Store unique integers. insert and remove return whether the set changed; getRandom returns
 * a uniformly random present value. All operations should take average O(1).
 *
 * Expected input/output: insert(1) -> true; insert(1) -> false; insert(2) -> true; remove(1)
 * -> true; getRandom() -> 2
 */

class RandomizedSet {

    constructor() {
        this.set = new Set();
        this.array = []
    }

    insert(v) {
        if (this.set.has(v)) {
            return false;
        } else {
            this.set.add(v);
            this.array.push(v);
            return true;
        }
    }

    remove(v) {
        return this.set.delete(v);
    }

    getRandom() {
        const v = this.array[Math.floor(Math.random() * this.array.length)];
        if (this.set.has(v)) return v;

        this.array = Array.from(this.set);
        return this.array[Math.floor(Math.random() * this.array.length)];
    }

}

const r = new RandomizedSet();
r.insert(1);
r.insert(2);
r.insert(3);
r.insert(4);

console.log(r.getRandom());
console.log(r.getRandom());
console.log(r.getRandom());


console.log(r.getRandom());
console.log(r.getRandom());
console.log(r.getRandom());

console.log(r.getRandom());
console.log(r.getRandom());
console.log(r.getRandom());

/*
 * Key insight:
 * Use an array plus a value-to-index map. Remove by swapping with the last value, updating
 * its index, and popping; sample a random array index.
 */
