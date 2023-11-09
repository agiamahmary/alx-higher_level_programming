def lookup(obj):
    """
    Used to search and return available attributes and methods attached to obj.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings containing the names of attributes and methods.
    """
    return dir(obj)
