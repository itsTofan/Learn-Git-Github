import os
import sys
def check_reboot():
    """return true if has pending reboot"""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print ("Pending Reboot")
        sys.exit(1)

main()