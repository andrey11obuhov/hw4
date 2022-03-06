text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
text=text.replace("\n", " ")
text=text.split(' ')

for i in text:
    if len(i)<4:
        text[text.index(i)]='N'


    else:
        text[text.index(i)]+=' '
n=1
while n!=4:
    for c in text:
        if c=="N":
            text.remove(c)
    n+=1
text=("".join(text))
text=text.split('.')
for i in text:
    text[text.index(i)]=i.split(' ')

print(text)