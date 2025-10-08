data = dict({'pat_001': ['bacZZt98', 'bac889Ytd'], 'pat_002': ['bac0GFrr'], 'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']})
print(data)
# Loop through the dict printing each key and each value as a list.
# for key_patient, value_bact_list in data.items():  
#   print(key_patient)
#   print(value_bact_list)

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

# for key_patient, value_bact_list in data.items():  
#   print(key_patient)
#   print(value_bact_list)
#   if 'bac889Ytd' in value_bact_list:
#         print(True)
#   else:
#         print(False)

unique_bacteria = list()
for value_bact_list in data.values():
    for bacterium in value_bact_list:
        if bacterium not in unique_bacteria:
            unique_bacteria.append(bacterium)
print(f"Unique bacteria: {unique_bacteria}")

dict_unique_bacteria = dict()
print(f"Data values: {data.values()}")
for value_bact_list in data.values():
    for bacterium in value_bact_list:
        if bacterium not in dict_unique_bacteria:
            dict_unique_bacteria[bacterium] = list()
            import pdb; pdb.set_trace()
            for key_patient, unique_bacteria in data.items():
                if bacterium in unique_bacteria:
                    print(f"found {bacterium} in {key_patient}")
                    dict_unique_bacteria[bacterium].append(key_patient)  
                    print(f"added {key_patient} to {bacterium} list")
print(dict_unique_bacteria)

