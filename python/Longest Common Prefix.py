def main():
    def longestCommonPrefix(strs) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
    
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog", "racecar", "car"]))
    print(longestCommonPrefix([""]))
    print(longestCommonPrefix(["a"]))

if __name__ == "__main__":
    main()