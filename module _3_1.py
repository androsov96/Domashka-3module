call = 0
def count_call():
    global call
    call += 1

def string_info(string):
    count_call()
    return len(string), string.upper(), string.lower()
print(string_info('CapyBaRa'))
print(string_info('ArmaGeDdoN'))

def is_contains(string, list_to_search):
    count_call()
    if isinstance(string, str):
        return True
    else:
        return False
print(is_contains({'hello world'}, ['hello', 'world']))
print(is_contains('Hello world', [3,34,5,3]))
print(call)




