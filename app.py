from Auxilios import *
from EdificioEmpresa import *
from OficinaAtencion import *
from Tipos import *


####################### SCRIPT DE PRUEVA DE TP #################################

########################Definicion de variables#################################
# IMPORTANTE: NO MODIFICAR ESTAS VARIABLES!!!!!!!!!!!!!!!!!!!!!!!
nroPisos = 15
nroHabitaculos = 8
zonas = ["Sur", "Norte", "Este", "Oeste", "CABA"]
tipos = ["Remolque", "Reparacion"]
estados = ["Espera", "Aprobado"]
oficinasData = {}
primerosAuxiliosPorInterno = {}
primerosAuxiliosDesdeCABA = {}

################################################################################
##############Creacion de edificio y carga de oficinas##########################
################################################################################

####################Lectura de archivo con datos de auxilios####################
auxiliosFile = open('TP_pilasColas_datosPrueba.csv')
for auxilio in auxiliosFile:
    auxilioData = auxilio[:-1].split(',')
    interno = int(auxilioData[0])
    if interno in oficinasData:
        oficinasData[interno][1].append(auxilioData[4:])
    else:
        oficinasData[interno] = []
        oficinasData[interno].append(auxilioData[1:4])
        oficinasData[interno].append([auxilioData[4:]])
auxiliosFile.close()
################################################################################

######################Creacion de edificio######################################
edificioDeEmpresa = EdificioEmpresa(nroPisos, nroHabitaculos)
################################################################################

######################Carga de oficinas#########################################
for interno in oficinasData:
    oficinaData = oficinasData[interno][0]
    cantCritica = int(oficinaData[0])
    nroPiso = int(oficinaData[1])
    nroHabitaculo = int(oficinaData[2])

    ############Creacion de oficina################
    oficina = OficinaAtencion(interno, cantCritica)

    ############Carga de auxilios a oficina########
    for auxilioData in oficinasData[interno][1]:
        patente = auxilioData[0]

        ###################Para uso con Enum########################################
        partida = ZonaAuxilio(zonas.index(auxilioData[2]))
        destino = ZonaAuxilio(zonas.index(auxilioData[3]))
        tipo = TipoAuxilio(tipos.index(auxilioData[1]))
        estado = EstadoAuxilio(estados.index(auxilioData[4]))
        ############################################################################

        ##############Creacion de auxilio#########################
        auxilio = Auxilio(patente, partida, destino, tipo, estado)
        ##############Envio de auxilio a oficina##################
        oficina.recibirAuxilio(auxilio)

    ################Ubicacion de oficina en edificio####################
    edificioDeEmpresa.establecerOficina(nroPiso, nroHabitaculo, oficina)

    ##############################################################################
    ##########Ejecucion de pruebas de operaciones de TDA OficinaAtencion##########
    ##############################################################################

    ##########################primerAuxilioAEnviar################################
    primerosAuxiliosPorInterno[interno] = oficina.primerAuxilioAEnviar()

    ##########################enviarAuxilio#######################################
    #####################Para uso con Enum########################################
    auxilioAEnviar = oficina.enviarAuxilio(ZonaAuxilio(
        zonas.index("CABA")))
    ##############################################################################

    primerosAuxiliosDesdeCABA[interno] = auxilioAEnviar
    oficina.recibirAuxilio(auxilioAEnviar)
################################################################################

#############################Impresion de edificio##############################
print("Edificio de empresa:\n")
print(edificioDeEmpresa)
print("-----------------------------------------------------------------------\n")

################################################################################
############Impresion de pruebas de operaciones de TDA OficinaAtencion##########
################################################################################

for interno in primerosAuxiliosPorInterno:
    ##########################primerAuxilioAEnviar################################
    print("Primer auxilio a enviar en oficina", interno,
          ":", primerosAuxiliosPorInterno[interno])

    ##########################enviarAuxilio#######################################
    print("Primer auxilio enviado desde CABA en oficina",
          interno, ":", primerosAuxiliosDesdeCABA[interno])

print("-----------------------------------------------------------------------\n")

################################################################################
################Prueba de operaciones de TDA EdificioEmpresa####################
################################################################################

#######################cantidadDeOficinasCriticas###############################
print("\n\nCantidades de oficinas criticas en cada piso:\n")
for nroPiso in range(nroPisos):
    print("Piso", nroPiso, ":", edificioDeEmpresa.cantidadDeOficinasCriticas(nroPiso))
print("-----------------------------------------------------------------------")

#########################oficinaMenosRecargada##################################
print("\n\nOficina menos recargada:\n")
print(edificioDeEmpresa.oficinaMenosRecargada())
print("-----------------------------------------------------------------------")

#########################buscaOficina###########################################
print("\n\nUbicacion de cada oficina en el edificio:\n")
for interno in oficinasData:
    print("Interno", interno, ":", edificioDeEmpresa.buscaOficina(interno))
print("-----------------------------------------------------------------------")

#########################moverAuxilio###########################################
print("\n\nMovimiento de auxilios de oficina 118 (piso cero) a oficina 136 (piso dos):\n")
print("Cantidad de oficinas criticas en piso cero antes:",
      edificioDeEmpresa.cantidadDeOficinasCriticas(0))
print("Cantidad de oficinas criticas en piso dos antes:",
      edificioDeEmpresa.cantidadDeOficinasCriticas(2))

for auxilioData in oficinasData[118][1]:
    patente = auxilioData[0]
    edificioDeEmpresa.moverAuxilio(patente, 118, 136)

print("\nCantidad de oficinas criticas en piso cero despues:",
      edificioDeEmpresa.cantidadDeOficinasCriticas(0))
print("Cantidad de oficinas criticas en piso dos despues:",
      edificioDeEmpresa.cantidadDeOficinasCriticas(2))
print("-----------------------------------------------------------------------")
