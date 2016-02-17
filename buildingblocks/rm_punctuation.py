import re
def removePunctuation(text):
    """Removes punctuation, changes to lower case, and strips leading and trailing spaces.

    Note:
        Only spaces, letters, and numbers should be retained.  Other characters should should be
        eliminated (e.g. it's becomes its).  Leading and trailing spaces should be removed after
        punctuation is removed.

    Args:
        text (str): A string.

    Returns:
        str: The cleaned up string.
    """
    text=re.sub(r'[^a-zA-Z0-9\s]+' ,'', text).lower().strip()
    return text
print removePunctuation('Hi, you!')
print removePunctuation(' No under_score!')
