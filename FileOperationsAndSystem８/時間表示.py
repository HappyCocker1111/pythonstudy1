import datetime
import time
import os
import shutil

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%F'))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

t = datetime.time(hour=1, minute=10, second=5,microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%F'))


w = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=365)
h = datetime.timedelta(hours=1)
m = datetime.timedelta(minutes=1)
s2 = datetime.timedelta(seconds=1)
m2 = datetime.timedelta(microseconds=1)
print('#####')
print(now - m2)

#指定の秒数まってくれる
print("######")
#time.sleep(3)
print("#####")

print(time.time())


file_name = 'test.txt'

#バックアップファイルを作る.あればバックアップ、なければ書き込む
if os.path.exists(file_name):
    shutil.copy(file_name,"{}.{}".format(
        file_name, now.strftime('%Y_%m_%d-%H_%M_%S_%F')))

with open(file_name, 'w') as f:
    f.write('test')





