import os

def check_reboot():
    """return true if has pending reboot"""
    return os.path.exists("/run/reboot-required")

def main():
    print("Hello World!")

main()