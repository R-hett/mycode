def main():

    #challenge list
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    # Print for challege.
    print("My ", challenge[2][1], "! The ", challenge[2][0], " do ", challenge[3], "!", sep="")

    #trial list
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

    # variables
    a = trial[2]["goggles"]
    b = trial[2]["eyes"]
    c = trial[-1]
    print("My ",a,"!"," The ",b," do ",c,"!", sep="")


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


    # variables
    eye = nightmare[0]["user"]["name"]["first"]
    gogg = nightmare[0]["kumquat"]
    noth = nightmare[0]["d"]


    print("My ",eye,"! The ",gogg," do ",noth,"!",sep="")


main()

