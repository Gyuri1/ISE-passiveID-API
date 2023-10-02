# ISE-passiveID-API

These scripts demonstrate how to use ISE PassiveID API and syslog providers.  

If You confiure pxGrid service between ISE and FMC, PassiveID service can update the username-IP address mappings on FMC as well.  


# How to install:


# How to run:


API
===
`python passiveid.py -n ise.company.local -u UserAPI -i 10.0.1.5 -a admin -p C1sco123 -d company.local -v`
  
where:  
-n ISE node's FQDN or IP address  
-u new username  
-i new user's IP address  
-a ISE PassiveID admin name  
-p ISE PassiveID admin password 
-d target domain 
-v verbose log



Syslog:
======
`python passiveid-syslog.py -n ise.company.local -u asauser1 -i 10.1.1.1 -s SENDER.company.com`
  
where:  
-n ISE node's FQDN or IP address  
-u new username  
-i new user's IP address  
-s syslog sending device's FQDN   


NOTES:
=====

- SENDER.company.com type of FQDN worked in my environment. The machine name part is capitalized.

- ASA-VPN Profile was used for syslog provider.

- API provider example was ported and modified from this repo:
  https://github.com/vbobrov/iseutils/blob/main/passiveid-rest.py
