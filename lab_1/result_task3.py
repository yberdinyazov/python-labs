import sys
# python lab_1/result_task.py lab_1/text.txt
my_dict={}
new_list=[]
result_value=0
value_number=0
denesdirme_san=float('-inf')
with open(sys.argv[1]) as f:
    for key, value in f:
        if key not in my_dict:
            my_dict[key] = []  
        fl_value=float(value) 
        result_value=value>denesdirme_san 
        denesdirme_san=value
    print(result_value)
       
       
        # my_dict[key].append(fl_value)