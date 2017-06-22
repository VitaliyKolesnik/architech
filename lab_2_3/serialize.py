import pickle
import yaml
import json


class Serialize:
    """Class Serialize of pickle, yaml and json"""

    def __init__(self):
        self.__pickle_type = "pickle"
        self.__yaml_type = "yaml"
        self.__json_type = "json"

    def load(self, file_obj, serialize_method):
        """ deserialize data"""
        if serialize_method == self.__pickle_type:
            return pickle.load(file_obj)
        elif serialize_method == self.__yaml_type:
            return yaml.load(file_obj)
        elif serialize_method == self.__json_type:
            return json.load(file_obj)

    def save(self, data, file_obj, serialize_method):
        """ serialize data """
        if serialize_method == self.__pickle_type:
            if file_obj:
                return pickle.dump(data, file_obj)
            else:
                return pickle.dumps(data)
        elif serialize_method == self.__yaml_type:
            return yaml.dump(data, file_obj, default_flow_style=False)
        elif serialize_method == self.__json_type:
            return json.dump(data, file_obj)
