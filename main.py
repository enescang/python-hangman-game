import random

class HangMan:
    remain = 3
    words = ["kodlib", "github", "hangmangame"]
    unique_chars = []

    def __init__(self, remain):
        self.remain = remain

    def select_random_word(self):
        self.random_word = random.choice(self.words)
        self.random_word_list = self.str_to_list(self.random_word)
        self.random_word_str = self.random_word
    
    def modify_selected_word(self):
        for element in range(0, len(self.random_word)):
            rnd_one = random.random()
            rnd_two = random.random()
            if rnd_one > rnd_two:
                self.unique_chars.append(self.random_word_list[element])
                self.random_word_list[element] = "_"
        print("THE WORD: " + self.list_to_str(self.random_word_list))

    def play(self):
        r = self.remain
        for a in range(0, self.remain):
            r -= 1
            print("-----------------------------")
            selected = input('Please Enter a Char: ')
            if selected in self.unique_chars:
                all_index_of_char = list(self.find(self.random_word, selected))
                for i in all_index_of_char:
                    self.random_word_list[i] = selected
                print(selected +" is found in the word")
                print("Remain: "+ str(r))
                print(self.list_to_str(self.random_word_list))
            else:
                print(selected +" is NOT found in the word")
                print("Remain: "+ str(r))
            if self.list_to_str(self.random_word_list).find('_') == -1:
                print("<<< YOU WIN >>>>")
                break
            if a == self.remain - 1 and self.list_to_str(self.random_word_list).find('_') != -1:
                print("<<< YOU LOST >>>>")
                print(self.list_to_str(self.random_word_list))
    def str_to_list(self, str):
        return list(str)

    def list_to_str(self, _list):
        return "".join(_list)

    def find(self, str, ch):
        for i, ltr in enumerate(str):
            if ltr == ch:
                yield i

h = HangMan(3)
h.select_random_word()
h.modify_selected_word()
h.play()