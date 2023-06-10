import os
import sys
def check_reboot():
    """return true if has pending reboot"""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print ("Pending Reboot PC")
        sys.exit(1)
    print ("Everything ok")
    sys.exit(0)
main()