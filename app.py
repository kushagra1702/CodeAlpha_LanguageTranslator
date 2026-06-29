
        from deep_translator import GoogleTranslator

languages = {
    "0": ("Auto Detect", "auto"),
    "1": ("English", "en"),
    "2": ("Hindi", "hi"),
    "3": ("French", "fr"),
    "4": ("Spanish", "es"),
    "5": ("German", "de"),
    "6": ("Japanese", "ja"),
    "7": ("Chinese", "zh-CN")
}

translation_count = 0

print("=" * 55)
print("🌍 CodeAlpha Language Translator v1.1")
print("=" * 55)

while True:

    print("\nAvailable Languages:")
    for key, value in languages.items():
        print(f"{key}. {value[0]}")

    source_choice = input("\nChoose source language (number): ")
    target_choice = input("Choose target language (number): ")

    if source_choice not in languages or target_choice not in languages:
        print("\n❌ Invalid language selection.\n")
        continue

    text = input("\nEnter text to translate:\n")

    try:
        source_lang = languages[source_choice][1]
        target_lang = languages[target_choice][1]

        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        translation_count += 1

        print("\n" + "=" * 55)
        print("✅ Translation Successful")
        print("=" * 55)
        print("Original Text : ", text)
        print("Translated Text : ", translated)

        with open("history.txt", "a", encoding="utf-8") as file:
            file.write("=" * 55 + "\n")
            file.write(f"Translation #{translation_count}\n")
            file.write(f"Source Language : {languages[source_choice][0]}\n")
            file.write(f"Target Language : {languages[target_choice][0]}\n")
            file.write(f"Original Text : {text}\n")
            file.write(f"Translated Text : {translated}\n")
            file.write("=" * 55 + "\n\n")

    except Exception as e:
        print("\n❌ Translation Failed")
        print(e)

    again = input("\nTranslate another sentence? (y/n): ").lower()

    if again != "y":
        break

print("\n" + "=" * 55)
print("🙏 Thank you for using CodeAlpha Language Translator!")
print(f"📊 Total translations this session: {translation_count}")
print("📝 Translation history saved in history.txt")
print("=" * 55)