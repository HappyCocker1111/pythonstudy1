import os
import pathlib
import glob
import shutil

#あるか否か
print(os.path.exists('test.txt'))
#ファイルか否か
#print(os.path.isfile('test.txt'))
#フォルダーか否か
#print(os.path.isdir('design'))

#os.rename('test.txt', 'renamed.txt')

#cope like
#os.symlink('renamed.txt', 'symlink.txt')

#os.mkdir('test_dir')
#os.rmdir('test_dir')

#make file
#pathlib.Path('empty.txt').touch()
#os.remove('empty.txt')

#ディレクトリ の中にディレクトリ 作ってその中に何があるか
#os.mkdir('test_dir')
#os.mkdir('test_dir/test_dir2')
#print(os.listdir('test_dir'))

#pathlib.Path('test_dir/test_dir2/empty.txt').touch()
#shutil.copy('test_dir/test_dir2/empty.txt',
#            'test_dir/test_dir2/empty2.txt')
#print(glob.glob('test_dir/test_dir2/*'))

#中身のあるディレクトリ を一気に消す
#shutil.rmtree('test_dir')

#今実行しているpython ファイルの場所を知る
print(os.getcwd())


