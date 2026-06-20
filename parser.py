import re

def detect_issue(describe_text):

    patterns = {
            "CrashLoopBackOff": r"CrashLoopBackOff",
            "ImagePullBackOff": r"ImagePullBackOff",
            "ErrImagePull": r"ErrImagePull",
            "OOMKilled": r"OOMKilled"
    }

    for issue, pattern in patterns.items():
        if re.search(pattern, describe_text, re.IGNORECASE):
            return issue
    
    return None
