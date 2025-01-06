data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(lst):
    total_numbers = 0
    total_strings = 0
    for i in data_structure:
        if isinstance(i, tuple):
            for j in i:
                if isinstance(j, (int, float)):
                    total_numbers += j
                elif isinstance(j, str):
                    total_strings += len(j)
                elif isinstance(j, dict):
                    for t in j.items():
                        if isinstance(t, (int, float)):
                            total_numbers += t
                        elif isinstance(t, str):
                            total_strings += len(t)
                        elif isinstance(t, tuple):
                            for r in t:
                                if isinstance(r, (int, float)):
                                    total_numbers += r
                                elif isinstance(r, str):
                                    total_strings += len(r)
                elif isinstance(j, list):
                    for l in j:
                        if isinstance(l, (int, float)):
                            total_numbers += l
                        elif isinstance(l, str):
                            total_strings += len(l)
                        elif isinstance(l, set):
                            for a in l:
                                if isinstance(a, (int, float)):
                                    total_numbers += a
                                elif isinstance(a, str):
                                    total_strings += len(a)
                                elif isinstance(a, tuple):
                                    for s in a:
                                        if isinstance(s, (int, float)):
                                            total_numbers += s
                                        elif isinstance(s, str):
                                            total_strings += len(s)
                                        elif isinstance(s, tuple):
                                            for d in s:
                                                if isinstance(d, (int, float)):
                                                    total_numbers += d
                                                elif isinstance(d, str):
                                                    total_strings += len(d)
        elif isinstance(i, list):
            for j in i:
                if isinstance(j, (int, float)):
                    total_numbers += j
                elif isinstance(j, str):
                    total_strings += len(j)
        elif isinstance(i, dict):
            for j in i.items():
                if isinstance(j, (int, float)):
                    total_numbers += j
                elif isinstance(j, str):
                    total_strings += len(j)
                elif isinstance(j, tuple):
                    for r in j:
                        if isinstance(r, (int, float)):
                            total_numbers += r
                        elif isinstance(r, str):
                            total_strings += len(r)
        elif isinstance(i, str):
            total_strings += len(i)
        elif isinstance(i, (int, float)):
            total_numbers += i
    return total_numbers + total_strings
print(calculate_structure_sum(data_structure))


