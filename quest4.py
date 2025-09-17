def check_palindrome(strings):
    result = []
    for s in strings:
        result.append(s == s[::-1])
    return result

strings = ['Palindrome', 'madamimadam', 'mom']
print(check_palindrome(strings))
