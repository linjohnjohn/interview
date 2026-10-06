class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let l = 1, r = Math.max(...piles);

        while (r > l) {
            const mid = l + Math.floor((r - l) / 2);

            const time = piles.reduce((total, bananas) => {
                return total + Math.ceil(bananas / mid);
            }, 0);

            if (time <= h) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }
}

const s = new Solution();
console.log(s.minEatingSpeed([5], 1));
console.log(s.minEatingSpeed([5], 6));
console.log(s.minEatingSpeed([5, 1], 6));
console.log(s.minEatingSpeed([5, 1, 15, 20], 6));