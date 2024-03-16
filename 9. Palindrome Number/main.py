def main():
    def isPalindrome(x) -> bool:
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]
    
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))

if __name__ == "__main__":
    main()