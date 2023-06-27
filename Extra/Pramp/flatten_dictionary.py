"""
Flatten a Dictionary

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it.
If a certain key is empty, it should be excluded from the output (see e in the example below).


input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
        
""" 


def flatten_dictionary(nested_dict):
    flat_dict = {}
    flat_dict_recurse(nested_dict, flat_dict)
    return flat_dict

def flat_dict_recurse(nested_dict, flat_dict, path=""):
    for key, value in nested_dict.items():

        # case 1
        # c : {a : 1, b : 2}
        # case 2
        # c : 2
        include_dot = 1 if path and key else 0

        updated_path = path + "." * include_dot + key
        
        if not isinstance(value, dict):
            flat_dict[updated_path] = value
        else:
            flat_dict_recurse(value, flat_dict, updated_path)

ref = {
    "Key1" : "1",
    "Key2" : {
        "a" : "2",
        "b" : "3",
        "c" : {
        "d" : "3",
        "e" : {
            "" : "1"
            }
    }
}
        }
print(flatten_dictionary(ref))