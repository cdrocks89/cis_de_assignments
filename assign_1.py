#  assignment 1
#  adding first and last name and showing the result in dictionary.

f_name = ['Chirag', 'Anagh', 'Palak', 'Mona']
l_name = ['Dave ', ' Dave', ' Dave', ' Thaker' ]

joined_list = [str(x) + y for x, y in zip(f_name, l_name)]

print(joined_list)


