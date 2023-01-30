import os
from tkinter import Tk, filedialog, Label, Entry, Button

root = Tk()
root.title("MP4 to GIF converter")
root.geometry("400x300")

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))
    file_label.config(text=file_path)

def convert_to_gif():
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    scale = scale_entry.get()
    frame_rate = frame_rate_entry.get()
    output_file = filedialog.asksaveasfilename(title="Save GIF as", defaultextension=".gif", filetypes=(("GIF files", "*.gif"), ("All files", "*.*")))
 

    # Generate palette
    os.system(f'ffmpeg -ss {start_time} -to {end_time} -i "{file_path}" -vf "fps={frame_rate},scale={scale}:flags=lanczos,palettegen" -y palette.png')

    # Generate GIF
    os.system(f'ffmpeg -ss {start_time} -to {end_time} -i "{file_path}" -i palette.png -lavfi "fps={frame_rate},scale={scale}:flags=lanczos[x];[x][1:v]paletteuse" -y "{output_file}"')
    
    
    

file_label = Label(root, text="No file selected")
file_label.pack()

browse_button = Button(root, text="Browse", command=browse_file)
browse_button.pack()

frame_rate_label = Label(root, text="Frame rate")
frame_rate_label.pack()

frame_rate_entry = Entry(root)
frame_rate_entry.insert(0, 30)
frame_rate_entry.pack()

scale_label = Label(root, text="Scale")
scale_label.pack()

scale_entry = Entry(root)
scale_entry.insert(0, "-1:-1")
scale_entry.pack()

start_time_label = Label(root, text="Start time (hh:mm:ss):")
start_time_label.pack()

start_time_entry = Entry(root)
start_time_entry.insert(0, "00:00:00")
start_time_entry.pack()

end_time_label = Label(root, text="End time (hh:mm:ss):")

end_time_label.pack()

end_time_entry = Entry(root)
end_time_entry.insert(0, "00:00:00")
end_time_entry.pack()

convert_button = Button(root, text="Convert", command=convert_to_gif)
convert_button.pack()

root.mainloop()
