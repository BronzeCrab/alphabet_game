import tkinter as tk
from tkinter import ttk
from random import randrange

FONT_SIZE = (24, 26, 28, 30, 32, 36, 40, 42, 44, 50, 56, 65, 72, 76, 78)
DEFAULT_SIZE = 46
NUMBER_OF_FONTS = len(FONT_SIZE)
FONT = ("Verdana", DEFAULT_SIZE)
LETTER_2 = ('О', 'Л', 'П')
LETTER_2_ENG = ('R', 'L', 'B')
COLORS = ("#563093", "#911414", "#cec379", "#B76EFF", "#FF90FF",
          "#9CFF9C", "#FFB76E", "#A3A375", "#9F9FFF", "#FF66CC")
NUMBER_OF_COLORS = len(COLORS)


class Game(tk.Tk):

    def __init__(self, original, timestap, changeFontSize,
                 randomOrder, changeColor, changePos, lang):
        global language
        language = lang
        self.original_frame = original
        tk.Toplevel.__init__(self)
        w = 800  # width for the Tk root
        h = 650  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.title("Алфавит")
        self.configure(background='white')

        self.canvas = tk.Canvas(self)
        self.canvas.grid()
        self.canvas.configure(background='white', width=800, height=600)
        # set initial letter
        random = randrange(3)

        if language == 'русский':
            initial_letter = chr(randrange(1040, 1072))
            initial_letter_2 = LETTER_2[random]
        else:
            initial_letter = chr(randrange(65, 91))
            initial_letter_2 = LETTER_2_ENG[random]

        if changeFontSize == 0 and randomOrder == 0 and changeColor == 0 and changePos == 0:
            # displaying two letters
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400, 260, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter_2)
            self.canvas.after(timestap, lambda: self.changeLetter(timestap))

        elif changeFontSize == 1 and randomOrder == 0 and changeColor == 0 and changePos == 0:
            # displaying two letters
            random_size = self.genRandSize()
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], random_size), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400,
                200 +
                random_size +
                random_size *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    random_size),
                text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterSize(
                    timestap, random_size))

        elif changeFontSize == 0 and randomOrder == 1 and changeColor == 0 and changePos == 0:
            # displaying two letters
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400, 260, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeRandomLetter(timestap))

        elif changeFontSize == 0 and randomOrder == 0 and changeColor == 1 and changePos == 0:
            # displaying two letters
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400, 260, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterColor(timestap))

        elif changeFontSize == 0 and randomOrder == 0 and changeColor == 0 and changePos == 1:
            # generating two random coord:
            rand_x, rand_y = self.genRandomCoord()
            # displaying two letters
            self.text1 = self.canvas.create_text(
                rand_x, rand_y, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                rand_x,
                rand_y +
                DEFAULT_SIZE +
                DEFAULT_SIZE *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    DEFAULT_SIZE),
                text=initial_letter_2)

            self.canvas.after(timestap, lambda: self.changeLetterPos(timestap))

        elif changeFontSize == 1 and randomOrder == 1 and changeColor == 0 and changePos == 0:
            # displaying two letters
            random_size = self.genRandSize()
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], random_size), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400,
                200 +
                random_size +
                random_size *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    random_size),
                text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterSizeOrder(
                    timestap, random_size))

        elif changeFontSize == 0 and randomOrder == 1 and changeColor == 0 and changePos == 1:
            # displaying two letters
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400, 260, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterOrderPos(timestap))

        elif changeFontSize == 0 and randomOrder == 1 and changeColor == 1 and changePos == 0:
            # displaying two letters
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400, 260, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterOrderColor(timestap))

        elif changeFontSize == 0 and randomOrder == 1 and changeColor == 1 and changePos == 1:
            # displaying two letters
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400, 260, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterOrderColorPos(timestap))

        elif changeFontSize == 1 and randomOrder == 0 and changeColor == 0 and changePos == 1:
            # displaying two letters
            random_size = self.genRandSize()
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], random_size), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400,
                200 +
                random_size +
                random_size *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    random_size),
                text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterSizePos(timestap))

        elif changeFontSize == 1 and randomOrder == 0 and changeColor == 1 and changePos == 0:
            # displaying two letters
            random_size = self.genRandSize()
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], random_size), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400,
                200 +
                random_size +
                random_size *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    random_size),
                text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterSizeColor(
                    timestap, random_size))

        elif changeFontSize == 1 and randomOrder == 0 and changeColor == 1 and changePos == 1:
            # displaying two letters
            random_size = self.genRandSize()
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], random_size), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400,
                200 +
                random_size +
                random_size *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    random_size),
                text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterSizePosColor(timestap))

        elif changeFontSize == 1 and randomOrder == 1 and changeColor == 0 and changePos == 1:
            # displaying two letters
            random_size = self.genRandSize()
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], random_size), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400,
                200 +
                random_size +
                random_size *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    random_size),
                text=initial_letter_2)
            self.canvas.after(
                timestap, lambda: self.changeLetterSizePosOrder(timestap))
        else:
            # displaying two letters
            random_size = self.genRandSize()
            self.text1 = self.canvas.create_text(
                400, 200, anchor=tk.W, font=(
                    FONT[0], random_size), text=initial_letter)
            # displaying second letter using randrange:
            self.text2 = self.canvas.create_text(
                400,
                200 +
                random_size +
                random_size *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    random_size),
                text=initial_letter_2)
            self.canvas.after(timestap, lambda: self.changeAll(timestap))

        btn = ttk.Button(self, text="Назад", command=self.onClose)
        btn.grid()

    def onClose(self):
        """
        closes the frame and sends a message to the main frame
        """
        self.destroy()
        self.original_frame.show()

    def genRandSize(self):
        random = randrange(NUMBER_OF_FONTS)
        return FONT_SIZE[random]

    def genRandomCoord(self):
        rand_x = randrange(100, 700)
        rand_y = randrange(100, 400)
        return rand_x, rand_y

    def changeOrd(self, cur_ord=None):
        if not cur_ord:
            cur_letter_ord = ord(self.canvas.itemcget(self.text1, "text"))
        else:
            cur_letter_ord = cur_ord
        if language == "русский":
            # буква Я, начинаем сначала
            if cur_letter_ord == 1071:
                cur_letter_ord = 1039
            # буква Е, выбираем Ё
            elif cur_letter_ord == 1045:
                cur_letter_ord = 1024
            # после Ё возврат к Ж
            elif cur_letter_ord == 1025:
                cur_letter_ord = 1045
            next_ord = cur_letter_ord + 1
        else:
            if cur_letter_ord == 90:
                cur_letter_ord = 64
        next_ord = cur_letter_ord + 1
        return next_ord

    def nextLetterTwo(self):
        random = randrange(3)
        if language == 'русский':
            next_letter_2 = LETTER_2[random]
        else:
            next_letter_2 = LETTER_2_ENG[random]
        return next_letter_2

    def genRandomOrd(self):
        """ return random rus ord А-Я or eng"""
        if language == 'русский':
            random = randrange(1040, 1072)
        else:
            random = randrange(65, 91)
        return random

    def genRandomColor(self):
        random = randrange(NUMBER_OF_COLORS)
        return COLORS[random]

    def changeLetter(self, timestap):
        next_ord = self.changeOrd()
        self.canvas.itemconfigure(self.text1, text=chr(next_ord))

        self.canvas.itemconfigure(self.text2, text=self.nextLetterTwo())

        self.after(timestap, lambda: self.changeLetter(timestap))

    def changeLetterColor(self, timestap):
        next_ord = self.changeOrd()
        self.canvas.itemconfigure(self.text1, text=chr(next_ord),
                                  fill=self.genRandomColor())
        self.canvas.itemconfigure(self.text2, text=self.nextLetterTwo(),
                                  fill=self.genRandomColor())
        self.after(timestap, lambda: self.changeLetterColor(timestap))

    def changeRandomLetter(self, timestap):
        next_ord = self.genRandomOrd()
        self.canvas.itemconfigure(self.text1, text=chr(next_ord))
        self.canvas.itemconfigure(self.text2, text=self.nextLetterTwo())
        self.after(timestap, lambda: self.changeRandomLetter(timestap))

    def changeLetterSize(self, timestap, prevSize):
        next_ord = self.changeOrd()
        self.canvas.itemconfigure(self.text1, text=chr(next_ord))
        random_size = self.genRandSize()
        self.canvas.itemconfigure(self.text1, font=(FONT[0], random_size))
        self.canvas.itemconfigure(self.text2, font=(FONT[0], random_size),
                                  text=self.nextLetterTwo())
        # раньше был зазор , теперь нужно понять как сместить вторую
        # вторую строку. Убираю старый зазор и ставлю новый
        self.canvas.move(self.text2, 0, 1.5 * (random_size - prevSize))

        self.after(
            timestap,
            lambda: self.changeLetterSize(
                timestap,
                random_size))

    def changeLetterPos(self, timestap, andSize=None):
        # запоминаю букву
        letter_ord = ord(self.canvas.itemcget(self.text1, "text"))
        next_ord = self.changeOrd(letter_ord)
        # очищаю экран
        self.canvas.delete("all")
        # заново создаю
        rand_x, rand_y = self.genRandomCoord()
        if andSize:
            random_size = self.genRandSize()
            self.text1 = self.canvas.create_text(
                rand_x, rand_y, anchor=tk.W, font=(
                    FONT[0], random_size), text=chr(next_ord))
            self.text2 = self.canvas.create_text(
                rand_x,
                rand_y +
                random_size +
                random_size *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    random_size),
                text=self.nextLetterTwo())
            self.after(
                timestap,
                lambda: self.changeLetterPos(
                    timestap,
                    andSize=True))
        else:
            self.text1 = self.canvas.create_text(
                rand_x, rand_y, anchor=tk.W, font=(
                    FONT[0], DEFAULT_SIZE), text=chr(next_ord))
            self.text2 = self.canvas.create_text(
                rand_x,
                rand_y +
                DEFAULT_SIZE +
                DEFAULT_SIZE *
                0.5,
                anchor=tk.W,
                font=(
                    FONT[0],
                    DEFAULT_SIZE),
                text=self.nextLetterTwo())

            self.after(timestap, lambda: self.changeLetterPos(timestap))

    def changeLetterSizeOrder(self, timestap, prevSize):
        self.changeLetterSize(timestap, prevSize)
        self.changeRandomLetter(timestap)

    def changeLetterOrderPos(self, timestap):
        self.changeLetterPos(timestap)
        self.changeRandomLetter(timestap)

    def changeLetterOrderColor(self, timestap):
        self.changeLetterColor(timestap)
        self.changeRandomLetter(timestap)

    def changeLetterOrderColorPos(self, timestap):
        self.changeLetterPos(timestap)
        self.changeLetterColor(timestap)
        self.changeRandomLetter(timestap)

    def changeLetterSizePos(self, timestap):
        self.changeLetterPos(timestap, andSize=True)

    def changeLetterSizeColor(self, timestap, prevSize):
        self.changeLetterSize(timestap, prevSize)
        self.changeLetterColor(timestap)

    def changeLetterSizePosColor(self, timestap):
        self.changeLetterPos(timestap, andSize=True)
        self.changeLetterColor(timestap)

    def changeLetterSizePosOrder(self, timestap):
        self.changeLetterPos(timestap, andSize=True)
        self.changeRandomLetter(timestap)

    def changeAll(self, timestap):
        self.changeLetterPos(timestap, andSize=True)
        self.changeRandomLetter(timestap)
        self.changeLetterColor(timestap)

