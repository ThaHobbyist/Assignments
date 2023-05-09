def generate_languages(regex, language=""):
    if not regex:
        return [language]
    
    first_char = regex[0]
    if first_char == "a":
        return generate_languages(regex[1:], language + "a") + generate_languages(regex[1:], language + "b")
    elif first_char == "b":
        return generate_languages(regex[1:], language + "b")
    elif first_char == "(":
        end_index = regex.index(")")
        options = regex[1:end_index].split("|")
        languages = []
        for option in options:
            languages += generate_languages(regex[end_index+1:], language + option)
        return languages

rgx = input("Enter a Regular Expression: ")
print(generate_languages(rgx))