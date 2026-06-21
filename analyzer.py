import ollama

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

def get_ai_suggestion(error_log):
    print("\n[AI] Rule-based system could not find a fix. Asking AI....")
    prompt = f"I am a k8s administrator. I have an error: '{error_log}'. Provide a  short, actionable fix in bullet points."

    response = ollama.chat(model='gemma:2b', messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']

def analyze_error(error_log):
    fix = get_fix(error_log)
    if fix:
        return fix

    ai_suggestion = get_ai_suggestion(error_log)
    return {
        "cause": "AI Detected Issue",
        "remediation": [ai_suggestion]
    }
