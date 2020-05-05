import pyeapi
import yaml
from pprint import pprint as pp

with open("hosts.yaml", "r") as host_file:
    hosts = yaml.load(host_file, Loader=yaml.FullLoader)

# print(hosts)

with open("config.yaml", "r") as config_file:
    cfg = yaml.load(config_file, Loader=yaml.FullLoader)

# print(cfg)

username = cfg['defaults']['username']
password = cfg['defaults']['password']
protocol = cfg['defaults']['protocol']

connection = pyeapi.connect(host=hosts['vEOS-LSW01']['host'],
                            transport=protocol,
                            username=username,
                            password=password)

node = pyeapi.client.Node(connection)

# pp(node.api('bgp').get())


vlans = node.api('interfaces').getall()['Vxlan1']['vlans'].keys()
print(vlans)
for vlan in vlans:
    node.api('vlans').create(vlan)
    node.api('vlans').set_name(vlan, name=f"TEST_{vlan}")

pp(node.api("vlans").getall())