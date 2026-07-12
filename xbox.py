import subprocess

class Xbox:
    def __init__(self, ip):
        self.ip = ip

    def is_on(self) -> bool:
        result = subprocess.run(
            ["ping", "-c", "1", self.ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
        