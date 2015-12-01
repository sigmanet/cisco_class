#!/usr/bin/env python
# __author__ = 'TMagill'

from device import Device
import xmltodict
import json
import sys


def get_hardware(switch):
    command = switch.show('show hardware')
    show_dict = xmltodict.parse(command[1])
    result_body = show_dict['ins_api']['outputs']['output']['body']
    result_table = show_dict['ins_api']['outputs']['output']['body']['TABLE_slot']['ROW_slot']['TABLE_slot_info']['ROW_slot_info']

    hardware_dict = {}
    serial_numbers = {}

    upinfo = (result_body['kern_uptm_days'], result_body['kern_uptm_hrs'], result_body['kern_uptm_mins'], result_body['kern_uptm_secs'])
    hardware_dict['uptime'] = "%s day(s) %s hour(s) %s mins(s) %s secs(s)" % upinfo   
    hardware_dict['hostname'] = result_body['host_name']
    hardware_dict['bootflash'] = result_body['bootflash_size']
    hardware_dict['os_version'] = result_body['rr_sys_ver']
    hardware_dict['memory'] = result_body['memory'] + result_body['mem_type']
    hardware_dict['last_boot_reason'] = result_body['rr_reason']
    hardware_dict['type'] = result_body['chassis_id']
    # print json.dumps( result_table, indent=4)
    for item in result_table:
        if 'model_num' in item:
            serial_numbers[item['serial_num']] = item['model_num']
    hardware_dict['serial_numbers'] = serial_numbers
    # print json.dumps( serial_numbers, indent=4)
    # print json.dumps( hardware_dict, indent=4)
    return hardware_dict

def get_mgmt(switch):
    command = switch.show('show interface mgmt0')
    show_dict = xmltodict.parse(command[1])
    result = show_dict['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    mgmt_intf = {}
    mgmt_dict = {}
    mgmt_intf['duplex'] = result['eth_duplex']
    mgmt_intf['speed'] = result['eth_speed']
    mgmt_intf['ip_addr'] = result['eth_ip_addr'] + '/' + result['eth_ip_mask']
    mgmt_intf['name'] = result['interface']
    mgmt_dict['mgmt_intf'] = mgmt_intf
    # print json.dumps(mgmt_dict, indent=4)
    return mgmt_dict

def main():
    args = sys.argv


    sw1 = Device(ip='172.31.217.134', username='admin', password='cisco123')
    sw1.open()

    hardware = get_hardware(sw1)
    mgmt = get_mgmt(sw1)
    facts =  dict(hardware, **mgmt)
    if len(args) == 1:
        print json.dumps( facts, indent=4)
    elif args[1] in facts:
        print args[1].upper() + ":", json.dumps(facts[args[1]], indent=4)
    else:
        print "Invalid Key.  Try again."

if __name__ == "__main__":
  main()



