from parser import detect_issue
from analyzer import get_fix

def run():
    with open("sample_data/crashloop_describe.txt","r") as f:
        data = f.read()

    issue = detect_issue(data)

    if issue:
        details = get_fix(issue)
        print("===========================")
        print(f"Detected Issue:\n{issue}\n")
        print(f"Portable Cause:\n{details['cause']}\n")
        print("Recommended Fixes:")
        for i, fix in enumerate(details['remediation'], 1):
            print(f"{i}. {fix}")
        print("============================")

    else:
        print("No known issue detected.")

if __name__ == "__main__":
    run()
