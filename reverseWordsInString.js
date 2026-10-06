/*
 * Problem: Reverse Words in a String
 * Reverse word order, remove leading/trailing whitespace, and use one space between words.
 *
 * Expected input/output: s="  the sky   is blue  " -> "blue is sky the"; s="hello" ->
 * "hello"
 */

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
    // Trim s so it starts and ends with words only
    // Then use split on space to get an array of words, but use regex to identify multiples spaces
    // Reverse array, and join with a space

    s = s.trim();
    const arr = s.split(/\s+/);
    arr.reverse();
    return arr.join(' ');
};

reverseWords(" the sky is blue ")

/*
 * Key insight:
 * Extract words independently of extra spaces, reverse the word list, and join with one
 * space.
 */
