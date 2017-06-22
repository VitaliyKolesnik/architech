from Controller import Controller
from Model import Model


from configuration.configParser import *

if __name__ == "__main__":
    
    ''' The result of config parser. '''
    result_dict = config_parser_result()

    ''' Model creation. '''
    model = Model('storage', result_dict[save_type_key])

    ''' Controller creation. Use model as agruement. '''
    controller = Controller(model)

    ''' The start of console application. '''
    controller.start()

    ''' The save of the model. '''
    model.save()
