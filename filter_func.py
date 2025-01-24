# basic filter function
# basic function
def check_string(s):
    if s.startswith("S"):
        return True
    else:
        return False
    
string_list = ["Sunny", "Hardik", "Arun", "Sujal"]
filtered_list = list(filter(check_string, string_list))

print(filtered_list)

# using lambda function
lambda_check_string = lambda s: True if s.startswith("S") else False

filtered_list = list(filter(lambda_check_string, string_list))
print(filtered_list)
