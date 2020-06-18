import speech_recognition as sr
import webbrowser as wb
r1=sr.Recognizer()
r2=sr.Recognizer()
with sr.Microphone() as source:
    print('Speak Now')
    audio=r1.listen(source)
try:
    if 'search' in r1.recognize_google(audio):
        print(r1.recognize_google(audio))
        url='https://www.google.com/'
        with sr.Microphone() as source:
            print('Search google')
            audio = r2.listen(source)
        print('p')
        get = r2.recognize_google()
        print(get)
        print(url+get)
        #wb.get().open_new(url + get)
    else:
        print('GO')
        print(r1.recognize_google())

except Exception:
    print('Something went wrong')



'''
import speech_recognition as sr
r1=sr.Recognizer()
filename='Recording.wav'
with sr.Microphone() as source:
    print('Speak Now')
    audio=r1.listen(source)
try:
    print(r1.recognize_google(audio))
except Exception:
    print('Something went wrong')
'''
