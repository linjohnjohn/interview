/*
 * Problem: Longest Common Prefix
 * Return the longest starting string shared by every word, or an empty string when there is
 * none.
 *
 * Expected input/output: strs=["flower","flow","flight"] -> "fl";
 * strs=["dog","racecar","car"] -> ""
 */

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    let i = 0;
    while (true) {
        let char;
        for (let s of strs) {
            if (char === undefined) {
                if (s[i] === undefined) return s.substring(0, i);
                char = s[i];
            } else {
                if (s[i] !== char) return s.substring(0, i);
            }
        }
        i++;
    }
};

/*
 * Key insight:
 * Compare one character position across all words; the first mismatch or word ending fixes
 * the prefix length.
 */
