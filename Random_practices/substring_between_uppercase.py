def print_substring_between_uppercse(input_str):
    upper_case_indices=[]
    for index in range(len(input_str)):
        if input_str[index].isupper()==True:
            upper_case_indices.append(index)

    first_upper_index = upper_case_indices[0]
    second_upper_index = upper_case_indices[1]

    sub_string = input_str[first_upper_index+1:second_upper_index]

    if len(sub_string) == 0:
        print("BLANK")
    else:
        print(sub_string)

print_substring_between_uppercse("amadeRdesherNam")