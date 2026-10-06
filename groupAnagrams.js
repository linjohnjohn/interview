/*
 * Problem: Group Anagrams
 * Group lowercase words that contain the same letters with the same frequencies. Group and
 * word order do not matter.
 *
 * Expected input/output: strs=["eat","tea","tan","ate","nat","bat"] ->
 * [["eat","tea","ate"],["tan","nat"],["bat"]]
 */

A_CHAR_CODE = 'a'.charCodeAt(0);
class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groupings = new Map();
        for (let s of strs) {
            let key = new Array(26).fill(0);
            for (let i = 0; i < s.length; i++) {
                key[s.charCodeAt(i) - A_CHAR_CODE]++;
            }
            key = key.join('-');

            if (groupings.get(key) === undefined) {
                groupings.set(key, [])
            }
            groupings.get(key).push(s);
        }

        return [...groupings.values()];
    }
}


let s = new Solution();

console.log(s.groupAnagrams(['cats', 'rats', 'tacs']));


/*
 * Key insight:
 * Use a 26-letter frequency signature as the hash-map key; anagrams share a signature.
 */
