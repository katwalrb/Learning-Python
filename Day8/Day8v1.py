#functions with inputs
#You're painting a wall. One can of paint can cover 5
#square meters of wall. Given a random height and
#width of wall, calculate how many cans of paint you'll
#need to buy
#number of cans = (wall height x wall width) / coverage
#per can.
import math
height = int(input("Height of the wall: "))
width = int(input("Width of the wall: "))
cov_per_can = int(input("Coverage per can: "))
def num_can(wall_height, wall_width, coverage):
    number_of_cans = wall_height*wall_width / coverage
    total_num = math.ceil(wall_height*wall_width / coverage)

    print(f"Number of cans = {total_num}")

num_can(wall_height=height,wall_width=width,coverage=cov_per_can)

