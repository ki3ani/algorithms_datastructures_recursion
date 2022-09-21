def ispali(word):

    if word == word[::-1]:

        return True

    return False

word = "adama"
ans = ispali(word)

print(ans)

#check for palindrome in 0(1) time



    