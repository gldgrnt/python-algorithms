# Create input for solutions
import random

def create_input(n=10, m=100):
    random_list = [ 0 ] * n

    for index in enumerate(random_list):
        random_list[index[0]] = random.randint(1, m)

    random_list_string = " ".join(map(str, random_list))

    # Write to file
    file = open("src/solutions/2_max_pairwise_product/input.txt", "w")
    file.writelines(f'{str(n)}\n')
    file.writelines(random_list_string)
    file.close()

create_input()