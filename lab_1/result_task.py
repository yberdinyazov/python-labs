import sys

# python lab_1/result_task.py lab_1/text.txt
my_dict={}
new_list=[]
my_list2=[]
result_value=0

with open(sys.argv[1]) as f:
    for my_list in f:
        data_list=my_list.strip()
        data_list=data_list.split(";")
        city=data_list[0]
        temperature=float(data_list[1])
        if city not in my_dict:     
            my_dict[city]=[temperature, temperature, temperature, 1]
        else:
            my_dict[city][0]=min(my_dict[city][0],temperature)
            my_dict[city][1]=max(my_dict[city][1],temperature) 
            my_dict[city][3]+=1
            my_dict[city][2]+=temperature
for key in sorted(my_dict):
    ortalama=my_dict[key][2] / my_dict[key][3]
    
    print(f"{key}, {my_dict[key][0]}, {ortalama:.1f},{ my_dict[key][1]}" )
