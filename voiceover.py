from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MyAwesomeScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="es"))
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        with self.voiceover(text="Éste es un ejemplo de la PAU de 2019") as tracker:
            self.play(Create(circle))
