This tool sets the official Microsoft registry key to allow installing Windows 11
on systems without TPM 2.0 or a supported CPU.

No USB boot required.

Requirements:
- A Windows 11 bootable ISO file
- Administrator privileges

How to use:
1. Right-click the Windows 11 ISO and select "Mount" (German: "Bereitstellen")
2. Compile the .py file to an .exe and run it as Administrator
3. Open the mounted ISO (it appears as a DVD drive)
4. Run setup.exe
5. Done

Optional:
- You can disable the internet during setup (not required)
- Do NOT set the created DWORD back to 0 if you want Windows Update to keep working

Registry key used:
HKLM\SYSTEM\Setup\MoSetup
AllowUpgradesWithUnsupportedTPMOrCPU = 1

Note:
This does not crack or modify Windows.
It uses an official Microsoft workaround for unsupported hardware.
