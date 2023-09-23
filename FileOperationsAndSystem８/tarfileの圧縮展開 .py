import tarfile

#test.tar.gzという圧縮ファイルができる
#展開するにはターミナル からtar zxvf test.tar.gz -C /tmp

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    #別ファイルとして圧縮ファイル を解凍
    #tr.extractall(path='test_tar')

    #既存ディレクトリ の特定のものにアクセス
    with tr.extractfile('test_dir/test_dir2/test2.txt') as f:
        print(f.read())


