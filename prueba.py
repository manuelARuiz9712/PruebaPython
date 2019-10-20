"""
Test Ajedres
"""
import numpy as np
import math 

file = open("params.txt",'r')
DimenMatriz = 0
TotalObstaculos = 0
PosReina =[]
Obstaculos = []

for i,line in enumerate(file  ):
    numsa = line.split()
    #print("my params",len( numsa ))
    if len( numsa ) != 2 and  len( numsa ) != 0 :
      print('Invalid params 2')
      break
    else:
       if i == 0:
           if  ( int( numsa[0] )> 0 and int( numsa[0]) <= pow(10,5) )  and  ( int( numsa[1] )>= 0 and int( numsa[1]) <= pow(10,5) )   :
               
               DimenMatriz = int( numsa[0] )
               TotalObstaculos= int(numsa[1] )
               


           else:
               print('Invalid params 1') 
               break
       elif i ==1:
            PosReina = numsa

       else:
            if( len(numsa) )  ==2:
                Obstaculos.append(numsa)
            else:
                print("Params",numsa,"Invalid")    
           

file.close();  
"""
n = filas y columnas tablero
k = numero de obstacilos
rq: numero de fila de la reina
cq: numero de columna de la reina
obstacles: obstaculos

Reina

"""


def ReverseI(i,n):
    return abs(( i-1) - (n-1)   )
"""
las posiciones empiezan desde cero

Para i debo invertir el numero por la dimension de la matriz
Vect = (j!,j->)
"""


