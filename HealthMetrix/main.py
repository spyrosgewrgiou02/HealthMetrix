# main.py

import psutil
import cpuinfo
import GPUtil
import logging
import platform
import time
import tqdm

# Import optional libraries for temperature
if platform.system() == "Windows":
    import wmi
elif platform.system() == "Linux":
    import os

# Set up logging
logging.basicConfig(filename='diagnostics.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def get_cpu_temp():
    try:
        if platform.system() == "Windows":
            w = wmi.WMI(namespace="root\wmi")
            temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
            temp = temperature_info.CurrentTemperature / 10.0 - 273.15
            return f"{temp:.2f} °C"
        elif platform.system() == "Linux":
            temp_output = os.popen('sensors').read()
            # Process the output to find CPU temperature
            temp_line = next(
                (line for line in temp_output.split('\n') if 'Core 0' in line),
                None)
            if temp_line:
                temp = float(temp_line.split()[2].replace('°C', ''))
                return f"{temp:.2f} °C"
            else:
                return "Unable to retrieve temperature"
        else:
            return "Temperature monitoring not supported on this OS"
    except Exception as e:
        logging.error(f"Error retrieving CPU temperature: {e}")
        return "Error retrieving CPU temperature"


def get_cpu_info():
    try:
        return cpuinfo.get_cpu_info()['brand_raw']
    except Exception as e:
        logging.error(f"Error retrieving CPU info: {e}")
        return "Error retrieving CPU info"


def get_ram_info():
    try:
        return psutil.virtual_memory().total
    except Exception as e:
        logging.error(f"Error retrieving RAM info: {e}")
        return "Error retrieving RAM info"


def get_disk_info():
    try:
        return psutil.disk_usage('/').total
    except Exception as e:
        logging.error(f"Error retrieving disk info: {e}")
        return "Error retrieving disk info"


def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        return gpus[0].name if gpus else 'No GPU detected or available'
    except Exception as e:
        logging.error(f"Error retrieving GPU info: {e}")
        return "Error retrieving GPU info"


def get_disk_health():
    try:
        disk_usage = psutil.disk_usage('/')
        health = f"Total: {format_size(disk_usage.total)}, Used: {format_size(disk_usage.used)}, Free: {format_size(disk_usage.free)}, Percent Used: {disk_usage.percent}%"
        return health
    except Exception as e:
        logging.error(f"Error retrieving disk health: {e}")
        return "Error retrieving disk health"


def get_disk_read_write_speeds():
    try:
        start_time = time.time()
        start_read = psutil.disk_io_counters().read_bytes
        start_write = psutil.disk_io_counters().write_bytes
        time.sleep(1)
        end_read = psutil.disk_io_counters().read_bytes
        end_write = psutil.disk_io_counters().write_bytes
        read_speed = (end_read - start_read) / (time.time() - start_time)
        write_speed = (end_write - start_write) / (time.time() - start_time)
        return f"Read Speed: {format_size(read_speed)}/s, Write Speed: {format_size(write_speed)}/s"
    except Exception as e:
        logging.error(f"Error retrieving disk read/write speeds: {e}")
        return "Error retrieving disk read/write speeds"


def get_network_activity():
    try:
        net_io = psutil.net_io_counters()
        return f"Bytes Sent: {format_size(net_io.bytes_sent)}, Bytes Received: {format_size(net_io.bytes_recv)}"
    except Exception as e:
        logging.error(f"Error retrieving network activity: {e}")
        return "Error retrieving network activity"


def format_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024


def display_system_info():
    print("\n=== System Information ===")
    print(f"CPU: {get_cpu_info()}")
    print(f"RAM: {format_size(get_ram_info())}")
    print(f"Disk: {format_size(get_disk_info())}")
    print(f"GPU: {get_gpu_info()}")
    print(f"CPU Temperature: {get_cpu_temp()}")


def display_disk_health():
    print("\n=== Disk Health Information ===")
    print(get_disk_health())


def display_diagnostics():
    print("\n=== Diagnostics ===")
    print(f"Disk Read/Write Speeds: {get_disk_read_write_speeds()}")
    print(f"Network Activity: {get_network_activity()}")


def main():
    print("Starting Diagnostics...\n")
    for _ in tqdm.tqdm(range(100), desc="Running Diagnostics", unit="%"):
        time.sleep(0.01)

    display_system_info()
    display_disk_health()
    display_diagnostics()

    print("\nDiagnostics completed. Check diagnostics.log for details.")
    print("\n© Spyros Gewrgiou 2025. All rights reserved.")


if __name__ == "__main__":
    main()
