import sys
from cli import main
from cli.errors import ArgumentError

try:
    main()
except (ArgumentError, AssertionError) as err:
    print(f"Error: {err}")

# import sys
#
# if len(sys.argv) < 2:
#     raise Exception('not enough args')
#
