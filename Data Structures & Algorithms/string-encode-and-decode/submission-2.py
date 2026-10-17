class Solution:
    def encode(self, strs):
        res = []

        for word in strs:
            res.append(str(len(word)) + "#" + word)

        return "".join(res)

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator after the length
            while s[j] != "#":
                j += 1

            # Parse the length
            length = int(s[i:j])

            # Extract exactly that many characters
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # Move to the next encoded string
            i = end

        return res