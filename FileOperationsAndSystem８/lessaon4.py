#テンプレート
import string

with open('design/email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Gin', contents='How are you?')
print(contents)