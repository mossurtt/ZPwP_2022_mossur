def zadanie1():
    sentence = "Żółte jaki lubią krzyczeć i ziewać, a wczoraj jodłowały podczas jedzenia batatów"
    vowels = "aeioyuąęó"
    vowelslist = [i for i in sentence if i in vowels]
    print(vowelslist)

def zadanie2():
    lista = ["hi", 4, 8.99, "apple", ("t,b", "n")]
    wynik = [(lista.index(i), i) for i in lista]
    print(wynik)


def zadanie3():
    sentence = "W 1984 roku w 13 przypadkach doszło do protestu, w którym wzięło udział ponad 1000 osób"
    word_list = sentence.split()
    num_list = [word for word in word_list if word.isnumeric()]
 
    print(num_list)

def zadanie4():
    liczby = [2, 4, 8 ,9]
    wynik = []
    for i in liczby:
        if i % 2 == 0:
            wynik += {'even'}
        else:
            wynik += {'odd'}
    print(wynik)

def zadanie5():
    lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista_b = [2, 7, 1, 12]
    pasujace = []
    for i in lista_a:
        for j in lista_b:
            if i == j:
                pasujace += {(i, j)}
    print(pasujace)

    
def main():

    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
    zadanie5()
    zadanie6 = [i for i in range(1, 1000) if i % 3 == 0 or i % 2 == 0]
    print(f"Zadanie 6: {zadanie6}")

main()