def queensAttack (n,k,r_q,c_q,obstacles):
    
    matriz =  np.zeros((n, n))
    Reina = [ int( r_q ) -1 ,int( c_q )-1]
    HorizontalDerecha = []
    HorizontalIzquierda = []
    VerticalSuperior = []
    VerticalInferior = []
    CreacienteDerecha = []
    CrecienteIzquierda = []
    DecrecienteDerecha = []
    DecrecienteIzquierda  = []
    #print(matriz)
    #print(r_q,c_q)
  
    matriz[ abs( Reina[0] - (n-1)  ) ,Reina[1]] = 100
    #matriz[2,1] =None

    #matriz[ (5-1)-(5-1)  ,5-1 ] = 4
    #print(matriz)
    #print("Obs",len(obstacles),obstacles)
    for x,obs in enumerate( obstacles ):
         i = int( obs[0] ) -1
         #i = abs(( i-1) - (n-1)   )
         j = int( obs[1] )-1
       
         #print( i,j )
         obstacles[x] = [ i ,j]
         #print("Os",obstacles[x])
         matriz[ abs( i- (n-1)) ,j] = None

    print("Matriz Obstaculos \n",)
    print( matriz )
    print("Reina",Reina)
    for I in range(n-1,-1,-1):
             
        for J in range(n):
            
            #VERTICAL --Horizotal
            
            if J == Reina[1]:
                if I < Reina[0]:
                 VerticalInferior.append( [I,J] )
                 
                elif I > Reina[0]:
                    
                    VerticalSuperior.append([I,J]) 

            if I == Reina[0]:
                  if J > Reina[1]:
                        HorizontalDerecha.append( [I,J] )
                  elif J < Reina[1]:
                    HorizontalIzquierda.append( [I,J] )

            #Crecientes en diagonal
    #Cambio el order para que su secuencia sea creciente
    HorizontalIzquierda = HorizontalIzquierda[::-1]
    #print("horr",HorizontalIzquierda)
    #print("horr2",HorizontalIzquierda[::-1])
    #HorizontalDerecha.reverse()
    
    count = 0  
    countDec = n      
    for X in range(0,n,1):
        count = count +1
        countDec = countDec -1

        #Creciente derecha
        #print(Reina[0]-X,Reina[1]+X  )
        if ( Reina[0]-X < Reina[0] and Reina[0]-X < n ) and ( Reina[1]+X  > Reina[1] and Reina[1]+X <n ) :
            #print("coors",[Reina[0]-X ,Reina[1]+X ])
            Coor = [Reina[0]-X,Reina[1]+X  ]
            if Coor != Reina:
               DecrecienteDerecha.append( Coor   )   
             #DecrecienteDerecha.append( [Reina[0]+X,Reina[1]+X  ])

        if ( Reina[0]+X <  n   ) and ( Reina[1]-X  >= 0 ):
            #print("coors 2",[Reina[0]+X,Reina[1]-X  ])
            Coor = [Reina[0]+X,Reina[1]-X  ]
            if Coor != Reina:
               CrecienteIzquierda.append( Coor   )   
            #CrecienteIzquierda.append( [  Reina[0]-X,Reina[1]-X  ]  )
        if  ( Reina[0]-X < Reina[0] and  Reina[1]-X < Reina[1]  ) and ( Reina[0]-X >= 0 and  Reina[1]-X >=0 ):
            #print("coors",[Reina[0]-X,Reina[1]-X  ])
            Coor = [Reina[0]+X,Reina[1]-X  ]
            if Coor != Reina:
                DecrecienteIzquierda.append( Coor   )
        if ( Reina[0]+X <n ) and ( Reina[1]+X < n ): 
            #print("coors",[Reina[0]+X,Reina[1]+X  ]) 
            Coor = [Reina[0]+X,Reina[1]+X  ]
            if Coor != Reina:
                CreacienteDerecha.append( Coor  )  

           

        Status = {
        "VS":True,#Vertical Superior
        "VI":True,#Vertical Inferior
        "HD":True,#Horzontal derecha
        "HI":True,#HorizontalIzquierda
        "CD":True,#Creciente derecha
        "CI":True,#Creciente izquierda
        "DECI":True,#Decreciente Izquierda
        "DECD":True#Decreciente derecha
        } 


    CountAttack = 0
    Prueba = 0


    for X in range(n):
            
            if   X  <  len( DecrecienteDerecha ):
                 
                 if Status['DECD'] ==True:
                     
                     if DecrecienteDerecha[X] not in obstacles and DecrecienteDerecha[X] is not  Reina:
                        CountAttack = CountAttack +1
                        
                        
                     else:
                         Status['DECD'] =False

            if   X  <  len( DecrecienteIzquierda ):
                 if Status['DECI'] ==True:
                     if DecrecienteIzquierda[X] not in obstacles  and DecrecienteIzquierda[X]  is not  Reina:
                        CountAttack = CountAttack +1
                     else:
                         Status['DECI'] =False

            if   X  <  len( CreacienteDerecha ):
                 if Status['CD'] ==True:
                     if CreacienteDerecha[X] not in obstacles  and CreacienteDerecha[X]  is not  Reina :
                        CountAttack = CountAttack +1
                     else:
                         Status['CD'] =False

            if   X  <  len( CrecienteIzquierda ):
                 if Status['CI'] ==True:
                     if CrecienteIzquierda[X] not in obstacles  and CrecienteIzquierda[X]  is not  Reina : 
                        CountAttack = CountAttack +1
                     else:
                         Status['CI'] =False

            if   X  <  len( VerticalSuperior ):
                 if Status['VS'] ==True:
                     if VerticalSuperior[X] not in obstacles  and VerticalSuperior[X]  is not  Reina : 
                        CountAttack = CountAttack +1
                     else:
                         Status['VS'] =False

            if   X  <  len( VerticalInferior ):
                 if Status['VI'] ==True:
                     if VerticalInferior[X] not in obstacles  and VerticalInferior[X]  is not  Reina :  
                        CountAttack = CountAttack +1
                      
                     else:
                         Status['VI'] =False  

            
            if   X  <  len( HorizontalDerecha ):
                 if Status['HD'] ==True:
                     if HorizontalDerecha[X] not in obstacles and HorizontalDerecha[X]  is not  Reina :
                        CountAttack = CountAttack +1
                     else:
                         Status['HD'] =False  


            if   X  <  len( HorizontalIzquierda ):
                 if Status['HI'] ==True:
                     #print("HOOUUU",HorizontalIzquierda[X])
                     if HorizontalIzquierda[X] not in obstacles and HorizontalIzquierda[X]  is not  Reina:
                        CountAttack = CountAttack +1
                     else:
                        Status['HI'] =False 




    



    


    
   
    """print("\n\n Data Test")
    print( VerticalInferior)
    print(VerticalSuperior)
    print(HorizontalDerecha)
    print("HO", HorizontalIzquierda)
    print(DecrecienteDerecha)
    print(DecrecienteIzquierda)
    print(CrecienteIzquierda)
    print( CreacienteDerecha)
    print( VerticalSuperior )
    print("Obst",obstacles)"""
    return CountAttack
    #print(VerticalSuperior,VerticalInferior)    
       
       
    





  


            



if TotalObstaculos != len( Obstaculos ):
   print('Invalid  obstacles number ')
else:

  attack = queensAttack(DimenMatriz,TotalObstaculos,int( PosReina[0]),int(PosReina[1]),Obstaculos)

  print("\n \n") 
  print("N° Atackk:: "+str( attack ))







   
        
   

  



