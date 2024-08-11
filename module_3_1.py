calls = 0
def count_calls():
    global calls
    calls = calls + 1
    print(calls)

def string_info(string):
    print((len(string), str.upper(string), str.lower(string)))
    global calls
    calls = calls + 1


def is_contains(string, list_to_search):
    for element in list_to_search:
        if element.lower() in string.lower():
            print(element in list_to_search)
            break
        else:
            print(element not in list_to_search)
            break
    global calls
    calls = calls + 1

string_info('Lada')
string_info('Nikolay')
is_contains('ANanas', ['ananas', 'coconut', 'apple'])
is_contains('pear', ['ananas', 'coconut', 'apple'])
print(calls)

