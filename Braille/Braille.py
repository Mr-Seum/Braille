from tkinter import *
from tkinter import font
from gtts import gTTS
from tkinter import filedialog
import os
import playsound
import datetime as dt

def main():


    root = Tk()
    root.title('Bangla To Braille')
    root.geometry("1200x800")
    # set the file status
    global open_status_name
    open_status_name = False

    global open_status_name2
    open_status_name2 = False


    # Create New file Funtion
    def new_file():
        my_text.delete("1.0", END)
        root.title("New File")


    # Create Open file Funtion
    def open_file():
        my_text.delete("1.0", END)
        root.title("Opened New File")
        text_file = filedialog.askopenfilename(title="Open File", filetypes=(
            ("Txt Files", "*.txt"), ("Docx Files", "*.docx"), ("All Files", "*.*")))
        if text_file:  # check if there is a file name
            global open_status_name  # if there is a file name then global it
            open_status_name = text_file
        # Open the File
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        # add file to textbox
        my_text.insert(END, stuff)
        # close the opened file
        text_file.close()


    def save_as_file():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(
            ("Txt Files", "*.txt"), ("Docx Files", "*.docx"), ("All Files", "*.*")))
        if text_file:
            text_file = open(text_file, 'w')
            text_file.write(my_text.get(1.0, END))
            text_file.close()




    def save_file():
        global open_status_name
        if open_status_name:
            text_file = open(open_status_name, 'w')
            text_file.write(my_text.get(1.0, END))
            text_file.close()
        else:
            save_as_file()


    my_frame = Frame(root)
    my_frame.pack(pady=5)
    ## Scroll bar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    # Creating Text Box
    my_text = Text(my_frame, width=97, height=10, font=("Siyam Rupali ANSI", 16), selectbackground="yellow",
                   selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
    my_text.pack(expand=True,fill=BOTH)
    # Configure our Scrollbar
    text_scroll.config(command=my_text.yview)

    # Create Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)


    # clse the Window
    def quit():
        root.destroy()


    # add File Menu
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quit)

    # add Edit Menu
    edit_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Undo")
    edit_menu.add_command(label="Redo")

    # add button Section

    button_bar = Label(root, text="Here It is")
    button_bar.pack(fill=X, side=TOP, ipady=10)


    def helloCallBack():
        root.showinfo("Hello Python", "Hello World")








    def braille_textbox():
        root.destroy()

        root2braille = Tk()
        root2braille.title('Braille To Bangla')
        root2braille.geometry("1200x800")
        # set the file status
        global open_status_name
        open_status_name = False


        # Create New file Funtion
        def new_file():
            my_text.delete("1.0", END)
            root2braille.title("New File")


        # Create Open file Funtion
        def open_file():
            my_text.delete("1.0", END)
            root2braille.title("Opened New File")
            text_file = filedialog.askopenfilename(title="Open File", filetypes=(
                ("Txt Files", "*.txt"), ("Docx Files", "*.docx"), ("All Files", "*.*")))
            if text_file:  # check if there is a file name
                global open_status_name  # if there is a file name then global it
                open_status_name = text_file
            # Open the File
            text_file = open(text_file, 'r')
            stuff = text_file.read()
            # add file to textbox
            my_text.insert(END, stuff)
            # close the opened file
            text_file.close()


        def save_as_file():
            text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(
                ("Txt Files", "*.txt"), ("Docx Files", "*.docx"), ("All Files", "*.*")))
            if text_file:
                text_file = open(text_file, 'w')
                text_file.write(my_text.get(1.0, END))
                text_file.close()


        def save_file():
            global open_status_name
            if open_status_name:
                text_file = open(open_status_name, 'w')
                text_file.write(my_text.get(1.0, END))
                text_file.close()
            else:
                save_as_file()


        my_frame = Frame(root2braille)
        my_frame.pack(pady=5)
        ## Scroll bar
        text_scroll = Scrollbar(my_frame)
        text_scroll.pack(side=RIGHT, fill=Y)

        # Creating Text Box
        my_text = Text(my_frame, width=97, height=10, font=('Swell Braille', 16), selectbackground="yellow",
                       selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
        my_text.pack(expand=True)
        # Configure our Scrollbar
        text_scroll.config(command=my_text.yview)

        # Create Menu
        my_menu = Menu(root2braille)
        root2braille.config(menu=my_menu)


        # clse the Window
        def quit():
            root2braille.destroy()


        # add File Menu
        file_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=new_file)
        file_menu.add_command(label="Open", command=open_file)
        file_menu.add_command(label="Save", command=save_file)
        file_menu.add_command(label="Save As", command=save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)

        # add Edit Menu
        edit_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")

        def bangla_textbox():
            root2braille.destroy()
            main()

        # Creating the  Braille to bangle convertion Funtion

        def braille2bangla(string):
            # measurement of length of the string
            string = string + "         "
            str_len = len(string)
            quote = False
            First = False
            Number_Prefix = False
            count_two = 0
            count_three = 0
            # creating a dictianary where keys are braille letter and values are bangla
            braille_2_ban_1by1 = {
                # Single One to one maping
                "⠅": "ক",  # braille pattern dots-13
                "⠨": "খ",  # braille pattern dots-46
                "⠣": "ঘ",  # braille pattern dots-126
                "⠬": "ঙ",  # braille pattern dots-346
                "⠡": "ছ",  # braille pattern dots-16
                "⠵": "ঝ",  # braille pattern dots-1356
                "⠾": "ট",  # braille pattern dots-23456
                "⠺": "ঠ",  # braille pattern dots-2456
                "⠫": "ড",  # braille pattern dots-1246
                "⠿": "ঢ",  # braille pattern dots-123456
                "⠞": "ত",  # braille pattern dots-2345
                "⠹": "থ",  # braille pattern dots-1456
                "⠧": "ভ",  # braille pattern dots-1236
                "⠤": "-",  # braille pattern dots-36
                "⠮": "ধ",  # braille pattern dots-2346
                "⠝": "ন",  # braille pattern dots-1345
                "⠏": "প",  # braille pattern dots-1234
                "⠍": "ম",  # braille pattern dots-134
                "⠽": "য",  # braille pattern dots-13456
                "⠗": "র",  # braille pattern dots-1235
                "⠇": "ল",  # braille pattern dots-123
                "⠩": "শ",  # braille pattern dots-146
                "⠯": "ষ",  # braille pattern dots-12346
                "⠎": "স",  # braille pattern dots-234
                "⠲": "।",  # braille pattern dots-256
                # "⠠⠦" : "‘", # braille pattern dots-6 and dots-236
                # "⠦⠄" : "’", #braille pattern dots-356 and dots-3
                # "⠠⠶" : "[", # braille pattern dots-6 and dots-2356
                # "⠶⠄" : "]", #braille pattern dots-2356 and dots-3
                "⠻": "ড়",  # braille pattern dots-12456
                "⠷": "ঢ়",  # braille pattern dots-12356
                #"⠢": "য়",  # braille pattern dots-26
                # "⠂⠞" : "ৎ", # braille pattern dots-5 and dots-2345
                "⠄": "ঁ",  # braille pattern dots-3
                # "⠰": "ং",  # braille pattern dots-56
                # "⠠": "ঃ",  # braille pattern dots-6
                "⠟": "ক্ষ",  # braille pattern dots-12345
                "⠱": "জ্ঞ",  # braille pattern dots-156
                "⠆": ";",  # braille pattern dots-23
                "⠖": "!",  # braille pattern dots-235
                # "⠰⠶" : "=", # Not Found in Wiki but dots-56 and dots-2356 from paper
                # "⠔⠔" : "*", # braille pattern dots-35 and dots-35
                " ": " "}

            # double two to one mapping
            braille_2_ban_rest = {

                "⠁": "অ",  # braille pattern dots-1

                "⢜": "আ",  # wiki has braille pattern dots-345 but paper has some difference

                "⠔": "ঈ",  # braille pattern dots-35

                "⠥": "উ",  # braille pattern dots-136

                "⠳": "ঊ",  # braille pattern dots-1256

                # "⠐⠗": "ঋ",  # braille pattern dots-5 and dots-1235

                "⠕": "ও",  # braille pattern dots-135

                "⠪": "ঔ",  # braille pattern dots-246

                "⠛": "গ",  # braille pattern dots-1245

                "⠉": "চ",  # braille pattern dots-14

                "⠚": "জ",  # braille pattern dots-245

                # "⠒": "ঞ",  # braille pattern dots-25

                # "⠼": "ণ",  # braille pattern dots-3456
                # "⠼" : "Np", # Np(Number Prefix) braille pattern dots-3456
                "⠙": "দ",  # braille pattern dots-145

                "⠋": "ফ",  # wiki uses braille pattern dots-235 differ in paper

                "⠃": "ব",  # braille pattern dots-12

                "⠓": "হ",  # braille pattern dots-125

                # "⠴": "্",  # wiki uses braille pattern dots-4

                # "⠦": "?",  # braille pattern dots-236

                # "⠶": "(",  # According to Unesco and paper

                # triple three to one mapping
                "⠊": "ই",  # braille pattern dots-24

                "⠑": "এ",  # braille pattern dots-15

                "⠌": "ঐ",  # braille pattern dots-34

                # "⠂": ",",  # braille pattern dots-2

            }

            braille_numbers = {
                "⠚": "০",  # braille pattern dots-245
                "⠁": "১",  # braille pattern dots-1
                "⠃": "২",  # braille pattern dots-12
                "⠉": "৩",  # braille pattern dots-14
                "⠙": "৪",  # braille pattern dots-145
                "⠑": "৫",  # braille pattern dots-15
                "⠋": "৬",  # braille pattern dots-124
                "⠛": "৭",  # braille pattern dots-1245
                "⠓": "৮",  # braille pattern dots-125
                "⠊": "৯",  # braille pattern dots-24
                # "⠂": ".",  # only from paper
                "⠌": "/"  # braille pattern dots-34
            }

            braille_kar = {
                "⢜": "া",  # wiki has braille pattern dots-345 but paper has some difference
                "⠊": "ি",  # braille pattern dots-24
                "⠔": "ী",  # braille pattern dots-35
                "⠥": "ু",  # braille pattern dots-136
                "⠳": "ূ",  # braille pattern dots-1256
                # "⠐⠗": "ৃ",  # braille pattern dots-5 and dots-1235
                "⠑": "ে",  # braille pattern dots-15
                "⠌": "ৈ",  # braille pattern dots-34
                "⠕": "ো",  # braille pattern dots-135
                "⠪": "ৌ",  # braille pattern dots-246
            }
            braille_symble = {
                "⠒": ":",  # braille pattern dots-25
                "⠴": "”",  # Not found in wiki according to paper and unesco
                "⠦": "“",  # braille pattern dots-236
                "⠶": ")",  # According to Unesco and paper

                "⠂": "’",  # only from paper
            }

            numbers = ['১', "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯", "০"]

            consonent = ["⠅", "⠨", "⠣", "⠬", "⠡", "⠵", "⠾", "⠺", "⠫", "⠿", "⠞", "⠹", "⠧", "⠮", "⠝", "⠏", "⠍", "⠽", "⠗",
                         "⠇",
                         "⠩", "⠯",
                         "⠎", "⠻", "⠷", "⠢", "⠄", "⠰", "⠠", "⠛", "⠉", "⠚", "⠒", "⠼", "⠙", "⠋", "⠃", "⠓"]
            # Creating empty string for output
            output = list()

            # length of braille text
            str_len = len(string)
            for i in range(str_len):
                # For Single Cell Braille and one vs one map
                if string[i] in braille_2_ban_1by1.keys():
                    output.append(braille_2_ban_1by1[string[i]])
                    Number_Prefix = False




                # FOR Double Cell Braille
                else:

                    if string[i] == "⠼":
                        Number_Prefix = False  # else a gele true hobe (Deafult value of Number_Prefix is False)
                        if string[i + 1] in ["⠾", "⠺", "⠫", "⠷",
                                             "⠼"]:  # ta borgio borner age "ণ" hoy # Na dileo houar kotha
                            output.append("ণ")
                        elif string[i - 1] == "⠗" and string[i - 2] == "⠐":  # rri er por "ণ" hoy
                            output.append("ণ")
                        elif string[i - 1] in ["⠗", "⠯"]:  # R and SSh er por "ণ" hoy
                            output.append("ণ")
                        # ka borgio dhonni ["⠅","⠨","⠛","⠣","⠬"]
                        # pa borgio dhonni ["⠏","⠋","⠃","⠧","⠍"]
                        # SSh ya ba ha ng ["⠯","⠢","⠃","⠓","⠰"]
                        # sorodhonni ["⠁","⢜","⠊","⠔","⠥","⠳","⠑","⠌","⠕","⠪","⠐⠗"]
                        # rri er por sorodhonni or ka borgio dhonni or pa borgio dhonni or Shh ya ba ha ng hole er por "ণ" hoy
                        elif string[i - 2] == "⠗" and string[i - 3] == "⠐" and (
                                string[i - 1] in ["⠁", "⢜", "⠊", "⠔", "⠥", "⠳", "⠑", "⠌", "⠕", "⠪", "⠐⠗"] or string[
                            i - 1] in [
                                    "⠯", "⠢", "⠃", "⠓", "⠰"] or string[i - 1] in ["⠅", "⠨", "⠛", "⠣", "⠬"] or string[
                                    i - 1] in ["⠏",
                                               "⠋",
                                               "⠃",
                                               "⠧",
                                               "⠍"]):
                            output.append("ণ")
                        # R and SSh er por sorodhonni or ka borgio dhonni or pa borgio dhonni or Shh ya ba ha ng hole er por "ণ" hoy
                        elif string[i - 2] in ["⠗", "⠯"] and (
                                string[i - 1] in ["⠁", "⢜", "⠊", "⠔", "⠥", "⠳", "⠑", "⠌", "⠕", "⠪", "⠐⠗"] or string[
                            i - 1] in [
                                    "⠯", "⠢", "⠃", "⠓", "⠰"] or string[i - 1] in ["⠅", "⠨", "⠛", "⠣", "⠬"] or string[
                                    i - 1] in ["⠏",
                                               "⠋",
                                               "⠃",
                                               "⠧",
                                               "⠍"]):
                            output.append("ণ")
                        elif string[i - 1] == "⠟":
                            output.append("ণ")
                        elif string[i - 2] == "⠉" and string[i - 1] == "⢜":  # caniky
                            output.append("ণ")
                        elif string[i - 2] == "⠍" and string[i - 1] == "⢜":  # maniky
                            output.append("ণ")
                        elif string[i - 1] == "⠛":
                            output.append("ণ")
                        elif string[i - 2] == "⠃" and string[i - 1] == "⢜":  # banijjo
                            output.append("ণ")
                        elif string[i - 2] == "⠇" and string[i - 1] == "⠃":  # lobon
                            output.append("ণ")
                        elif string[i - 1] == "⠍":  # mon
                            output.append("ণ")
                        elif string[i - 2] == "⠃" and string[i - 1] == "⠑":  # benu
                            output.append("ণ")
                        elif string[i - 2] == "⠃" and string[i - 1] == "⠔":  # bIna
                            output.append("ণ")
                        elif string[i - 4] == "⠅" and string[i - 3] == "⠈" and string[i - 2] == "⠬" and string[
                            i - 1] == "⠅":  # "কঙ্কণ"
                            output.append("ণ")
                        elif string[i - 1] == "⠅":
                            output.append("ণ")
                        elif string[i - 5] == "⠅" and string[i - 4] == "⠈" and string[i - 3] == "⠇" and string[
                            i - 2] == "⠽" and \
                                string[i - 1] == "⢜":  # "কল্যাণ" ['⠅', '⠈', '⠇', '⠽', '⢜', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠩" and string[i - 1] == "⠕":  # "শোণিত" ['⠩', '⠕', '⠼', '⠊', '⠞', ' ']
                            output.append("ণ")
                        elif string[i - 1] == "⠍":  # "মণি" ['⠍', '⠼', '⠊', ' ']
                            output.append("ণ")
                        elif string[i - 4] == "⠈" and string[i - 3] == "⠎" and string[i - 2] == "⠹" and string[
                            i - 1] == "⢜":  # "স্থাণু" ['⠈', '⠎', '⠹', '⢜', '⠼', '⠥', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠛" and string[i - 1] == "⠥":  # গুণ ['⠛', '⠥', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 3] == "⠏" and string[i - 2] == "⠥" and string[
                            i - 1] == "⠈":  # পুণ্য ['⠏', '⠥', '⠈', '⠼', '⠽', ' ']
                            output.append("ণ")
                        elif string[i - 1] == "⠋":  # "ফণী ['⠋', '⠼', '⠔', ' ']
                            output.append("ণ")
                        elif string[i - 1] == "⠁":  # "অণু" ['⠁', '⠼', '⠥', ' ']
                            output.append("ণ")
                        elif string[i - 3] == "⠃" and string[i - 2] == "⠊" and string[
                            i - 1] == "⠏":  # "বিপণি" ['⠃', '⠊', '⠏', '⠼', '⠊', ' ', ' ']
                            output.append("ণ")
                        elif string[i - 1] == "⠛":  # "গণিকা" ['⠛', '⠼', '⠊', '⠅', '⢜', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⢜" and string[i - 1] == "⠏":  # "আপণ"  ['⢜', '⠏', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 4] == "⠇" and string[i - 3] == "⢜" and string[i - 2] == "⠃" and string[
                            i - 1] == "⠈":  # "লাবণ্য" ['⠇', '⢜', '⠃', '⠈', '⠼', '⠽', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠃" and string[i - 1] == "⢜":  # বাণী ['⠃', '⢜', '⠼', '⠔', ' ']
                            output.append("ণ")
                        elif string[i - 4] == "⠝" and string[i - 3] == "⠊" and string[i - 2] == "⠏" and string[
                            i - 1] == "⠥":  # নিপুণ ['⠝', '⠊', '⠏', '⠥', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 1] == "⠧":  # ভণিতা ['⠧', '⠼', '⠊', '⠞', '⢜', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠏" and string[i - 1] == "⢜":  # পাণি  ['⠏', '⢜', '⠼', '⠊', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠛" and string[i - 1] == "⠪":  # গৌণ ['⠛', '⠪', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠅" and string[i - 1] == "⠕":  # কোণ ['⠅', '⠕', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠧" and string[i - 1] == "⢜":  # ভাণ ['⠧', '⢜', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 1] == "⠏":  # পণ  ['⠏', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠩" and string[i - 1] == "⢜":  # শাণ ['⠩', '⢜', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 5] == '⠉' and string[i - 4] == '⠊' and string[i - 3] == '⠈' and string[
                            i - 2] == '⠅' and \
                                string[i - 1] == '⠅':  # "চিক্কণ"['⠉', '⠊', '⠈', '⠅', '⠅', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 5] == '⠝' and string[i - 4] == '⠊' and string[i - 3] == '⠈' and string[
                            i - 2] == '⠅' and \
                                string[i - 1] == '⠅':  # "নিক্কণ"['⠝', '⠊', '⠈', '⠅', '⠅', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠞" and string[i - 1] == "⠳":  # তূণ ['⠞', '⠳', '⠼', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠅" and string[i - 1] == "⠋":  # "কফণি" ['⠅', '⠋', '⠼', '⠊', ' ']
                            output.append("ণ")
                        elif string[i - 1] == "⠃":  # বণিক ['⠃', '⠼', '⠊', '⠅', ' ']
                            output.append("ণ")
                        elif string[i - 1] == "⠛":  # গণনা ['⠛', '⠼', '⠝', '⢜', ' ']
                            output.append("ণ")
                        elif string[i - 2] == "⠏" and string[i - 1] == "⠊":  # পিণাক ['⠏', '⠊', '⠼', '⢜', '⠅', ' ']
                            output.append("ণ")
                        else:
                            Number_Prefix = True
                    elif string[i] in braille_numbers.keys() and Number_Prefix == True:
                        output.append(braille_numbers[string[i]])
                    elif string[i] in braille_kar.keys() and ((string[i - 1] in consonent) or (
                            string[i - 2] == "⠂" and string[i - 1] == "⠞")):  # "ৎ" alada diye rakhsi 2 cell tai
                        output.append(braille_kar[string[i]])
                        Number_Prefix = False
                    elif string[i] == "⠗" and string[i - 1] == "⠐" and ((string[i - 1] in consonent) or (
                            string[i - 2] == "⠂" and string[i - 1] == "⠞")):
                        output.append("ৃ")
                        Number_Prefix = False
                    elif string[i] == "⠗" and string[i - 1] == "⠐":
                        output.append("ঋ")
                        Number_Prefix = False
                    elif string[i] == "⠦" and string[i - 1] == " " and string[i + 1] != " " and quote == False:
                        output.append("“")
                        quote = True
                        Number_Prefix = False
                    elif string[i] == "⠦" and string[i + 1] == " ":
                        output.append("?")
                        Number_Prefix = False
                    elif string[i] == "⠴" and quote == True:
                        output.append("”")
                        quote = False
                        Number_Prefix = False
                    elif string[i] == "⠴" and quote == False:
                        output.append("্")
                        Number_Prefix = False
                    elif string[i] == "⠶" and First == False:
                        output.append("(")
                        First = True
                    elif string[i] == "⠶" and First == True:
                        output.append(")")
                        First = False
                    elif string[i] == "⠂" and string[i + 1] != " " and string[i - 1] != " ":
                        output.append(".")
                    elif string[i] == "⠂" and string[i + 1] == " " and string[i - 1] != " ":
                        output.append(",")
                    elif string[i] == "⠒" and string[i - 1] == " " and string[i + 1] == " ":
                        output.append(":")
                    elif string[i] == "⠒" and string[i - 1] != " ":
                        output.append("ঞ")
                    elif string[i] in braille_2_ban_rest.keys():
                        output.append(braille_2_ban_rest[string[i]])
                        Number_Prefix = False
                        if string[i - 1] in consonent and string[i] == "⠁" and string[i + 1] in ["⠊", "⠥", "⠕"]:
                            del output[-1]

                    # "⠠⠦" : "‘", # braille pattern dots-6 and dots-236
                    # "⠦⠄" : "’", #braille pattern dots-356 and dots-3
                    # "⠠⠶" : "[", # braille pattern dots-6 and dots-2356
                    # "⠶⠄" : "]", #braille pattern dots-2356 and dots-3

                    elif string[i - 1] == "⠠" and string[i] == "⠦":
                        output.append("‘")

                    elif string[i - 1] == "⠦" and string[i] == "⠄":
                        output.append("’")

                    elif string[i - 1] == "⠠" and string[i] == "⠶":
                        output.append("[")

                    elif string[i - 1] == "⠶" and string[i] == "⠄":
                        output.append("]")

                    # "⠰⠶" : "=", # Not Found in Wiki but dots-56 and dots-2356 from paper
                    # "⠔⠔" : "*", # braille pattern dots-35 and dots-35

                    elif string[i - 1] == "⠰" and string[i] == "⠶":
                        output.append("=")

                    elif string[i - 1] == "⠔" and string[i] == "⠔":
                        output.append("*")

                    # "⠂⠞" : "ৎ", # braille pattern dots-5 and dots-2345

                    # "⠰": "ং",  # braille pattern dots-56
                    # "⠠": "ঃ",  # braille pattern dots-6

                    elif string[i - 1] == "⠂" and string[i] == "⠞":
                        output.append("ৎ")

                    elif string[i] == "⠰":
                        output.append("ং")

                    elif string[i] == "⠠":
                        output.append("ঃ")
                    #"⠢": "য়",  # braille pattern dots-26
                    elif string[i] == "⠢":
                        output.append("য়")

                if string[i - 1] == "⠈" and string[i] in consonent and string[i + 1] in consonent:
                    output.append("্")
                if string[i - 1] == "⠨" or string[i - 2] == "⠨" or string[i - 3] == "⠨" and string[i] in consonent and string[i + 1] in consonent:

                    if string[i - 1] == "⠨":
                        del output[-2]
                    output.append("্")

            string = ''

            return string.join(output)

        def braille2banglaTranslate():
            text = my_text.get(1.0, END)
            translation = braille2bangla(text)
            translate.config(state="normal")
            translate.delete(1.0, END)
            translate.insert(END, translation)
            translate.config(state="disabled")

        def speak(text):
            tts = gTTS(text, lang="bn")
            os.chdir(os.path.join(os.getcwd(), "Audio"))
            now = dt.datetime.now()
            filename = "audio_" + now.strftime("%Y_%m_%d_%H_%M_%S") + ".mp3"
            tts.save(filename)
            playsound.playsound(filename)
            os.chdir('../')

        def braille2banglaAudio():
            text = my_text.get(1.0, END)
            translation = braille2bangla(text)
            speak(translation)

        button_bar = Label(root2braille, text="Here It is")
        button_bar.pack(fill=X, side=TOP, ipady=10)

        Bangla = Button(button_bar, text="Bangla TextBox", command=bangla_textbox)
        Bangla.pack(side=LEFT, expand=True, fill=X)

        Translate_to_bangla = Button(button_bar, text="Translate To Bangla", command=braille2banglaTranslate)
        Translate_to_bangla.pack(side=LEFT, expand=True, fill=X)

        text_to_speech = Button(button_bar, text="Text To Speech", command=braille2banglaAudio)
        text_to_speech.pack(side=LEFT, expand=True, fill=X)

        # another Frame
        my_frame2 = Frame(root2braille)
        my_frame2.pack(fill="both")
        ## Scroll bar
        text_scroll2 = Scrollbar(my_frame2)
        text_scroll2.pack(side=RIGHT, fill=Y)

        translate = Text(my_frame2, font=("Helvetica", 16), bd=0, bg="#fff", selectbackground="yellow",
                         selectforeground="black", yscrollcommand=text_scroll2.set)


        translate.config(state="disabled")
        translate.pack(pady=20, fill=BOTH)

        text_scroll2.config(command=translate.yview)

        root2braille.mainloop()


    # Translating to Braille

    # Creating the bangle to Braille convertion Funtion

    def bangla2braille(string):
        # measurement of length of the string
        string = string + " "
        str_len = len(string)
        # creating a dictianary where keys are bangla letter and values are braille
        ban_2_braille = {
            # Single One to one maping
            "ক": "⠅",  # braille pattern dots-13
            "খ": "⠨",  # braille pattern dots-46
            "ঘ": "⠣",  # braille pattern dots-126
            "ঙ": "⠬",  # braille pattern dots-346
            "ছ": "⠡",  # braille pattern dots-16
            "ঝ": "⠵",  # braille pattern dots-1356
            "ট": "⠾",  # braille pattern dots-23456
            "ঠ": "⠺",  # braille pattern dots-2456
            "ড": "⠫",  # braille pattern dots-1246
            "ঢ": "⠿",  # braille pattern dots-123456
            "ত": "⠞",  # braille pattern dots-2345
            "থ": "⠹",  # braille pattern dots-1456
            "ভ": "⠧",  # braille pattern dots-1236
            "-": "⠤",  # braille pattern dots-36
            "ধ": "⠮",  # braille pattern dots-2346
            "ন": "⠝",  # braille pattern dots-1345
            "প": "⠏",  # braille pattern dots-1234
            "ম": "⠍",  # braille pattern dots-134
            "য": "⠽",  # braille pattern dots-13456
            "র": "⠗",  # braille pattern dots-1235
            "ল": "⠇",  # braille pattern dots-123
            "শ": "⠩",  # braille pattern dots-146
            "ষ": "⠯",  # braille pattern dots-12346
            "স": "⠎",  # braille pattern dots-234
            "।": "⠲",  # braille pattern dots-256
            "‘": "⠠⠦",  # braille pattern dots-6 and dots-236
            "’": "⠦⠄",  # braille pattern dots-356 and dots-3
            "[": "⠠⠶",  # braille pattern dots-6 and dots-2356
            "]": "⠶⠄",  # braille pattern dots-2356 and dots-3
            "ড়": "⠻",  # braille pattern dots-12456
            "ঢ়": "⠷",  # braille pattern dots-12356
            "য়": "⠢",  # braille pattern dots-26
            "ৎ": "⠂⠞",  # braille pattern dots-2 and dots-2345
            "ঁ": "⠄",  # braille pattern dots-3
            "ং": "⠰",  # braille pattern dots-56
            "ঃ": "⠠",  # braille pattern dots-6
            "ক্ষ": "⠟",  # braille pattern dots-12345
            "জ্ঞ": "⠱",  # braille pattern dots-156
            ";": "⠆",  # braille pattern dots-23
            "!": "⠖",  # braille pattern dots-235
            "=": "⠰⠶",  # Not Found in Wiki but dots-56 and dots-2356 from paper
            "*": "⠔⠔",  # braille pattern dots-35 and dots-35
            " ": " ",

            # double two to one mapping

            "অ": "⠁",  # braille pattern dots-1
            "১": "⠁",  # braille pattern dots-1
            "আ": "⢜",  # wiki has braille pattern dots-345 but paper has some difference
            "া": "⢜",  # wiki has braille pattern dots-345 but paper has some difference
            "ঈ": "⠔",  # braille pattern dots-35
            "ী": "⠔",  # braille pattern dots-35
            "উ": "⠥",  # braille pattern dots-136
            "ু": "⠥",  # braille pattern dots-136
            "ঊ": "⠳",  # braille pattern dots-1256
            "ূ": "⠳",  # braille pattern dots-1256
            "ঋ": "⠐⠗",  # braille pattern dots-5 and dots-1235
            "ৃ": "⠐⠗",  # braille pattern dots-5 and dots-1235
            "ও": "⠕",  # braille pattern dots-135
            "ো": "⠕",  # braille pattern dots-135
            "ঔ": "⠪",  # braille pattern dots-246
            "ৌ": "⠪",  # braille pattern dots-246
            "গ": "⠛",  # braille pattern dots-1245
            "৭": "⠛",  # braille pattern dots-1245
            "চ": "⠉",  # braille pattern dots-14
            "৩": "⠉",  # braille pattern dots-14
            "জ": "⠚",  # braille pattern dots-245
            "০": "⠚",  # braille pattern dots-245
            "ঞ": "⠒",  # braille pattern dots-25
            ":": "⠒",  # braille pattern dots-25
            "ণ": "⠼",  # braille pattern dots-3456
            "Np": "⠼",  # Np(Number Prefix) braille pattern dots-3456
            "দ": "⠙",  # braille pattern dots-145
            "৪": "⠙",  # braille pattern dots-145
            "ফ": "⠋",  # wiki uses braille pattern dots-235 differ in paper
            "৬": "⠋",  # braille pattern dots-124
            "ব": "⠃",  # braille pattern dots-12
            "২": "⠃",  # braille pattern dots-12
            "হ": "⠓",  # braille pattern dots-125
            "৮": "⠓",  # braille pattern dots-125
            # "্" : "⠴", # wiki uses braille pattern dots-4
            "”": "⠴",  # Not found in wiki according to paper and unesco
            "?": "⠦",  # braille pattern dots-236
            "“": "⠦",  # braille pattern dots-236
            "(": "⠶",  # According to Unesco and paper
            ")": "⠶",  # According to Unesco and paper

            # triple three to one mapping
            "ই": "⠊",  # braille pattern dots-24
            "ি": "⠊",  # braille pattern dots-24
            "৯": "⠊",  # braille pattern dots-24
            "এ": "⠑",  # braille pattern dots-15
            "ে": "⠑",  # braille pattern dots-15
            "৫": "⠑",  # braille pattern dots-15
            "ঐ": "⠌",  # braille pattern dots-34
            "ৈ": "⠌",  # braille pattern dots-34
            "/": "⠌",  # braille pattern dots-34
            ",": "⠂",  # braille pattern dots-2
            ".": "⠂",  # only from paper
            "’": "⠂",  # only from paper
        }

        numbers = ['১', "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯", "০"]

        consonent = ["ক", "খ", "ঘ", "ঙ", "ছ", "ঝ", "ট", "ঠ", "ড", "ঢ", "ত", "থ", "ভ", "ধ", "ন", "প", "ম", "য", "র", "ল",
                     "শ", "ষ",
                     "স", "ড়", "ঢ়", "য়", "ৎ", "ঁ", "ং", "ঃ", "গ", "চ", "জ", "ঞ", "ণ", "দ", "ফ", "ব", "হ"]
        # Creating empty string for output
        output = list()
        i = 0
        count_conjuntion = 0
        # tracking the start of numbers
        start_of_number = False
        for i in range(str_len):

            if string[i] in ban_2_braille.keys():
                output.append(ban_2_braille[string[i]])

                if string[i] not in numbers:
                    start_of_number = False

                    if (string[i] == "ই" or string[i] == "উ" or string[i] == "ও") and (string[i - 1] in consonent) and (
                            i != 0):  # samner ta consonent kina dekhte hobe
                        output.insert(-1, ban_2_braille["অ"])

                        if string[i] != "্" and string[i - 1] != "্":
                            count_conjuntion = 0
                            if count_conjuntion == 0 and string[i - 1] == "ষ" and string[i - 2] == "্" and string[
                                i - 3] == "ক":
                                output[-4] = ban_2_braille["ক্ষ"]
                                del output[-2]
                                del output[-2]


                            elif count_conjuntion == 0 and string[i - 1] == "ঞ" and string[i - 2] == "্" and string[
                                i - 3] == "জ":
                                output[-4] = ban_2_braille["জ্ঞ"]
                                del output[-2]
                                del output[-2]



                    elif string[i] != "্" and string[i - 1] != "্":
                        count_conjuntion = 0

                        if count_conjuntion == 0 and string[i - 1] == "ষ" and string[i - 2] == "্" and string[
                            i - 3] == "ক":
                            output[-4] = ban_2_braille["ক্ষ"]
                            del output[-2]
                            del output[-2]


                        elif count_conjuntion == 0 and string[i - 1] == "ঞ" and string[i - 2] == "্" and string[
                            i - 3] == "জ":
                            output[-4] = ban_2_braille["জ্ঞ"]
                            del output[-2]
                            del output[-2]





                elif (string[i] in numbers) and not start_of_number:
                    del output[-1]
                    output.append(ban_2_braille["Np"])
                    output.append(ban_2_braille[string[i]])
                    start_of_number = True


            elif string[i] == "্" and i >= 1:
                if count_conjuntion == 0:
                    output.insert(-1, "⠈")
                    count_conjuntion += 1

                elif (count_conjuntion == 1):
                    output[-3] = ban_2_braille["খ"]
                    count_conjuntion += 1

                elif (count_conjuntion == 2):
                    output[-4] = ban_2_braille["খ"]
                    count_conjuntion += 1

                elif (count_conjuntion == 3):
                    count_conjuntion = 0

                elif string[i] != "্" and string[i - 1] != "্":
                    count_conjuntion = 0

        string = ''

        return string.join(output)

    def bangla2brailleTranslate():
        text=my_text.get(1.0, END)
        translation = bangla2braille(text)
        translate.config(state="normal")
        translate.delete(1.0, END)
        translate.insert(END,translation)
        translate.config(state="disabled")

    def speak(text):
        tts = gTTS(text, lang="bn")
        os.chdir(os.path.join(os.getcwd(),"Audio"))
        now = dt.datetime.now()
        filename =  "audio_"+now.strftime("%Y_%m_%d_%H_%M_%S") +".mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.chdir('../')

    def bangla2brailleAudio():
        text = my_text.get(1.0, END)
        speak(text)

    Bangla_Braille = Button(button_bar, text="Braille TextBox", command=braille_textbox)
    Bangla_Braille.pack(side=LEFT, expand=True, fill=X)



    Translate_to_braille = Button(button_bar, text="Translate To Braille", command=bangla2brailleTranslate)
    Translate_to_braille.pack(side=LEFT, expand=True, fill=X)


    text_to_speech = Button(button_bar, text="Text To Speech", command=bangla2brailleAudio)
    text_to_speech.pack(side=LEFT, expand=True, fill=X)

    #another Frame
    my_frame2 = Frame(root)
    my_frame2.pack(fill="both")
    ## Scroll bar
    text_scroll2 = Scrollbar(my_frame2)
    text_scroll2.pack(side=RIGHT, fill=Y)



    translate = Text(my_frame2, font=("Helvetica", 16), bd=0, bg="#fff", selectbackground="yellow",
                   selectforeground="black", yscrollcommand=text_scroll2.set)


    translate.config(state="disabled")
    translate.pack(pady=20, fill=BOTH)

    text_scroll2.config(command=translate.yview)


    root.mainloop()

if __name__ == '__main__':
    # Creating a Directory of audio if not already exist
    if not os.path.exists('Audio'):
        os.makedirs('Audio')
    main()