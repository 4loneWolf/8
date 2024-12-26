class Menu:

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
        pass
    
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
