# txt = "welcome; to; the; jungle"

# x = txt.split()

# print(x)
my_dict={}
liste=[['Dili', '40.5'], ['Anchorage', '14.5'], ['Ahvaz', '35.1'], ['Moscow', '9.5'], ['Malabo', '17.6'], ['Hanoi', '10.7'], ['Hanoi', '24.1'], ['Dili', '15.5']]

denesdirme_san=float('-inf')
# result_value=0
for key, value in liste:
    if key not in my_dict:
        my_dict[key] = []   
    fl_value=float(value) 
    my_dict[key].append(float(value))
    my_dict[key].append(fl_value)
    result_value=fl_value>denesdirme_san 
    denesdirme_san=fl_value
    # result_value+=fl_value

print()
# res=max(my_dict, key=lambda k: max(my_dict[k]))
# res2=min(my_dict, key=lambda k: min(my_dict[k]))
# print(res,max(my_dict[res]))
# print(res2,min(my_dict[res2]))
