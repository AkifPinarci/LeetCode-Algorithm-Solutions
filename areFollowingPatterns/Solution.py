def areFollowingPatterns(strings, patterns):
    hlist = {strings[0]:patterns[0]}
    if len(patterns) == 1:
        return True
    for i in range(len(patterns)):
        if strings[i] not in hlist and patterns[i] in hlist.values():
            return False
        if strings[i] not in hlist:
            hlist[strings[i]] = patterns[i]
        if strings[i] in hlist and hlist[strings[i]] != patterns[i]:
            return False
 

    return True