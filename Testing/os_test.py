import os
print(os.listdir('static'))

l = [x for x in os.listdir('static')]

print(l[0])
print(l[0]=='static/545905.jpg')