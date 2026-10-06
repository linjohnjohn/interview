/*
 * Problem: Valid Parentheses
 * Decide whether a string of (), [], and {} brackets is correctly nested and every opener
 * has a matching closer.
 *
 * Expected input/output: s="()[]{}" -> true; s="([)]" -> false; s="" -> true
 */

BRACKET_MATCHES = {
    ']': '[',
    ')': '(',
    '}': '{',
}
class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];

        for (const c of s) {
            if (BRACKET_MATCHES[c]) {
                const lastBrackeet = stack.pop();
                if (lastBrackeet !== BRACKET_MATCHES[c]) return false;
            } else {
                stack.push(c);
            }
        }

        return stack.length === 0;
    }
}


const s = new Solution();
console.log(s.isValid(''));
console.log(s.isValid('()'));
console.log(s.isValid('({}'));
console.log(s.isValid('({})[]{()[]}'));

/*
 * Key insight:
 * Push opening brackets onto a stack; each closer must match the latest opener. The stack
 * must be empty at the end.
 */
