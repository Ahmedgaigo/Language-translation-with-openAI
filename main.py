import openai
from replit import clear
    
print("en = English\n fr = French\n sp = Spanish\nAt any moment, you can type stop to end")

openai.api_key = "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"


def translate(text, source_language, target_language):
    prompt = (f"translate {text} from {source_language} to {target_language}")
    completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)
    message = completions.choices[0].text
    return message

end = False
while not end:
    source_language = input("en or fr or sp: ").lower()
    if source_language == "stop":
        clear()
        break
        
    text = input("text: ").lower()
    if text == "stop":
        clear()
        break
        
    target_language = input("en or fr or sp: ").lower()
    if target_language == "stop":
        clear()
        break

    translated_text = translate(text,  source_language, target_language)
    print(f"\nYour {source_language} text:\n{text}")
    print(f"\nYour {target_language}: {translated_text}")
    again = input("\nagain? y/n: ")
    clear()
    if again == "n" or again == "stop":
        end = False
