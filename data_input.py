import pickle


def create_dict(fio, dob, ser_pass, num_pass):
    my_dict = {'fio': fio, 'dob': dob, 'ser_pass': ser_pass, 'num_pass': num_pass}
    return my_dict

my_input_dict = create_dict(input("Enter fio: "), input("Enter dob: "), input("Enter ser_pass: "), input("Enter num_pass: "))

with open("dict.pickle", "wb") as handle:
    pickle.dump(my_input_dict, handle)