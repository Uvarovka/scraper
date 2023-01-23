import pickle


def create_dict(fio, dob, ser_pass, num_pass):
    my_dict = {'fio': fio, 'dob': dob, 'ser_pass': ser_pass, 'num_pass': num_pass}
    return my_dict

my_input_dict = create_dict(input("ФИО в формате (Иванов Иван Иванович): "), input("Дата рождения в формате (xx.xx.xxxx): "), input("Серия паспорта: "), input("Номер паспорта: "))

with open("dict.pickle", "wb") as handle:
    pickle.dump(my_input_dict, handle)