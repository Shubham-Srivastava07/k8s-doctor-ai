import ollama

try:
    response = ollama.chat(model='gemma:2b', messages=[
        {'role':'user', 'content': 'Is k8s easy to learn?'}
    ])
    print(response['message']['content'])

except Exception as e:
    print(f"Error: {e}")
