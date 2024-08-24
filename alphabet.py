import tkinter as tk
from tkinter import ttk
import sys
from random import randrange

FONT_SIZE = (24, 26, 28, 30, 32, 36, 40, 42, 44, 50, 56, 65, 72, 76, 78)
DEFAULT_SIZE = 46
NUMBER_OF_FONTS = len(FONT_SIZE)
FONT = ("Verdana", DEFAULT_SIZE)
LETTERS_BOTTOM_RUS = ("О", "Л", "П")
LETTERS_BOTTOM_ENG = ("R", "L", "B")
COLORS = (
    "#563093",
    "#911414",
    "#cec379",
    "#B76EFF",
    "#FF90FF",
    "#9CFF9C",
    "#FFB76E",
    "#A3A375",
    "#9F9FFF",
    "#FF66CC",
)
NUMBER_OF_COLORS = len(COLORS)
RUSSIAN = "russian"
ENGLISH = "english"
FACTOR = 2
WIDTH = 1024
HEIGHT = 768


class AlphabetSettings:

    def __init__(self, parent):
        # заголовок окна
        self.root = parent
        self.root.title("Alphabet. Settings")
        # главный фрейм, задаем отступы
        main_frame = tk.Frame(parent)
        main_frame.grid(padx=50, pady=10)
        # настройка языка
        lang_setting_frame = tk.Frame(main_frame)
        lang_setting_frame.grid(pady=1)
        # тест настройки языка
        label = tk.Label(lang_setting_frame, text="Language of alphabet")
        label.grid(column=0, row=0, sticky=tk.E)
        # стринговая переменная язык
        language = tk.StringVar()
        # select - элемент для выбора языка
        language_box = ttk.Combobox(
            lang_setting_frame, textvariable=language, state="readonly"
        )
        language_box["values"] = (RUSSIAN, ENGLISH)
        language_box.current(0)
        language_box.grid(column=1, row=0)

        settings_frame = tk.Frame(main_frame)
        settings_frame.grid(padx=50)
        # int переменная для настройки отображения
        # букв в случайном порядке
        random_order = tk.IntVar()
        random_order_btn = tk.Checkbutton(
            settings_frame,
            text="Show letters in random order",
            variable=random_order,
            onvalue=1,
            offvalue=0,
        )
        random_order_btn.grid(column=0, row=1, sticky=tk.W)
        # int переменная для настройки
        # менять ли расположение на экране
        change_pos = tk.IntVar()
        change_pos_btn = tk.Checkbutton(
            settings_frame,
            text="Change screen position",
            variable=change_pos,
            onvalue=1,
            offvalue=0,
        )
        change_pos_btn.grid(column=0, row=2, sticky=tk.W)
        # int переменная для настройки
        # менять ли размер шрифта
        change_font_size = tk.IntVar()
        change_font_size_btn = tk.Checkbutton(
            settings_frame,
            text="Change font size",
            variable=change_font_size,
            onvalue=1,
            offvalue=0,
        )
        change_font_size_btn.grid(column=0, row=3, sticky=tk.W)
        # int переменная для настройки
        # менять ли цвет
        change_color = tk.IntVar()
        change_color_btn = tk.Checkbutton(
            settings_frame,
            text="Change color",
            variable=change_color,
            onvalue=1,
            offvalue=0,
        )
        change_color_btn.grid(column=0, row=4, sticky=tk.W)
        # фрейм для паузы
        pause_frame = tk.Frame(main_frame)
        pause_frame.grid(pady=10)

        label = ttk.Label(pause_frame, text="Pause between shows")
        label.grid(column=0, row=5, sticky=tk.E)

        pause = tk.StringVar()
        pause_box = ttk.Combobox(pause_frame, textvariable=pause, state="readonly")
        pause_box["values"] = (
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
            10,
        )
        pause_box.current(0)
        pause_box.grid(column=1, row=5)

        game_btn_frame = tk.Frame(main_frame)
        game_btn_frame.grid(pady=10)
        # Создаем кнопку "Играть", переменную pause
        # переводим в миллисекунды
        btn = ttk.Button(
            game_btn_frame,
            text="Play",
            command=lambda: self.open_frame(
                language.get(),
                random_order.get(),
                change_pos.get(),
                change_font_size.get(),
                change_color.get(),
                int(float(pause.get()) * 1000),
            ),
        )
        btn.grid()

    def open_frame(
        self, lang, random_order, change_pos, change_font_size, change_color, pause
    ):
        self.hide()
        AlphabetGame(
            self, lang, random_order, change_pos, change_font_size, change_color, pause
        )

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()


