import subprocess

#subprocess.run(['ls', '-al'])

#パイプが使えるけどShellはセキュリティー的に推奨されていない
#subprocess.run('ls -al | grep test', shell=True, check=True)

#shell=Trueより安全にいろいろやるには
p1 = subprocess.Popen(['ls', '-ls'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE
)
p1.stdout.close()
output = p2.communicate()[0]
print(output)



