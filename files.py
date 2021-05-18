try:
    file = open("how-to-turn-dirt-into-gold.txt", "r")
    text = file.read()
    letters = text.split()
    count_of_the = letters.count("the")
    count_of_if = letters.count("if")
    count_of_e = letters.count("e")
    file.close()
except IOError:
    count_of_the = 0
    count_of_if = 0
    count_of_e = 0
    try:
    file_for_statistics = open("statistics_of_letters.txt", "w")
    text_for_statistics = file_for_statistics.write()
    file_for_statistics.write = ("The count of 'the' is" + str(count_of_the) +'\n')
    file_for_statistics.write = ("The count of 'if' is" + str(count_of_if) +'\n')
    file_for_statistics.write = ("The count of 'e' is" + str(count_of_e) + '\n')
    file_for_statistics.close()
    except IOError:
        count_of_the = 0
        count_of_if = 0
        count_of_e = 0
