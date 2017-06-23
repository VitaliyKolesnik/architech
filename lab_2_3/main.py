import model
import controller


def start(config, filename):
    """function for run project"""
    md = model.Model(filename, config)
    ct = controller.Controller(md)
    ct.menu()
start(".config", "db.txt")
