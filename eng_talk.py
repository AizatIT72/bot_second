from langdetect import detect
while True:
    user = input()
    if detect(user) == 'en':
        print(f"Все хорошо! {user}")
    else:
        print("Общайтесь на английском")
    break