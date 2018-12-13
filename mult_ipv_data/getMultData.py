import sys
import os
import re
# This script reads through queries.log and extracts the ipv4 and ipv6 responses 
# gotten from multiple_ipv4.py and multiple_ipv6.py

# As arguments is takes the location of queries.log, as well as what 
# specific files from there you want read.
# example: python mult_ipv_data.py <path to imaal.full> <wherever you want the outpt>
#example path to imaal_full is ~/scan_code/2018-08-23-11\:23\:28/imaal_full
if len(sys.argv) <= 2:
    print("Usage: python {} {} {}".format(sys.argv[0], "<imaal_full location>", "<destfileloc>"))
    sys.exit(1)
ipv4Log = "ipv4_mult.ipv"
ipv6Log = "ipv6_mult.ipv"

pathToLog = sys.argv[1]
destfileloc = sys.argv[2]

def write_out(output_file,response_ip,query):
    with open(output_file, "a") as f:
        f.write("%s | %s\n" % (response_ip, query))


def extract(output_file, pathToLog, identifier):
    # reset file
    open(output_file, "w").close()
    # go through all specified query logs and read them
    with open(pathToLog, "r") as f:
        for line in f:
            # if line matches what we want, write just the IP address to the output file 
            is_mult_ipv = re.search(identifier, line)
            if is_mult_ipv:
                response_ip = re.search(r'client ([^#]+)', line).group(1)
                timestamp = re.search(r'\([^.]*.[^.]*', line, re.DOTALL).group(0)
                write_out(output_file, response_ip, timestamp[1:]) 
               
identifier = "\.ipv4\."
extract(destfileloc + ipv4Log, pathToLog, identifier)
identifier = "\.ipv6\."
extract(destfileloc + ipv6Log, pathToLog, identifier)

