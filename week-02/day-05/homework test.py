fw = open('simple.txt', 'w')
fw.write('kecskebéka fára mászik')
fw.wrtie('sok a nagy fa az erdőben ezért nincs könnyű dolga')
fw.close()

fr = open('simple.txt','r')
text = fr.read()
print(text)

fr.close