import In_out
import Control
import serialize
import pickle

def save_result ():
    print ("\n\nSave result as:\n1. pickle\n2. yaml\n3. json\n")
    res = int(raw_input("Select: "))
    if res == 1:
        return "pickle"
    elif res == 2:
        return "yaml"
    elif res == 3:
        return "json"
    else:
        return ""


def start(config, file_name):
    """function for run project"""

    file_obj = open (config, "r")
    tp = pickle.load(file_obj);
    file_obj.close()
    
    file_obj = open (file_name, "r ");
    calendar = serialize.load(file_obj, tp)
    file_obj.close()
    calendar = Control.menu(calendar)

    new_tp = save_result()
    file_obj = open (file_name, "w");
    
    if new_tp == "":
        serialize.save(calendar, file_obj, tp)
    else:
        fl = open(config, "w")
        pickle.dump(new_tp, fl)
        fl.close()
        serialize.save(calendar, file_obj, new_tp)
    file_obj.close()
