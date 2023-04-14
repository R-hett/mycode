def main():

    # Requests user imput. saves to a variable.
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")

    # Requests user imput. saves to a variable.
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

    # marvel char with facts
    marvelchars = {
        "Starlord":
            {"real name": "peter quill",
             "powers": "dance moves",
             "archenemy": "Thanos"},

        "Mystique":
            {"real name": "raven darkholme",
             "powers": "shape shifter",
             "archenemy": "Professor X"},

        "Hulk":
            {"real name": "bruce banner",
             "powers": "super strength",
             "archenemy": "adrenaline"}
    }

    char_fact = marvelchars[char_name][char_stat]

    print(f"{char_name}'s {char_stat} is {char_fact}")


main()


