/*
 * Problem: Minimum Window Substring
 * Return the shortest substring of s containing all characters of t with their required
 * multiplicities. Return an empty string if impossible.
 *
 * Expected input/output: s="ADOBECODEBANC", t="ABC" -> "BANC"; s="a", t="aa" -> ""
 */

class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        if (s.length < t.length) return '';
        const tFreq = new Map();
        for (const c of t) {
            tFreq.set(c, (tFreq.get(c) || 0) + 1);
        }

        let l = 0, matched = 0;
        const need = tFreq.size;

        const windowFreq = Array.from(tFreq.keys()).reduce((acc, c) => acc.set(c, 0), new Map());

        let min = Infinity, argMin;


        for (let r = 1; r <= s.length; r++) {
            const newChar = s.charAt(r - 1);
            if (windowFreq.has(newChar)) {
                windowFreq.set(newChar, windowFreq.get(newChar) + 1);

                if (tFreq.get(newChar) === windowFreq.get(newChar)) {
                    matched++;
                }

                while (matched === need) {
                    if (r - l < min) {
                        min = r - l;
                        argMin = [l, r];
                    }

                    const oldChar = s.charAt(l++);
                    if (windowFreq.has(oldChar)) {
                        windowFreq.set(oldChar, windowFreq.get(oldChar) - 1);
                        if (tFreq.get(oldChar) > windowFreq.get(oldChar)) {
                            matched--;
                        }
                    }
                }
            }
        }

        return argMin === undefined ? '' : s.substring(...argMin);
    }
}

const s = new Solution();
console.log(s.minWindow("ABC", "ABC"))
console.log(s.minWindow("ABBCA", "ABC"))
console.log(s.minWindow("AA", "ABC"))


/*
 * Key insight:
 * Track required counts in a sliding window. Expand until all requirements are met, then
 * shrink while valid to find the shortest window.
 */
