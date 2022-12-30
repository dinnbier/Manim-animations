from manim import *

class surfearCurva(MovingCameraScene):
    def construct(self):


         #1: MOSTRAR TÍTULO Y LOGO DE MANIM
        titulo1 = Title("Movimientos de cámara con Manim")
        titulo1.shift(DOWN)
        banner = ManimBanner()
        banner.scale(0.4)
        self.play(Create(titulo1), banner.create())
        self.play(banner.expand())
        self.wait(1)
        self.play(Unwrite(banner))
        
        #2: 
        texto1 = Text("El uso de cámaras en manim permite realizar\nanimaciones siguiendo el movimiento de objetos.")
        texto1.scale(0.75)
        
        self.play(FadeIn(texto1), run_time=6)
        
        #3: 
        texto2=Text("La función MoveAlongPath, permite por ejemplo,\nmover un objeto a lo largo de una gráfica.")
        texto2.scale(0.75)
        
        self.play(ReplacementTransform(texto1, texto2))
        
        #4:
        code1 = '''
            def update_curva(mob):
            mob.move_to(puntoAmover.get_center())
            self.camera.frame.add_updater(update_curva)
            self.play(
                MoveAlongPath(puntoAmover, curva, 
                rate_func=rate_functions.double_smooth), 
                run_time=7
            )'''
        rendered_code1 = Code(code=code1, tab_width=4, background="rectangle",
                            language="Python", font="Monospace").scale(0.8)
        rendered_code1.move_to(texto2).shift(2*DOWN)
        
        self.play(FadeIn(rendered_code1))
        self.wait(4);
        
        self.play(Unwrite(texto2), FadeOut(rendered_code1))
        
        #5:
        texto3=Text("El ejemplo siguiente muestra un punto \nmoviéndose a lo largo de un curva")
        texto3.scale(0.75)
        
        texto4=Tex(r"$f(x)=x^2$")
        texto4.shift(2*DOWN)
        texto4.scale(1.5)
        
        self.play(FadeIn(texto3), FadeIn(texto4))
        self.wait(4)
        
        self.play(FadeOut(texto3), FadeOut(texto4))
        self.play(Unwrite(titulo1))
        
        #6 BLOQUE CENTRAL DE ESTE EJEMPLO (Y EL MÁS IMPORTANTE)
    
        # Guardamos el estado original de la cámara para volver a él al final
        self.camera.frame.save_state()
    
        # Creación de los ejes
        ejes = Axes()
        ejes.shift(DOWN);
        
        #creación de la función x^2
        curva=ejes.plot(lambda x:x**2, x_range=[-2, 2]).set_color(BLUE_B)
    
        #i2gp Devuelve las coordenadas de un punto de la gráfica correspondiente al valor de x proporcionado. 
        #i2gp = "input to graph point" 
        puntoAmover= Dot(ejes.i2gp(-2, curva), color=YELLOW)

        self.play(Create(ejes), Create(curva))
        
        self.play(self.camera.frame.animate.scale(0.4).move_to(puntoAmover))
        
        #definición de la función "updater" asociada al frame. En cada frame se invocará. 
        def update_curva(mob):
            mob.move_to(puntoAmover.get_center())

        self.camera.frame.add_updater(update_curva)
        
        self.play(MoveAlongPath(puntoAmover, curva, rate_func=rate_functions.double_smooth), run_time=7)
        #self.play(puntoAmover.animate.set_color(BLUE_A)
        curva.reverse_points()
        self.play(self.camera.frame.animate.scale(2.5).move_to(puntoAmover))
        self.play(MoveAlongPath(puntoAmover, curva, rate_func=rate_functions.double_smooth), run_time=7)
        
        
        self.camera.frame.remove_updater(update_curva)
        

        # Restaurar a estado original
        # al final de la animacion
        self.play(Restore(self.camera.frame))
