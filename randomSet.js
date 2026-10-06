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