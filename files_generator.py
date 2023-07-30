# generate 26 files with a rand number in each one and create a summary file
import random


def generate_txt_files():
    for code in range(65, 91):
        letter = chr(code)
        file_name = f"{letter}.txt"

        num = random.randint(1, 100)

        with open(file_name, "w") as file, open("summary.txt", mode="a") as sum_file:
            file.write(str(num))
            sum_file.write(f"{file_name}: {num}\n")


generate_txt_files()