class AlphabetGame(tk.Toplevel):

    def __init__(
        self,
        original_frame,
        lang,
        random_order,
        change_pos,
        change_font_size,
        change_color,
        pause,
    ):
        tk.Toplevel.__init__(self)
        self.original_frame = original_frame
        self.lang = lang
        self.pause = pause
        self.protocol("WM_DELETE_WINDOW", sys.exit)
        # задаем размеры окна игры
        w = WIDTH
        h = HEIGHT

        # получаем размеры экрана
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        # вычисляем координаты расположения окна
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # задаем расположение, навзание, цвет
        self.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.title("Alphabet")
        self.configure(background="white")

        self.canvas = tk.Canvas(self)
        self.canvas.grid()
        self.canvas.configure(background="white", width=WIDTH, height=HEIGHT - 100)

        btn = ttk.Button(self, text="Back", command=self.close_and_back_to_settings)
        btn.grid()

        # случайный инт от 0 до 2 для выбора нижней буквы
        random_int = randrange(3)
        # задаем начальные буквы (верхнюю и нижнюю)
        if lang == RUSSIAN:
            initial_letter_top = chr(randrange(1040, 1072))
            initial_letter_bottom = LETTERS_BOTTOM_RUS[random_int]
        else:
            initial_letter_top = chr(randrange(65, 91))
            initial_letter_bottom = LETTERS_BOTTOM_ENG[random_int]

        # 0
        if all(
            (
                change_font_size == 0,
                random_order == 0,
                change_color == 0,
                change_pos == 0,
            )
        ):
            self.init_default_letters(initial_letter_top, initial_letter_bottom)
            # выполняется после отображения двух букв:
            self.canvas.after(self.pause, lambda: self.change_letters())
        # 1
        elif all(
            (
                change_font_size == 0,
                random_order == 0,
                change_color == 0,
                change_pos == 1,
            )
        ):
            rand_x, rand_y = self.gen_random_coords()
            self.top_letter_id = self.canvas.create_text(
                rand_x,
                rand_y,
                anchor=tk.W,
                font=(FONT[0], DEFAULT_SIZE),
                text=initial_letter_top,
            )
            self.bottom_letter_id = self.canvas.create_text(
                rand_x,
                rand_y + DEFAULT_SIZE + DEFAULT_SIZE * 0.5,
                anchor=tk.W,
                font=(FONT[0], DEFAULT_SIZE),
                text=initial_letter_bottom,
            )
            self.canvas.after(
                self.pause,
                lambda: self.change_letter_pos(),
            )
        # 2
        elif all(
            (
                change_font_size == 0,
                random_order == 0,
                change_color == 1,
                change_pos == 0,
            )
        ):
            self.init_default_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letters_colors())

        # 3
        elif all(
            (
                change_font_size == 0,
                random_order == 0,
                change_color == 1,
                change_pos == 1,
            )
        ):
            self.init_default_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_pos_color())
        # 4
        elif all(
            (
                change_font_size == 0,
                random_order == 1,
                change_color == 0,
                change_pos == 0,
            )
        ):
            self.init_default_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_random_letters())
        # 5
        elif all(
            (
                change_font_size == 0,
                random_order == 1,
                change_color == 0,
                change_pos == 1,
            )
        ):
            self.init_default_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_order_pos())
        # 6
        elif all(
            (
                change_font_size == 0,
                random_order == 1,
                change_color == 1,
                change_pos == 0,
            )
        ):
            self.init_default_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_order_color())
        # 7
        elif all(
            (
                change_font_size == 0,
                random_order == 1,
                change_color == 1,
                change_pos == 1,
            )
        ):
            self.init_default_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_order_color_pos())
        # 8
        elif all(
            (
                change_font_size == 1,
                random_order == 0,
                change_color == 0,
                change_pos == 0,
            )
        ):
            self.init_random_size_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_size())
        # 9
        elif all(
            (
                change_font_size == 1,
                random_order == 0,
                change_color == 0,
                change_pos == 1,
            )
        ):
            self.init_random_size_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_size_pos())
        # 10
        elif all(
            (
                change_font_size == 1,
                random_order == 0,
                change_color == 1,
                change_pos == 0,
            )
        ):
            self.init_random_size_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_size_color())
        # 11
        elif all(
            (
                change_font_size == 1,
                random_order == 0,
                change_color == 1,
                change_pos == 1,
            )
        ):
            self.init_random_size_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_size_pos_color())
        # 12
        elif all(
            (
                change_font_size == 1,
                random_order == 1,
                change_color == 0,
                change_pos == 0,
            )
        ):
            self.init_random_size_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_size_order())
        # 13
        elif all(
            (
                change_font_size == 1,
                random_order == 1,
                change_color == 0,
                change_pos == 1,
            )
        ):
            self.init_random_size_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_size_pos_order())
        # 14
        elif all(
            (
                change_font_size == 1,
                random_order == 1,
                change_color == 1,
                change_pos == 0,
            )
        ):
            self.init_random_size_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_letter_size_order_color())
        # 15
        else:
            self.init_random_size_letters(initial_letter_top, initial_letter_bottom)
            self.canvas.after(self.pause, lambda: self.change_all())

    def init_default_letters(self, initial_letter_top, initial_letter_bottom):
        self.top_letter_id = self.canvas.create_text(
            400, 200, anchor=tk.W, font=(FONT[0], DEFAULT_SIZE), text=initial_letter_top
        )
        self.bottom_letter_id = self.canvas.create_text(
            400,
            200 + DEFAULT_SIZE * FACTOR,
            anchor=tk.W,
            font=(FONT[0], DEFAULT_SIZE),
            text=initial_letter_bottom,
        )

    def init_random_size_letters(self, initial_letter_top, initial_letter_bottom):
        random_size = self.gen_rand_size()
        self.top_letter_id = self.canvas.create_text(
            400, 200, anchor=tk.W, font=(FONT[0], random_size), text=initial_letter_top
        )
        self.bottom_letter_id = self.canvas.create_text(
            400,
            200 + random_size * FACTOR,
            anchor=tk.W,
            font=(FONT[0], random_size),
            text=initial_letter_bottom,
        )

    def change_ord(self):
        cur_letter_ord = ord(self.canvas.itemcget(self.top_letter_id, "text"))
        if self.lang == RUSSIAN:
            # буква Я, начинаем сначала
            if cur_letter_ord == 1071:
                cur_letter_ord = 1039
            # буква Е, выбираем Ё
            elif cur_letter_ord == 1045:
                cur_letter_ord = 1024
            # после Ё возврат к Ж
            elif cur_letter_ord == 1025:
                cur_letter_ord = 1045
        else:
            if cur_letter_ord == 90:
                cur_letter_ord = 64
        next_ord = cur_letter_ord + 1
        return next_ord

    def get_next_bottom_letter(self):
        random = randrange(3)
        if self.lang == RUSSIAN:
            next_bottom_letter = LETTERS_BOTTOM_RUS[random]
        else:
            next_bottom_letter = LETTERS_BOTTOM_ENG[random]
        return next_bottom_letter

    def gen_rand_size(self):
        random = randrange(NUMBER_OF_FONTS)
        return FONT_SIZE[random]

    def change_letters(self):
        self.canvas.itemconfigure(self.top_letter_id, text=chr(self.change_ord()))
        self.canvas.itemconfigure(
            self.bottom_letter_id,
            text=self.get_next_bottom_letter(),
        )
        self.after(self.pause, lambda: self.change_letters())

    def change_sizes(self):
        random_size = self.gen_rand_size()
        self.canvas.itemconfigure(self.top_letter_id, font=(FONT[0], random_size))
        current_size = int(
            self.canvas.itemconfig(self.bottom_letter_id)["font"][-1].split()[1]
        )
        self.canvas.itemconfigure(self.bottom_letter_id, font=(FONT[0], random_size))
        self.canvas.move(
            self.bottom_letter_id, 0, FACTOR * (random_size - current_size)
        )
        self.after(self.pause, lambda: self.change_sizes())

    def gen_random_ord_for_top_letter(self):
        """return random rus ord А-Я or eng"""
        if self.lang == RUSSIAN:
            random = randrange(1040, 1072)
        else:
            random = randrange(65, 91)
        return random

    def change_random_letters(self):
        next_ord = self.gen_random_ord_for_top_letter()
        self.canvas.itemconfigure(self.top_letter_id, text=chr(next_ord))
        self.canvas.itemconfigure(
            self.bottom_letter_id, text=self.get_next_bottom_letter()
        )
        self.after(self.pause, lambda: self.change_random_letters())

    def gen_random_color(self):
        random = randrange(NUMBER_OF_COLORS)
        return COLORS[random]

    def change_colors(self):
        self.canvas.itemconfigure(
            self.top_letter_id,
            fill=self.gen_random_color(),
        )
        self.canvas.itemconfigure(
            self.bottom_letter_id,
            fill=self.gen_random_color(),
        )
        self.after(self.pause, lambda: self.change_colors())

    def gen_random_coords(self):
        rand_x = randrange(100, 700)
        rand_y = randrange(100, 400)
        return rand_x, rand_y

    def change_pos(self):
        rand_x, rand_y = self.gen_random_coords()
        self.canvas.coords(self.top_letter_id, (rand_x, rand_y))
        current_size = int(
            self.canvas.itemconfig(self.bottom_letter_id)["font"][-1].split()[1]
        )
        self.canvas.coords(
            self.bottom_letter_id, (rand_x, rand_y + current_size * FACTOR)
        )
        self.after(self.pause, lambda: self.change_pos())

    def change_letter_pos(self):
        self.change_letters()
        self.change_pos()

    def change_letter_size_order(self):
        self.change_random_letters()
        self.change_sizes()

    def change_letter_order_pos(self):
        self.change_random_letters()
        self.change_pos()

    def change_letters_colors(self):
        self.change_letters()
        self.change_colors()

    def change_letter_order_color(self):
        self.change_random_letters()
        self.change_colors()

    def change_letter_pos_color(self):
        self.change_letters()
        self.change_pos()
        self.change_colors()

    def change_letter_order_color_pos(self):
        self.change_random_letters()
        self.change_colors()
        self.change_pos()

    def change_letter_size(self):
        self.change_letters()
        self.change_sizes()

    def change_letter_size_color(self):
        self.change_letters()
        self.change_sizes()
        self.change_colors()

    def change_letter_size_pos(self):
        self.change_letters()
        self.change_sizes()
        self.change_pos()

    def change_letter_size_pos_color(self):
        self.change_letters()
        self.change_sizes()
        self.change_pos()
        self.change_colors()

    def change_letter_size_pos_order(self):
        self.change_random_letters()
        self.change_sizes()
        self.change_pos()

    def change_letter_size_order_color(self):
        self.change_random_letters()
        self.change_sizes()
        self.change_colors()

    def change_all(self):
        self.change_random_letters()
        self.change_sizes()
        self.change_pos()
        self.change_colors()

    def close_and_back_to_settings(self):
        """Функция для закрытия окна игры и возврата к настройкам"""
        self.destroy()
        self.original_frame.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    app = AlphabetSettings(root)
    root.mainloop()
