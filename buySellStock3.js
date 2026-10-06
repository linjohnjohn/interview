/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    const m = prices.length;
    const highestPriceIndex = new Array(m);
    let maxPrice = 0, argMax = null;
    for (let i = m - 1; i >= 0; i--) {
        highestPriceIndex[i] = argMax;
        if (prices[i] > maxPrice) {
            maxPrice = prices[i];
            argMax = i;
        }
    }

    // 2 x m array
    const profitMemo = [new Array(m).fill(0), new Array(m), new Array(m)];
    profitMemo[1][m - 1] = 0;
    profitMemo[2][m - 1] = 0;

    for (let txn = 1; txn <= 2; txn++) {
        for (day = m - 2; day >= 0; day--) {
            const sellDate = highestPriceIndex[day];
            const candidates = [profitMemo[txn][day + 1]];
            const profit = sellDate === null ? 0 : prices[sellDate] - prices[day];
            if (profit > 0) {
                candidates.push(profit + profitMemo[txn - 1][sellDate]);
            }
            profitMemo[txn][day] = Math.max(...candidates);
        }
    }

    return profitMemo[2][0];
};

console.log(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]));