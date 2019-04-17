class cola:
	def __init__(self):
		self.cola_p = []
		self.inicio = 0
		self.final = -1
	def es_vacio_c(self):
		return len(self.cola_p) == 0
	def agregar_proceso(self, idP, t_lleg, dur):
		self.idP, self.t_lleg, self.dur = idP, t_lleg, dur
		self.cola_p.append([self.t_lleg, self.idP , self.dur])
	def ciclo_cola(self):
		#self.cola_p[self.inicio]
		self.recorre()
	def recorre(self, cola_p4):
		self.col_aux = cola_p4
		if self.inicio == len(self.col_aux)-1:
			self.inicio = 0
			self.final = -1
			#print("proceso: {} ".format(self.col_aux[self.inicio]))
		elif len(self.col_aux) == 0:
			pass
			#print("proceso: {} ".format(self.col_aux))
		else:
			self.inicio += 1
			self.final += 1
			#print("proceso: {} ".format(self.col_aux[self.inicio]))
	def quitar_proceso(self):
		self.cola_p.pop(0)
	def devolver_col_p(self):
		self.cola_pp = self.cola_p.sort()
		return self.cola_p
	'''
		for lis_proc in self.c.devolver_col_p():
			self.quitar_tiempo = 1
			while self.quitar_tiempo <= self.t_chunk:
				print("Soy el proceso Numero: {}".format(lis_proc[0]))
				lis_proc[2] = int(lis_proc[2]) - self.quitar_tiempo
				self.quitar_tiempo += 1
		'''


	

		