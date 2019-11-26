import git
import os
import shutil
import platform
from tkinter import *
import jsonCreator
#import imp
from git import Repo,remote
import webbrowser
#import finalPrinter
import subprocess
from subprocess import Popen, PIPE, STDOUT
import stat
#try:
    #imp.find_module('pyperclip')
    #found = True
#except ImportError:
    #found = False
    
#if found:
import pyperclip

devMode = False
src=os.path.dirname(os.path.realpath(__file__))

usn='Insert username here!'
pwd='Insert password here!'

abortWhenClose=True

def onerror(func, path, exc_info):
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWUSR)
            func(path)
        else:
            raise

if(os.path.exists(f'{src}/quiz')):
    shutil.rmtree(f'{src}/quiz', onerror=onerror)
git.Git(".").clone("https://github.com/cubered/quiz.git")

def clearScreen():
    if(platform.system()=='Windows'):
        os.system('cls')
    else:
        os.system('clear')
    return
    

root=Tk()
final=[]
tempbool=False
temp=[]
name=""
root.title('Földrajz quiz')
root.iconphoto(True, PhotoImage(file="./Data/bolygo.png"))
NevText=Label(root, text="Név: ")
NevText.pack()
NevEntry=Entry(root)
NevEntry.pack()

index = 1

def closeAddQTab(entry, tab):
    global temp
    global final
    temp[0]=str(entry.get())
    tab.destroy()
    print('tempwhenclose: ', temp)
    final.append(temp)
    return



def closeAddAnsTab(entry, tab, checkbx):
    global temp
    global tempbool
    temp.append([str(entry.get()), tempbool])
    tab.destroy()
    return



def makeAddQTab():
    global temp
    temp=[]
    temp.append("")
    addQTab=Tk()
    KerdesText=Label(addQTab, text="Kérdés: ")
    entry = Entry(addQTab)
    KerdesText.pack()
    entry.pack()
    
    addAnsButton=Button(addQTab, text='Válasz hozzáadása', command= lambda: addAnswer())
    closeBTN=Button(addQTab, text='Kész', command= lambda: closeAddQTab(entry, addQTab))
    addAnsButton.pack()
    closeBTN.pack()
    
    addQTab.title('Kérdés hohzzáadása')
    #addQTab.iconphoto(True, PhotoImage(file="./Data/bolygo.png"))
    addQTab.mainloop()
    print('temp: ', temp)
    #del temp[-1]
    #del temp[-1]
    return
    
    
def toggle():
    global tempbool
    tempbool=not(tempbool)
    
def addAnswer():
    global temp
    global tempbool
    tempbool=False
    addAnsTab=Tk()
    addAnsTab.title('Válasz hozzáadása')
    #addAnsTab.iconphoto(True, PhotoImage(file="./Data/bolygo.png"))
    ValaszText=Label(addAnsTab, text="Válasz: ")
    entry = Entry(addAnsTab)
    ValaszText.pack()
    entry.pack()
    correct=Checkbutton(addAnsTab, text="Helyes?", command=toggle)
    correct.pack()
    
    closeBTN=Button(addAnsTab, text='Kész', command= lambda: closeAddAnsTab(entry, addAnsTab, correct))
    closeBTN.pack()



def addQuestion():
    makeAddQTab()
    print('final:', final)
    return
    
def cancelQuiz():
	global root
	root.destroy()

def done(entry):
    global root
    global name
    global abortWhenClose
    name=str(entry.get())
    if(name==''):
        name='unnamed'
    print(name)
    abortWhenClose=False
    root.destroy()

addQButton=Button(root, text='Kérdés hozzáadása', command= lambda: addQuestion())
addQButton.pack()

doneButton=Button(root, text='Kész', command= lambda: done(NevEntry))
doneButton.pack()

cancelButton=Button(root, text='Mégse', command= lambda: cancelQuiz())
cancelButton.pack()

root.mainloop()

