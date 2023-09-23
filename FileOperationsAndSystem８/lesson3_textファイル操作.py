""""
f = open('test.txt', 'w')
f.write('Test\n')
print('My', 'name' 'is', 'Mike', sep='#', end='!', file=f)
f.close()
"""

"withでつけることでcloseする必要がなくなる"
s = """\
AAA
BBB
CCC
DDD
"""

#with open('test.txt', 'w') as f:
#    f.write('Hi, Gin!\n')
#    f.write(s)

with open('test.txt', 'r') as f:
    #print(f.read())
    """while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break"""
    """while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break"""
"""    print(f.tell())
    print(f.read(1))
    f.seek(8)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(17)
    print(f.read(1))
    f.seek(8)
    print(f.read(1))"""

#書き込んだ後に読み込みたいとき,'w+'を置いてSeekで先頭に戻る
#'w+'で書いた時は書き込み用になるのでまっさらになるので注意r+は読み込みが最初にできないとエラーになる
with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

with open('test.txt', 'r+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())





