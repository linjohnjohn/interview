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