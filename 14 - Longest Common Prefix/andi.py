def longestCommonPrefix(self, strs: List[str]) -> str:
        finpref = ''
        lostr = len(strs)
        for x in range(lostr):
            currentLengthOfPref = len(finpref)
            if x == 0:
                finpref = strs[0]
            else:
                wordToDecypher = strs[x]
                for inspectedLetter in wordToDecypher:
                    if not inspectedLetter == finpref[wordToDecypher.index(inspectedLetter)]:
                        finpref = finpref[:wordToDecypher.index(inspectedLetter)-1]
        return finpref
