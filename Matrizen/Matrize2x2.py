class Matrize2x2:
	def __init__(self, a, b, c, d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
	def Anzeigen(self):
		print("    (",self.a,self.b,")")
		print("M=  (     )")
		print("    (",self.c,self.d,")")
	def MultipliziereZahl(self, zahl):
		self.a*=zahl
		self.b*=zahl
		self.c*=zahl
		self.d*=zahl
	def Addiere(self,matrize):
		self.a += matrize.a
		self.b += matrize.b
		self.c += matrize.c
		self.d += matrize.d

matrize_objekt = Matrize2x2(3,7,-2,7)

matrize_objekt.Anzeigen()

matrize_objekt.MultipliziereZahl(2)

matrize_objekt.Anzeigen()



matrize2_objekt = Matrize2x2(5,7,2,-7)

matrize2_objekt.Anzeigen()

matrize2_objekt.Addiere(matrize_objekt)

matrize2_objekt.Anzeigen()