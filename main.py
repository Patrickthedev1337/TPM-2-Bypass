import winreg as reg
import ctypes
import sys

REG_PATH = r"SYSTEM\Setup\MoSetup"
VALUE_NAME = "AllowUpgradesWithUnsupportedTPMOrCPU"
VALUE_DATA = 1

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def modify_registry():
    if not is_admin():
        print("[-] Please run this script as Administrator.")
        sys.exit(1)

    try:
        with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, REG_PATH) as key:
            reg.SetValueEx(key, VALUE_NAME, 0, reg.REG_DWORD, VALUE_DATA)
            print(f"[+] Registry value '{VALUE_NAME}' set to {VALUE_DATA}")
    except Exception as e:
        print(f"[!] Error while modifying registry: {e}")

if __name__ == "__main__":
    modify_registry()
