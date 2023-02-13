from manim import *
import numpy as np

#Animación que explica la gráfica de la función seno a partir de la circunferencia goniométrica
#Y un punto que orbita en su exterior
#Autor: Adrián Martin Dinnbier
#Web: http://dinnbier.com



class SineCurveUnitCircle(Scene):
    def construct(self):
 
        #Definicion del tracker que controla la animción y valor inicial
        tracker = ValueTracker(0)
        
        #Función que redibuja el punto alrededor de la circunferencia
        def go_around_circle(mob, dt):
            #El parámetro dt no lo empleo. Contiene el tiempo transcurrido desde que se invocó a la función
            mob.move_to(orbit.point_from_proportion(tracker.get_value()))
        
        #Funciones que construyen el entorno (círculo y ejes)
        self.show_axis()
        self.show_circle()
   
        
        #La circunferencia goniométrica será al órbita del movimiento del punto 
        orbit = self.circle
         
        #PUNTO 
        #punto sobre la goniométrica
        dot = Dot(radius=0.08, color=YELLOW)
        #point_from_proportion recibe un número de 0 a 1 y te da las coordenadas del punto moviéndose por 
        #el objeto (en este caso se trata del objeto órbita, que no es el otro que la circunferencia goniométrica)
        dot.move_to(orbit.point_from_proportion(0))
    
        #GRÁFICA DE LA FUNCIÓN SENO
        #Configuración de la gráfica del seno que vamos a dibujar
        #Cada tramo se dibuja con una función "get_curve"
    
        def get_curve1():
            sine_graph= FunctionGraph(
                lambda t: np.sin(t+3),
                [-3, -3+tracker.get_value()*2*np.pi],
                color=BLUE,
            )

            return sine_graph
        
        def get_curve2():
            sine_graph= FunctionGraph(
                lambda t: np.sin(t+3),
                [-3+np.pi/2, -3+np.pi/2+tracker.get_value()*2*np.pi],
                color=BLUE,
            )

            return sine_graph
        
        def get_curve3():
            sine_graph= FunctionGraph(
                lambda t: np.sin(t+3),
                [-3+np.pi, -3+np.pi+tracker.get_value()*2*np.pi],
                color=BLUE,
            )

            return sine_graph
        

        #creamos un updater para que actualice al punto
        dot.add_updater(go_around_circle)
        
        self.play(Create(dot));
     
        
        #TRAMO 1 (PI/2)
        sine_curve_line1 = always_redraw(get_curve1)
        self.play(tracker.animate.set_value(0.25),Create(sine_curve_line1), run_time=2)

        #Dibujamos el tramo que hasta ahora se ha representado. 
        sine_graph_1= FunctionGraph(
                lambda t: np.sin(t+3),
                [-3, -3+np.pi/2],
                color=BLUE,
            )
        self.add(sine_graph_1);
        self.remove(sine_curve_line1);
        
        
        #Segmentos que van desde el circunferencia a la gráfica (I)
        intervalos=10
        angulo_tramo=np.pi/2
        for i in range(1, intervalos+1):
            angle=i*angulo_tramo/intervalos;
            posx=np.cos(angle);
            posy=np.sin(angle);
            seg_1=Line(np.array([-4+posx,0,0]),np.array([-4+posx,posy,0]), color=GREEN_B,
                stroke_width=5, stroke_opacity= 1)
            self.play(Create(seg_1),run_time=0.5);
            seg_2=Line(np.array([-3+angle,0,0]),np.array([-3+angle,posy,0]), color=GREEN_B,
                stroke_width=4, stroke_opacity= 1)
            self.play(Transform(seg_1, seg_2), run_time=0.5);
            
        
        #TRAMO 2 (PI)
        sine_curve_line2 = always_redraw(get_curve2)
        
        
        self.play(tracker.animate.set_value(0.5),Create(sine_curve_line2), run_time=2)
         #Dibujamos el tramo que hasta ahora se ha representado. 
        sine_graph_2= FunctionGraph(
                lambda t: np.sin(t+3),
                [-3, -3+np.pi],
                color=BLUE,
            )
        self.add(sine_graph_2);
        self.remove(sine_curve_line2);
        
        #TRAMO 3 (3*PI/2)
        sine_curve_line3 = always_redraw(get_curve3)
        
        self.wait()
        self.play(tracker.animate.set_value(1),Create(sine_curve_line3), run_time=2)
         #Dibujamos el tramo que hasta ahora se ha representado. 
        sine_graph_3= FunctionGraph(
                lambda t: np.sin(t+3),
                [-3+np.pi, -3+2*np.pi],
                color=BLUE,
            )
        self.add(sine_graph_3);
        self.remove(sine_curve_line3);
        
        
        #segmentos en la circun
        
        
        
        self.wait();
        
        
    #dibuja los segmentos en un intervalos en la goniométrica y ls desplaza hasta la gráfica
           

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
        
    