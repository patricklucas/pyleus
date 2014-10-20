import sys

python_version = (sys.version_info[0], sys.version_info[1])

if python_version < (3, 0):
    from cStringIO import StringIO
    BytesIO = StringIO
else:
    from io import BytesIO
    from io import StringIO

_ = BytesIO  # pyflakes
_ = StringIO  # pyflakes

if python_version < (2, 7):
    import simplejson as json
else:
    import json

_ = json  # pyflakes
