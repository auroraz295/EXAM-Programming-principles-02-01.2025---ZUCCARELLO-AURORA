import os
import json

class Virgilio:
    def __init__(self, directory):
        self.directory = directory

# exception personalizzata esercizio16   
    class CantoNotFoundError(Exception):
        def __init__(self):
            super.__init__("canto_number must be between 1 and 34")
    
#lista con tutte le righe
    def read_canto_lines(self, canto_number, strip_lines=False, num_lines=None):
        self.canto_number = canto_number
#modifica esercizio15
        if not int(canto_number):
            try:
                raise TypeError 
            except Exception as e: 
                print(e)
#modifica esercizio16
        if canto_number <0 or canto_number>34:
            raise CantoNotFoundError      
        
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
#modifica esercizio17        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                read_canto = file.readlines()
                return read_canto
#modifica esercizio13 
            if strip_lines:
                lines = [line.strip() for line in lines]
#modifica esercizio14            
            if num_lines is not None:
                lines = lines[:num_lines]
            print(lines)
        except Expection:
            print(f"error while opening {file_path}")    
        

#numero versi canto specifico
    def count_verses(self, canto_number):
        self.canto_number = canto_number
        lines = self.read_canto_lines(canto_number)
        number_lines = (len(lines))
        print(f"Il numero di versi del canto n.{self.canto_number} è di {number_lines}.")

#numero terzine
    def count_tercets(self, canto_number):
        self.canto_number = canto_number
        self.canto_number = canto_number
        lines = self.read_canto_lines(canto_number)
        number_lines = (len(lines))
        tercets = number_lines // 3
        print(f"Il canto n.{self.canto_number} contiene {tercets} terzine.")

#numero parola specifica di un canto specifico
    def count_word(self, canto_number, word):
        self.canto_number = canto_number
        self.word = word
        lines = self.read_canto_lines(canto_number)
        verses = "".join(lines).lower()
        #verses = canto paragrafato senza lista
        count = verses.count(word)
        print(f"La parola '{self.word}' è contenuta {count} volte nel canto n.{self.canto_number}.")

#verso in cui è presente parola
    def get_verse_with_word(self, canto_number, word):
        self.canto_number = canto_number
        self.word = word
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
           read_canto = file.readlines()
        rows = read_canto
        #rows = canto con versi divisi in lista
        for row in rows:
            if self.word in row:
                print(row)

#lista verso in cui è presente parola
    def get_verses_with_word(self, canto_number, word):
        self.canto_number = canto_number
        self.word = word
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
           read_canto = file.readlines()
        rows = read_canto
        for row in rows:
            if self.word in row:
                print(row.split(" "))

#verso più lungo
    def get_longest_verse(self, canto_number):
        self.canto_number = canto_number 
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
           read_canto = file.readlines()
        rows = read_canto
        max_row_lenght = 0
        for row in rows:
            row_lenght = len(row)
            if row_lenght > max_row_lenght:
                max_row_lenght = row_lenght
        print(f"Nel canto n.{canto_number}, il verso più lungo è il {max_row_lenght}.")

#dizionario canto con più versi
    def get_longest_canto(self):
        max_verses = 0 
        for canto_number in range(1,35):
            lines = self.read_canto_lines(canto_number)
            verses = "".join(lines).lower()
            number_lines = (len(verses))
            if number_lines > max_verses:
                max_verses = number_lines
                longest_canto = canto_number
        dict= {
            "canto_number": longest_canto, 
            "canto_len" :max_verses,
            }       
        print(dict)

#lista di conteggio parole di un canto
    def count_words(self, canto_number, words):
        self.canto_number = canto_number
        self.words = words
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
           read_canto = file.readlines()
        verses = "".join(read_canto).lower()
        count = verses.count(words)
        dict= {
            words: count,
        }
        print(dict)
#modifica esercizio 18: 
        with open("words_count.json", "w", encoding="utf-8") as file:
            json.dump(dict, file, ensure_ascii=True, indent=3)  

#lista versi totali dei canti
    def get_hell_verses(self):
        for canto_number in range(1,35):
            lines = self.read_canto_lines(canto_number)
            print(lines)

#numero versi totali dei canti
    def count_hell_verses(self):   
        total_verses = 0 
        for canto_number in range(1,35):  
            file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                read_canto = file.readlines()
            number_verses = len(read_canto) 
            total_verses += number_verses
        print(f"Il numero totale di versi contenuto nell'Inferno è {total_verses}.") 

#lunghezza media dei versi di tutti i canti
    def get_hell_verse_mean_len(self):
        total_verses= 0
        for canto_number in range(1,35):  
            file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                read_canto = file.readlines()
            number_verses = len(read_canto) 
            total_verses += number_verses
    
        for canto_number in range(1,35):  
            total_line_lenght = 0
            lines = self.read_canto_lines(canto_number)
            for line in lines:
                verses = "".join(line).lower()
                verses.strip()
                line_lenght = len(verses)    
                total_line_lenght += line_lenght

        mean_leng = total_line_lenght / total_verses
        print(f"La lunghezza media dei versi dell'Inferno è di {mean_leng}.")        

         
Canto = Virgilio("canti")

esercizio1 = Canto.read_canto_lines(7)
print(esercizio1)

esercizio2 = Canto.count_verses(7)  

esercizio3 = Canto.count_tercets(7)

esercizio4 = Canto.count_word(7, "gente")

esercizio5 = Canto.get_verse_with_word(7, "gente")

esercizio6 = Canto.get_verses_with_word(7, "gente")

esercizio7 = Canto.get_longest_verse(7)

esercizio8 = Canto.get_longest_canto()

esercizio9 = Canto.count_words(7, "gente")

esercizio10 = Canto.get_hell_verses()

esercizio11 = Canto.count_hell_verses()

esercizio12 = Canto.get_hell_verse_mean_len()



