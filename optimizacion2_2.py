from manim import *


class optimizacion2(Scene):

    def construct(self):
    
        
        #variables para las medidas de la escena        
        pixel_height = config["pixel_height"]  #  1080 is default
        pixel_width = config["pixel_width"]  # 1920 is default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        
        
        #el hilo del que hacemos partes
        hilo = Line((frame_width-1) * LEFT / 2, (frame_width-1) * RIGHT / 2)
        self.play(Create(hilo))
        texto_hilo=Tex("140 metros").next_to(hilo, UP)
        texto_hilo.shift(UP)
        self.play(Create(texto_hilo))
        
        
        
        #Definir el tracker que gestionará la animacion
        trackerAnimacion = ValueTracker(frame_width/10)
        
        #extremos del hilo         
        puntoA=[(frame_width-1)/2, 0, 0]
        puntoB=[-(frame_width-1)/2, 0, 0]
        
        #límites de los tres trozos
        puntoC = [-((frame_width-1)/2-trackerAnimacion.get_value()), 0, 0]
        puntoD = [-((frame_width-1)/2-3*trackerAnimacion.get_value()), 0, 0]
        
        puntoE = [-((frame_width-1)/2-2*trackerAnimacion.get_value()), 0, 0]
        
        
        dotA = Dot(radius=0.09, point=puntoA, color=RED)        
        dotB = Dot(radius=0.09, point=puntoB, color=RED)
        dotC = Dot(radius=0.09, point=puntoC, color=RED)
        dotD = Dot(radius=0.09, point=puntoD, color=RED)
        
        dotE = Dot(radius=0.09, point=puntoE, color=BLUE)
        
        dotC.add_updater(lambda x: x.move_to([-((frame_width-1)/2-trackerAnimacion.get_value()), 0, 0]))
        dotD.add_updater(lambda x: x.move_to([-((frame_width-1)/2-3*trackerAnimacion.get_value()), 0, 0]))
        dotE.add_updater(lambda x: x.move_to([-((frame_width-1)/2-2*trackerAnimacion.get_value()), 0, 0]))
       
        self.add(dotA)
        self.add(dotB)
        
        
        
        
    
        tramo1rotar1= Line(dotB, dotC, color=YELLOW, stroke_width=7)
        tramo1rotar2= Line(dotC, dotE, color=YELLOW, stroke_width=7)
        self.play(Create(tramo1rotar1))
        self.add(dotC)
        
        def dibujar_tramo1():         
            tramo = Line(
                dotB, 
                dotC, 
                color=YELLOW,
                stroke_width=7)
            texto=(Tex("x").next_to(tramo, UP))
            grupo=VGroup(tramo, texto)
            return grupo
        
        tramo1 = always_redraw(dibujar_tramo1)
        
        self.play(Create(tramo1))
        
        self.wait(1)
        
        self.play(
            Rotate(
                tramo1rotar1,
                angle=-PI,
                about_point=puntoC,
                rate_func=linear,
            )
        )
        self.add(dotE)
        self.add(tramo1rotar2)
        #tramo1rotar1.set_color(BLUE);
        self.wait(1)
        self.play(
            Rotate(
                tramo1rotar1,
                angle=-PI,
                about_point=puntoE,
                rate_func=linear,
            )
        )
        
        
        self.add(dotD)
        
        self.wait(1)
        
        
        
        
        
        
        def dibujar_tramo2():         
            tramo = Line(
                dotC, 
                dotD, 
                color=BLUE,
                stroke_width=7)
            texto=(Tex("2x").next_to(tramo, UP))
            grupo=VGroup(tramo, texto)
            return grupo
        
        tramo2 = always_redraw(dibujar_tramo2)
        self.play(Create(tramo2))
        
        self.remove(tramo1rotar1, tramo1rotar2)

        
        def dibujar_tramo3():         
            tramo = Line(
                dotD, 
                dotA, 
                color=GREEN,
                stroke_width=7)
            texto=(Tex("140-3x").next_to(tramo, UP))
            grupo=VGroup(tramo, texto)
            return grupo

        
        tramo3 = always_redraw(dibujar_tramo3)
        self.play(Create(tramo3))

             
        self.play(trackerAnimacion.animate.set_value(frame_width/6), run_time=4,  rate_func=there_and_back)
        
        d2 = Line(dotB, dotC, color=YELLOW, stroke_width=7)
        self.add(d2)
        
        d3 = Line(dotC, dotD, color=BLUE, stroke_width=7)
        self.add(d3)
        
        d4 = Line(dotD, dotA, color=GREEN, stroke_width=7)
        self.add(d4)
        
        #self.add(d2)
        #self.add(Text(str(pixel_height)).next_to(d2, RIGHT))
        
        def circulo2():         
            circulo = Square(trackerAnimacion.get_value()/4,
                color=YELLOW,
                stroke_width=7)
            circulo.next_to(tramo1, DOWN)
            return circulo
        
        c2=Square(trackerAnimacion.get_value()/4, color=YELLOW, stroke_width=7)
        c2.next_to(d2,DOWN)
        circ2 = always_redraw(circulo2)
        self.play(Transform(d2, c2))
        self.add(circ2)
        self.remove(d2)

        def circulo3():         
            circulo = Square(2*trackerAnimacion.get_value()/4,
                color=BLUE,
                stroke_width=7)
            circulo.next_to(tramo2, DOWN)
            return circulo
        
        c3=Square(2*trackerAnimacion.get_value()/4, color=BLUE, stroke_width=7)
        c3.next_to(d3,DOWN)
        circ3 = always_redraw(circulo3)
        self.play(Transform(d3, c3))
        self.add(circ3)
        self.remove(d3)
        
        def circulo4():         
            circulo = Square((frame_width-1-3*trackerAnimacion.get_value())/(4),
                color=GREEN,
                stroke_width=7)
            circulo.next_to(tramo3, DOWN)
            return circulo
        
        c4=Square((frame_width-1-3*trackerAnimacion.get_value())/(4), color=GREEN, stroke_width=7)
        c4.next_to(d4,DOWN)
        self.play(Transform(d4, c4))
        circ4 = always_redraw(circulo4)
        self.play(Transform(d4, c4))
        self.add(circ4)
        self.remove(d4)
        
        
        self.play(trackerAnimacion.animate.set_value(frame_width/6), run_time=4,  rate_func=there_and_back)
        
        self.wait(5)