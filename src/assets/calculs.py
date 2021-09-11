from enum import Enum
import module_svg as msvg

class shadows(Enum):
        dark = "rgba(30,30,30,0.9)"
        slate = "rgba(30,30,30,0.7)"
        red = "rgba(255,30,30,0.7)"
        white = "rgba(255,255,255,0.7)"
        wheat = "rgba(245,222,179,0.7)"

class Color(Enum):
    BARRE_TITRE = "url(#g4)"
    # SPECTRUM = "lightgrey"
    SPECTRUM = "url(#g9)"
    TITLE_HAUT = shadows.dark.value
    TITLE_BAS = "red"
    # LAT_G_D = "url(#g5)"
    # LAT_G_D = shadows.slate.value
    LAT_G_D = "url(#g8)"
    # LAT_H = "url(#g6)"
    LAT_H = "url(#g7)"
    LAT_B = shadows.dark.value
    BAS_GAUCHE = "url(#g1)"
    BAS_DROIT = "url(#g2)"

class Boutons:
    def __init__(self, long, ecart):
        self.long = long
        self.ecart = ecart

    def decalage(self):
        maxi = self.long /2
        dec = (maxi - self.ecart) /2
        return dec

    def play(self, s: msvg.svg, stroke,fill,sw=5):
        self.add(s, "\n<!-- play -->")
        cx = self.ecart/2 + self.decalage()
        cy = self.long - (self.ecart /2)
        r = self.ecart /2 - sw
        s.circle(cx,cy,r, stroke=stroke, fill=fill, sw=sw)
        tri = r /2
        leftX = cx - tri
        hautY = cy - tri
        basY = cy + tri
        rightX = cx + tri
        trian=[
            (leftX,hautY), 
            (leftX, basY), 
            (rightX, cy)
        ]
        s.chemin(trian,stroke="white",fill=shadows.dark.value,sw=sw/2)
        self.add(s,"\n")

    def pause(self, s: msvg.svg, stroke, fill, sw=5):
        cx = self.long - self.ecart/2 - self.decalage()
        cy = self.long - (self.ecart /2)
        r = self.ecart /2 - sw
        s.circle(cx,cy,r, stroke=stroke, fill=fill, sw=sw)

    def gradients(self, s):
        s.addGradient("g1",-1,'h',shadows.dark.value,"white",shadows.dark.value) 
        s.addGradient("g2",-1,'h',shadows.dark.value,shadows.dark.value,shadows.dark.value,"white",shadows.dark.value)
        s.addGradient("g3",7,'h',"transparent","red")
        s.addGradient("g4",-1,'v',"black",shadows.red.value,"black")
        s.addGradient("g5",300,'h',shadows.dark.value,shadows.red.value)
        s.addGradient("g6",30,'v',shadows.wheat.value,"black")
        s.addGradient("g7",-1,'h',shadows.dark.value,shadows.slate.value,shadows.dark.value)
        s.addGradient("g8",-1,'v',shadows.slate.value,shadows.dark.value,shadows.slate.value)
        s.addGradient("g9",-1,'v',shadows.slate.value,shadows.wheat.value,shadows.wheat.value,shadows.wheat.value,shadows.slate.value)

    def add(self,s, text):
        f = open(s.fichier, 'a')
        f.write(text+'\n')
        f.close()

    def barres(self, s, sw=5):
        sw = sw/2
        tab = [
            (sw, self.long-self.ecart),
            (self.ecart, self.long-sw),
            (self.long/2, self.long-sw),
            (self.long/2, self.long-self.ecart),
            (sw, self.long-self.ecart)
            ]
        s.chemin(tab,sw=0, fill=Color.BAS_GAUCHE.value)
        tab = [
            (self.long-sw, self.long-self.ecart),
            (self.long-self.ecart, self.long-sw),
            (self.long/2, self.long-sw),
            (self.long/2, self.long-self.ecart),
            (sw, self.long-self.ecart)
            ]
        s.chemin(tab,sw=0, fill=Color.BAS_DROIT.value)
        tab=[
            (self.ecart * 1.5, sw),
            (self.ecart * 1.5, self.ecart*0.7),
            (self.ecart *2.3, self.ecart),
            (self.long-self.ecart*2.3, self.ecart),
            (self.long-self.ecart*1.5, self.ecart*0.7),
            (self.long-self.ecart*1.5, sw)
        ]
        # titre
        s.chemin(tab, sw=0.5, fill=Color.BARRE_TITRE.value)
        tab=[
            (sw, self.ecart),
            (self.ecart *1.5, self.ecart*0.7),
            (self.ecart *2.3, self.ecart)
        ]
        s.chemin(tab,fill=Color.TITLE_BAS.value,sw=0)
        tab=[
            (self.long-sw, self.ecart),
            (self.long-self.ecart*2.3, self.ecart),
            (self.long-self.ecart*1.5, self.ecart*0.7)
        ]
        s.chemin(tab,fill=Color.TITLE_BAS.value,sw=0)
        tab=[
            (self.long-sw, self.ecart),
            (self.long-self.ecart*1.5, self.ecart*0.7),
            (self.long-self.ecart*1.5, sw),
            (self.long-self.ecart, sw)
        ]
        s.chemin(tab,fill=Color.TITLE_HAUT.value,sw=0)
        tab=[
            (sw, self.ecart),
            (self.ecart*1.5, self.ecart*0.7),
            (self.ecart*1.5, sw),
            (self.ecart, sw)
        ]
        s.chemin(tab,fill=Color.TITLE_HAUT.value,sw=0)
        tab=[
            (sw, self.ecart),
            (self.ecart, self.long*0.3),
            (0.7*self.ecart, self.long *0.5),
            (self.ecart, self.long*0.7),
            (sw, self.long-self.ecart)
        ]
        s.chemin(tab,fill=Color.LAT_G_D.value,sw=0)
        tab=[
            (self.long-sw, self.ecart),
            (self.long-self.ecart, self.long*0.3),
            (self.long-0.7*self.ecart, self.long *0.5),
            (self.long-self.ecart, self.long*0.7),
            (self.long-sw, self.long-self.ecart)
        ]
        s.chemin(tab,fill=Color.LAT_G_D.value,sw=0)
        tab=[
            (sw, self.ecart),
            (self.ecart, self.long*0.3),
            (self.long*0.5, self.long*0.25),
            (self.long-self.ecart, self.long*0.3),
            (self.long-sw, self.ecart)
        ]
        s.chemin(tab,fill=Color.LAT_H.value,sw=0, stroke="none")
        tab=[
            (sw, self.long-self.ecart),
            (self.ecart, self.long*0.7),
            (self.long*0.5, self.long*0.75),
            (self.long-self.ecart, self.long*0.7),
            (self.long-sw, self.long-self.ecart)
        ]
        s.chemin(tab,fill=Color.LAT_B.value,sw=0, stroke="none")
        tab=[
            (self.long-self.ecart, self.long*0.3),
            (self.long-0.7*self.ecart, self.long *0.5),
            (self.long-self.ecart, self.long*0.7),
            (self.long*0.5, self.long*0.75),
            (self.ecart, self.long*0.7),
            (0.7*self.ecart, self.long *0.5),
            (self.ecart, self.long*0.3),
            (self.long*0.5, self.long*0.25)
        ]
        s.chemin(tab,fill=Color.SPECTRUM.value,sw=sw, stroke="darkgrey")

LEN = 500
ECART = 65

SVG = msvg.svg(LEN, ECART, "./player.svg")
BTNS=Boutons(LEN, ECART)

SVG.start_svg()
BTNS.gradients(SVG)
SVG.polygon(sw=5, stroke="url(#g3)")
BTNS.barres(SVG, sw=3)
BTNS.play(SVG, shadows.red.value,shadows.dark.value)
BTNS.pause(SVG, shadows.red.value,shadows.dark.value)
SVG.finish_svg()