import win32com.client
import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import openai

def ai(prompt):
    openai.api_key = os.getenv("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")
    text = f"OpenAI response for Prompt: {prompt} \n*********\n\n"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="prompt",
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response["choices"][0]["text"])
    if not os.path.exists("Openai"):
        os.makedirs("Openai")

    with open(f"prompt- {random.randint(1, 23443212)}", "w") as f:
        f.write(text)

speaker = win32com.client.Dispatch("SAPI.SpVoice")
def say(text):
    os.system(f"say {text}")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except Exception:
            return "Some Error Occurred . Sorry from Om"
if __name__ == '__main__':
    speaker.Speak("Hello I Am Parita AI")
    while True:
        print("Listening")
        query = takecommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"], ["facebook", "https://www.facebook.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

        songs = [["tere vaste", "https://www.youtube.com/watch?v=X7WXHhokylc&ab_channel=SaregamaMusic"], ["senorita", "https://www.youtube.com/watch?v=Pkh8UtuejGw&ab_channel=ShawnMendesVEVO"]]
        for song in songs:
            if f"Play {song[0]}".lower() in query.lower():
                speaker.Speak(f"Playing {song[0]} Sir...")
                webbrowser.open(song[1])

            if"the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                minute = datetime.datetime.now().strftime("%M")
                second = datetime.datetime.now().strftime("%S")
                speaker.Speak(f"Sir the time is {hour}bajjke {minute}minutees aur {second}seconds huve he ")
                break
            #if "play video".lower() in query.lower():
                #os.system(f"open C:\Users\Om\Videos\Captures")

            if "using AI".lower() in query.lower():
                ai(prompt=query)
        #speaker.Speak(text)