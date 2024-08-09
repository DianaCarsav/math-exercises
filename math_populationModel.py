##Work presented by Diana Carolina Salazar Velandia group MIBT-23-6A
import numpy as np
#####creating the matrix A with size 100x100######
def generar_matriz_100x100():
    # create a random row
    primera_fila = np.random.randint(1, 10000, size=100)
    
    # create a dummy cero matrix size 100X100
    matriz = np.zeros((100, 100))
    
    # put the first row in their place in A
    matriz[0] = primera_fila
    
    # We assign random values between 0 and 1 to the diagonal below to principal diagonal
    for i in range(1, 20):
        matriz[i, i-1] = np.random.rand()
    
    return matriz

# Generate A
A = generar_matriz_100x100()

# Show A
print("Matriz Generada: ", A)


#####creating the vector X_1 with size 100x1 and ramdom values between 0 and 10000######
def generar_columna_aleatoria(n, min_valor=0, max_valor=10000):
   
    return np.random.randint(min_valor, max_valor, size=n)

X_1 = generar_columna_aleatoria(100)
print("X_1:", X_1)

#####creating the vector X_T with size 100x1 and ramdom values between 0 and 10000 but wit the condition that their elements HAVE TO BE MINORS THAN ELEMENTS IN X_1######
def generar_columna_aleatoria_condicionada(n, vector_condicion):
    
    X_T = np.zeros(n, dtype=int)  # Inicializamos la columna aleatoria con ceros
    
    # create aleatory numbers acording with condition elements HAVE TO BE MINORS THAN ELEMENTS IN X_1
    for i in range(n):
        X_T[i] = np.random.randint(0, vector_condicion[i])
    
    return X_T

# Vector condition
vector_condicion = X_1

X_T = generar_columna_aleatoria_condicionada(100, vector_condicion)
print("X_T:", X_T)

#### Create the identity matrix 100X100###

I = np.eye(100)

# Mostrar la matriz identidad
print("I:", I)



### Aplying the equation to get U... X_T =A**(T-1)X_1+A**(19)+(I+A+A**(2)+...+A**(18))U ####
### Create the variable "rigth_side_equation" to save the result of computing A**(19)+(I+A+A**(2)+...+A**(18)) 

for i in range(1,20):
    rigth_side_equation= A**(19)@X_1+(I+A**(i))
    
print("rigth_side_equation= ",rigth_side_equation)

#### Now i have the equation  X_T = rigth_side_equation U, so to find U i have to calculate the inverse matrix of the matrix "rigth_side_equation" #####

# Calcular la inversa de B
rigth_side_equation_inverse = np.linalg.inv(rigth_side_equation)

print("the inverse of rigth_side_equation is:", rigth_side_equation_inverse)

### Therefore X_T@rigth_side_equation_inverse=U ####

U = X_T@rigth_side_equation_inverse
print("U= ", U)