class Communication:
    def speak(self):
        print(" speaks")

class Human(Communication):
    def speak(self, language):
        print(" speaks ", language)
        return language

class Alien(Communication):
    def speak(self):
        print(" speaks something indecipherable")

kira = Human()
kira.speak("Japanese")      

Loki = Alien()
Loki.speak()


