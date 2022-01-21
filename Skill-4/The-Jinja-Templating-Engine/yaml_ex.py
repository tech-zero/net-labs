from xml.dom import pulldom
import yaml
from rich import print as rprint

def pull_yaml():
    '''
    Function to pull yaml data
    '''
    config_data = yaml.safe_load(open("R1.yaml"))
    rprint(config_data)
    
pull_yaml()