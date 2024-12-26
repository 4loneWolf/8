class Menu:
    def __init__(self):
        text = None
        frequency = None

    def input_data(self):
        self.text = None
        self.text = input("Введите текст: ")

    def analyze(self, text):
        text = ''.join(filter(str.isalnum, text))
        frequency = {}
        total_chars = len(text)
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        self.frequency = {char: count / total_chars for char, count in frequency.items()}

    def display_menu(self):
        print("Меню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")

    def print_result(self, frequency):
        print("Частотный анализ текста:")
        for char, freq in frequency.items():
            print(f"{char}: {freq:.4f}")

    def handle_choice(self, choice):
        if choice == '1':
            self.input_data()
        elif choice == '2':
            if self.text is not None:
                self.analyze(self.text)
            else:
                print("Сначала введите данные.")
        elif choice == '3':
            if self.frequency is not None:
                self.print_result(self.frequency)
            else:
                print("Сначала выполните алгоритм.")
        elif choice == '4':
            print("Завершение работы программы.")
            return False
        else:
            print("Неверный выбор. Попробуйте снова.")
        return True

def main():
    menu = Menu()
    while True:
        menu.display_menu()
        choice = input("Выберите пункт меню: ")
        if not menu.handle_choice(choice):
            break

main()