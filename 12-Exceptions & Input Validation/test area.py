
def HasValidLength(input):
    result = False
    return len(input) >= 2 and len(input) <= 32





def IsValidEmail(email):
    result = False
    #check if contains @
    #check if has text before and after @
    #check that there is at least one '.' after the @
    #check before @ is between 2 and 32 chards
    #check after @ is between 2 and 
    atlist = email.split('@')

    if len(atlist) != 2:
        return False
    
    
    dotlist = atlist[1].split('.')

    if len (dotlist) >=2:
        return False

    if not HasValidLength(atlist[0]) and HasValidLength(dotlist[0])):``
        return False

