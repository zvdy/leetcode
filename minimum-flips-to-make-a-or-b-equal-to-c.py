class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Find the maximum number of bits
        max_bits = max(a.bit_length(), b.bit_length(), c.bit_length())
        # Convert a, b, c to binary strings
        a = bin(a)[2:].zfill(max_bits)
        b = bin(b)[2:].zfill(max_bits)
        c = bin(c)[2:].zfill(max_bits)
        # Count the number of flips
        flips = 0
        for i in range(max_bits):
            if c[i] == '0':
                if a[i] == '1':
                    flips += 1
                if b[i] == '1':
                    flips += 1
            else:
                if a[i] == '0' and b[i] == '0':
                    flips += 1
        return flips