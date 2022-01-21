from xml.dom import pulldom
import yaml
from rich import print as rprint

def pull_yaml():
    '''
    Function to pull yaml data
    '''
    config_data = yaml.safe_load(open("R1.yaml"))
    bgp_stuff = config_data["BGP"]
    rprint(bgp_stuff)
    rprint(bgp_stuff["ASN"])
    peers = bgp_stuff["peers"]
    rprint(peers)
    for peer in peers:
        rprint(peer)
        nbor = peer["neighbor"]
        asnumber = peer["peer_asn"]
        rprint(f"The neighbor {nbor} has an ASN of {asnumber}")
    
pull_yaml()