s ='abcdefghijklmnopqrx'
print(s)

#c = s[2:6]
c = s[-4:]
print(c)

s2 = s[2:4] +s[-4:]
print(s2)


s1 = "afl\\kamdf\nadf\t\tjlka "# python use unicode
print(s1)
s2 = r'aslkdfndlasflkdasnflk///t/t/t\t\t\n\n' # r앞에 쓰면 다 출력 가능
print(s2)

a= 10
s2 = f'a\t{a}'
print(s2)

s3 = "I can't"
print(s3)

s4 = 'I can\'t'
print(s4)

print("----------Methd---------")
# method
s5 = 'a={}'
print(s5.format(a))
print("----------Methd---------")
s6 =  ("안녕하세요 나는 기김성혁입니다. 한"
       "국에서 폴란드로 와써요") # 엔터키 눌러서 할수도 있고, ''' ''' 이 사이에 넣어서 자유롭게 쓸 수도 있음. 그런데 후자는 싱글라인 아님. 여러라인


print(s6.find("김"))  # 단어로 찾는거랑 글자 하나 찾는거랑 차이감 뭔지 궁금하네
print(s6.index("김")) # 그런데 find 는 찾는 게 없으면 -1 을 출력하고, index 는 에러를 만들어냄
print(s6.rindex("김")) # 뒤에서부터 찾음
print(s6.rfind("김")) # 뒤에서부터 찾음?
print(s6.count("요"))