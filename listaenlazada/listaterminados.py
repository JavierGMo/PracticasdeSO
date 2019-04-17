class terminados:
	def __init__(self):
		self.li_terminados = []
	def terminado_vacio(self):
		return len(self.li_terminados) == 0
	def agregar_terminado(self, lis_ter):
		self.li_terminados.append(lis_ter)
	def esta_terminado(self):
		self.cont = 0
		if self.terminado_vacio():
			return False
		else:
			for i in self.li_terminados:
				if i[2] == 0:
					self.cont += 1
		if self.cont == len(self.li_terminados):
			return True
