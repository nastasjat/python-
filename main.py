# copy the content to another file in uppercase
def create_file(file_name):
    with open(file_name, "w") as file:
        file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore "
            "magna aliqua. Ut enim ad minim veniam, quis nostrud "
            "exercitation ullamco laboris nisi ut aliquip ex ea "
            "commodo consequat. Duis aute irure dolor in reprehenderit "
            "in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, "
            "sunt in culpa qui officia deserunt mollit anim id est laborum."
        )


def copy_content(first_file, second_file):
    with open(first_file, "r") as first, open(second_file, "w") as second:
        text = first.read()
        second.write(text.upper())


create_file("first.txt")
copy_content("first.txt", "second.txt")
