ss = "mxohcihhudbpsrxhxrrsykmwbaetdzpenjpomyiudctewaizxokvyabqycmmncuggnxskgzwavpmouwfwhxouegyrvtjzctltksglwszmenaqdipvqyyvuyqnueyyhsfpivabtugmckgqzfxquehjecrvmptoxxbcxcbmdmvzflojosixtnwtgnggcyhydnjaeziamnpajbrjuqwucnybbdwmdretgjxzomobimmukhiewphdjsqrrovfdadjyybtipgxbpoqnckpprbenbynelmhwqshwqsuicpktltthfunmbspajxazhuakixmlabkuqaakygliiqzacpjnpvexpsajkianbngcztzlmcwcfupbzajduhpdvxuwzorocmmflcfvtmfvwnecwdfbafpyidpvaxsdyipwmuytrwyuszkuipgihwtookwmlxzcozqurgnnleanaigdcktrcgmwgdivrrbqjfoqfhjdiiddredunjruzkegwsyizunxcgzuyzqtxlhxcujcczcouljtfzqhegebcluximwdpmnoypjpxudbrptuoztorpvvmqkqtxywudnmvejmegxcnqstqrqmkuulxqehvpzpuizsllyabufronymiylvngdhnqfaikxifjfwfrzetfyxhtmhycyxuoptyncviqfvhcbptgatninschckgfjormgykqgethbhypphkixwmdisjfqkcaxxnqtstefwlxyuuezqlhtqourzyagqirmjilbtayfvedtumpxfniplexmzzcevnsseaqczwhdvuplxcegxpyuvieocpbdnfydaowbalutasoppzrvseztjifarlouexsllduiurlbtjbcwoqkuzrtlmcmwqzdmdbxfhmtswwfjvcbjkcbfqemfxmilvmhvshkkrioanlrskrrfencidayguuhmqclyribjhlyjtngtkbrbyqjbopkqjqtdkabgdxpbeustjjnchdxfh"
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

# def validPalindrome(s):
#     front = 0
#     back = -1
#     if s == s[::-1]:
#         return True
#     for i in range(len(s)//2):
#         if s[front + i] == s[back - i]:
#             pass
#         else:
#             if front == 1:
#                 return False
#             if back == -2:
#                 return False           
#             if s[front + i] == s[back - i - 1]:
#                 back -= 1
#             elif s[front + 1 + i] == s[back - i]:
#                 front += 1
#             else:
#                 return False
#     if front == 1 or back == -2:
#         return True
#     return False
# print(validPalindrome(s))



def checkPalindrome(string):
    if string == string[::-1]:
        return True
    return False
def validPalindrome(s):
    if s == s[::-1]:
        return True
    for i in range(len(s)):
        if checkPalindrome(s[0:i] + s[i+1:len(s)]):
            return True
    return False

print(validPalindrome(ss))