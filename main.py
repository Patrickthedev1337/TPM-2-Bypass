import winreg as reg
import ctypes

def modify_registry():
    # Pfad zum Schlüssel
    reg_path = r"SYSTEM\Setup\MoSetup"
    value_name = "AllowUpgradesWithUnsupportedTPMOrCPU"
    value_data = 1

    try:

        if not ctypes.windll.shell32.IsUserAnAdmin():
            raise PermissionError("Please run as admin!")


        with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, reg_path) as key:

            reg.SetValueEx(key, value_name, 0, reg.REG_DWORD, value_data)
            print(f"Dwort '{value_name}' setted  {value_data} Step 1")
    except PermissionError as pe:
        print(f"Error: {pe}")
    except Exception as e:
        print(f"Unexpected Error !: {e}")

if __name__ == "__main__":
    modify_registry()
