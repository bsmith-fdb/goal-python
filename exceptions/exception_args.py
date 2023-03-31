class ExampleError(Exception):
    def __init__(self, *args):
        self.args = args

    pass


def bad_function():
    raise ExampleError("error message", 1, 2, 3, 'foo')


try:
    bad_function()
except ExampleError as err:
    message, x, y, *other = err.args
    print(f"message: {message}; x: {x}; y: {y}; args:{other}")  # message: error message; x: 1; y: 2; args:[3, 'foo']
