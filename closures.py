def greeter(prefix):  # "factory" function
    def greet(name):
        print(f"{prefix} {name}")

    return greet


hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Nancy")
goodbye("Rachel")
