class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created.")

    def __del__(self):
        print(f"Object {self.name} destroyed.")

obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

del obj1
del obj2
obj3 = MyClass("Object 3")