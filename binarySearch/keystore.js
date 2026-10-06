/*
 * Problem: Time Based Key-Value Store
 * set stores a key's value at an increasing timestamp. get returns the value at the greatest
 * stored timestamp no later than the query, or an empty string if none exists.
 *
 * Expected input/output: set("foo","bar",1); get("foo",3) -> "bar"; get("foo",0) -> ""
 */

class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        const arr = this.keyStore.get(key) || [];
        arr.push([value, timestamp]);
        this.keyStore.set(key, arr);
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        const arr = this.keyStore.get(key) || [];
        if (!arr) return "";
        let l = 0, r = arr.length;

        while (l < r) {
            const mid = l + Math.floor((r - l) / 2);

            const [_, tMid] = arr[mid];

            if (tMid > timestamp) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if (l >= 1) {
            return arr[l - 1][0];
        } else {
            return "";
        }
    }
}

const k = new TimeMap();
k.set("key1", "value1", 10);
// k.set("alice", "three", 3);
// k.set("alice", "five", 5);
console.log(k.get("key1", 1));
console.log(k.get("key1", 10));
console.log(k.get("key1", 11));

/*
 * Key insight:
 * Store each key's versions in timestamp order and binary-search the first timestamp above
 * the query; its predecessor is the answer.
 */
