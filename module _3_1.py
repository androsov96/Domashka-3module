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
    if string.lower() in (i.lower() for i in list_to_search):
        return True
    else:
        return False
print(is_contains('hello', ['heLlo', 'HeLlO', 'WoRlD']))
print(is_contains('Hello world', ['HeLlO', 'WoRld', 'UrBaN']))
print(call)




