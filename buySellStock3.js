/*
 * Problem: Best Time to Buy and Sell Stock III
 * Given daily stock prices, find the maximum profit from at most two buy-then-sell
 * transactions. Hold at most one share at a time.
 *
 * Expected input/output: prices=[3,3,5,0,0,3,1,4] -> 6; prices=[7,6,4,3,1] -> 0
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    if (prices.length < 2) {
        return 0;
    }

    const m = prices.length;

    // 2 x m array
    const profitMemo = [new Array(m).fill(0), new Array(m), new Array(m)];
    profitMemo[1][m - 1] = 0;
    profitMemo[2][m - 1] = 0;

    for (let txn = 1; txn <= 2; txn++) {
        for (day = m - 2; day >= 0; day--) {
            // choose to skip day 
            const candidates = [profitMemo[txn][day + 1]];
            for (sellDate = day + 1; sellDate < m; sellDate++) {
                // choose to buy today and sell at future sellDate
                const profit = prices[sellDate] - prices[day];
                if (profit > 0) {
                    candidates.push(profit + profitMemo[txn - 1][sellDate]);
                }
            }
            profitMemo[txn][day] = Math.max(...candidates);
        }
    }

    return profitMemo[2][0];
};

console.log(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]));
console.log(maxProfit([1, 5, 2, 8]));
console.log(maxProfit([1]));
console.log(maxProfit([]));

/*
 * Key insight:
 * Track the best balance after the first buy, first sell, second buy, and second sell. The
 * best sale need not be the highest future price.
 */
