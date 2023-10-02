# ISE-passiveID-API

These scripts demonstrate how to use ISE PassiveID API and syslog providers.

If You confiure pxGrid service between ISE and FMC, PassiveID service can update the users on FMC as well.


# How to install:


# How to run:


`python passiveid-syslog.py -n ise.company.local -u asauser1 -i 10.1.1.1 -s SENDER.company.com`


NOTES:

SENDER.company.com type of FQDN worked in my environment.  

ASA-VPN Profile was used for syslog provider.

API provider example was ported and modified from this repo:
https://github.com/vbobrov/iseutils/blob/main/passiveid-rest.py
