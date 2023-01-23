from manim import *

from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

class parte1(VoiceoverScene):

    def construct(self):
        self.set_speech_service(RecorderService())
        #1: MOSTRAR TÍTULOls
        
        titulo1 = Title("Valencia EBAU Junio 2019. B3").shift(DOWN)
        
        with self.voiceover(text="Valencia, ebau, Junio de 2019. Ejercicio B3") as tracker:
            self.play(Create(titulo1))
        
        #2: REFERENCIA ENUNCIADO
        texto1 = Tex("Las coordenadas iniciales de los puntos $A$ y $B$ \nson $(0,0)$ y $(250, 0)$")
        texto1.scale(0.75)
        texto1.shift(UP)
        
        with self.voiceover(text="Las coordenadas iniciales de los puntos A y B son cero cero y 250 cero") as tracker:
            self.play(FadeIn(texto1), run_time=1)
        
    
        texto2 = Tex("Vamos a situar ambos puntos en los ejes de coordenadas")
        texto2.scale(0.75)
        texto2.shift(UP)
        with self.voiceover(text="Empezaremos por situar ambos puntos en los ejes de coordenadas") as tracker:
            self.play(Transform(texto1, texto2), run_time=1)
        
        self.play(Unwrite(titulo1), FadeOut(texto1))
        
        
        #FUNCIÓN QUE CALCULA LA DISTANCIA EUCLIDIA EN PANTALLA DE DOS OBJETOS DOT
        def calcula_distancia2(puntoA, puntoB):
            """ 
             Return euclidean distance between points p and q
                assuming both to have the same number of dimensions
             """
            # sum of squared difference between coordinates
            s_sq_difference = (puntoA.get_x()-puntoB.get_x())**2
            s_sq_difference += (puntoA.get_y()-puntoB.get_y())**2
            s_sq_difference += (puntoA.get_z()-puntoB.get_z())**2
    
            # take sq root of sum of squared difference
            distance = s_sq_difference**0.5
            return distance
        
        def calcula_distancia(p, q):
            """ 
             Return euclidean distance between points p and q
                assuming both to have the same number of dimensions
             """
            # sum of squared difference between coordinates
            s_sq_difference = (p[0]-q[0])**2
            s_sq_difference += (p[1]-q[1])**2
    
            # take sq root of sum of squared difference
            distance = s_sq_difference**0.5
            return distance
            
        
        #ejes
        ax = Axes(
            x_range=[0, 250, 10],
            y_range=[0, 190, 10],
            tips = False,
            axis_config={"include_numbers": False},
        )
        #El tiempo en patalla
        decimal_tiempo = DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=False,
            unit="s"
            
        )
        decimal_tiempo.shift(2*UP)
        tiempo_txt=Tex("Tiempo:")
        tiempo_txt.move_to(decimal_tiempo).shift(2*LEFT)
        
        #Distancia en pantalla
        decimal_distancia= DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=False,
            unit="  u.l."
            
        )
        decimal_distancia.shift(UP)
        distancia_txt=Tex("Distancia:")
        distancia_txt.move_to(decimal_distancia).shift(2*LEFT)
        
        #Definir el tracker y darle un valor de partida
        trackerAnimacion = ValueTracker(0)
        
        
        
        
       
        
        #PUNTO A
        puntoA = [ax.coords_to_point(0, trackerAnimacion.get_value())]
        #construimos el vector de A
        vectorA = Vector([0, 1, 0], color=RED)
        #Creamos un objeto dibujable dot
        dotA = Dot(radius=0.09, point=puntoA, color=RED)
        textoA=Tex("30 km/h")
    
        dotA.add_updater(lambda x: x.move_to(ax.c2p(0, 30*trackerAnimacion.get_value())))
        vectorA.add_updater(lambda x: x.move_to(ax.c2p(0, 30*trackerAnimacion.get_value())).shift(UP/2))
        textoA.move_to(dotA).shift(0.5*UP, 1.5*RIGHT)
       

        #PUNTO B
        puntoB = [ax.coords_to_point(250, 0)]
        #construimos el vector de B
        vectorB = Vector([-1, 0, 0], color=BLUE)
        #Creamos un objeto dibujable dot
        dotB = Dot(radius=0.09, point=puntoB, color=BLUE)
        textoB=Tex("40 km/h")
        textoB.move_to(dotB).shift(0.5*UP)

        dotB.add_updater(lambda x: x.move_to(ax.c2p(250-40*trackerAnimacion.get_value(), 0)))
        vectorB.add_updater(lambda x: x.move_to(dotB).shift(LEFT/2))
        
        
        
        def dibujar_linea():         
            dashed_line = DashedLine(
                dotA, 
                dotB, 
                dash_length=0.06,
                color=GREEN,
                stroke_width=10)

            return dashed_line
        
        dashed_line = always_redraw(dibujar_linea)
        
        
        #ANIMACIÓN GRÁFICO
        
        self.play(Create(ax))
        self.wait(1)
        
        self.add(dotA)
        with self.voiceover(text="Como hemos dicho antes el punto A se sitúa en cero cero") as tracker:
            self.play(FocusOn(dotA, color=RED, opacity=0.5))
        
        
        
        self.wait(1)
        
        self.add(dotB)
        with self.voiceover(text="Y sabemos que el punto B se sitúa en 250 0") as tracker:
            self.play(FocusOn(dotB, color=BLUE, opacity=0.5))
        
        
        with self.voiceover(text="Cada uno de ellos se mueve con una velocidad distinta") as tracker:
            self.play(Create(vectorA), Create(vectorB), Create(textoA), Create(textoB))
        
        
        self.wait(1)
        self.play(Unwrite(textoA), Unwrite(textoB))
        
        
        decimal_tiempo.add_updater(lambda d: d.set_value(trackerAnimacion.get_value()))
        with self.voiceover(text="Pongamos un reloj para poder activar la animación") as tracker:
            self.play(Write(tiempo_txt), Create(decimal_tiempo))
        
        #Cálculo de la distancia entre los puntos y mostrarla en pantalla 
        decimal_distancia.add_updater(lambda d: d.set_value(calcula_distancia([250-40*trackerAnimacion.get_value(), 0], [0, 30*trackerAnimacion.get_value()])))
        with self.voiceover(text="Y mostremos también la distancia entre los dos puntos en cada momento") as tracker:
            self.play(Write(distancia_txt), Create(decimal_distancia), Create(dashed_line))

        with self.voiceover(text="Ahora observa cómo se desplazan los móviles a medida que el tiempo avanza") as tracker:
            self.play(trackerAnimacion.animate.set_value(6.25), FadeOut(vectorA), FadeOut(vectorB), run_time=5, rate_func=smooth)
       
        
        with self.voiceover(text="Y observa la posición final de los móviles.") as tracker:
            self.wait(1)
        
        with self.voiceover(text="Volvamos ahora al punto de partida") as tracker:
            self.play(trackerAnimacion.animate.set_value(0), run_time=4, rate_func=smooth)
   

        with self.voiceover(text="Y veamos el movimiento de ida y vuelta") as tracker:
            self.play(trackerAnimacion.animate.set_value(6.25), run_time=3, rate_func=there_and_back)
        
        with self.voiceover(text="Buscamos ese momento en el que la distancia entre ambos móviles es mínima") as tracker:
            self.play(trackerAnimacion.animate.set_value(3.25), FadeIn(vectorA), FadeIn(vectorB), run_time=4, rate_func=smooth)
        
        with self.voiceover(text="¿Cuándo estarán más cerca?") as tracker:
            self.play(trackerAnimacion.animate.set_value(5), FadeOut(vectorA), FadeOut(vectorB), run_time=4, rate_func=there_and_back)
        
        with self.voiceover(text="Ese es el objetivo del problema, encontrar el momento en que la distancia entre ambos móviles es mínima") as tracker:
            self.play(trackerAnimacion.animate.set_value(6.25), run_time=4, rate_func=there_and_back)
        
        self.play(trackerAnimacion.animate.set_value(0), run_time=4, rate_func=smooth)
        self.wait(3)
        
        
        
        
        
     