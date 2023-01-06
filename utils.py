import os


class Utils:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    cwd = os.getcwd()


u = Utils()
print(u.cwd)
