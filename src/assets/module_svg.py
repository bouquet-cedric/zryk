class svg():
    def __init__(self, long, ecart, fichier):
        self.long= long
        self.ecart = ecart
        self.fichier = fichier

    def chemin(self,tab, fill="transparent", sw=5, stroke="black"):
        f = open(self.fichier, 'a')
        f.write("<path d=\"")
        f.write(f"M {tab[0][0]}, {tab[0][1]} ")
        for i in tab:
            if i != tab[0]:
                f.write(f"L {i[0]}, {i[1]} ")
        f.write(f"Z\" fill=\"{fill}\" stroke=\"{stroke}\" stroke-width=\"{sw}\"/>\n")
        f.close()

    def polygon(self, sw=5, stroke="lighskyblue"):
        sw /= 2
        tab = [
            (self.ecart, sw),
            (sw, self.ecart),
            (sw, self.long-self.ecart),
            (self.ecart, self.long-sw),
            (self.long-self.ecart, self.long-sw),
            (self.long-sw, self.long-self.ecart),
            (self.long-sw, self.ecart),
            (self.long-self.ecart, sw),
            (self.ecart, sw)
            ]
        self.chemin(tab, sw=sw,stroke=stroke)

    def start_svg(self):
        f = open(self.fichier, "w")
        f.write(f"<svg xmlns='http://www.w3.org/2000/svg' width='{self.long}' height='{self.long}' viewBox='0 0 {self.long} {self.long}'>\n")
        f.close()


    def addGradient(self, id, nb=-1, dir='h', *col):
        f = open(self.fichier, 'a')
        if dir == 'v':
            f.write(f"<defs>\n<linearGradient x1=\"0\" x2=\"0\" y1=\"0\" y2=\"1\" id=\"{id}\">\n")
        elif dir == 'h':
            f.write(f"<defs>\n<linearGradient x1=\"0\" x2=\"1\" y1=\"1\" y2=\"1\" id=\"{id}\">\n")
        if nb == -1:
            nb = len(col)
        ratio = 100/(nb-1)
        cpt = 0
        ind = 0
        while cpt < nb:
            i = col[ind]
            f.write(f"\t<stop offset=\"{cpt * ratio}%\" stop-color=\"{i}\"/>\n")
            cpt += 1
            ind += 1
            if ind>=len(col):
                ind = 0
        f.write("</linearGradient>\n</defs>\n")
        f.close()

    def circle(self, cx, cy, r, stroke, fill, sw=5):
        f = open(self.fichier, 'a')
        f.write(f"<circle cx=\"{cx}\" cy=\"{cy}\" r=\"{r}\" stroke=\"{stroke}\" fill=\"{fill}\" stroke-width=\"{sw}\"/>\n")
        f.close()

    def triangle(self, x,y,x2,y2,x3,y3,stroke,fill,sw=5):
        tab=[
            (x,y),
            (x2,y2),
            (x3,y3)
        ]
        self.chemin(tab, fill=fill, sw=sw,stroke=stroke)

    def finish_svg(self):
        f = open(self.fichier, 'a')
        f.write('</svg>')
        f.close() 