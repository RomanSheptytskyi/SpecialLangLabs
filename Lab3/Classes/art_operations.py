from Classes.error_handler import SymbolError


class ArtOperations:
    def __init__(self, ascii_art):
        self.ascii_art = ascii_art

    def scale_art(self, width, height):
        if width < 1 or height < 1:
            raise ValueError("Ширина і висота повинні бути не менше 1.")

        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError("Ширина і висота повинні бути цілими числами.")

        lines = self.ascii_art.split('\n')
        scaled_art = ""

        for line in lines:
            scaled_art += ''.join([char * width for char in line]) + '\n' * height

        return scaled_art

    def change_symbol(self, color_choice, color_manager):
        while True:
            change_symbol = input("Бажаєте змінити символ? (yes/no): ").strip().lower()
            if change_symbol in ['yes']:
                new_symbol = input("Введіть новий символ: ")
                if not new_symbol:
                    raise SymbolError(new_symbol)
                self.ascii_art = self.choose_custom_symbols(self.ascii_art, new_symbol)
                ascii_art_colored = color_manager.get_colored_art(self.ascii_art, color_choice)
                print("\nASCII-арт з новим символом")
                print(ascii_art_colored)
            elif change_symbol in ['no', ""]:
                break
            else:
                print("Невірний ввід. Введіть 'yes' або 'no'.")

    def choose_custom_symbols(self, ascii_art, symbol):
        new_art = ""
        for char in ascii_art:
            if char == ' ':
                new_art += ' '
            elif char != '\n':
                new_art += symbol
            else:
                new_art += char
        return new_art
