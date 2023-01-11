from manim import *

class parte1(Scene):

    def construct(self):
        
        #1: MOSTRAR TÍTULO Y LOGO DE MANIM
        titulo1 = Title("Valencia EBAU Junio 2019. B3").shift(DOWN)
        self.play(Create(titulo1))
     

        
        #2: PRIMERA EXPLICACIÓN SOBRE EL USO DE TRACKERS
        texto1 = Tex("Las coordenadas iniciales de los puntos $A$ y $B$ \nson $(0,0)$ y $(250, 0)$")
        texto1.scale(0.75)
        self.play(FadeIn(texto1), run_time=1)
        self.wait(2)
        #self.play(FadeOut(texto1), run_time=0.2)
        
        texto2 = Tex("Vamos a situar ambos puntos en los ejes de coordenadas")
        texto2.scale(0.75)
        self.play(Transform(texto1, texto2), run_time=1)
        self.wait(1)
        self.play(Unwrite(titulo1))
        self.play(FadeOut(texto1), run_time=0.2)
        
        def calcula_distancia(puntoA, puntoB):
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
            
        

        ax = Axes(
            x_range=[0, 250, 10],
            y_range=[0, 190, 10],
            tips = False,
            axis_config={"include_numbers": False},
        )
        
        self.play(Create(ax))
        self.wait(1)
        
        decimal_tiempo = DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=False,
            unit="  segundos"
            
        )
        
        decimal_tiempo.add_updater(lambda d: d.set_value(tracker.get_value()))
        self.add(decimal_tiempo)
        decimal_tiempo.shift(2*UP)
        
        tiempo_txt=Tex("Tiempo:")
        tiempo_txt.move_to(decimal_tiempo).shift(3*LEFT)
        self.add(tiempo_txt)
        
       
        #mostrar la distancia
        decimal_distancia= DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=False,
            unit="  unidades"
            
        )
        
       
        
        
        #Definir el tracker y darle un valor de partida
        tracker = ValueTracker(0)
        
        #construimos el punto A
        puntoA = [ax.coords_to_point(0, tracker.get_value())]
        #construimos el vector de A
        vectorA = Vector([0, 2, 0], color=RED)
        #Creamos un objeto dibujable dot
        dotA = Dot(radius=0.09, point=puntoA, color=RED)
        
      
        
        dotA.add_updater(lambda x: x.move_to(ax.c2p(0, 30*tracker.get_value())))
        vectorA.add_updater(lambda x: x.move_to(ax.c2p(0, 30*tracker.get_value())).shift(UP))
       

        
        #construimos el punto B
        puntoB = [ax.coords_to_point(250, 0)]
        #construimos el vector de B
        vectorB = Vector([-2, 0, 0], color=BLUE)
        #Creamos un objeto dibujable dot
        dotB = Dot(radius=0.09, point=puntoB, color=BLUE)
        #dotB.add_updater(lambda x: x.move_to(ax.c2p(-30*tracker.get_value(), 0)))
       

        dotB.add_updater(lambda x: x.move_to(ax.c2p(250-40*tracker.get_value(), 0)))
        vectorB.add_updater(lambda x: x.move_to(dotB).shift(LEFT))
        
        #Calculo de la distancia entre los puntos y mostrala en pantalla 
        decimal_distancia.add_updater(lambda d: d.set_value(calcula_distancia(dotB, dotA)))
        self.add(decimal_distancia)
        decimal_distancia.shift(UP)
        
        distancia_txt=Tex("Distancia:")
        distancia_txt.move_to(decimal_distancia).shift(3*LEFT)
        self.add(distancia_txt)
        
        def dibujar_linea():         
            dashed_line = DashedLine(
                dotA, 
                dotB, 
                dash_length=0.06,
                color=GREEN,
                stroke_width=10)

            return dashed_line
        
        
       
        
        

        dashed_line = always_redraw(dibujar_linea)
        
        
    
        
        self.play(Create(dotA))
        self.wait(1)
        self.play(Create(dotB))
        self.play(Create(vectorA), Create(vectorB))
        self.wait(1)
        self.play(Create(dashed_line))
        self.play(tracker.animate.set_value(6.25), run_time=5, interpolation="linear")
       
        self.wait(1)
        self.play(tracker.animate.set_value(0), run_time=5, interpolation="linear")
        self.wait(1)
        self.play(tracker.animate.set_value(6.25), run_time=2, interpolation="linear")
        self.wait(1)
        self.play(tracker.animate.set_value(3.2), run_time=3, interpolation="linear")
        self.wait(1)
        self.play(tracker.animate.set_value(0), run_time=3, interpolation="linear")
        
        
        
        
        
        
        
     