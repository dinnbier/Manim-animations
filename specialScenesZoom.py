from manim import *


# ZoomedCamera

class zoomEcuacion(ZoomedScene):

    def construct(self):

        
        #1: 
        titulo1 = Title("ZoomedScene: haciendo zoom en una sección.").shift(DOWN)
        banner = ManimBanner()
        banner.scale(0.4)
        self.play(Create(titulo1), banner.create())
        self.play(banner.expand())
        self.wait(1)
        self.play(Unwrite(banner))
        
        #2: 
        texto1 = Text("El efecto de Zoom permite ampliar\nuna sección de la pantalla\nen un recuadro que puede moverse.")
        texto1.scale(0.75)
        self.play(FadeIn(texto1), run_time=6)
        
        #3: 
        texto2=Text("Para mostrar su uso emplearemos \nuna función cuadrática.")
        texto2.scale(0.75)
        self.play(ReplacementTransform(texto1, texto2))
        self.wait(1)
        
        self.play(FadeOut(texto2))
        
        #Dibujo de la parábola
        ax = Axes(
            x_range=[-2, 10, 1],
            y_range=[-2, 22, 1],
            tips = False,
            axis_config={"include_numbers": False},
        )
        cuadricula=number_plane = NumberPlane(
            x_range=[-2, 10, 1],
            y_range=[-2, 22, 1],
            x_length=5,
            y_length=5
        )
        #ax.scale(0.9).shift(DOWN)
        
        y_label = ax.get_y_axis_label("y")
        x_label = ax.get_x_axis_label("x")
        #grid_labels = VGroup(x_label, y_label)
        titulo2 = Title(
            # spaces between braces to prevent SyntaxError
            r"Estudio de la parábola $f(x)=2x^2-12x+20$",
            include_underline=False,
            font_size=40,
        )
        
        #definimos la función a dibujar
        def func(x):
            return 2*x**2-12*x+20
        
        quadratic =  ax.plot(func, color=BLUE)
        
        grafica=VGroup(quadratic,  ax)
        #grafica.move_to(ORIGIN)
        
        titulo2.shift(DOWN)
        self.play(Unwrite(titulo1))
        self.wait(1);
        self.play(Write(titulo2))
        self.wait(1);
        
        
        self.play(Unwrite(titulo2))
        self.play(Create(grafica[0]))
        self.play(Create(grafica[1]))
        self.wait(1);

        '''self.play(AnimationGroup(*[
            grafica.animate(lag_ratio=0.2, run_time=1.5).shift(DOWN)ç
        ]))'''
        
        
        
        #ECUACIÓN DE LA PARÁBOLA
        #lo define así, separado por comas para poder acceder como si fuera una array
        eq = MathTex("y ", " = ", " 2 ", " x ", " ^2 "," -12 ", " x ",  "+20").to_corner(UR).shift(DOWN)

        frame_text = Text("Frame", color=BLUE, font_size=26)
        zoomed_camera_text = Text("Zoomed frame", color=GREEN, font_size=26)

        self.play(Write(eq))
        

        #DEFINICIONES:
        
       
        #zoomed_camera: la camara que apunta a lo que queremos ampliar
        zoomed_camera = self.zoomed_camera
        #zoomed_display: el display donde se muestra la imagen de la cámara ampliada
        zoomed_display = self.zoomed_display

        #frame de la "zoomed_camara"
        frame = zoomed_camera.frame
        #frame del display 
        frame_zoom = zoomed_display.display_frame

        #apuntamos la cámara al lugar que queremos ampliar
        frame.move_to(eq[0])
        
        
        #Damos colores a los dos frames para distinguirlos
        #frame.set_color(GREEN)
        #frame_zoom.set_color(RED)
        
        #colocamos el display en el origen de coordenadas
        zoomed_display.move_to(ORIGIN).shift(2*LEFT, DOWN)
        
        #Movemos la gráfica para dejar espacio para el trabajo posterior
        self.play(grafica.animate.shift(4*UP, LEFT))
        
        #pegamos el texto del frame a éste
        frame_text.next_to(frame, UR).add_updater(lambda m: m.next_to(frame, UP))

        #creamos el frame y el texto
        self.play(Create(frame), FadeIn(frame_text, shift=UP))
        
        #PONE EN MARCHA EL ZOOM 
        self.activate_zooming()

        #GENERA LA ANIMACIÓN QUE HACE APARECER EL DISPLAY DEL ZOOM
        self.play(self.get_zoomed_display_pop_out_animation())

        #situamos el texto del zoom junto a éste
        zoomed_camera_text.next_to(frame_zoom, RIGHT)
        
        #hacemos aparecer el texto del zoom
        self.play(FadeIn(zoomed_camera_text, shift=UP))     


        #ESCALAMOS TANTO EL ZOOM COMO EL DISPLAY DEL ZOOM
        # Scale in      x   y  z
        scale_factor1 = [2, 2, 0]
        scale_factor2 = [1, 1, 0]
        self.play(
            frame.animate.scale(scale_factor1),
            zoomed_display.animate.scale(scale_factor2),
        )

        self.wait()

        texto = Text("Variable dependiente", font_size=28).next_to(frame_zoom, DOWN)
        #self.play(ScaleInPlace(zoomed_display, 1.1))
        self.play(Create(texto))
        self.wait()

        texto2 = Text("Coeficiente del término de mayor grado", font_size=28).next_to(frame_zoom, DOWN)
        self.play(frame.animate.move_to(eq[2]))
        self.play(ReplacementTransform(texto, texto2))
        self.wait()

        texto3 = Text("Coeficiente del término en x", font_size=28).next_to(frame_zoom, DOWN)
        self.play(frame.animate.move_to(eq[5]))
        self.play(ReplacementTransform(texto2, texto3))
        self.wait()

        texto4 = Text("Corte con el eje y",font_size=28).next_to(frame_zoom, DOWN)
        self.play(frame.animate.move_to(eq[7]))
        self.play(ReplacementTransform(texto3, texto4))
        self.wait()
        
        #DESHACER el ZOOM
        self.play(Unwrite(zoomed_camera_text), Unwrite(frame_text), Unwrite(texto4))
        self.play(self.get_zoomed_display_pop_out_animation(), rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(frame_zoom), FadeOut(frame))
        self.wait(1)

        texto5 = Text("El valor del término independiente, que es 20 en este caso,\n define el punto donde la parábola corta al eje y", font_size=30)
        texto5.shift(DOWN, 2*LEFT)

        self.play(Create(texto5))
        
        self.wait(2)
        
        self.play(FadeOut(texto5))
        
        #Bajamos la gra´fica para que se vea el punto
        self.play(grafica.animate.shift(4*DOWN, RIGHT))
             
        #construimos el punto de corte
        corte_y = [ax.coords_to_point(0, func(0))]
        #Creamos un objeto dibujable dot
        dot = Dot(radius=0.07, point=corte_y, color=RED)
        
        
        self.play(Indicate(dot))
        

        self.wait(3)

