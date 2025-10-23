def my_function():
    result = 3 * 2
    return result
output = my_function()
print(output)



def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("Julia", "BERGER")
print(formated_string)

def function_1(text):
    return text + text
def function_2(text):
    return text.title()
output = function_2(function_1("hello"))
print(output)