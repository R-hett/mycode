def main():
    wordbank = ["indentation", "spaces"]

    tlgstudents = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua',
                   'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang',
                   'Yaping']

    wordbank.append(4)

    num = int(input("Pick a student number!"))

    choice = num
    student_name = tlgstudents[choice]

    print(student_name, "always uses", wordbank[2], wordbank[1], "to indent.")


main()

