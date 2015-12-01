#!/usr/bin/env python

vlan_names = ['web' ,'db', 'web2', 'db2', 'voice', 'video', 'srvs', 'test', 'prod', 'qa']

from cli import *
if __name__ == '__main__':

for vlan in range(10,20):
	cmdtext = 'config t ; ' + 'vlan ' + str(vlan) + ' ; ' + 'name ' + vlan_names[10-vlan] + ' ; '
	print cmdtext
    # cli(cmdtext)