import glob

def pause():
    print("Press any key to continue...")
    input()

def list(pattern):
    return glob.glob(pattern)

