def print_title(title):
    print("\n-----------------------------------------------------")
    print("\n<<<<<"+title+">>>>>\n")
    print("-----------------------------------------------------\n")
    
def print_var(var, var_name):
    print("\n-----------------------------------------------------")
    print(var_name, ":")
    print("-----------------------------------------------------\n")
    print(var)

def print_array(arr, arr_name):
    print("\n-----------------------------------------------------")
    print(arr_name, ":")
    print("-----------------------------------------------------\n")
    for row in arr:
        print(row)

def print_float(var, var_name):
    print("\n-----------------------------------------------------")
    print(var_name, ":")
    print("-----------------------------------------------------\n")
    print("%.3f" % var )

def print_dict(dict, dict_name):
    print("\n-----------------------------------------------------")
    print(dict_name, ":")
    print("-----------------------------------------------------\n")
    for row in dict.items():
        print(row)
        # for row in dict:
        # print(row)
    
