This script is created to identify the Internet facing interfaces and default route next-hop from a bungh of Internet Break Out Palo Alto firewalls. 
It identifies interfaces on the basis of a comment (INET in this case) that your org uses to describe the interface usage and then finds details about the default route next-hop.

Usage: Copy all config files into the CONFIGS directory and run the script after editing the comment - Replace "INET" with the comment you have for Internet interfaces.
If no interface is found that matches the comment, or  no default route exists, value "None" is entered in the respective fields

Input: Config files from various Palo Alto firewalls 
Output: Comma Separated output of ConfigFile Name,Comment,Interface,RouteName,NextHopIP



Example:

[user@vm1 INET_PA_Route]$ ./get_ips_lids_palo.py 
FirewallName,Comment,Interface,RouteName,NextHopIP
fw1.conf,"Internet",ethernet1/2,"Default Route",1.1.1.1
fw2.conf,"Internet",ethernet1/2,Default-0.0.0.0-Primary,2.2.2.2
fw3.conf,Internet,ethernet1/2.666,Default,3.3.3.3
fw4.conf,None,None,Default,4.4.4.4
