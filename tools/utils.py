import subprocess
from subprocess import CalledProcessError
from os import PathLike
from pathlib import Path

import cpuinfo

NVIDIA_SMI_DEFAULT_ATTRIBUTES = (
    "index",
    "uuid",
    "name",
    "timestamp",
    "memory.total",
    "memory.free",
    "memory.used",
    "utilization.gpu",
    "utilization.memory",
)


def check(condition: bool, message: str) -> bool:
    if not condition:
        print(f'ERROR: {message}')
        return False
    return True


def describe_cpu():
    print("====== cpu info ============")
    for key, value in cpuinfo.get_cpu_info().items():
        print(f"CPU INFO: {key:20s}: {value}")
    print("============================")


def describe_gpu(nvidia_smi_path="nvidia-smi", no_units=True):
    try:
        keys = NVIDIA_SMI_DEFAULT_ATTRIBUTES
        nu_opt = "" if not no_units else ",nounits"
        cmd = f'{nvidia_smi_path} --query-gpu={",".join(keys)} --format=csv,noheader{nu_opt}'
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE)
        lines = output.decode().split("\n")
        lines = [line.strip() for line in lines if line.strip() != ""]
        lines = [{k: v for k, v in zip(keys, line.split(", "))} for line in lines]

        print("====== show GPU information =========")
        for line in lines:
            for k, v in line.items():
                print(f"{k:25s}: {v}")
        print("=====================================")
    except CalledProcessError:
        print("====== show GPU information =========")
        print("  No GPU was found.")
        print("=====================================")
