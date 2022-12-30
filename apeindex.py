from manim import * 
import pandas as pd

# Información general sobre el ape index extraída de:
# https://en.wikipedia.org/wiki/Ape_index
# Datos sobre el ape index de algunos escaladores profesionales conocidos: 
# https://climbinghouse.com/ape-index-calculator/




# Alternativa de lambda para animar funciones 
class apeIndex(Scene):

    def construct(self):
        
        titulo0 = Title("Gráficos de barras en Manim").shift(DOWN)
        self.play(Create(titulo0))
        
        banner = ManimBanner()
        banner.scale(0.4)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.play(Unwrite(titulo0))
        

        titulo1 = Title("Ape index")
        self.play(Create(titulo1))
        
        texto1 = Text("El ""Ape index"", ""ape factor"", o ""gorilla index"" \nes una jerga que se usa para describir una medida de la \nrelación entre la extensión de los brazos \nde un individuo y su altura.")
        texto1.scale(0.75)
        self.play(FadeIn(texto1), run_time=6)

        
        texto2=Text("Se han realizado múltiples estudios sobre \nel efecto de factores fisiológicos, \ncomo la antropometría y la flexibilidad, \nen la determinación del rendimiento en escalada deportiva.")
        texto2.scale(0.75)
        self.play(ReplacementTransform(texto1, texto2))
        self.wait(5)
        
        texto3=Text("Varios de estos estudios han incluido el Ape index \ncomo una de las variables.")
        texto3.scale(0.75)
        self.play(ReplacementTransform(texto2, texto3))
        self.wait(5)
        
        
        texto4=Text("A continuación te mostramos el valor del Ape index \npara algunos de los escaladores profesionales \nmás conocidos en el mundo.")
        texto4.scale(0.75)
        self.play(ReplacementTransform(texto3, texto4))
        self.wait(5)
        self.play(FadeOut(texto4))
        
        
        
    
    
        titulo2 = Title("Ape index de escaladores profesionales")
        self.play(ReplacementTransform(titulo1, titulo2))
        
        data = pd.read_csv("ape.csv")
        #print(data)
   

        escaladores = ["Daniel Woods","Dave Graham","Chris Sharma","Alex Puccio","Sasha DiGiulian","Stefano Ghisolfi","Magnus Midtbø","Adam Ondra","Alex Megos","Lynn Hill", "Babsi Zangerl"]
        #escaladores=["Daniel Woods","Dave Graham","Chris Sharma"]

        cleanedData = data.query("`Climber` in @escaladores")
        
        
        #cambioGDP=apeIndex
        
        #apeIndex= round((cleanedData["Embergadura"].astype(float) - cleanedData["Altura"].astype(float)), 2)
        #nombres=cleanedData['Climber'].astype("string")
        t_ape = cleanedData['Ape'].to_numpy() 
        t_nombres = cleanedData['Climber'].to_numpy() 
        
        gruposApe=np.array_split(t_ape, 4)
        #print(len(gruposApe));
        gruposNombres=np.array_split(t_nombres, 4)

        chart0 = BarChart(
            values=gruposApe[0],
            bar_names=gruposNombres[0],
            y_range=[0, 11, 1],
            y_length=5,
            x_length=8,
            x_axis_config={"font_size": 30},
        )

        chart1 = BarChart(
            values=gruposApe[1],
            bar_names=gruposNombres[1],
            y_range=[0, 11, 1],
            y_length=5,
            x_length=8,
            x_axis_config={"font_size": 30},
        )
        chart2 = BarChart(
            values=gruposApe[2],
            bar_names=gruposNombres[2],
            y_range=[0, 11, 1],
            y_length=5,
            x_length=8,
            x_axis_config={"font_size": 30},
        )
        chart3 = BarChart(
            values=gruposApe[3],
            bar_names=gruposNombres[3],
            y_range=[0, 11, 1],
            y_length=5,
            x_length=8,
            x_axis_config={"font_size": 30},
        )
        
        bar_labels0 = chart0.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=25
        )
        bar_labels1 = chart1.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=25
        )
        bar_labels2 = chart2.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=25
        )
        bar_labels3 = chart3.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=25
        )
        
        y_label0 = chart0.get_y_axis_label(Text("APE index (cm)").scale(0.7).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=0.3,)

        
        #self.play(Create(chart0), Create(bar_labels0))
        self.play(DrawBorderThenFill(chart0),Create(bar_labels0), FadeIn(y_label0))
        
        #self.play(FadeIn(chart0.get_bar_labels(font_size=10)), FadeIn(y_label0))
        #self.play(FadeOut(chart0.get_bar_labels(font_size=10)))
        #self.play(FadeOut(chart0))
        #self.play(FadeOut(bar_labels0 ))
        self.wait(3);
        self.play(FadeOut(bar_labels0 ))
        self.play(ReplacementTransform(chart0, chart1))
        self.play(FadeIn(bar_labels1 ))
        self.wait(4);
        
        self.play(FadeOut(bar_labels1))
        self.play(ReplacementTransform(chart1, chart2))
        self.play(FadeIn(bar_labels2))
        self.wait(4);
        
        self.play(FadeOut(bar_labels2))
        self.play(ReplacementTransform(chart2, chart3))
        self.play(FadeIn(bar_labels3))
        self.wait(4);
        
        

       
        
'''
        
        self.play(ReplacementTransform(chart1, chart2))
        self.play(FadeIn(chart2.get_bar_labels(font_size=24)), FadeIn(y_label2))
        
        self.play(FadeOut(chart2.get_bar_labels(font_size=24)), FadeOut(y_label2))
        
        self.play(ReplacementTransform(chart2, chart3))
        self.play(FadeIn(chart3.get_bar_labels(font_size=24)), FadeIn(y_label3))
'''