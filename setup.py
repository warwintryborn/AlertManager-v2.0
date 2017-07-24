from cx_Freeze import setup, Executable

exe = [Executable("AlertManager.py", base = "Win32GUI")]

setup(
    name = "AlertManager",
    version = "1.0.0",
    description = "Alert Manager e-Vertical",
    executables = exe)
