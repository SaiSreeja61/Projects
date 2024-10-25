from tkinter import *
from nltk.chat.util import Chat, reflections
import requests  # To fetch weather data from API

# Define pairs and reflections for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a bot. You can call me Crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You?",]
    ],
    [
        r"I'm also good",
        ["How can I help you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you? :)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, seriously you're asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["A person created me using Python's NLTK library", "top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ["Nagpur, Maharashtra",]
    ],
    [
        r"how is weather in (.*)?",
        ["Fetching weather for %1...",]
    ],
    [
        r"(.*) raining in (.*)",
        ["No rain here in %2", "It's raining too much in %2!"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy!",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a fan of Football!",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messi", "Ronaldo", "Rooney"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit",
        ["Bye, take care! See you soon :)", "It was nice talking to you, goodbye! :)"]
    ],
]

# Weather API function
def get_weather(city_name):
    api_key = "b61ed19db20e808f94a13ce93643bf72"  # Your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

    try:
        # Make API request to get weather data
        response = requests.get(complete_url)
        data = response.json()

        # Check if the response contains valid data
        if data["cod"] == 200:  # Code 200 means successful API response
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temperature = main["temp"]

            return f"The weather in {city_name} is {weather_desc} with a temperature of {temperature}°C."
        else:
            # If the city is not found or other error
            return f"City {city_name} not found. Please check the spelling or try another city."
    except:
        # In case of any other errors (like connectivity issues)
        return "Could not fetch the weather at this time."

# Define tkinter GUI elements
class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.txt = Text(master)
        self.txt.grid(row=0, column=0, columnspan=2)

        self.e = Entry(master, width=100)
        self.e.grid(row=1, column=0)

        self.send_btn = Button(master, text="Send", command=self.send)
        self.send_btn.grid(row=1, column=1)

    def send(self):
        user_input = self.e.get().lower()
        self.txt.insert(END, "\nYou -> " + user_input)
        response = self.chatbot_response(user_input)
        self.txt.insert(END, "\nBot -> " + response)
        self.e.delete(0, END)

    def chatbot_response(self, user_input):
        chat = Chat(pairs, reflections)

        # Check for weather-related queries
        if "weather in" in user_input:
            city_name = user_input.split("in")[-1].strip()  # Extract city name and remove any spaces
            return get_weather(city_name)
        else:
            return chat.respond(user_input)

# Run the tkinter application
def main():
    root = Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
