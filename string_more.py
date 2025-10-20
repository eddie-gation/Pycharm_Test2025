s1 = 'booker12\t9012\tRachel\tBooker'

ar1 = [131, 1542, 63645]
print(type(ar1))
print(ar1)
print(ar1[0])
print(ar1[1])

ars1 = s1.split('\t')
print(type(ars1))
print(ars1)
print('------------')
s2 = '|'.join(ars1) # 잘려져 있는 리스트를 내가 원하는 문자를 넣어서 하나로 만드는건가?
print(type(s2))  #str 타입
print(s2)

print('------------')

print(chr(98)) # b 가 나올거임 , ASCII table
