import pyttsx3
from django.http import JsonResponse
import speech_recognition as sr
import datetime
from .models import VoiceRegistration


def enroll_voice(request):
    text = ''
    feedback = ''
    bot = pyttsx3.init()
    bot.setProperty("rate", 178)
    voices = bot.getProperty('voices')
    bot.setProperty('voice', voices[11].id)
    bot.say("You are welcome. Please say something, you have five seconds")
    bot.runAndWait()
    speak = sr.Recognizer()
    with sr.Microphone(device_index=4) as source:
        try:
            speak.adjust_for_ambient_noise(source)
            audio = speak.listen(source, timeout=5)
            text = speak.recognize_google(audio)
            print("{}".format(text))
            res = create_voice(request, text)
            print(res)
        except NameError:
            print("Invalid request")
            res = "Invalid"
    return JsonResponse(res, safe=False)


def create_voice(request, text):
    if request.method == 'POST':
        form = request.POST
        save_record = VoiceRegistration()
        save_record.username = form.get('username')
        save_record.voice = text
        save_record.date_time = datetime.datetime.now()
        save_record.save()
        feedback = {
            'status': 'success',
            'msg': 'Your voice was registered successfully',
            'text': text
        }
    else:
        feedback = {
            'status': 'Invalid request',
            'msg': 'Your voice was invalid, please try again.',
        }
    return feedback
