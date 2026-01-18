def IsVowel(character):
    if (character == 'a') or (character == 'e') or (character == 'i') or (character == 'o') or (character == 'u'):
        return True
    else:
        return False


def main():
    Ret = IsVowel('a')
    
    if Ret == True:
        print("Vowel")
    else:
        print("Not a vowel")

if __name__ == "__main__":
    main()