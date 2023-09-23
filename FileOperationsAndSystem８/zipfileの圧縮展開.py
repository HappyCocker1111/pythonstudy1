import glob
import zipfile

#zipファイル作る
with zipfile.ZipFile('test.zip', 'w') as z:
    #z.write('test_dir')
    #z.write('test_dir/test.txt')

#対象以下を全部呼び出してくれる
    for f in glob.glob('test_dir/**',recursive=True):
        print(f)
        z.write(f)






