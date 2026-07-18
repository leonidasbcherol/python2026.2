nomes = ["ana", "marcos", "Bruno"]
print (f" Listagem de nomes {nomes}")

nomes.append("João")

print(f"Listagem de nomes atualizada {nomes}")
n = input("Digite um nome a ser excluído =")
nomes.remove(n)
print(f"Listagem de nomes atualizada {nomes}")