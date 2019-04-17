from tailprocess import *
from listaterminados import *

class round_robin:
	def __init__(self, t_chunk, num_pros):
		self.t_chunk = t_chunk
		self.num_pros = num_pros
		self.c = cola()
		self.term = terminados()
		#print(type(self.c.inicio))
	def agregar_procesos(self):
		self.idP = 0
		self.h_lle = 0
		self.dur = 0
		while self.idP < self.num_pros:
			self.h_lle = int(input("Hora de llegada: "))
			self.dur = int(input("Duracion: "))
			self.c.agregar_proceso(self.idP, self.h_lle, self.dur)
			self.idP += 1
	def proceso_ciclo(self):
		self.lis_proc = self.c.devolver_col_p()[:]
		self.imprimir_lista_procesos(self.lis_proc)
		#self.imprimir()
		self.n = 0
		self.quitar_tiempo = 1
		#cambiar despues por listatemrinados es_vacia
		while True:
			if self.c.es_vacio_c():
				break
			self.quitar_tiempo = 1
			while self.quitar_tiempo <= self.t_chunk:
				#self.inicio_proceso(self.lis_proc[self.c.inicio][2], self.lis_proc[self.c.inicio][1])
				#Eself.lis_proc[self.c.inicio][2] = int(self.lis_proc[self.c.inicio][2]) - self.quitar_tiempo
				if self.lis_proc[self.c.inicio][2] >= 0:
					print("Soy el proceso Numero: {}  Tiempo: {}".format(self.lis_proc[self.c.inicio][1], self.lis_proc[self.c.inicio][2]))
				self.lis_proc[self.c.inicio][2] = int(self.lis_proc[self.c.inicio][2]) - self.quitar_tiempo
				if self.lis_proc[self.c.inicio][2] <= 0:
					self.term.agregar_terminado(self.lis_proc[self.c.inicio])
					self.fin_proceso(self.lis_proc[self.c.inicio][1])
					self.c.quitar_proceso()
					self.lis_proc.pop(0)
					self.c.recorre(self.lis_proc)
				self.quitar_tiempo += 1
			self.c.recorre(self.lis_proc)
			#self.n += 1
	def inicio_proceso(self,inicio,lis_proc):
		self.inicio = int(inicio)
		self.l_pr = lis_proc
		print(self.l_pr)
		if self.inicio == self.dur:
			print("Proceso: {} aqui estoy...".format(self.l_pr))
		elif self.l_pr < 0:
			pass
		else:
			pass
	def fin_proceso(self, idPcs):
		self.idPcs = idPcs
		print("Proceso: {} adios...".format(self.idPcs))
	def imprimir_lista_procesos(self,lp_p):
		#impresion por orden de llegada
		self.lp_p = lp_p
		print("\n\nPlanificacion de procesos por hora de llegada \nLista de procesos: {} \n\n".format(self.lp_p))
		#print(self.c.devolver_col_p())

t_chunk = int(input("Tiempo de chunk: "))
num_pros = int(input("Numero de procesos: "))
r_ro = round_robin(t_chunk, num_pros)
r_ro.agregar_procesos()
r_ro.proceso_ciclo()
#r_ro.imprimir()
'''
IR RESTANTO AL TIEMPO DE EJECUCION EN 1 EN UNO Y DESPUES VOLVER A 0 EL QUE VA A RESTAR POR EJEMPLO
TIEMPO: 5
RESTADOR = 0
TIEMPO - (RESTADOR++)
'''
















'''
t_chunk = 5
cont_tiempo = 0
procesos = []
temp = []
identificador = {'id_process':0,'h_llegada':0, 'p_duracion': 0}


f = open('procesos', 'r')
for i in f.read():
	if i != '\n':
		temp.append(i)
#mensaje = f.readlines()
'''
'''
for i in mensaje:
	print(i)
'''
'''
print(temp)
f.close()

print(procesos)
print("\n")







s = linked_list() # Instancia de la clase
s.add_at_front(5) # Agregamos un elemento al frente del nodo
s.add_at_end(8) # Agregamos un elemento al final del nodo
s.add_at_front(9) # Agregamos otro elemento al frente del nodo

s.print_list() # Imprimimos la lista de nodos
'''