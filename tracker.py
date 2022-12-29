from manim import *

#About the use of the function always_redraw: 
#https://infograph.tistory.com/179

class tracker(Scene):

    def construct(self):
        
        #TÍTULO
        
        titulo1 = Title("Trackers en manim").shift(DOWN)
        banner = ManimBanner()
        banner.scale(0.4)
        
        self.play(Create(titulo1), banner.create())
        self.play(banner.expand())
        self.wait(1)
        self.play(Unwrite(banner))
        
        
        #PRIMERA EXPLICACIÓN
        
        texto1 = Text("El uso de trackers en manim permite realizar\nanimaciones complejas que logran\nefectos de movimiento notables.")
        texto1.scale(0.75)
        self.play(FadeIn(texto1), run_time=6)

        
        
        #TE VOY A MOSTRAR UN POCO DE CÓDIGO

        texto2=Text("Ésta es la llamada \nque se emplea para definir un tracker.")
        texto2.scale(0.75)
        self.play(ReplacementTransform(texto1, texto2))
        
        #MOSTRAMOS EL CÓDIGO DEL TRACKER
        code1 = '''
            class trackersEnEscena(Scene):
                 def construct(self):
                tracker = ValueTracker(1) '''
        
        rendered_code1 = Code(code=code1, tab_width=4, background="rectangle",
                            language="Python", font="Monospace")
        
        rendered_code1.move_to(texto2).shift(1.5*DOWN)
        self.play(FadeIn(rendered_code1))
        self.wait(3);
        self.play(Unwrite(texto2), FadeOut(rendered_code1))
    

        #ACLARACIÓN 1 SOBRE EL CÓDIGO
        
        texto3=Text("El tracker servirá como una variable que se modifica\ndurante la animación y a la que podemos acceder\npara actualizar el estado de diferentes objetos. ")
        texto3.scale(0.75)
        self.play(FadeIn(texto3))
        self.wait(3)
        
        #ACLARACIÓN 2 SOBRE EL CÓDIGO y MOSTRAMOS EL CÓDIGO 2 DEL TRACKER
        
        texto4=Text("La forma de acceder al valor que toma el tracker\nes usar la función 'get_value()' \ntal y como te mostramos a continuación:")
        texto4.scale(0.75)
        code2 = '''
                class trackersEnEscena(Scene):
                 def construct(self):
                    tracker = ValueTracker(1) 
                    tracker.get_value() '''
        
        rendered_code2 = Code(code=code2, tab_width=4, background="rectangle",
                            language="Python", font="Monospace")
        rendered_code2.move_to(texto4).shift(2*DOWN)
        
        self.play(ReplacementTransform(texto3, texto4), FadeIn(rendered_code2))
        self.wait(5)
        self.play(FadeOut(texto4), FadeOut(rendered_code2))
    
        
        #INTRODUCIMOS EL EJEMPLO
        
        texto5=Text("A continuación, vamos a ver un ejemplo \nde cómo emplear un tracker en una animación \nsobre el cálculo del mínimo de una función:")
        texto5.scale(0.75)
        self.play(Create(texto5))
        self.wait(5)
        self.play(FadeOut(texto5))
        
        #CONFIGURACIÓN DE LOS EJES
        ax = Axes(
            x_range=[-2, 10, 1],
            y_range=[-2, 5, 1],
            tips = False,
            axis_config={"include_numbers": False},
        )
        ax.scale(0.9).shift(DOWN)
        
        y_label = ax.get_y_axis_label("y")
        x_label = ax.get_x_axis_label("x")
        grid_labels = VGroup(x_label, y_label)
        titulo2 = Title(
            # spaces between braces to prevent SyntaxError
            r"Estudio del mínimo en la función $f(x)=x^2-6x+10$",
            include_underline=False,
            font_size=40,
        )
        titulo2.shift(DOWN)
        self.play(Unwrite(titulo1))
        self.play(Create(titulo2))
        
        
        
        
        #FUNCIÓN Y TRACKER
        #definimos la función a dibujar
        def func(x):
            return x**2-6*x+10
        def func2(x):
            return 2*x-6;
       
        #Configuración del punto y el tracker
        #Definir el tracker y darle un valor de partida
        tracker = ValueTracker(1)
        
        initial_point = [ax.coords_to_point(tracker.get_value(), func(tracker.get_value()))]
        #Creamos un objeto dibujable dot
        dot = Dot(radius=.15, point=initial_point, color=RED)
        #creamos una etiqueta que acompañará al punto
        label = MathTex("punto").add_updater(lambda m: m.next_to(dot, UP)).scale(0.7)
        
        #definimos coordenadas del punto inicial
       
        def get_tangent_line():
            line = Line(
                ORIGIN, 5 * RIGHT,
                color=RED,
                stroke_width=4,
            )
            dx = 0.0001
            x = tracker.get_value()
            #p0=ax.c2p(tracker.get_value()-dx, func(tracker.get_value()-dx))
            #p0 = np.array([x-dx,func(x-dx),0])
            #p1 = np.array([x, func(x), 0])
            p1=ax.c2p(tracker.get_value(), func(tracker.get_value()))
            #p2 = np.array([x + dx, func(x + dx), 0])
            p2=ax.c2p(tracker.get_value()+dx, func(tracker.get_value()+dx))

            angle = angle_of_vector(p2 - p1)
            line.rotate(angle)
            line.move_to(p1)

           
            return line
        
        line = always_redraw(get_tangent_line)
        
        #creamos un updater para que actualice al punto
        dot.add_updater(lambda x: x.move_to(ax.c2p(tracker.get_value(), func(tracker.get_value()))))
        quadratic = ax.plot(func, color=BLUE)
        tangent=TangentLine(quadratic, alpha=tracker.get_value(), color=YELLOW)
        tangent.add_updater(lambda m: m.move_to(ax.c2p(tracker.get_value(), func(tracker.get_value()))))
        linear = ax.plot(func2, color=RED)
    
        
        line_1 = ax.get_vertical_line(ax.input_to_graph_point(3, quadratic), color=YELLOW)
        line_2 = ax.get_horizontal_line(ax.input_to_graph_point(3, quadratic), color=YELLOW)
        
        
       
        
        self.play(Create(ax));
        self.play(Create(grid_labels));
        self.play(Uncreate(titulo2));
        self.play(Create(quadratic));
        self.play(Create(dot));
        self.play(Create(label));
        self.play(Create(line))
       
        
       
        #secuencia de movimientos del punto al cambiar los valores del tracker
        self.wait(0.2)
        self.play(tracker.animate.set_value(5)),
        self.wait(0.2)
        self.play(tracker.animate.set_value(1))
        self.wait(0.2)
        self.play(tracker.animate.set_value(4))
        self.wait(0.2)
        self.play(tracker.animate.set_value(2))
        self.wait(0.2)
        self.play(tracker.animate.set_value(3))
        self.play(FadeOut(line))
        
        self.play(Create(line_1, run_time=1))
        self.play(Create(line_2, run_time=1))
        self.wait(4)
        
      