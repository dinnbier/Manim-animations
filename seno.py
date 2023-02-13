from manim import *

class SineCurveUnitCircle(Scene):
    def construct(self):
            self.show_axis()
            self.show_circle()
            self.move_dot_and_draw_curve()
            self.wait()

    #dibuja los ejes 
    def show_axis(self):
        #posición del eje x en el dibujo
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        #posición del eje y en el dibujo
        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])
        
        #cofiguramos el ejex  el ejey (inicio a fin)
        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)
        
        #añado las lineas al dibujo
        self.add(x_axis, y_axis)
        #añado las etiquetas del eje x
        self.add_x_labels()

        #defino las coordenadas del origen en mis nuevos ejes 
        self.origin_point = np.array([-4,0,0])
        #en este punto se iniciará la función seno
        self.curve_start = np.array([-3,0,0])

    #añade etiquetas a los ejes creados
    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    #crea el círculo 
    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle
        
    
    #Esta función crea el movimiento de la animación
    def move_dot_and_draw_curve(self):
        #la órbita es la circunferencia goniométrica
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        #point_from_proportion recibe un número de 0 a 1 y te da las coordenadas del punto moviéndose por 
        #el objeto (en este caso se trata del objeto órbita, que no es otro que la circunferencia goniométrica)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        #función vinculada al updater que hará girar el círculo alrededor de la circunferencia
        '''update_function (Updater)
        mob: el objeto que la ha llamado al updater
        dt: el tiempo en segundos desde que se hizo la mmañada anterior
        The update function to be added. 
        Whenever update() is called, this update function gets called using self as the first parameter. 
        The updater can have a second parameter dt. If it uses this parameter, 
        it gets called using a second value dt, 
        usually representing the time in seconds since the last call of update().'''
        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))
            
            

        #el segmento que une el centro de la circunferencia con el punto que gira en su perímetro
        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=RED)
        

        #la línea que une el punto con el dibujo de la función
        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=LIGHT_PINK, stroke_width=2 )
        
      
        self.curve = VGroup()
        self.curve.add(Line(dot.get_center(),self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=DARK_BROWN)
            self.curve.add(new_line)

            return self.curve
        
        #segmentos en la goniométrica
        
        self.segments = VGroup()
        self.segments.add(Line(dot.get_center(),np.array([dot.get_center()[0],self.origin_point[1],0]), color=BLUE,
                stroke_width=3, stroke_opacity= 0.2))
        
        def get_segments():
            self.segments.add(Line(dot.get_center(),np.array([dot.get_center()[0],self.origin_point[1],0]), color=BLUE,
                stroke_width=3, stroke_opacity= 0.2))
            
            return self.segments
        
        
        #segmentos en la curva
        
        self.segments2 = VGroup()
        x = self.curve_start[0] + self.t_offset * 4
        y = dot.get_center()[1]
        self.segments2.add(Line( np.array([x,y,0]) ,np.array([x,self.origin_point[1],0]), color=BLUE,
                stroke_width=3, stroke_opacity= 0.2))
        
        def get_segments2():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            self.segments2.add(Line( np.array([x,y,0]) ,np.array([x,self.origin_point[1],0]), color=BLUE,
                stroke_width=3, stroke_opacity= 0.2))
            return self.segments2
        
      


        #el updater está referido al punto que se mueve girando entorno a la circunferencia.
        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)
        segments_in_circle = always_redraw(get_segments)
        segments_in_graph=always_redraw(get_segments2)
        
   
        
        
            
        #self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)

        
        self.add(dot)
        
        self.add( orbit, segments_in_circle,  segments_in_graph, origin_to_circle_line,   sine_curve_line, dot_to_curve_line)
        
        self.wait(5);
        
        
        

        dot.remove_updater(go_around_circle)