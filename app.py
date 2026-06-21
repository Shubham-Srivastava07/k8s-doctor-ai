from parser import detect_issue
from analyzer import analyze_error

def run():
    
    try:
        with open("sample_data/unknown_error.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: File not found!")
        return

    
    issue = detect_issue(data)
    
    
    issue_to_analyze = issue if issue else data
    
    
    details = analyze_error(issue_to_analyze)
    
    print("===========================")
    print(f"Analysis For: {issue if issue else 'Unknown Issue'}")
    print(f"Cause: {details['cause']}\n")
    print("Recommended Fixes:")
    

    for i, fix in enumerate(details['remediation'], 1):
        print(f"{i}. {fix}")
    print("============================")

if __name__ == "__main__":
    run()
