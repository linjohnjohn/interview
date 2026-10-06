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