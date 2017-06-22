import model
import controller


def start():
    """function for run project"""
    md = model.Model()
    ct = controller.Controller(md)
    ct.menu()
