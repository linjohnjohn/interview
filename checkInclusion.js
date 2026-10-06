/*
 * Problem: Permutation in String
 * Decide whether s2 contains a contiguous substring that is a rearrangement of all
 * characters in s1.
 *
 * Expected input/output: s1="ab", s2="eidbaooo" -> true; s1="ab", s2="eidboaoo" -> false
 */

class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean} true if s2 contains a permutation of s1 somewhere in s2
     * 
     * A permutation s1 is just anagram of s1, there for we can just store a freq map
     * rep of s1 and have a sliding window of s2 of the same length that stores a freq
     * map of it's characters. Then for each window compare the f maps 
     * 
     * ABCA
     * AAZZZJAASCABA
     */
    checkInclusion(s1, s2) {
        if (s2.length < s1.length) return false;
        const s1Map = new Map(), s2Map = new Map();

        for (let i = 0; i < s1.length; i++) {
            const s1Char = s1.charAt(i), s2Char = s2.charAt(i);
            s1Map.set(s1Char, (s1Map.get(s1Char) || 0) + 1);
            s2Map.set(s2Char, (s2Map.get(s2Char) || 0) + 1);
        }

        if (this.freqEquals(s1Map, s2Map)) return true;


        for (let r = s1.length; r < s2.length; r++) {
            const newChar = s2.charAt(r);
            const oldChar = s2.charAt(r - s1.length);
            s2Map.set(newChar, (s2Map.get(newChar) || 0) + 1);
            s2Map.set(oldChar, (s2Map.get(oldChar) || 0) - 1);
            if (this.freqEquals(s1Map, s2Map)) return true;
        }

        return false;
    }

    /**
     * @param {Map} m1
     * @param {Map} m2
     * @returns {boolean}
     **/
    freqEquals(m1, m2) {
        for (const k of m1.keys()) {
            if (m1.get(k) !== m2.get(k)) {
                return false;
            }
        }

        return true;
    }
}


/*
 * Key insight:
 * An anagram has identical character counts. Slide a window of exactly len(s1), updating the
 * entering and leaving characters.
 */
