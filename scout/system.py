import os
import platform
import psutil

def get_computer_name():
    return platform.node()

def get_operating_system():
    return f"{platform.system()} {platform.release()}"

def get_processor():
    return platform.processor()

def get_memory():
    memory = psutil.virtual_memory()
    return f"{memory.total / (1014 ** 3):.2f} GB"

def get_storage():
    disk = psutil.disk_usage(os.getenv("SystemDrive", "C:"))

    used = disk.used / (1024 ** 3)
    total = disk.total / (1024 ** 3)

    return f"{used:.1f} GB used of {total:.1f} GB"