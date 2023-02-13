from manim import *



class optimizacion2(Scene):

    def construct(self):
    
        
        #self.play(Create(linia))
        
        
        pixel_height = config["pixel_height"]  #  1080 is default
        pixel_width = config["pixel_width"]  # 1920 is default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        
        
       
        d1 = Line((frame_width-1) * LEFT / 2, (frame_width-1) * RIGHT / 2)
        self.play(Create(d1))
        self.add(Text(str(pixel_width)).next_to(d1, UP))
        
        
        
        #Definir el tracker y darle un valor de partida
        trackerAnimacion = ValueTracker(frame_width/10)
        
        #ejes
        ax = Axes(
            x_range=[0, 250, 10],
            y_range=[0, 190, 10],
            tips = False,
            axis_config={"include_numbers": False},
        )
        
        #PUNTO A
        
        puntoA=[(frame_width-1)/2, 0, 0]
        puntoB=[-(frame_width-1)/2, 0, 0]
        
        
        #Creamos un objeto dibujable dot
        dotA = Dot(radius=0.09, point=puntoA, color=RED)
        self.add(dotA)
        
        dotB = Dot(radius=0.09, point=puntoB, color=RED)
        self.add(dotB)
        
        
        puntoC = [-((frame_width-1)/2-trackerAnimacion.get_value()), 0, 0]
        dotC = Dot(radius=0.09, point=puntoC, color=RED)
        dotC.add_updater(lambda x: x.move_to([-((frame_width-1)/2-trackerAnimacion.get_value()), 0, 0]))
        
        
        self.add(dotC)
        
        puntoD = [-((frame_width-1)/2-3*trackerAnimacion.get_value()), 0, 0]
        dotD = Dot(radius=0.09, point=puntoD, color=RED)
        dotD.add_updater(lambda x: x.move_to([-((frame_width-1)/2-3*trackerAnimacion.get_value()), 0, 0]))
        self.add(dotD)
        
        def dibujar_tramo1():         
            tramo = Line(
                dotB, 
                dotC, 
                color=YELLOW,
                stroke_width=10)
            texto=(Tex("x").next_to(tramo, UP))
            grupo=VGroup(tramo, texto)
            return grupo
        
        tramo1 = always_redraw(dibujar_tramo1)
        self.play(Create(tramo1))
        

        
        
        def dibujar_tramo2():         
            tramo = Line(
                dotC, 
                dotD, 
                color=BLUE,
                stroke_width=10)
            texto=(Tex("2x").next_to(tramo, UP))
            grupo=VGroup(tramo, texto)
            return grupo
        
        tramo2 = always_redraw(dibujar_tramo2)
        self.play(Create(tramo2))
      
        #self.add(Tex("2x").next_to(tramo2, UP))
        
        def dibujar_tramo3():         
            tramo = Line(
                dotD, 
                dotA, 
                color=GREEN,
                stroke_width=10)
            texto=(Tex("y").next_to(tramo, UP))
            grupo=VGroup(tramo, texto)
            return grupo

        
        tramo3 = always_redraw(dibujar_tramo3)
        self.play(Create(tramo3))
        
        #self.add(Tex("y").next_to(tramo3,UP))
        
        
        self.play(trackerAnimacion.animate.set_value(frame_width/6), run_time=4,  rate_func=there_and_back)
        
        d2 = Line(dotB, dotC, color=YELLOW, stroke_width=10)
        self.add(d2)
        
        d3 = Line(dotC, dotD, color=BLUE, stroke_width=10)
        self.add(d3)
        
        d4 = Line(dotD, dotA, color=GREEN, stroke_width=10)
        self.add(d4)
        
        #self.add(d2)
        #self.add(Text(str(pixel_height)).next_to(d2, RIGHT))
        
        def circulo2():         
            circulo = Circle(radius=trackerAnimacion.get_value()/(2*PI),
                color=YELLOW,
                stroke_width=10)
            circulo.next_to(tramo1, DOWN)
            return circulo
        
        c2=Circle(trackerAnimacion.get_value()/(2*PI), color=YELLOW, stroke_width=10)
        c2.next_to(d2,DOWN)
        circ2 = always_redraw(circulo2)
        self.play(Transform(d2, c2))
        self.add(circ2)
        self.remove(d2)
        
        def circulo3():         
            circulo = Circle(radius=2*trackerAnimacion.get_value()/(2*PI),
                color=BLUE,
                stroke_width=10)
            circulo.next_to(tramo2, DOWN)
            return circulo
        
        c3=Circle(2*trackerAnimacion.get_value()/(2*PI), color=BLUE, stroke_width=10)
        c3.next_to(d3,DOWN)
        circ3 = always_redraw(circulo3)
        self.play(Transform(d3, c3))
        self.add(circ3)
        self.remove(d3)
        
        def circulo4():         
            circulo = Circle((frame_width-1-3*trackerAnimacion.get_value())/(2*PI),
                color=GREEN,
                stroke_width=10)
            circulo.next_to(tramo3, DOWN)
            return circulo
        
        c4=Circle((frame_width-1-3*trackerAnimacion.get_value())/(2*PI), color=GREEN, stroke_width=10)
        c4.next_to(d4,DOWN)
        self.play(Transform(d4, c4))
        circ4 = always_redraw(circulo4)
        self.play(Transform(d4, c4))
        self.add(circ4)
        self.remove(d4)
        
        
        self.play(trackerAnimacion.animate.set_value(frame_width/6), run_time=4,  rate_func=there_and_back)
        
        self.wait(5)