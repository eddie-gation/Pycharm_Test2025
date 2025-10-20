from operator import truediv

p = True
q = False

if p:
    print("p")
    a = 10
else:
    print("not p")
    a = 8

print(f'a = {a}')



if p and q:
    print('p and q')
else:
    print('not p or q')

if p or q:
    print('p or q')
else:
    print('not p or q')

if p and not q:
    print('p and not q')
else:
    print('not p or q')

#xor 이거 쓰면 둘 중에 하나만 맞아야 true 가 나옴 --> 정확한 건 더 찾아봐

if p ^ q:
    print('p xor q')
else :
    print('not p ^ q')