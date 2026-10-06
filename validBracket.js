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