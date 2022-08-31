import sys
input = lambda : sys.stdin.readline().rstrip()
import re

S=input()

check=1
language=[] #문자열 저장 
output=[] #출력 값
a=[]  #괄호 안의 단어

for i in range(len(S)):
    if S[i]=='<':
        a.append(S[i])
        if language:
            language.reverse()
            output.append(language)
            language=[]
        check=0
    elif S[i] =='>':
        a.append(S[i])
        output.append(a)
        a=[]
        check=1
    elif S[i]==' ':
        if check==0:
            a.append(S[i])
        else:
            language.reverse()
            language.append(S[i])
            output.append(language)
            language=[]
   # else:
    #    if check==0:
     #       a.append(S[i])
      #  else:
       #     language.append(S[i])

#if language:
 #   language.reverse()
  #  output.append(language)

for i in range(len(output)):
    print(''.join(output[i]),end='')
  