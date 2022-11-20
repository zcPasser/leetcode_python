

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_code_table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                            "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
                            ]
        transformations = set()
        for word in words:
            trans = ''
            for ch in word:
                trans += morse_code_table[ord(ch) - ord('a')]
            transformations.add(trans)

        return len(transformations)

