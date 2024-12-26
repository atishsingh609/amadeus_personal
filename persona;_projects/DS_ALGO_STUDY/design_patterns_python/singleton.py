import threading

class Singleton:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            with cls.__lock:
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, value):
        self.value = value


instance_1 = Singleton(10)
instance_2 = Singleton(20)

print(instance_1, instance_2)