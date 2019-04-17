class cola_circular:
	def __init__(self):
		#se crea la cola
		self.cola_c = [[1,2,3], [2,3,4]]
		self.inicio = 0
		self.final = -1
	def es_vacia(self):
		if self.cola_c is None:
			return True
		else:
			return False
	def agregar_elem(self, elem):
		if self.es_vacia():
			self.cola_c.append(elem)
		else:
			self.cola_c.append(elem)
			self.inicio = 0
			self.final = -1
	'''
	def siguiente(self):
		self.inicio += 1
	def anterior(self):
		self.final += 1
	'''
	def ciclo_cola(self):
		print(self.cola_c[self.inicio])
		self.recorre()
		'''
		self.n = 0
		while True:
			if self.n == 8:
				break
			print(self.cola_c[self.inicio])
			self.recorre()
			self.n += 1
		'''
	def recorre(self):
		if self.inicio == len(self.cola_c)-1:
			self.inicio = 0
			self.final = -1
		else:
			self.inicio += 1
			self.final += 1
	def imprimir_cola(self):
		print(self.cola_c)
		print("\nini: {} final: {}".format(self.cola_c[self.inicio], self.cola_c[self.final]))
	def quitar_elemento(self):
		pass



c = cola_circular()
'''
c.agregar_elem(5)
c.agregar_elem(7)
c.agregar_elem(4)
c.agregar_elem(3)

c.recorre()
c.imprimir_cola()
c.recorre()
c.imprimir_cola()
c.recorre()
c.imprimir_cola()
'''
c.ciclo_cola()
c.ciclo_cola()
c.ciclo_cola()
c.ciclo_cola()
#c.ciclo_cola()
#c.ciclo_cola()

#c.ciclo_cola()
