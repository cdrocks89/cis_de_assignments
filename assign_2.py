# find a path

import os


def get_file_names():
    path = "C:\\Users\\cdroc\\OneDrive\\Documents\\sample"
    full_path = []
    file_names = []
    file_name = os.listdir(path)
    for i in file_name:
        file_names.append(i)
    full_path.append(os.path.join(path, i))
    for i in range(len(full_path)):
        print("file name is: ", file_names[i])
        print("full path is: ", full_path[i])
        print("\n")

    output_path = "C:\\Users\\cdroc\\OneDrive\\Documents\\output_file"
    output_file = open("C:\\Users\\croc\\OneDrive\\Documents\\output_file\\root.txt", 'w')
    output_file.writelines(file_names)
    output_file.close()


get_file_names()