/*
 * Problem: Integer to Roman; Length of Last Word
 * intToRoman: Convert an integer in 1..3999 to Roman numerals, including subtractive pairs
 * such as IV and IX. lengthOfLastWord: Return the length of the final word, ignoring
 * trailing spaces.
 *
 * Expected input/output: intToRoman(58) -> "LVIII"; intToRoman(1994) -> "MCMXCIV";
 * lengthOfLastWord("Hello World  ") -> 5
 */


const CONVERSION_MAP = [
    new Map([[1, "I"], [5, "V"], [4, "IV"], [9, "IX"]]),
    new Map([[1, "X"], [5, "L"], [4, "XL"], [9, "XC"]]),
    new Map([[1, "C"], [5, "D"], [4, "CD"], [9, "CM"]]),
    new Map([[1, "M"]]),
];

/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
    let numDigits = Math.floor(Math.log10(num));
    const s = [];

    while (numDigits >= 0) {
        const unit = 10 ** numDigits;
        let digit = Math.floor(num / unit);
        num = num % unit;
        const unitMap = CONVERSION_MAP[numDigits];
        const v = unitMap.get(digit);
        if (v) {
            s.push(v);
            digit = 0;
        } else if (digit > 5) {
            s.push(unitMap.get(5));
            digit -= 5;
        }
        s.push(unitMap.get(1).repeat(digit));

        numDigits -= 1;
    }

    return s.join('')
};

console.log(intToRoman(3999));
console.log(intToRoman(321));
console.log(intToRoman(14));

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
    let hasWordStarted = false, len = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] != ' ') {
            if (!hasWordStarted) {
                hasWordStarted = true;
            }
            len += 1;
        } else {
            if (hasWordStarted) return len;
        }
    }

    return len;
};

/*
 * Key insight:
 * Roman conversion: process place values using special forms for 4 and 9. Last word: scan
 * backward past spaces, then count letters until the next space.
 */
