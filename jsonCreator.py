import json
import os

added = False
full=[]
def addAnswer(data, dat, added):
	print('Got there')
	print(dat)
	if(not(added)):
		added=True
		for i in range(len(dat)):
			data['answers'].append({
				'text':dat[i][0],
				'correct': dat[i][1]
			})
	print(data)
	addQ(True, data, dat)
def addQ(makeData, dataf, dat):
	if(not(makeData)):
		data = {}
		data['question']=dat[0]
		del dat[0]
		data['answers']=[]
		addAnswer(data, dat, added)
	print(dataf)
	if(not(dataf==None)):
		full.append(dataf)

def getAns():
	if(input('Correct? ').upper()=='Y'):
		return True
	else:
		return False

def write():
	with open('data.json', 'w',encoding="utf8") as outfile:
		json.dump(full, outfile, ensure_ascii=False)


	f=open('data.json', 'r',encoding="utf8")
	line=f.readline()
	line=line.replace('"question"','question')
	line=line.replace('"text"','text')
	line=line.replace('"answers"','answers')
	line=line.replace('"correct"','correct')
	f.close()
	f=open('data.json','w',encoding="utf8")
	f.write(line)
	f.close()


	f=open('final.js','w',encoding="utf8")
	j=open('data.json','r',encoding="utf8")
	g=open('temp.js','r',encoding="utf8")
	f.write(f'const q = {j.readline()}\n')
	for i in range(96):
		f.write(f'{g.readline()}\n')
	f.close()
	j.close()
	g.close()
	os.remove('data.json')

def main(dat):
	'''if(len(full)==0):
		addQ(False, None)
	else:
		if(input('Add question? ').upper()=='Y'):
			addQ(False, None)
		else:
			print(full)
			write()'''
	print(len(dat))
	for i in range(len(dat)):
		addQ(False, None, dat[i])
	write()
#main([['Alma?', ['yeet', True], ['Nay', False]], ['Alma?', ['yeet', True], ['Nay', False]]])
