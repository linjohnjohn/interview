/*
 * Problem: Car Fleet
 * Cars travel toward a target without passing. A car that catches another joins its fleet.
 * Return how many fleets reach the target, including cars that meet there.
 *
 * Expected input/output: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
 */

class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        const positionSpeed = position.map((p, i) => [p, speed[i]]);
        positionSpeed.sort((a, b) => a[0] - b[0]);

        const timeToReach = positionSpeed.map((ps) => {
            const [p, s] = ps;
            return (target - p) / s;
        });

        let slow = -1, fleets = 0;
        for (let i = timeToReach.length - 1; i >= 0; i--) {
            const t = timeToReach[i];

            if (t > slow) {
                fleets += 1;
                slow = t;
            }
        }

        return fleets;
    }
}


const s = new Solution();
console.log(s.carFleet(10, [1, 4], [3, 2]));
console.log(s.carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]));
console.log(s.carFleet(10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4]));


/*
 * Key insight:
 * Process cars from closest to the target backward. A car joins the fleet ahead if its
 * arrival time is no larger than that fleet's time.
 */
