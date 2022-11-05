import os
for (root, dirs, files) in os.walk(os.path.join( '.'), topdown=False):
    for name in files:
        print(name)
