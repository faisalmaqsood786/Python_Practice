def string_manipulation(word):
    words = word.split()
    first_conversion = " "
    second_conversion = " "

    for i in words:
        name = i.capitalize()
        first_conversion += name

    for i in words:
        name = i.lower()
        second_conversion = second_conversion + " " + name

    print("word", word)
    print("1st Conversion", first_conversion.strip())
    print("2nd Conversion", second_conversion.strip().capitalize())


string_manipulation('My name is faisal')
