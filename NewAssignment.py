flag = 0

pass_dic = input("Enter any Alien/English Language Word: ")

alien_wordlist = input("File Name: ")

with open("alien_wordlist.txt", "r") as File:
    for line in File:
        word = line.split('=')[0].strip()
        if word == pass_dic:
            print("Alien Word Found!")
            print("Alien Word is: " + line)
            flag = 1
            break


if flag == 0:
    print("Alien/English Word is not in the list!")

print("Don't forget to thank Noourl!")