if not(abortWhenClose):
	print('final2: ', final)
	jsonCreator.main(final)
	clearScreen()

	def callback(url):
		webbrowser.open_new(url)



	nameind=2
	if(os.path.exists(f'{src}/quiz/{name}')):
		while(True):
			if(os.path.exists(f'{src}/quiz/{name}({nameind}))')):
				nameind+=1
			else:
				break
		name=f'{name}({nameind})'
		
	os.system(f'mkdir {src}/quiz/{name}')


	dirstocopy = ['img','sass']
	filestocopy = ['index.html','output.css','output.css.map']

	for item in dirstocopy:
		shutil.copytree(f'{src}/quiz/template/{item}', f'{src}/quiz/{name}/{item}')

	for item in filestocopy:
		shutil.copyfile(f'{src}/quiz/template/{item}', f'{src}/quiz/{name}/{item}')
	shutil.copyfile(f'{src}/final.js', f'{src}/quiz/{name}/index.js')
	os.remove('final.js')
	print('done!')






	bf=open('push.bat','w')
	bf.write(f'cd quiz && git init && git remote set-url origin https://{usn}:{pwd}@github.com/cubered/quiz.git && git add . && git commit -m "Added {name}" && git push origin master')
	bf.close()
	os.system('push')

	'''subprocess.call(['git init'], cwd=f'{src}/quiz', shell=True)
	subprocess.call([f'git remote set-url origin https://{usn}:{pwd}@github.com/cubered/quiz.git'], cwd=f'{src}/quiz', shell=True)
	#subprocess.call(['git checkout gh-pages'], cwd=f'{src}/quiz', shell=True)
	#subprocess.call(['git branch -u origin/gh-pages gh-pages'], cwd=f'{src}/quiz', shell=True)
	subprocess.call(['git add .'], cwd=f'{src}/quiz', shell=True)
	subprocess.call([f'git commit -m "Added {name}"'], cwd=f'{src}/quiz', shell=True)
	subprocess.call(['git push origin master'], cwd=f'{src}/quiz', shell=True)'''
	'''p = Popen(
		['git push origin master'],
		cwd=f'{src}/quiz',
		shell=True,
		stdin=PIPE,
		stdout=PIPE,
		stderr=PIPE)
	p.stdin.write(f'{usn}')
	p.stdin.write(f'{pwd}')

	stdout, stderr = p.communicate()
	print('---STDOUT---')
	print(stdout)
	print('---STDERR---')
	print(stderr)'''

	print('---')
	clearScreen()
	'''print('Siker! Lehetséges, hogy a quiz csak pár perc múlva lesz látható.')
	print(f'Link: https://quiz.cubered.xyz/{name}')'''
	os.remove(f'{src}/push.bat')
	'''if found:
		pyperclip.copy(f'https://quiz.cubered.xyz/{name}')'''
	if not(devMode):
		shutil.rmtree(f'{src}/quiz', onerror=onerror)
	'''finalfile=open('textfile.txt','w')
	finalfile.write(f'Siker! Lehetséges, hogy a quiz csak pár perc múlva lesz látható!\nLink: https://quiz.cubered.xyz/{name}')
	finalfile.close()
	if devMode:
		finalPrinter.main()
	else:
		subprocess.Popen(([r".\finalPrinter.exe"]))'''
	#finalPrinter.main(f'https://quiz.cubered.xyz/{name}',True)
	finalTab=Tk()
	def closefinaltab():
		global finalTab
		finalTab.destroy()
	def copytoclipboard():
		pyperclip.copy(f'https://quiz.cubered.xyz/{name}')
	finalTab.title('Kész!')
	finalTab.iconphoto(True, PhotoImage(file="./Data/bolygo.png"))
	finalText=Label(finalTab, text="Siker! Lehetséges, hogy a quiz csak pár perc múlva lesz látható!")
	Link=Label(finalTab,text=f'https://quiz.cubered.xyz/{name}',fg='blue',cursor='hand2')
	copyButton=Button(finalTab,text='Link másolása',command=lambda: copytoclipboard())
	finalButton=Button(finalTab,text='Bezárás',command=lambda: closefinaltab())
	finalText.pack()
	Link.pack()
	copyButton.pack()
	finalButton.pack()
	Link.bind("<Button-1>", lambda e: callback(f'https://quiz.cubered.xyz/{name}'))
	finalTab.mainloop()
print('Done!')
