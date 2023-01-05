
from datetime import date
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pyttsx3 as p
import speech_recognition as sr


today = date.today()
current_date = today.strftime("%B %d, %Y")
current_day = today.strftime("%A")

text = ""

r = sr.Recognizer() 
AI = p.init()
rate = AI.getProperty('rate')
AI.setProperty('rate', 160)
voices = AI.getProperty('voices')
AI.setProperty('voice', voices[2].id)


def AI_Speak(txt):
   
    AI.say(txt)
    print("AI : " + txt)
    AI.runAndWait()

    
def play_youtube(query):
  
  options = webdriver.ChromeOptions()
  options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  url = "https://www.youtube.com/results?search_query="+query

  driver.maximize_window()
  driver.get(url)
  video= driver.find_element(by=By.ID, value=("video-title"))
  video.click()

def play_music(query):
  
  options = webdriver.ChromeOptions()
  options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  url = "https://music.youtube.com/search?q="+query

  driver.maximize_window()
  driver.get(url)
  music= driver.find_element(by=By.XPATH, value=('//*[@id="play-button"]/div/yt-icon'))
  music.click()
 
  

def user_speak():
    with sr.Microphone() as source:
      print("AI : listening...")
      try:
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("User : " + text)

        if "what" and "is" and "your" and "name" in text:
           AI_Speak("kontol")
           user_speak()

               
        elif "are " and "you " and "human" in text:
             AI_Speak("No, I am an artificial intelligence")
             user_speak()

        
        elif "who" and "created" in text:
               AI_Speak("I was created by student of President University, his name is Ida Bagus Wikananda")
               user_speak()

        elif "why" and " created" in text:
               AI_Speak("I was created to help you in your daily life")
               user_speak()
                
        elif "hello" in text:
               AI_Speak("Hai, I am lucia, your personal assistant")
               user_speak()

        elif "speak" and "English" in text:
               AI_Speak("Yes, I can speak English")
               user_speak()

        elif "speak" and "Indonesia" in text:
               AI_Speak("No, I can't speak Indonesia")
               user_speak()

        elif "how" and "do" and "you" and "feel" in text:
           AI_Speak("I'am feeling good sir, how about you? i hope you always in a good condition")
           user_speak()

        elif  "play" and "video" in text:
           AI_Speak("yes, what video sir?")
           user_speak2()
           
        elif "play" and "music" in text:
           AI_Speak("ok, what music sir?")
           user_speak3()
        elif  "day"  in text:
           AI_Speak("today is "+current_day)
           user_speak()

        elif "date"  in text:
           AI_Speak("today is "+current_date)
           user_speak()
                 
        elif "weather" in text:
           AI_Speak("Wait a second, I'm checking the weather")
           check_weather()
           user_speak()

        elif"login" and "to" and "Facebook" in text:
             AI_Speak("ok, i will login to your facebook, but before that please fill completly your account with your username and password")
             AI_Speak("first, please enter your facebook username")
             username=input("Please enter your facebook username : ")
             AI_Speak("ok, now please enter your facebook password")
             password=input("Please enter your facebook password : ")
             AI_Speak("Thank you for entering your facebook username and password, now i will login to your facebook, here you go")
             login_to_facebook(username,password)
      
        elif "find" and "price" and "item" in text:
               AI_Speak("ok, what item sir?")
               find_item_price_list()
        

        elif "thank" and "you" in text:
           AI_Speak("your welcome sir")
           user_speak()

        elif "bye" in text:
             AI_Speak("Bye, have a nice day")
            
                    
        else:
           AI_Speak("I don't understand")
           user_speak() 

      except:
          
          AI_Speak("I can't hear your voice, would you repeat it?")
          user_speak()
         
  
     



def user_speak2():
    with sr.Microphone() as source:
       print("AI : listening...")
       try:
        r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source)
        text = r.recognize_google(audio)
       except:
        AI_Speak("Can you repeat it ?, your voice is no clear")
        user_speak2()
    print("User : "+text)
    AI_Speak(text+" Play in YouTube, enjoy the video")
    play_youtube(text)

def user_speak3():
    with sr.Microphone() as source:
       print("AI : listening...")
       try:
        r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source)
        text = r.recognize_google(audio)
       except:
        AI_Speak("Can you repeat it ?, your voice is no clear")
        user_speak3()
    print("User : "+text)
    AI_Speak(text+" Play in YouTube Music, enjoy the music")
    play_music(text)

def login_to_facebook(name,passw):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    driver.find_element(by=By.XPATH, value=('//*[@id="email"]')).click()
    driver.find_element(by=By.XPATH, value=('//*[@id="email"]')).send_keys(name)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=('//*[@id="pass"]')).click()
    driver.find_element(by=By.XPATH, value=('//*[@id="pass"]')).send_keys(passw)
    time.sleep(2)
    driver.find_element(by=By.NAME, value=("login")).click()


    
def check_weather():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.com/search?q=weather ")
    txt_temperature= driver.find_element(by=By.ID, value=("wob_tm")).text
    txt_weather= driver.find_element(by=By.ID, value=("wob_dc")).text
    location = driver.find_element(by=By.XPATH, value=('//*[@id="wob_loc"]')).text
    
    AI_Speak("The weather in "+location+" is currently " +txt_weather+" and the temperature is "+txt_temperature+" degrees celcius")

def find_item_price_list():
   with sr.Microphone() as source:
       print("AI : listening...")
       try:
        r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source)
        text = r.recognize_google(audio)
       except:
        AI_Speak("Can you repeat it ?, your voice is no clear")
        find_item_price_list()
   print("User : "+text)
   AI_Speak("Searching for price list of "+text+" in Tokopedia")
   options = webdriver.ChromeOptions()
   options.add_experimental_option("detach", True)
   driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
   driver.maximize_window()
   driver.get("https://www.tokopedia.com/search?st=product&q="+text)


AI_Speak("hello sir, i am your personal assistant, i can help you to do many things, what can i do for you?")
user_speak()







