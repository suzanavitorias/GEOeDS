# GEOeDS
#grupo: suzana, lívia, isabela v., laura n.
UPA= float(input("tem quantas UPAs tem no seu bairro? "))
médico= str(input("tem médico em tempo integral? "))
enfermeiro=str(input("tem enfermeiros em tempo integral? "))
remedio=str(input("falta medicação no UPA? "))
tempo=str(input("seu atendimento é rápido? "))
equipamentos=str(input("os equipamentos estão funcionando? "))
satisfacao=float(input("de 0 a 10, qual a sua satisfação com o UPA? "))
while satisfacao>10:
    print("Insira um número entre 0 e 10")
    satisfacao=float(input("de 0 a 10, qual a sua satisfação com o UPA? "))
if UPA>=3 and médico=="sim" and enfermeiro=="sim" and remedio=="nao" and tempo=="sim" and equipamentos=="sim" and satisfacao>=5:
    print("o bairro tem uma saúde adequada.")
else:
    print("o bairro não tem uma saúde adequada.")