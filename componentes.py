class Resistor():
    def __init__(self):
        self.color1_2={'preto':0,'castanho':1,'vermelho':2,'laranja':3,'amarelo':4,
        'verde':5,'azul':6,'violeta':7,'cinzento':8,'branco':9 }
        self.cor_3={'prata':0.01,'ouro':0.1,'preto':1,'castanho':10,'vermelho':100,
                    'laranja':1000,'amarelo':10000,'verde':100000,'azul':1000000}
        self.tolerancia={'prata':0.1,'ouro':0.05,'castanho':0.01,'vermelho':0.02}
        self.valor=0
        self.minimo=0
        self.maximo=0
        self.valk=0
        self.valM=0
        self.valu=0

    def measure(self,cor1,cor2,cor3,cor4):
        self.valor=(self.color1_2[cor1]*10+self.color1_2[cor2])*self.cor_3[cor3]
        self.minimo=self.valor*(1 - self.tolerancia[cor4])
        self.maximo=self.valor*(1 + self.tolerancia[cor4])
        mega=1000000
        kilo=1000
        if self.valor>mega:
            self.valM=self.valor/mega
            return
        if self.valor>kilo:
            self.valk=self.valor/kilo
            return
        if self.valor>0:
            self.valu=self.valor
            return

resistencia=Resistor()

resistencia.measure('branco','cinzento','verde','prata')
print(f' R={resistencia.valor} ohm Limites=[{resistencia.minimo} ; {resistencia.maximo}] ohm')
if resistencia.valk!=0:
    print('R=',resistencia.valk, 'k ohm')
if resistencia.valM!=0:
    print('R=',resistencia.valM, 'M ohm')
if resistencia.valu!=0:
    print('R=',resistencia.valu, ' ohm')



