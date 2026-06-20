ISSUE_DATABASE = {
        "CrashLoopBackOff": {
            "cause": "Application repeatedly crashing during startup.",
            "remediation": [
                "Check pod logs",
                "Verify startup command",
                "Verify environment variables"
                ]
            },
         "ImagePullBackOff": {
             "cause": "Container image could not pe pulled.",
             "remediation": [
                  "Verify image name",
                  "Check image tag",
                  "Check registry credentials"
                 ]
             },
         "ErrImagePull": {
             "cause": "Continer image pull failed.",
             "remediation": [
                 "Verify registry access",
                 "Verify image availability"
                 ]
             },
         "OOMKilled": {
             "cause": "Container exceeded memoory limit.",
             "remediation":[
                 "Increase memory limit",
                 "Optimize application memory uasge"
                 ]
             }
         }
def get_fix(issue_name):
    return ISSUE_DATABASE.get(issue_name, None)
