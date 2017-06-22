import pickle
import yaml
import json

pickle_type = "pickle"
yaml_type = "yaml"
json_type = "json"


def load(file_obj, serialize_method):
    """ deserialize data"""
    if serialize_method == pickle_type:
        return pickle.load(file_obj)
    elif serialize_method == yaml_type:
        return yaml.load(file_obj)
    elif serialize_method == json_type:
        return json.load(file_obj)


def save(data, file_obj, serialize_method):
    """ serialize data """
    if serialize_method == pickle_type:
        if file_obj:
            return pickle.dump(data, file_obj)
        else:
            return pickle.dumps(data)
    elif serialize_method == yaml_type:
        return yaml.dump(data, file_obj, default_flow_style=False)
    elif serialize_method == json_type:
        return json.dump(data, file_obj)
