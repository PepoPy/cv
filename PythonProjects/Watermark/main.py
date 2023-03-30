from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageFont, ImageDraw, Image, ImageTk


FONT = ('Courier', 15, 'normal')
FONT_SIZE = 700
OPTIONS_MENU = ('Bebas Neue', 'Delius Unicase', 'Neucha', 'Red Rose', 'Righteous', 'Wallpoet')
FONTS_PATH = {'Bebas Neue': 'Fonts/BebasNeue-Regular.ttf',
              'Delius Unicase': 'Fonts/DeliusUnicase-Regular.ttf',
              'Neucha': 'Fonts/Neucha-Regular.ttf',
              'Red Rose': 'Fonts/RedRose-VariableFont_wght.ttf',
              'Righteous': 'Fonts/Righteous-Regular.ttf',
              'Wallpoet': 'Fonts/Wallpoet-Regular.ttf'}


def upload_file(text):
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    watermark(filename, text)


def watermark(filename, text):
    font_selected = variable.get()
    font_size = int(size_entry.get())
    with Image.open(filename).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        # get a font
        text = text.upper()
        fnt = ImageFont.truetype(FONTS_PATH[font_selected], font_size)
        # Calculates the width of the watermark for centering purposes
        text_width = fnt.getlength(text)
        # get a drawing context
        d = ImageDraw.Draw(txt)
        # Calculates the width start of the text to be centered in image
        width_display = (base.width - text_width)/2
        # draw text, half opacity, at the center of image
        d.text((width_display, base.height/2), text, font=fnt, fill=(255, 255, 255, 128))
        out = Image.alpha_composite(base, txt)
        out = out.convert('RGB')
        out.show()
        out.save('WatermarkImage.jpg')


window = Tk()
window.title('Watermarking')
window.config(pady=50, padx=50)
title_label = Label(text='Python Watermarking', font=FONT)
title_label.grid(column=0, row=0, columnspan=4)
content_label = Label(text='Watermark Content:', font=FONT)
content_label.grid(column=0, row=1, columnspan=2)
content_text = Entry()
content_text.grid(column=2, row=1, columnspan=2)
font_label = Label(text='Font:', font=FONT)
font_label.grid(column=0, row=2)
variable = StringVar(window)
variable.set(OPTIONS_MENU[0])
font_menu = OptionMenu(window, variable, *OPTIONS_MENU)
font_menu.config(width=10)
font_menu.grid(column=1, row=2)
size_label = Label(text='Size:', font=FONT)
size_label.grid(column=2, row=2)
size_entry = Entry(width=5)
size_entry.grid(column=3, row=2)
button_upload=Button(text='Upload Image', command=lambda:upload_file(content_text.get()))
button_upload.grid(column=0, row=3, columnspan=4)
button_close = Button(text='Close App', command=window.destroy)
button_close.grid(columnspan=4, column=0, row=4)

window.mainloop()