from utils.task1 import get_tree
from utils.task2 import create_csv
from utils.userlist import user_list
from utils.task3 import get_image
import os

print("Task 1")
get_tree(os.getcwd() + "/utils/tree")
print("Task 2")
create_csv(user_list, 'userlist.csv')
print("Task3")
url = "https://dummyimage.com/600x400/000/fff"
get_image(url)
