from os import listdir

"prints to all open terminals then closes the file"

things = listdir('/dev/pts/')
things.remove('ptmx')

for term in things:
    file = open(f'/dev/pts/{term}','w')
    file.write('Hello World\n')
    file.close()
