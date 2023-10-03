# ISE-passiveID-API

These scripts demonstrate how to use ISE PassiveID API and syslog providers.  

If You confiure pxGrid service between ISE and FMC, PassiveID service can update the username-IP address mappings on FMC as well.  

Like this way: 

  script -> ISE PassiveID (API or syslog provider) -> pxGrid -> FMC (ID firewall service)  



# How to install:

 
Install the necessary python modules
`pip install `


# How to use:


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

ISE logging:  
`show logging  application passiveid-api.log tail`


ISE Configuration:



Notes:
- Thank You very much for the great support Viktor Bobrov!
- API provider example was ported and modified from this repo:
  https://github.com/vbobrov/iseutils/blob/main/passiveid-rest.py

Syslog:
======
`python passiveid-syslog.py -n ise.company.local -u asauser1 -i 10.1.1.1 -s SENDER.company.com`
  
where:  
-n ISE node's FQDN or IP address  
-u new username  
-i new user's IP address  
-s syslog sending device's FQDN   

ISE Configuration:


ISE logging:  
`show logging application passiveid-syslog.log tail`

Notes:
- SENDER.company.com type of FQDN worked in my environment. The machine name part is capitalized.
- ASA-VPN Profile was used for syslog provider.
