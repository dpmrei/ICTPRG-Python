def IsPalindrome(a):
    clean = a.lower().replace(" ", "")
    rev = "".join(reversed(clean))
    if rev == clean:
        return True
    else:
        return False