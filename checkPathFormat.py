import os

def checkPathNdFormat(path: str) -> bool:
    """Check Path And Format
    this is a functions to check the given path and format if its a valid file
    Args:
        path (str): path to file
    Returns:
        bool: false in case of error
    """
    file_extension = os.path.splitext(path)[1].lower()
    if os.path.isfile(path):
        if file_extension in ['.csv']:
            return True
    return False