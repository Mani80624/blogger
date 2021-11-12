#!/usr/bin/env python
# coding: utf-8

# # Métodos directos para resolver sistemas de ecuaciones lineales
# ## Método de Gauss-Jordan
# ### Ejemplo: 
# Un comerciante compra tres productos: $A,B,C,$ pero en las facturas únicamente consta la cantidad comprada en Kg, y el valor total de la compra. Se necesita determinar el precio unitario de cada producto. Para esto dispone de tres facturas con los siguientes datos:
# 

# Factura | Cantidad de $A$ | Cantidad de $B$ | Cantidad de $C$ | Valor pagado
# ------- | --------------- | --------------- | --------------- | ------------
# 1| 4 | 2|  5 | \$60.70
# 2 | 2 |  5 | 8 | \$92.30
# 3 | 5 | 4 | 3  | \$56.30
# 
# 

# **Solucion:**
# Sean $x_1,x_2,x_3$ variables que representan al precio unitario de cada producto en dólares por Kg. Entonces, se puede escribir:
# 
# $$4x_1 + 2x_2 + 5x_3 = 60.70$$
# $$2x_1 + 5x_2 + 8x_3 = 92.90$$
# $$5x_1 + 4x_2 + 3x_3 = 56.30$$
# Reconocemos a primera vista como un sistema lineal no hómogeneo de tres ecuaciones con tres variables.

# La estrategia del método Gauss-Jordan consiste en transformar la matriz $A$ del sistema $AX = B$ y reducirla a la matriz identidad $I$ (Siempre y cuando $det(A)\neq 0$). Donde:
# $$ A = \left( \begin{array}{ccc} 
# 4 & 2 & 5 \\
# 2 & 5 & 8 \\ 
# 5 & 4 & 3 \\
# \end{array} \right)~~~~
# X = \left( \begin{array}{c}
# x_1 \\ 
# x_2 \\
# x_3
# \end{array} \right)~~~~ 
# B =\left( \begin{array}{c}
# 60.70 \\ 
# 92.90 \\
# 56.30
# \end{array} \right)
# $$
# 

# En el caso de que la solución para $X$ exista, el procedimiento debe transformar las ecuaciones mediante operaciones lineales que no modifiquen la solución del sistema original:
# 

# (a) Intercambiar ecuaciones.

# (b) Multiplicar ecuaciones por alguna constante no nula

# (c) Sumar alguna ecuación a otra ecuación

# **Ahora formulamos el algoritmo para resolver este problema:**
# Entonces primero definimos nuestros arreglos tanto el $A$ como el $B$

# In[1]:


from numpy import*
a  = array([[4,2,5],
           [2,5,8],
           [5,4,3]], float)
b = array([[60.70],
           [92.90],
           [56.30]], float)


# Reescribimos como una matriz aumentada y hacemos uso de (axis)

# In[2]:


c = concatenate([a,b],axis=1)
print(c)


# Se multiplica la primera fila por 1/4

# In[3]:


c[0,0:] = c[0,0:]/c[0,0]
print(c)


# Utilizando la propiedad (c) podemos reducir la matriz $c$, restando de la segunda fila el producto de la primera por 2, y restando de la tercer fila el producto de la primera por 5

# In[4]:


c[1,0:] = c[1,0:] - c[1,0]*c[0,0:]
c[2,0:] = c[2,0:] - c[2,0]*c[0,0:]
print(c)


# Multiplicamos la segunda fila por 1/4

# In[5]:


c[1,1:] = c[1,1:]/c[1,1]
print(c)


# Análogo al paso anterior utilizamos la propiedad (c)

# In[6]:


c[0,1:] = c[0,1:] - c[0,1]*c[1,1:]
c[2,1:] = c[2,1:] - c[2,1]*c[1,1:]
print(c)


# Aplicamos la segunda propiedad:

# In[7]:


c[2,2:] = c[2,2:]/c[2,2]
print(c)


# Propiedad (c) nuevamente

# In[8]:


c[0,2:] = c[0,2:]-c[0,2]*c[2,2:]
c[1,2:] = c[1,2:]-c[1,2]*c[2,2:]
print(c)


# Solución del sistema de ecuación lineal:

# In[9]:


x = c[:,3]
print(x)


# Se puede demostrar que la solución hallada es la correcta multiplicando la matriz $A$ por la matriz $X$:

# In[10]:


b = dot(a,x)
print(b)


# **Referencia:**

# Ojeda, L. R. (2016). Análisis numérico básico. Guayaquil: Facultad de ciencias naturales y matemáticas (Departamento de Matemáticas).

# página: 105

# In[ ]:




