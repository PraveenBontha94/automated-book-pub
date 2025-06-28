def load_reviewed_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def edit_text_interactively(text):
    print("\n📖 Reviewed Output:\n")
    print("=" * 50)
    print(text)
    print("=" * 50)

    choice = input("\nDo you want to make manual edits? (y/n): ").strip().lower()
    if choice == 'y':
        print("\n✍️ Please enter your edited version below. (End input with an empty line):\n")
        lines = []
        while True:
            line = input()
            if not line.strip():
                break
            lines.append(line)
        return "\n".join(lines)
    else:
        print("✅ Using reviewed version as final.")
        return text

def save_final_version(content, path="outputs/version_3_final.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ Final version saved at {path}")

if __name__ == "__main__":
    reviewed = load_reviewed_text("outputs/version_2_ai_reviewer.txt")
    final_version = edit_text_interactively(reviewed)
    save_final_version(final_version)

