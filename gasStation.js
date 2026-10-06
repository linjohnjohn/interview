/*
 * Problem: Gas Station
 * Stations form a circle. gas[i] is fuel available and cost[i] is fuel needed for the next
 * station. Starting empty, return a valid start index or -1.
 *
 * Expected input/output: gas=[1,2,3,4,5], cost=[3,4,5,1,2] -> 3; gas=[2,3,4], cost=[3,4,3]
 * -> -1
 */

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function (gas, cost) {
    const m = gas.length;
    const eff = new Array(m)
    for (let i = 0; i < m; i++) {
        eff[i] = gas[i] - cost[i]
    }

    let candidate = null, total = 0;
    for (let i = 0; i < m; i++) {

        if (candidate === null && eff[i] > 0) {
            candidate = i;
            total = eff[i];
        } else {
            total += eff[i];

            if (total < 0) {
                candidate = null;
                total = 0;
            }
        }
    }

    if (candidate === null) return -1;

    for (let i = 0; i < candidate; i++) {
        total += eff[i];

        if (total < 0) {
            return -1;
        }
    }
    return candidate;
};

/*
 * Key insight:
 * If total gas is below total cost, no start works. When the running tank becomes negative,
 * every start in that failed segment can be skipped.
 */
