

print("file1 __name__ = %s" %__name__)

if __name__ == "__main__":
    print("File1 is being run directly")
else:
    print("File1 is being imported")

print("11111111111111111111111111111")

print("file2 __name__ = %s" %__name__)

if __name__ != "__main__":
    print("file2 in running")
else:
    print("file2 is imported")
