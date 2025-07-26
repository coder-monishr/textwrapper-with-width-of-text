import textwrap

#this converts ---> ABCDEFGHIJ -----> as  ----> wrapwidth = 3 -----> ABC in next line EFG HIJ 

a = 'a'
n = input("whrer to stp: ")
morecharorders = ""
current = 0
ordofstart = ord(a)
ordofend = ord(n)
for i in range(0, 11):
    current = ordofstart+i
    chre = chr(current)
    morecharorders = morecharorders+chre
print(morecharorders)

finaltext = textwrap.fill(morecharorders, 3)
print(finaltext)