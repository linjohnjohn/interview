# Problem: Counting Bits; Reverse Bits; Missing Number; Sum of Two Integers; Reverse Integer
# countBits: Count set bits for every integer from 0 through n. reverseBits: Reverse all 32
# bits of an unsigned integer. missingNumber: Find the absent value among distinct numbers
# from 0..len(nums). getSum: Add signed 32-bit integers without + or -. reverse: Reverse
# decimal digits, preserve sign, and return 0 on signed 32-bit overflow.
#
# Expected input/output: countBits(5) -> [0,1,1,2,1,2]; reverseBits(1) -> 2147483648;
# missingNumber([3,0,1]) -> 2; getSum(-2,3) -> 1; reverse(-120) -> -21; reverse(1534236469) ->
# 0


class Solution:
    def countBits(self, n: int) -> list[int]:
        bits = [0]
        for i in range(1, n + 1):
            ones = 0
            while i > 0:
                ones += 1 & i
                i = i >> 1
            bits.append(ones)
        return bits
    
    def reverseBits(self, n: int) -> int:
        rev = []
        for _ in range(32):
            rev.append(n & 1)
            n = n >> 1
        ans = 0
        for idx in range(0, 32):
            ans = ans << 1
            i = rev[idx]
            ans += i
        return ans

    def missingNumber(self, nums: list[int]) -> int:
        s = 0
        for i in nums:
            s += i
        n = len(nums)
        return (n * (n + 1)/2) - s

    def getSum(self, a: int, b: int) -> int:
        # iterate a and b and get last digit
        # XOR to get the new current digit, AND them together to get the carry bit
        # let b be carry
        while b > 0:
            newCarry = a & b
            a = a ^ b
            b = newCarry << 1
        return a

    MAX = 2147483647
    MAX_WITHOUT_LAST = MAX // 10
    MIN = -2147483648
    MIN_WITHOUT_LAST = MIN // 10

    # You are given a signed 32-bit integer x.
    # Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.
    # Solve the problem without using integers that are outside the signed 32-bit integer range.
    def reverse(self, x: int) -> int:
        rArr = []
        is_negative = x < 0
        while x != 0 or x != -0:
            rArr.append(str(x % 10))
            x = int(x / 10)
        
        if len(rArr) < 10:
            return int("".join(rArr))
        else:
            without_last = int("".join(rArr[:9]))
            if (without_last > self.MAX_WITHOUT_LAST):
                return 0
            elif without_last == self.MAX_WITHOUT_LAST:
                if is_negative and int(rArr[-1]) > 8:
                    return 0
                elif not is_negative and int(rArr[-1]) > 7:
                    return 0
                else:
                    return int("".join(rArr))
            else:
                return int("".join(rArr))



s = Solution()
print(s.reverse(-2147483647))
print(s.reverse(-7463847412))

# print(s.reverseBits(2147483648))
# print(s.reverseBits(21))

# Key insight:
# Counting bits: shifting right removes the last bit. Reverse bits: consume exactly 32 low
# bits into a new value. Missing number: subtract the actual sum from n*(n+1)//2. Sum: XOR
# adds without carry; shifted AND supplies carry (mask to 32 bits for signed Python inputs).
# Reverse integer: extract digits and check bounds before appending each digit.
