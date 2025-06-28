import openai

# Your Together API credentials
openai.api_key = "a083f657d0e087535effc17a3123afda72af0466de229b2615c78efbe2625032"
openai.api_base = "https://api.together.xyz/v1"

def load_raw_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def spin_chapter(content):
    prompt = f"""
You are an AI Writer. Rewrite the following literary chapter to preserve its original meaning, tone, and storytelling, but modernize the language slightly and make it more engaging for a younger audience. Keep the story detailed and accurate.

--- START TEXT ---
{content}
--- END TEXT ---
"""

    response = openai.ChatCompletion.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2048  # Adjust based on your content length
    )
    
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    raw_text = load_raw_text("outputs/raw_chapter.txt")
    rewritten = spin_chapter(raw_text)

    output_path = "outputs/version_1_ai_writer.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten)

    print(f"✅ AI Writer output saved to {output_path}")

