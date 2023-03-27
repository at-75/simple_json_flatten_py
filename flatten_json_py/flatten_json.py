def flatten_json(json_obj_, name_=""):
    flat_dict = {}
    
    def join_(a, b):
        if not isinstance(a, str): a = str(a)
        if not isinstance(b, str): b = str(b)
        return a + '_' + b
    
    def __flat__json(json_obj, name):
        for x, y in json_obj.items():
            c_name = join_(name, x)
            if isinstance(y, list):
                for i, j in enumerate(y):
                    if isinstance(j, str):
                        flat_dict[join_(c_name, i)] = j
                    elif isinstance(j, dict):
                        __flat__json(j, join_(c_name, i))  # Recursively break down JSON
            elif isinstance(y, dict):
                __flat__json(y, c_name)  # Recursively break down JSON
            else:
                flat_dict[c_name] = y

    __flat__json(json_obj_, name_)
    return flat_dict
