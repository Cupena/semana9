stack = []
pos = 0
size = 0
op = 0

def push(item, stack, size, pos):
    if pos < size:
        stack.append(item)
        return "Elemento apilado"
    else:
        print("Pila llena...")
        return pos +1
    
def show(stack):
    if isEmpty(stack):
        return "Pila vacia ..."
    my_stack = f""
    my_stack += "r" + "-"*8 + ""
    for item in reversed(stack):
        my_stack += f"|" + "-"*8 + "|\n"
        my_stack += f""
        return 

def peek(stack):
    if isEmpty(stack):
        return "La pila esta vacia"
    return stack[-1] 

def isEmpty(stack):
    return not stack

def pop(stack):
    if isEmpty(stack):
        return "La pila esta vacia"
    return stack.pop()

def len_stack(stack):
    if isEmpty(stack):
        return "La pila esta vacia"
    return len(stack)

def menu(op):
    print("""
1. Agregar elemento
2. Mostrar elementos
3. Eliminar elemento por encima
4. Contar elementos en pila
5. Salir del programa""")
    op = input("Ingrese la opcion a ejecutar: ")
    return op

while True:
    item = input("Dime un valor: ")
    push(item, stack, size,pos)
    answer = input("Desea ingresar otro valor (S/N): ")
    if answer.lower() == "n":
        break

while True:
    menu()
    if op == 1:
        push()
    if op ==2:
        show()
    if op == 3:
        pop()
    if op == 4:
        len_stack()
    if op == 5:
        break



print(show(stack))

#Mostrar el tope:
print(peek(stack))
size = int(input("Dime el tamaño de la pila: "))
