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
	def MultipliziereMatrize(self,matrize):
		a = self.a * matrize.a + self.b * matrize.c
		b = self.a * matrize.b + self.b * matrize.d
		c = self.c * matrize.a + self.d * matrize.c
		d = self.c * matrize.b + self.d * matrize.d
		self.a = a
		self.b = b
		self.c = c
		self.d = d
	def Umkehren(self):
		a= self.d
		b= -self.b
		c= -self.c
		d= self.a
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.MultipliziereZahl(1/self.Determinante())
	def Determinante(self):
		det=self.a*self.d-self.c*self.b
		return det
	def UmkehrmatrizeExistiert(self):
		if matrize_objekt.Determinante==0:
			return False
		else:
			return True
	
class Matrize2x1:
	def __init__(self, a, c):
		self.a=a
		self.c=c
	def Anzeigen(self):
		print("    (",self.a,")")
		print("M=  (   )")
		print("    (",self.c,")")
	def MultipliziereZahl(self, zahl):
		self.a*=zahl
		self.c*=zahl
	def Addiere(self,matrize):
		self.a += matrize.a
		self.c += matrize.c
	def MultipliziereMatrize(self,matrize):
		a = matrize.a * self.a + matrize.b * self.c
		c = matrize.c * self.a + matrize.d * self.c
		self.a = a
		self.c = c
	
class Gleichungssystem:
	def  __init__(self, a, b):
		self.a = a
		self.b = b
	def Loesung(self):
		self.a.Umkehren()
		self.b.MultipliziereMatrize(self.a)
		return self.b
	def Anzeigen(self):
		print("Gleichungssystem:")
		self.a.Anzeigen()
		self.b.Anzeigen()
		print("Loesung:")
		self.Loesung().Anzeigen()
	def GibtEsEineLoesung(self):
		det = self.a.Determinante()
		if det != 0:
			return True
		else:
			return False
matrize_objekt = Matrize2x2(4,10,-2,7)
print("Matrize1:")
matrize_objekt.Anzeigen()

matrize_objekt.MultipliziereZahl(2)
print("Matrize mit Zahl multipliziert:")
matrize_objekt.Anzeigen()

matrize2_objekt = Matrize2x2(5,2,2,-7)
print("Matrize2:")
matrize2_objekt.Anzeigen()

matrize_objekt.MultipliziereMatrize(matrize2_objekt)
print("Matrize1*Matrize2:")
matrize_objekt.Anzeigen()

matrize2_objekt.Addiere(matrize_objekt)
print("Matrize1+Matrize2:")
matrize2_objekt.Anzeigen()


matrize4_objekt = Matrize2x2(4,10,-2,7)
matrize5_objekt = Matrize2x2(4,10,-2,7)
print("Determinante=",matrize4_objekt.Determinante())
matrize4_objekt.Umkehren()
matrize4_objekt.Anzeigen()
matrize5_objekt.MultipliziereMatrize(matrize4_objekt)
matrize5_objekt.Anzeigen()
print("Umkehrmatrize Überprüfung=", matrize_objekt.UmkehrmatrizeExistiert())

matrize6_objekt = Matrize2x2(4,10,-2,7)
Matrize2x1_objekt = Matrize2x1(4,10)
print("Matrize2x1:")
Matrize2x1_objekt.Anzeigen()
print("Matrize Multipliziert:")
Matrize2x1_objekt.MultipliziereMatrize(matrize6_objekt)
Matrize2x1_objekt.Anzeigen()

Gleichungssystem1 = Gleichungssystem(matrize2_objekt, Matrize2x1_objekt)
Gleichungssystem1.Anzeigen()