import tkinter as tk
from tkinter import ttk


class AlphabetSettings():

    def __init__(self, parent):
        # заголовок окна
        self.root = parent
        self.root.title("Алфавит. Настройки")
        # главный фрейм, задаем отступы
        main_frame = tk.Frame(parent)
        main_frame.grid(padx=50, pady=10)
        # настройка языка
        lang_setting_frame = tk.Frame(main_frame)
        lang_setting_frame.grid(pady=1)
        # тест настройки языка
        label = tk.Label(lang_setting_frame, text='Язык алфавита')
        label.grid(column=0, row=0, sticky=tk.E)
        # стринговая переменная язык
        language = tk.StringVar()
        # select - элемент для выбора языка
        language_box = ttk.Combobox(
            lang_setting_frame, textvariable=language)
        language_box['values'] = ('русский', 'английский')
        language_box.current(0)
        language_box.grid(column=1, row=0)

        settings_frame = tk.Frame(main_frame)
        settings_frame.grid(padx=50)
        # int переменная для настройки отображения
        # букв в случайном порядке
        random_order = tk.IntVar()
        random_order_btn = tk.Checkbutton(
            settings_frame,
            text='Отображать буквы в случайном порядке',
            variable=random_order,
            onvalue=1,
            offvalue=0)
        random_order_btn.grid(column=0, row=1, sticky=tk.W)
        # int переменная для настройки
        # менять ли расположение на экране
        change_pos = tk.IntVar()
        change_pos_btn = tk.Checkbutton(
            settings_frame,
            text='Менять расположение на экране',
            variable=change_pos,
            onvalue=1, offvalue=0)
        change_pos_btn.grid(column=0, row=2, sticky=tk.W)
        # int переменная для настройки
        # менять ли размер шрифта
        change_font_size = tk.IntVar()
        change_font_size_btn = tk.Checkbutton(
            settings_frame, text='Менять размер шрифта',
            variable=change_font_size,
            onvalue=1, offvalue=0)
        change_font_size_btn.grid(column=0, row=3, sticky=tk.W)
        # int переменная для настройки
        # менять ли цвет
        change_color = tk.IntVar()
        change_color_btn = tk.Checkbutton(
            settings_frame, text='Менять цвет',
            variable=change_color,
            onvalue=1, offvalue=0)
        change_color_btn.grid(column=0, row=4, sticky=tk.W)
        # фрейм для паузы
        pause_frame = tk.Frame(main_frame)
        pause_frame.grid(pady=10)

        label = ttk.Label(pause_frame, text='Пауза между показами')
        label.grid(column=0, row=5, sticky=tk.E)

        pause = tk.StringVar()
        pause_box = ttk.Combobox(pause_frame, textvariable=pause)
        pause_box['values'] = (0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.3,
                               1.5, 1.7, 2, 3, 4,
                               5, 7, 10)
        pause_box.current(0)
        pause_box.grid(column=1, row=5)

        game_btn_frame = tk.Frame(main_frame)
        game_btn_frame.grid(pady=10)
        # Создаем кнопку "Играть", переменную pause
        # переводим в миллисекунды
        btn = ttk.Button(
            game_btn_frame,
            text="Играть",
            command=lambda: self.open_frame(
                language.get(),
                random_order.get(),
                change_pos.get(),
                change_font_size.get(),
                change_color.get(),
                int(float(pause.get()) * 1000))
            )
        btn.grid()

    def open_frame(self, lang, random_order,
                   change_pos, change_font_size,
                   change_color, pause):
        print(lang, random_order, change_pos,
              change_font_size, change_color, pause)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x250")
    app = AlphabetSettings(root)
    root.mainloop()
