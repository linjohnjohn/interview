/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy1 = function (ratings) {
    const m = ratings.length;
    const ratingsToIndicies = new Map();

    ratings.forEach((r, i) => {
        if (ratingsToIndicies.get(r) === undefined) {
            ratingsToIndicies.set(r, []);
        }

        ratingsToIndicies.get(r).push(i);
    });

    const keys = [...ratingsToIndicies.keys()];
    keys.sort((a, b) => a - b);

    const candies = new Array(m);
    let totalCandy = 0;
    for (const r of keys) {
        const indicies = ratingsToIndicies.get(r);
        for (let i of indicies) {
            let minCandy = 1;
            if (i - 1 >= 0 && ratings[i - 1] < r) {
                minCandy = Math.max(minCandy, candies[i - 1] + 1);
            }

            if (i + 1 < m && ratings[i + 1] < r) {
                minCandy = Math.max(minCandy, candies[i + 1] + 1);
            }
            totalCandy += minCandy;
            candies[i] = minCandy;
        }
    }

    return totalCandy;
};

/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function (ratings) {
    const m = ratings.length;
    const candies = new Array(m);
    candies[0] = 1;

    for (let i = 1; i < m; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        } else {
            candies[i] = 1;
        }
    }

    for (let i = m - 1; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = Math.max(candies[i + 1] + 1, candies[i]);
        }
    }

    return candies.reduce((s, v) => s + v, 0);
};

console.log(candy([1, 0, 2]));
console.log(candy([3, 2, 1, 0, 2]));
console.log(candy([3, 2, 2, 2, 1, 0, 2]));
console.log(candy([1, 6, 10, 8, 7, 3, 2]));
