import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

#一時的ではなく残しておきたい場合
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('tes\n')
        f.seek(0)
        print(f.read())

#ディレクトリ でのテンポラリが作れる
with tempfile.TemporaryDirectory() as td:
    print(td)
temp_dir = tempfile.mkdtemp()
print(temp_dir)


