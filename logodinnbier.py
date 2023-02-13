from manim import *
config.background_color = WHITE

class logo(MovingCameraScene):

    def construct(self):
        position_list_square = [
            [0.5, 1, 0],  # middle right
            [-0.5, 1, 0],  # bottom right
            [-0.5, 2, 0],  # bottom left
            [0.5, 2, 0],  # top left
        ]
        position_list_triangle1 = [
            [-0.57, 1, 0],  # C'
            [-0.57, 2, 0],  # bottom left
            [-1.19, 1.36, 0],  # top left
        ]
 
        position_list_triangle2 = [
            [-0.5, .93, 0],  # middle right
            [0.5, 0.93, 0],  # bottom right
            [-0.3692, 0.2325, 0],  # bottom left

        ]
        # creacióm de objetos
        self.camera.frame.save_state()
        cuadrados=[]
        for i in range(6):
            cuadrados.append(Polygon(*position_list_square, color=BLACK).set_fill(color=BLACK, opacity=0.4))
        triangulos=[]
        for i in range(6):
            triangulos.append(Polygon(*position_list_triangle1, color=BLACK).set_fill(color=BLACK, opacity=0.4))
        triangulos2=[]
        for i in range(6):
            triangulos2.append(Polygon(*position_list_triangle2, color=BLACK).set_fill(color=BLACK, opacity=0.4))
      

        cuadrado = Polygon(*position_list_square, color=BLACK)
        triangulo1 = Polygon(*position_list_triangle1, color=BLACK)
        triangulo2 = Polygon(*position_list_triangle2, color=BLACK)
        cuadrado.set_fill(BLACK, opacity=1)  # set the color and transparency
        triangulo1.set_fill(BLACK, opacity=1)
        triangulo2.set_fill(BLACK, opacity=1)
        
        numberplane = NumberPlane(
            x_range=(0, 30, 1),
            y_range=(0, 20, 1),
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 3,
                "stroke_opacity": 0.4
            }
        )
        #aparición de los elementos
        self.play(Create(numberplane))
        self.play(DrawBorderThenFill(cuadrado),run_time=0.7)
        self.play(DrawBorderThenFill(triangulo1), run_time=0.7)
        self.play(DrawBorderThenFill(triangulo2),run_time=0.7)
        
        for i in range(5):
           self.play(
               Rotate(
                cuadrados[0],
                angle=2*PI/6,
                about_point=(0, 0, 0),
                rate_func=linear,
                ),
               Rotate(
                triangulos[0],
                angle=2*PI/6,
                about_point=(0, 0, 0),
                rate_func=linear,
                ),
               Rotate(
                triangulos2[0],
                angle=2*PI/6,
                about_point=(0, 0, 0),
                rate_func=linear,
                ),
               run_time=0.3
            )
           self.play(DrawBorderThenFill(cuadrados[i+1].rotate((i+1)*2*PI/6, about_point=(0, 0, 0)).set_fill(color=BLACK, opacity=1)), 
                     DrawBorderThenFill(triangulos[i+1].rotate((i+1)*2*PI/6, about_point=(0, 0, 0)).set_fill(color=BLACK, opacity=1)), 
                     DrawBorderThenFill(triangulos2[i+1].rotate((i+1)*2*PI/6, about_point=(0, 0, 0)).set_fill(color=BLACK, opacity=1)),
                     run_time=0.7)
        
        texto=Text("dinnbier.com", color=BLACK, font="sans-serif")
        texto.shift(3*DOWN)
        self.play(FadeOut(numberplane))
        self.play(Write(texto));
        self.wait(4)
    
        
        
        
           
