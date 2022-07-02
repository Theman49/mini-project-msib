from automation import *

id_lab = createLab('project_lab')

nodes = [
    {
        'x': 0,
        'y': 0,
        'label': 'bridge',
        'configuration': "./script-config/config-external-connector.txt",
        'node_definition': 'external_connector',
        'image_definition': 'null'
    },
    {
        'x': 0,
        'y': 200,
        'label': 'unmanaged switch',
        'configuration': "",
        'node_definition': 'unmanaged_switch',
        'image_definition': 'null'
    },
    {
        'x': 0,
        'y': 400,
        'label': 'R1',
        'configuration': "",
        'node_definition': 'csr1000v',
        'image_definition': 'csr1000vb'
    },
    {
        'x': -400,
        'y': 700,
        'label': 'S1',
        'configuration': "",
        'node_definition': 'nxosv9000',
        'image_definition': 'nxosv9000'
    },
    {
        'x': 400,
        'y': 700,
        'label': 'S2',
        'configuration': "",
        'node_definition': 'nxosv9000',
        'image_definition': 'nxosv9000'
    },
    {
        'x': -400,
        'y': 900,
        'label': 'host1',
        'configuration': "./script-config/config-host1.txt",
        'node_definition': 'desktop',
        'image_definition': 'desktop-3-13-2-xfce'
    },
    {
        'x': 200,
        'y': 900,
        'label': 'host2',
        'configuration': "./script-config/config-host2.txt",
        'node_definition': 'desktop',
        'image_definition': 'desktop-3-13-2-xfce'
    },
    {
        'x': 600,
        'y': 900,
        'label': 'host3',
        'configuration': "./script-config/config-host3.txt",
        'node_definition': 'desktop',
        'image_definition': 'desktop-3-13-2-xfce'
    }
]    

for node in nodes:
    print(createNode(id_lab, node))


    

mynode = {
    'bridge': 'n0',
    'uswitch': 'n1',
    'router': 'n2',
    's1': 'n3',
    's2': 'n4',
    'host1': 'n5',
    'host2': 'n6',
    'host3': 'n7'
}

# update config host setting ip
for node in nodes:
    if node['label'] == 'bridge' or node['label'] == 'host1' or node['label'] == 'host2' or node['label'] == 'host3':
        n = node['label']
        print(updateConfigNodes(id_lab, mynode[n], node['configuration']))

interfaces = [
    {
        'node': mynode['bridge'],
        'slot': 0
    },
    {
        'node': mynode['uswitch'],
        'slot': 0
    },
    {
        'node': mynode['uswitch'],
        'slot': 1
    },
    {
        'node': mynode['uswitch'],
        'slot': 2
    },
    {
        'node': mynode['uswitch'],
        'slot': 3
    },
    {
        'node': mynode['router'],
        'slot': 0
    },
    {
        'node': mynode['router'],
        'slot': 1
    },
    {
        'node': mynode['router'],
        'slot': 2
    },
    {
        'node': mynode['s1'],
        'slot': 0
    },
    {
        'node': mynode['s1'],
        'slot': 1
    },
    {
        'node': mynode['s1'],
        'slot': 2
    },
    {
        'node': mynode['s2'],
        'slot': 0
    },
    {
        'node': mynode['s2'],
        'slot': 1
    },
    {
        'node': mynode['s2'],
        'slot': 2
    },
    {
        'node': mynode['host1'],
        'slot': 0
    },
    {
        'node': mynode['host2'],
        'slot': 0
    },
    {
        'node': mynode['host3'],
        'slot': 0
    },
    {
        'node': mynode['s2'],
        'slot': 3
    },
]

for interface in interfaces:
    print(createInterfaces(id_lab, interface))

links = [
    {
        'src_int': 'i3',
        'dst_int': 'i4'
    },
    {
        'src_int': 'i5',
        'dst_int': 'i8'
    },
    {
        'src_int': 'i9',
        'dst_int': 'i12'
    },
    {
        'src_int': 'i10',
        'dst_int': 'i15'
    },
    {
        'src_int': 'i11',
        'dst_int': 'i6'
    },
    {
        'src_int': 'i14',
        'dst_int': 'i7'
    },
    {
        'src_int': 'i13',
        'dst_int': 'i17'
    },
    {
        'src_int': 'i16',
        'dst_int': 'i18'
    },
    {
        'src_int': 'i19',
        'dst_int': 'i20'
    }
]

for link in links:
    print(createLinks(id_lab, link))

print("Done!!!")