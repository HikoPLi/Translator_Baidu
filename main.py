import URLrequest


def main():
    while "_keep_" == "_keep_":
        userinput = input(
            "Enter what you want to translate(Enter 'q' to quite.): ")

        if userinput == "q":
            print("Thanks for using!")
            break

        targetLan = input("Target language: ")
        words = [userinput]
        for u in URLrequest.get_myurl(words, targetLan):
            URLrequest.get_translate_word(u)


if "_main_" == "_main_":
    print("http://api.fanyi.baidu.com/doc/21")
    with open("referenceSheet.txt") as reference:
        print(str(reference.readline()))
        print("")
    main()
