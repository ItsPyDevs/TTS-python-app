try: import tkinter as tk, pyttsx3, threading, os
except: print("PLEASE INSTALL PYTTSX3 & THREADING")

voice = pyttsx3.init()
app = tk.Tk()
app.geometry("400x200")
app.title("Tk2Voice")

def parler(): 
    texte = Content.get()
    if texte != "": voice.say(texte) ; threading.Thread(target=lambda: voice.runAndWait()).start() ; Content.delete(0, tk.END)
    else: voice.say("ERROR") ; threading.Thread(target=lambda: voice.runAndWait()).start()

Content = tk.Entry(app, cursor="xterm #FFFFFF")
Content.pack(pady=50)
tk.Button(text="Démarer le TTS !", command=parler).pack()
tk.Button(text="Quit", command=lambda: os._exit(0)).pack()
app.mainloop()