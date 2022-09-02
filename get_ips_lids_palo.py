#!/usr/bin/env python
import os
import re
filesList=os.scandir('./CONFIGS/')
print("FirewallName,Comment,Interface,RouteName,NextHopIP")
for i in filesList:
  firewall=i.name
  with open ('./CONFIGS/'+i.name,'r') as f:
    config=f.read()
    ifsAndLid=re.findall('set network interface ethernet (ethernet.*) comment (.*INET;.*)',config)
    if len(ifsAndLid)==0:
        ifsAndLid=[('None','None')]
    if 'units' in ifsAndLid[0][0]:
        ifsAndLid=re.findall('set network interface ethernet .* layer3 units (ethernet.*) comment (.*INET;.*)',config)
    defRouteNames=re.findall('set network virtual-router ECN-vrouter routing-table ip static-route (.*) destination 0.0.0.0/0',config)
    if len(defRouteNames)==0:
        defRouteNames.append('None')
    for name in defRouteNames:
      routeNextHopRegex='set network virtual-router ECN-vrouter routing-table ip static-route '+name+' nexthop ip-address (.*)'
      routeNextHop=re.findall(routeNextHopRegex,config)
      routeInterfaceRegex='set network virtual-router ECN-vrouter routing-table ip static-route '+name+' interface (.*)'
      routeInterface=re.findall(routeInterfaceRegex,config)
      for group in ifsAndLid:
        try:
            if ifsAndLid[0][0]=='None':
                print(firewall+','+group[1]+','+group[0]+','+name+','+routeNextHop[0])
            elif routeInterface[0]==group[0]:
                print(firewall+','+group[1]+','+group[0]+','+name+','+routeNextHop[0])
        except IndexError:
            print(firewall+','+group[1]+','+group[0]+','+name+','+'')

