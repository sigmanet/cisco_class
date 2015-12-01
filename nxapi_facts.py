#!/usr/bin/env python
# __author__ = 'TMagill'

from device import Device
import xmltodict
import json



def get_hardware(switch):
    command = switch.show('show hardware')
    show_dict = xmltodict.parse(getdata[1])
    result = show_dict['ins_api']['outputs']['output']['body']['TABLE
    hardware_dict = ''
    return hardware_dict

def get_mgmt(switch):
    command = switch.show('show interface mgmt0')
    show_dict = xmltodict.parse(getdata[1])
    result = show_dict['ins_api']['outputs']['output']['body']['TABLE
    mgmt_intf = {}
    mgmt_dict = {}
    mgmt_intf['duplex'] = result['']
    mgmt_intf['speed'] = result['']
    mgmt_intf['ip_addr'] = result[''] + '/' + result['']
    mgmt_intf['name'] = result['']
    mgmt_dict['mgmt_intf'] = mgmt_intf
    return mgmt_dict

def main():
    sw1 = Device(ip='172.32.217.134', username='admin', password='cisco123')
    sw1.open()

    hardware = get_hardware(sw1)
    mgmt = get_mgmt(sw1)
    facts =  dict(hardware, **mgmt)
    print json.dumps( facts, indent=4)

    # facts = hardware.copy()
    # facts.update(y)