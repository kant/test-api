# -*- coding: utf-8 -*-
import platform
import multiprocessing
import threading
import sys
import os
import psutil
import datetime


def get_status():
    result: dict = {"status": "UP", "current_datetime": str(datetime.datetime.now())}
    return result


def get_platform() -> dict:
    """
    [summary]
    Get all system, OS, and Python version information

    Returns:
        dict -- ["os": os,
        "system": system,
        "node": node,
        "processor": processor,
        "cpu_count": cpu_count,
        "memory_use": memory_use,
        "python_version": python_version,]
    """
    os = platform.platform()
    processor = platform.processor()
    node = platform.node()
    system = platform.system()
    cpu_count = multiprocessing.cpu_count()
    memory_use = sys.getsizeof({})
    friendly_maxsize = {2 ** 31 - 1: "32 bit", 2 ** 63 - 1: "64 bit"}.get(
        sys.maxsize
    ) or "unknown bits"
    friendly_version = f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} {sys.version_info[3]}"  # .{sys.version_info[0]}" #.format(*sys.version_info)
    python_version = "{0} ({1})".format(friendly_version, friendly_maxsize)

    # 'threads_size': threads_size, threads_size = threading.stack_size()

    result = {
        "os": os,
        "system": system,
        "node": node,
        "processor": processor,
        "cpu_count": cpu_count,
        "memory_use": memory_use,
        "python_version": python_version,
    }
    return result


def get_processes() -> dict:
    """
    Get running processes and filter by python processes

    Returns:
        dict -- [pid, name, username]
    """
    result = []
    proc = psutil.process_iter(attrs=["pid", "name", "username"])
    process_check = ["python", "python3", "gunicorn", "uvicorn", "hypercorn", "daphne"]

    for p in proc:
        if p.info["name"] in process_check:
            result.append(p.info)

    print(result)
    return result


if __name__ == "__main__":
    get_processes()
