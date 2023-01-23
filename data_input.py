import pickle


def create_dict(fio, dob, ser_pass, num_pass):
    my_dict = {'ФИО в формате (Иванов Иван Иванович)': fio, 'Дата рождения в формате (xx.xx.xxxx)': dob, 'Серия паспорта': ser_pass, 'Номер паспорта': num_pass}
    return my_dict

my_input_dict = create_dict(input("Enter fio: "), input("Enter dob: "), input("Enter ser_pass: "), input("Enter num_pass: "))

with open("dict.pickle", "wb") as handle:
    pickle.dump(my_input_dict, handle)