from googletrans import Translator

text = input("enter your text :-")



from_language = "en"


to_language = "ja"

translator = Translator()
google_translation = translator.translate(text, src=from_language, dest=to_language).text

print(google_translation)
