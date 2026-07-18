cursos = ["Excel", "Python"]
print("Listagem dos cursos")
for x in cursos:
    print(x)
n = input("Digite um curso a ser adicionado = ")
cursos.append(n)
print(f"Listagem dos cursos atualizada {cursos}")
c = input("Digite um curso a ser excluído = ")
cursos.remove(c)
print(f"Listagem dos cursos atualizada {cursos}")