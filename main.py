import URLrequest
import json


def main():
    while "_keep_" == "_keep_":
        userinput = input(
            "Enter what you want to translate(Enter 'q' to quit.): ")

        if userinput == "q":
            print("Thanks for using!")
            break

        targetLan = input("Target language: ")
        words = [userinput]
        for u in URLrequest.get_myurl(words, targetLan):
            URLrequest.get_translate_word(u)


if "_main_" == "_main_":
    print("http://api.fanyi.baidu.com/doc/21")
    print("")
    with open("referenceSheet.json") as reference:
        referenceCN = str(json.load(reference)[0])
        referenceCN = referenceCN.replace("]", "")
        referenceCN = referenceCN.replace("[", "")
        referenceCN = referenceCN.replace("}", "")
        referenceCN = referenceCN.replace("{", "")
        referenceCN = referenceCN.replace("'", "")

    with open("referenceSheet.json") as reference:
        referenceEN = str(json.load(reference)[1])
        referenceEN = referenceEN.replace("]", "")
        referenceEN = referenceEN.replace("[", "")
        referenceEN = referenceEN.replace("}", "")
        referenceEN = referenceEN.replace("{", "")
        referenceEN = referenceEN.replace("'", "")

        print(referenceCN)
        print("")
        print(referenceEN)

        print("")
    main()
