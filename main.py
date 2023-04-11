import URLrequest
import json


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
    with open("referenceSheet.json") as reference:
        reference = str(json.load(reference))
        reference = reference.replace("]", "")
        reference = reference.replace("[", "")
        reference = reference.replace("}", "")
        reference = reference.replace("{", "")
        reference = reference.replace("'", "")
        print(reference)
        print("")
    main()
