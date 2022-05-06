import tkinter as tk
import tkinter.font as font
from tkvideo import tkvideo
from tkinter import filedialog
from find_motion import find_motion
from detect_mask_video import detect_mask
from social_distancing_detection import social_distance_detector_live

window =  tk.Tk()
window.title = "Smart Surveillance Systems"
window.geometry("500x300")
window.configure(bg="#141414")


def bttn(x, y, text, bcolor, fcolor, cmd):
	def on_enter(e):
		mybutton['background']=bcolor
		mybutton['foreground']=fcolor

	def on_leave(e):
		mybutton['background']=fcolor
		mybutton['foreground']=bcolor

	mybutton = tk.Button(window, width=70, height=2, text=text, 
		fg=bcolor, 
		bg=fcolor, 
		activeforeground=fcolor,
		activebackground=bcolor, 
		command=cmd,)

	mybutton.bind('<Enter>', on_enter)
	mybutton.bind('<Leave>', on_leave)
	mybutton.place(x=x, y=y)

"""
def openfile():
	window.filename = filedialog.askopenfilename( initialdir="/vids", title="Select a file", 
		filetype=( ("all files", "*.mp4"),))
	video_label = tk.Label(window)
	video_label.pack()

	player = tkvideo("window.filename", video_label,
                 loop = 1, size = (500, 300))

"""

label = tk.Label(window, text='Smart Surveillance Systems', 
	width=70, height=5, font='25',
	bg='#141414',
	fg='#ffffff')
label.pack()


bttn(0, 100, 'DETECT THEFT', '#1ad1ff', '#141414', find_motion)
bttn(0, 137, 'DETECT FACE MASK', '#00cc00', '#141414', detect_mask)
bttn(0, 174, 'DETECT SOCIAL DISTANCING', '#ff00ff', '#141414', social_distance_detector_live)
bttn(0, 211, 'E X I T', '#ff0000', '#141414', window.quit)

window.mainloop()

