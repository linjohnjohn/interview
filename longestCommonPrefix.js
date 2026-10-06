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