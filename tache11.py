# programme qui permet de convertit la liste en dictionnaire 

import itertools

transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]

transaction_list_iter = iter(transaction_list)

transaction_list_dict_objet = itertools.zip_longest(transaction_list_iter, transaction_list_iter, fillvalue=None)

transaction_list_dict = dict(transaction_list_dict_objet)

print(transaction_list_dict)
