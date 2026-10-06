/*
 * Problem: Koko Eating Bananas
 * Koko eats at most k bananas from one pile per hour; unused time in that hour cannot be
 * spent on another pile. Return the smallest integer k that finishes all piles within h
 * hours.
 *
 * Expected input/output: piles=[3,6,7,11], h=8 -> 4; piles=[30,11,23,4,20], h=5 -> 30
 */

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

/*
 * Key insight:
 * Required hours are sum(ceil(pile/k)); this decreases as k increases, so binary-search the
 * first feasible speed.
 */
