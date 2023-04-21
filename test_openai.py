import openai

openai.api_key = "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"
prompt = """def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)


# test case
def 
"""
output= openai.Completion.create(engine='code-cushman-001',\
                                      prompt=prompt, max_tokens=200)

print(output.choices[0].text)