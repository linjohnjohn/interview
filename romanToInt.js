/*
 * Problem: Roman to Integer
 * Convert a valid Roman numeral to its integer value, handling subtractive pairs such as IV,
 * IX, and CM.
 *
 * Expected input/output: s="III" -> 3; s="MCMXCIV" -> 1994
 */

const ROMAN_TO_INT = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
}
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    let sum = 0;
    for (let i = 0; i < s.length; i++) {
        let v = ROMAN_TO_INT[s[i]], next = ROMAN_TO_INT[s[i + 1]];
        if (next && next > v) {
            v = next - v;
            i++;
        }

        sum += v;
    }

    return sum;
};




/*
 * Key insight:
 * A symbol before a larger symbol is subtracted; otherwise add it. Alternatively consume
 * subtractive pairs together.
 */
