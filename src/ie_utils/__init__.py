"""
IE Titanic utils
"""

__version__= "0.1.0" # semver.org

def tokenize(text):
    return text.split()

if __name__ == "__main__":
    print(tokenize("Hello World!"))