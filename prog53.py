def ano(n,a):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        return n - a
n = int(input("Digite o ano atual "))
a = int(input("Digite o ano em que vc nasceu "))
ano = n - a
if ano >= 18:
    print(" maior de idade")
if ano >= 60:
    print("Coroa")
if ano < 18:
    print("menor")
