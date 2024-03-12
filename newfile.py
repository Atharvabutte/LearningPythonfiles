import sys


def linux_interaction():
    if "linux" not in  sys.platform:
        print(sys.platform)
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")


if __name__ == "__main__":
   linux_interaction()