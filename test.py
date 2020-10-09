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
#print(edificioDeEmpresa)
#print(oficinasData)
#print(len(oficinasData))
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

        # Comentar si usan strings
        partida = ZonaAuxilio(zonas.index(auxilioData[2]))
        # Comentar si usan strings
        destino = ZonaAuxilio(zonas.index(auxilioData[3]))
        # Comentar si usan strings
        tipo = TipoAuxilio(tipos.index(auxilioData[1]))
        # Comentar si usan strings
        estado = EstadoAuxilio(estados.index(auxilioData[4]))
        ############################################################################

        ###################Para uso con strings#####################################
        # partida = auxilioData[2]                                                   ###Comentar si usan Enums
        # destino = auxilioData[3]                                                   ###Comentar si usan Enums
        # tipo = auxilioData[1]                                                      ###Comentar si usan Enums
        # estado = auxilioData[4]                                                    ###Comentar si usan Enums
        ############################################################################


        ##############Creacion de auxilio#########################
        auxilio = Auxilio(patente, partida, destino, tipo, estado)
        ##############Envio de auxilio a oficina##################
        #print(type(auxilio))
        #print(auxilio)
        oficina.recibirAuxilio(auxilio)
    
    ################Ubicacion de oficina en edificio####################
    edificioDeEmpresa.establecerOficina(nroPiso, nroHabitaculo, oficina)

    ##############################################################################
    ##########Ejecucion de pruebas de operaciones de TDA OficinaAtencion##########
    ##############################################################################

    ##########################primerAuxilioAEnviar################################
    primerosAuxiliosPorInterno[interno] = oficina.primerAuxilioAEnviar()
    #print(primerosAuxiliosPorInterno[interno])

    ##########################enviarAuxilio#######################################
    #####################Para uso con Enum########################################
    auxilioAEnviar = oficina.enviarAuxilio(ZonaAuxilio(zonas.index("CABA")))  # Comentar si usan strings
    ##############################################################################

    #####################Para uso con strings#####################################
    # auxilioAEnviar = oficina.enviarAuxilio("CABA")                               ###Comentar si usan Enums
    ##############################################################################

    primerosAuxiliosDesdeCABA[interno] = auxilioAEnviar
    #print(primerosAuxiliosDesdeCABA[interno])
    oficina.recibirAuxilio(auxilioAEnviar)
################################################################################
#print(edificioDeEmpresa)
print("Edificio de empresa:\n")
print(edificioDeEmpresa)
print("-----------------------------------------------------------------------\n")
################################################################################
############Impresion de pruebas de operaciones de TDA OficinaAtencion##########
################################################################################
"""
for interno in primerosAuxiliosPorInterno:
    ##########################primerAuxilioAEnviar################################
    print("Primer auxilio a enviar en oficina", interno,
          ":\n", primerosAuxiliosPorInterno[interno])

    ##########################enviarAuxilio#######################################
    print("Primer auxilio enviado desde CABA en oficina",
          interno, ":\n", primerosAuxiliosDesdeCABA[interno])

print("-----------------------------------------------------------------------\n")
"""

################################################################################
################Prueba de operaciones de TDA EdificioEmpresa####################
################################################################################
"""
#######################cantidadDeOficinasCriticas###############################
print("\n\nCantidades de oficinas criticas en cada piso:\n")
for nroPiso in range(nroPisos):
    print("Piso", nroPiso, ":", edificioDeEmpresa.cantidadDeOficinasCriticas(nroPiso))
print("-----------------------------------------------------------------------")
"""