########################################################################


class Alphabet(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Алфавит. Настройки")
        self.frame = tk.Frame(parent)
        self.frame.grid(padx=50, pady=10)

        frame1 = tk.Frame(self.frame)
        frame1.grid(pady=20)
        label = tk.Label(frame1, text='Язык алфавита')
        label.grid(column=0, row=0, sticky=tk.E)

        self.languagevar = tk.StringVar()
        language = ttk.Combobox(frame1, textvariable=self.languagevar)
        language['values'] = ('русский', 'английский')
        language.current(0)
        language.grid(column=1, row=0)

        frame2 = tk.Frame(self.frame)
        frame2.grid(padx=50)
        self.randomOrder = tk.IntVar()
        check1 = tk.Checkbutton(
            frame2,
            text='Отображать буквы в случайном порядке',
            variable=self.randomOrder,
            onvalue=1,
            offvalue=0)
        check1.grid(column=0, row=1, sticky=tk.W)

        self.changePos = tk.IntVar()
        check2 = tk.Checkbutton(frame2, text='Менять расположение на экране',
                                variable=self.changePos,
                                onvalue=1, offvalue=0)
        check2.grid(column=0, row=2, sticky=tk.W)

        self.changeFontSize = tk.IntVar()
        check3 = tk.Checkbutton(frame2, text='Менять размер шрифта',
                                variable=self.changeFontSize,
                                onvalue=1, offvalue=0)
        check3.grid(column=0, row=3, sticky=tk.W)

        self.changeColor = tk.IntVar()
        check4 = tk.Checkbutton(frame2, text='Менять цвет',
                                variable=self.changeColor,
                                onvalue=1, offvalue=0)
        check4.grid(column=0, row=4, sticky=tk.W)

        frame3 = tk.Frame(self.frame)
        frame3.grid(pady=10)

        label = ttk.Label(frame3, text='Пауза между показами')
        label.grid(column=0, row=5, sticky=tk.E)

        self.pausevar = tk.StringVar()
        pause = ttk.Combobox(frame3, textvariable=self.pausevar)
        pause['values'] = (
            0.5,
            0.6,
            0.7,
            0.8,
            0.9,
            1,
            1.3,
            1.5,
            1.7,
            2,
            3,
            4,
            5,
            7,
            10)
        pause.current(0)
        pause.grid(column=1, row=5)

        frame4 = tk.Frame(self.frame)
        frame4.grid(pady=10)
        btn = ttk.Button(
            frame4,
            text="Играть",
            command=lambda: self.open_frame(
                int(
                    float(
                        self.pausevar.get()) *
                    1000),
                self.changeFontSize.get(),
                self.randomOrder.get(),
                self.changeColor.get(),
                self.changePos.get(),
                self.languagevar.get()))
        btn.grid()

    def open_frame(self, timestap, changeFontSize,
                   randomOrder, changeColor,
                   changePos, lang):
        """
        opens other frame and hides main frame
        """
        self.hide()
        sub_frame = Game(self, timestap, changeFontSize,
                         randomOrder, changeColor, changePos, lang)

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x250")
    app = Alphabet(root)
    root.mainloop()
