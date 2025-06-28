import openai

openai.api_key = "a083f657d0e087535effc17a3123afda72af0466de229b2615c78efbe2625032"
openai.api_base = "https://api.together.xyz/v1"

def load_writer_output(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def review_chapter(content):
    prompt = f"""
You are an AI Reviewer. Carefully read the following rewritten literary chapter.

Your tasks:
1. Identify any unclear or awkward parts and rewrite them.
2. Ensure all sentences flow smoothly and naturally.
3. Keep the tone, meaning, and storyline intact.
4. Fix any grammar, punctuation, or clarity issues.

--- START TEXT ---
{content}
--- END TEXT ---

Now return the improved and reviewed version of this chapter.
"""

    response = openai.ChatCompletion.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=2048
    )
    
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    ai_writer_output = load_writer_output("outputs/version_1_ai_writer.txt")
    reviewed_output = review_chapter(ai_writer_output)

    output_path = "outputs/version_2_ai_reviewer.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(reviewed_output)

    print(f"✅ AI Reviewer output saved to {output_path}")

