def zadanie1():
    sentence = "Żółte jaki lubią krzyczeć i ziewać, a wczoraj jodłowały podczas jedzenia batatów"
    vowels = "aeioyuąęó"
    vowelslist = [i for i in sentence if i in vowels]
    print(vowelslist)

def zadanie3():
    sentence = "W 1984 roku w 13 przypadkach doszło do protestu, w którym wzięło udział ponad 1000 osób"
    word_list = sentence.split()
    num_list = [word for word in word_list if word.isnumeric()]
 
    print(num_list)
    
def main():

    #????zadanie6 = [i for i in range(1, 1000) if i %  == 0]
    #print(f"Zadanie 6: {zadanie6}")
    zadanie1()
    zadanie3()
    
main()