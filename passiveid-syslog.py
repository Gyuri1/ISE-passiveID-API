# ISE Passive ID - Syslog demo
import sys
import argparse
from logging import getLogger, Formatter
import logging.handlers

# Please use UDP in ISE
UDP_PORT = 40514

parser = argparse.ArgumentParser(description='Passive ID syslog provider demo script')
parser.add_argument('-n', '--node', required=True, help='ISE address or name')
parser.add_argument('-i', '--ip', required=True, help='IP address')
parser.add_argument('-u', '--username', required=True, help='Username')
parser.add_argument('-s', '--source', required=True, help='Source device FQDN (no IP address))')
args = parser.parse_args()

ISE_IP = args.node
MESSAGE = '%ASA-6-113039 Group group User '+args.username+' IP ' + args.ip + ' AnyConnect parent session started.'

print('ISE Passive ID - Syslog demo')
print("ISE target IP:", args.node)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)
print("Source Device:", args.source)


# Get the root logger
logger = getLogger()
syslogHandler = logging.handlers.SysLogHandler(address=(args.node,UDP_PORT ))
logger.setLevel(logging.INFO)
logger.addHandler(syslogHandler)
logger.info(args.source+ ' ' + MESSAGE)
