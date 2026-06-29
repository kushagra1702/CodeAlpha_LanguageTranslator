from deep_translator import GoogleTranslator

languages = {
    "1": ("English", "en"),
    "2": ("Hindi", "hi"),
    "3": ("French", "fr"),
    "4": ("Spanish", "es"),
    "5": ("German", "de"),
    "6": ("Japanese", "ja"),
    "7": ("Chinese", "zh-CN")
}

print("=" * 50)
print("🌍 Welcome to CodeAlpha Language Translator")
print("=" * 50)

while True:
    print("\nAvailable Languages:")
    for key, value in languages.items():
        print(f"{key}. {value[0]}")

    source_choice = input("\nChoose source language (number): ")
    target_choice = input("Choose target language (number): ")

    if source_choice not in languages or target_choice not in languages:
        print("\n❌ Invalid language selection. Please try again.")
        continue

    text = input("\nEnter text to translate:\n")

    if text.strip() == "":
        print("\n❌ Text cannot be empty.")
        continue

    try:
        translated = GoogleTranslator(
            source=languages[source_choice][1],
            target=languages[target_choice][1]
        ).translate(text)

        print("\n" + "=" * 50)
        print("✅ Translation Successful")
        print("=" * 50)
        print(f"\nTranslated Text:\n{translated}")

    except Exception as e:
        print("\n❌ Translation Failed")
        print(e)

    again = input("\nDo you want to translate another sentence? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thank you for using CodeAlpha Language Translator!")
        break