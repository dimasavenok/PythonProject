class ZeroQuatityError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"ZeroQuatityError: {self.msg}"