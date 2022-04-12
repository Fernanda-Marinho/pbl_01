"""Autor: Fernanda Marinho Silva
Componente Curricular: MI - Algoritmos I
Concluido em: 08/04/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação."""

#Contadoras de todos os itens (básicos e extra), que foram doados por pessoas físicas 

acucar_pessoas_fisicas = 0 
arroz_pessoas_fisicas = 0 
cafe_pessoas_fisicas = 0 
ext_tomate_pessoas_fisicas = 0
macarrao_pessoas_fisicas = 0
bolacha_pessoas_fisicas = 0
oleo_pessoas_fisicas = 0 
farinha_trigo_pessoas_fisicas = 0
feijao_pessoas_fisicas = 0
sal_pessoas_fisicas = 0
item_extra_pessoas_fisicas = 0

#Contadoras de todos os itens (básicos e extra), que foram doados por pessoas jurídicas 

acucar_pessoas_juridicas = 0 
arroz_pessoas_juridicas = 0 
cafe_pessoas_juridicas = 0 
ext_tomate_pessoas_juridicas = 0
macarrao_pessoas_juridicas = 0
bolacha_pessoas_juridicas = 0
oleo_pessoas_juridicas = 0 
farinha_trigo_pessoas_juridicas = 0
feijao_pessoas_juridicas = 0
sal_pessoas_juridicas = 0 
item_extra_pessoas_juridicas = 0

#Contadoras necessárias referentes às cestas 
cesta = 0
cesta_com_item_extra = 0 


print("="*60)
print("\tBEM VINDO(A) AO DISPENSÁRIO SANTANA!")
print("\nDigite 1 para começar as doações:")

cond_1 = input()  #Responsável pelo while principal rodar, o que possibilita várias pessoas doarem 

#Validação de que o que o usuário digitar será um número entre 1 e 2, todas as seguintes 
#validações desse tipo irei chamar apenas de "validação de MENU"
while cond_1.isdigit() == False or int(cond_1) != 1:
    cond_1 = input("Por favor, digite o NÚMERO 1\n") 
    
#While principal     
while cond_1 == "1": 
    print("\nQual tipo de doador você é:")
    print("1)Pessoa Física")
    print("2)Pessoa Jurídica")
    tipo_doador = input()
    
    #Validação de MENU 
    while tipo_doador.isdigit() == False or int(tipo_doador) < 1 or int(tipo_doador) > 2:
        tipo_doador = input("Por favor, digite um NÚMERO entre 1 e 2!\n")
        
    if tipo_doador == "1":

        #Começa o processo de doação por pessoa física 
        nome = input("\nDigite seu nome:\n")
        
        #Validação de que o que o usuário digitar será somente letras
        while nome.isalpha() == False:
            nome = input("Por favor, digite apenas LETRAS:\n")
            
        cond_2 = "1" #Responsável pelo while secundário rodar, o que possibilita a mesma pessoa
                     #realizar mais de uma doação 
        
        #While secundário 
        while cond_2 == "1": 
            
            #O while secundário roda a cada doação de pessoa física, não é necessário 
            #perguntar o nome do doador novamente pois quando esse while roda, o doador já se 
            #identifica lá em cima 
            print(f"\n{nome}, qual tipo de item você deseja doar:")
            print("1)Itens Básicos")
            print("2)Itens Extras")
            tipo_item = input()
            
            #Validação de MENU 
            while tipo_item.isdigit() == False or int(tipo_item) < 1 or int(tipo_item) > 2:
                tipo_item = input("Por favor, digite um NÚMERO entre 1 e 2!\n")
                
            if tipo_item == "1":
                print("\tDigite qual item básico você deseja doar:")
                print("\t1) Açúcar")
                print("\t2) Arroz")
                print("\t3) Café")
                print("\t4) Extrato de tomate")
                print("\t5) Macarrão")
                print("\t6) Bolacha")
                print("\t7) Óleo")
                print("\t8) Farinha de Trigo")
                print("\t9) Feijão")
                print("\t0) Sal")
                escolha_item = input()
                
                #Validação de MENU 
                while escolha_item.isdigit() == False or int(escolha_item) < 0 or \
                int(escolha_item) > 9:
                    escolha_item = input("Por favor, digite um NÚMERO entre 0 e 9!\n")
                
                if escolha_item == "1":      #Caso o usuário escolha "Açúcar"
                    quantidade = input("Digite a quantidade de açúcar que você deseja doar:\n")
                    
                    #Validação caso o usuário digite um número negativo. Irei chamar outras
                    #desse tipo de "Validação de negativos"
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    acucar_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "2":    #Caso o usuário escolha "Arroz"
                    quantidade = input("Digite a quantidade de arroz que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    arroz_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "3":    #Caso o usuário escolha "Café"
                    quantidade = input("Digite a quantidade de café que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    cafe_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "4":    #Caso o usuário escolha "Extrato de Tomate"
                    quantidade = input("Digite a quantidade de extrato de tomate que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    ext_tomate_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "5":    #Caso o usuário escolha "Macarrão"
                    quantidade = input("Digite a quantidade de macarrão que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    macarrao_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "6":    #Caso o usuário escolha "Bolacha"
                    quantidade = input("Digite a quantidade de bolacha que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    bolacha_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "7":     #Caso o usuário escolha "Óleo"
                    quantidade = input("Digite a quantidade de óleo que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    oleo_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "8":    #Caso o usuário escolha "Farinha de Trigo"
                    quantidade = input("Digite a quantidade de Farinha de trigo que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    farinha_trigo_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "9":    #Caso o usuário escolha "Feijão"
                    quantidade = input("Digite a quantidade de feijão que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    feijao_pessoas_fisicas += int(quantidade)
                    
                elif escolha_item == "0":    #Caso o usuário escolha "Sal"
                    quantidade = input("Digite a quantidade de sal que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    sal_pessoas_fisicas += int(quantidade)
                    
                    
            if tipo_item == "2": 
                #Doação de Item Extra 
                nome_item_extra = input(f"\n{nome}, digite o nome do item extra que você irá doar:\n")
                
                #Validação para o que for digitado seja somente letras
                while nome_item_extra.isalpha() == False:
                    nome_item_extra = input("Por favor, digite apenas LETRAS!\n")
                quantidade = input(f"Digite a quantidade de {nome_item_extra} que você deseja doar:\n")
                
                #Validação de negativos
                while quantidade.isdigit() == False or int(quantidade) < 0:
                    quantidade = input("Por favor, digite um número POSITIVO!\n")
                item_extra_pessoas_fisicas += int(quantidade)

            print(f"\n{nome}, deseja realizar outra doação?")
            print("1)Sim")
            print("2)Não")
            
            #Confirmação para o while secundário rodar novamente,
            #permitindo doações diferentes de uma mesma pessoa 
            cond_2 = input()
            
            #Validação de MENU
            while cond_2.isdigit() == False or int(cond_2) < 1 or int(cond_2) > 2:
                cond_2 = input("Por favor, digite um NÚMERO entre 1 e 2!\n") 
            
    if tipo_doador == "2":
        #Começa o processo de doação por pessoa jurídica 
        
        nome = input("\nDigite seu nome:\n")
        cond_2 = "1"  #Responsável pelo while secundário rodar, o que possibilita a mesma pessoa
                      #realizar mais de uma doação 
        
        #While secundário               
        while cond_2 == "1": 
            #O while secundário roda a cada doação de pessoa física, não é necessário 
            #perguntar o nome do doador novamente pois quando esse while roda, o doador já se 
            #identifica lá em cima
            
            print(f"\n{nome}, qual tipo de item você deseja doar:")
            print("1)Itens Básicos")
            print("2)Itens Extras")
            tipo_item = input()
            
            #Validação de MENU 
            while tipo_item.isdigit() == False or int(tipo_item) < 1 or int(tipo_item) > 2:
                tipo_item = input("Por favor, digite um NÚMERO entre 1 e 2!\n")
            
            if tipo_item == "1":
                print("\tDigite qual item básico você deseja doar:")
                print("\t1) Açúcar")
                print("\t2) Arroz")
                print("\t3) Café")
                print("\t4) Extrato de tomate")
                print("\t5) Macarrão")
                print("\t6) Bolacha")
                print("\t7) Óleo")
                print("\t8) Farinha de Trigo")
                print("\t9) Feijão")
                print("\t0) Sal")
                escolha_item = input()
                
                #Validação de MENU 
                while escolha_item.isdigit() == False or int(escolha_item) < 0 or \
                int(escolha_item) > 9:
                    escolha_item = input("Por favor, digite um NÚMERO entre 0 e 9!\n")
                
                if escolha_item == "1":    #Caso o usuário escolha "Açúcar"
                    quantidade = input("Digite a quantidade de açúcar que você deseja doar:\n")
                    
                    #Validação caso o usuário digite um número negativo. Irei chamar outras
                    #desse tipo de "Validação de negativos"
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    acucar_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "2":    #Caso o usuário escolha "Arroz"
                    quantidade = input("Digite a quantidade de arroz que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    arroz_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "3":    #Caso o usuário escolha "Café"
                    quantidade = input("Digite a quantidade de café que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    cafe_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "4":    #Caso o usuário escolha "Extrato de Tomate"
                    quantidade = input("Digite a quantidade de extrato de tomate que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    ext_tomate_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "5":    #Caso o usuário escolha "Macarrão"
                    quantidade = input("Digite a quantidade de macarrão que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    macarrao_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "6":    #Caso o usuário escolha "Bolacha"
                    quantidade = input("Digite a quantidade de bolacha que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    bolacha_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "7":    #Caso o usuário escolha "Óleo"
                    quantidade = input("Digite a quantidade de óleo que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    oleo_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "8":    #Caso o usuário escolha "Farinha de Trigo"
                    quantidade = input("Digite a quantidade de Farinha de trigo que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    farinha_trigo_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "9":    #Caso o usuário escolha "Feijão"
                    quantidade = input("Digite a quantidade de feijão que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    feijao_pessoas_juridicas += int(quantidade)
                    
                elif escolha_item == "0":    #Caso o usuário escolha "Sal"
                    quantidade = input("Digite a quantidade de sal que você deseja doar:\n")
                    
                    #Validação de negativos
                    while quantidade.isdigit() == False or int(quantidade) < 0:
                        quantidade = input("Por favor, digite um número POSITIVO!\n")
                    sal_pessoas_juridicas += int(quantidade)
                    
                    
            if tipo_item == "2":
                #Doação de Item Extra 
                
                nome_item_extra = input(f"\n{nome}, digite o nome do item extra que você irá doar:\n")
                
                #Validação para o que for digitado seja somente letras
                while nome_item_extra.isalpha() == False:
                    nome_item_extra = input("Por favor, digite apenas LETRAS!\n")
                quantidade = input(f"Digite a quantidade de {nome_item_extra} que você deseja doar:\n")
                
                #Validação de negativos
                while quantidade.isdigit() == False or int(quantidade) < 0:
                    quantidade = input("Por favor, digite um número POSITIVO!\n")
                item_extra_pessoas_juridicas += int(quantidade)
            
            print(f"\n{nome}, deseja realizar outra doação?")
            print("1)Sim")
            print("2)Não")
            
            #Confirmação para o while secundário rodar novamente,
            #permitindo doações diferentes de uma mesma pessoa
            cond_2 = input()
            
            #Validação de MENU
            while cond_2.isdigit() == False or int(cond_2) < 1 or int(cond_2) > 2:
                cond_2 = input("Por favor, digite um NÚMERO entre 1 e 2!\n")
            
            
    print("\tAGRADECEMOS A SUA DOAÇÃO")
    print("="*60)
    print("\tBEM VINDO(A) AO DISPENSÁRIO SANTANA!")
    print("\nO que você deseja fazer?")
    print("1)Doações")
    print("2)Exibir relatório parcial")
    print("3)Exibir relatório Final")
    resp = input()
    
    #Validação de MENU
    while resp.isdigit() == False or int(resp) < 1 or int(resp) > 3:
        resp = input("Por favor, digite um NÚMERO entre 1 e 3!\n")

    if resp == "2":
        #Exibição do relatório parcial 

        #Contadoras totais de todos os itens
        acucar_total = acucar_pessoas_fisicas + acucar_pessoas_juridicas 
        arroz_total = arroz_pessoas_fisicas + arroz_pessoas_juridicas
        cafe_total = cafe_pessoas_fisicas + cafe_pessoas_juridicas
        ext_tomate_total = ext_tomate_pessoas_fisicas + ext_tomate_pessoas_juridicas
        macarrao_total = macarrao_pessoas_fisicas + macarrao_pessoas_juridicas
        bolacha_total = bolacha_pessoas_fisicas + bolacha_pessoas_juridicas
        oleo_total = oleo_pessoas_fisicas + oleo_pessoas_juridicas
        farinha_trigo_total = farinha_trigo_pessoas_fisicas + farinha_trigo_pessoas_juridicas
        feijao_total = feijao_pessoas_fisicas + feijao_pessoas_juridicas
        sal_total = sal_pessoas_fisicas + sal_pessoas_juridicas
        item_extra_total = item_extra_pessoas_fisicas + item_extra_pessoas_juridicas

        #Soma tudo que foi doado por pessoa física
        total_itens_pessoas_fisicas = acucar_pessoas_fisicas + arroz_pessoas_fisicas + \
        cafe_pessoas_fisicas + ext_tomate_pessoas_fisicas + macarrao_pessoas_fisicas + \
        bolacha_pessoas_fisicas + oleo_pessoas_fisicas + farinha_trigo_pessoas_fisicas + \
        feijao_pessoas_fisicas + sal_pessoas_fisicas + item_extra_pessoas_fisicas    

        #Soma tudo que foi doado por pessoas jurídicas 
        total_itens_pessoas_juridicas = acucar_pessoas_juridicas + arroz_pessoas_juridicas \
        + cafe_pessoas_juridicas + ext_tomate_pessoas_juridicas + macarrao_pessoas_juridicas \
        + bolacha_pessoas_juridicas + oleo_pessoas_juridicas + farinha_trigo_pessoas_juridicas \
        + feijao_pessoas_juridicas + sal_pessoas_juridicas + item_extra_pessoas_juridicas 

        #Total de cada item recebido;
        print("="*60)
        print("\tRELATÓRIO PARCIAL:")
        print("="*60)
        print("\tTOTAL DE CADA ITEM:")
        print("-"*60)
        print(f"\tAçúcar -> {acucar_total}Kg")
        print(f"\tArroz -> {arroz_total}Kg")
        print(f"\tCafé -> {cafe_total}Kg")
        print(f"\tExtrato de tomate -> {ext_tomate_total}Un")
        print(f"\tMacarrão -> {macarrao_total}Un")
        print(f"\tBolacha -> {bolacha_total}Pct") 
        print(f"\tÓleo -> {oleo_total}L")
        print(f"\tFarinha de Trigo -> {farinha_trigo_total}Kg")
        print(f"\tFeijão -> {feijao_total}Kg")
        print(f"\tSal -> {sal_total}Kg")
        print(f"\tItens Extras -> {item_extra_total}Un")
        print("-"*60)

        #Total de itens (independente do tipo) doados por pessoas físicas e por pessoas jurídicas
        print(f"\tTOTAL DE ITENS POR PESSOAS FÍSICAS -> {total_itens_pessoas_fisicas} Itens")   
        print(f"\tTOTAL DE ITENS POR PESSOAS JURÍDICAS -> {total_itens_pessoas_juridicas} Itens") 
        print("-"*60)
        
        #Formação de cestas
        cond_formar_cesta = True   
        while cond_formar_cesta == True:
            if acucar_total >= 1 and arroz_total >= 4 and cafe_total >= 2 and ext_tomate_total >= 2 \
            and macarrao_total >= 3 and bolacha_total >= 1 and oleo_total >= 1 and farinha_trigo_total \
            >= 1 and feijao_total >= 4 and sal_total >= 1:
                cesta += 1
                acucar_total -= 1
                arroz_total -= 4
                cafe_total -= 2
                ext_tomate_total -= 2
                macarrao_total -= 3
                bolacha_total -= 1
                oleo_total -= 1
                farinha_trigo_total -= 1
                feijao_total -= 4
                sal_total -= 1

                #Adição do Item Extra à cesta (Caso houver)
                if item_extra_total > 0:
                    cesta_com_item_extra += 1
                    item_extra_total -= 1   
                cond_formar_cesta = True
            else:
                cond_formar_cesta = False 
        cesta_sem_item_extra = cesta - cesta_com_item_extra 
                    
        #Informação sobre as cestas
        print(f"\tCESTAS BÁSICAS ATÉ O MOMENTO -> {cesta}") 
        print("-"*60)
        print(f"\tCESTAS BÁSICAS COM ITEM EXTRA ATÉ O MOMENTO -> {cesta_com_item_extra}")
        print("-"*60)
        print(f"\tCESTAS BÁSICAS SEM ITEM EXTRA ATÉ O MOMENTO -> {cesta_sem_item_extra}")
        print("-"*60)

        #Informação sobre os restos 
        print("\tSOBRARAM OS SEGUINTES ITENS ATÉ O MOMENTO:")
        print(f"\tAçúcar -> {acucar_total}")
        print(f"\tArroz -> {arroz_total}")
        print(f"\tCafé -> {cafe_total}")
        print(f"\tExtrato de Tomate -> {ext_tomate_total}")
        print(f"\tMacarrão -> {macarrao_total}")
        print(f"\tBolacha -> {bolacha_total}")
        print(f"\tÓleo -> {oleo_total}")
        print(f"\tFarinha de Trigo -> {farinha_trigo_total}")
        print(f"\tFeijão -> {feijao_total}")
        print(f"\tSal -> {sal_total}")
        print(f"\tItem Extra -> {item_extra_total}")
        print("="*60)
        print("\nFIM DO RELATÓRIO PARCIAL")
        print("="*60)


        print("\tBOAS VINDAS")
        print("\nO que você deseja fazer?")
        print("1)Doações")
        print("2)Exibir relatório Final")
        cond_1 = input()

        #Validação de MENU
        while cond_1.isdigit() == False or int(cond_1) < 1 or int(cond_1) > 2:
            cond_1= input("Por favor, digite um NÚMERO entre 1 e 2!\n")

    #Caso satisfeita, o while principal volta a rodar 
    elif resp == "1":
        cond_1 = "1"

    #Exibição do relatório final
    elif resp == "3":
        cond_1 = "3"



#Contadoras totais de todos os itens
acucar_total = acucar_pessoas_fisicas + acucar_pessoas_juridicas 
arroz_total = arroz_pessoas_fisicas + arroz_pessoas_juridicas
cafe_total = cafe_pessoas_fisicas + cafe_pessoas_juridicas
ext_tomate_total = ext_tomate_pessoas_fisicas + ext_tomate_pessoas_juridicas
macarrao_total = macarrao_pessoas_fisicas + macarrao_pessoas_juridicas
bolacha_total = bolacha_pessoas_fisicas + bolacha_pessoas_juridicas
oleo_total = oleo_pessoas_fisicas + oleo_pessoas_juridicas
farinha_trigo_total = farinha_trigo_pessoas_fisicas + farinha_trigo_pessoas_juridicas
feijao_total = feijao_pessoas_fisicas + feijao_pessoas_juridicas
sal_total = sal_pessoas_fisicas + sal_pessoas_juridicas
item_extra_total = item_extra_pessoas_fisicas + item_extra_pessoas_juridicas

#Soma tudo que foi doado por pessoa física
total_itens_pessoas_fisicas = acucar_pessoas_fisicas + arroz_pessoas_fisicas + \
cafe_pessoas_fisicas + ext_tomate_pessoas_fisicas + macarrao_pessoas_fisicas + \
bolacha_pessoas_fisicas + oleo_pessoas_fisicas + farinha_trigo_pessoas_fisicas + \
feijao_pessoas_fisicas + sal_pessoas_fisicas + item_extra_pessoas_fisicas    

#Soma tudo que foi doado por pessoa jurídica 
total_itens_pessoas_juridicas = acucar_pessoas_juridicas + arroz_pessoas_juridicas \
+ cafe_pessoas_juridicas + ext_tomate_pessoas_juridicas + macarrao_pessoas_juridicas \
+ bolacha_pessoas_juridicas + oleo_pessoas_juridicas + farinha_trigo_pessoas_juridicas \
+ feijao_pessoas_juridicas + sal_pessoas_juridicas + item_extra_pessoas_juridicas 


print("="*60)
print("\tRELATÓRIO FINAL:")
print("="*60)
print(f"\tTOTAL DE CADA ITEM:")
print("-"*60)
print(f"\tAçúcar -> {acucar_total}Kg")
print(f"\tArroz -> {arroz_total}Kg")
print(f"\tCafé -> {cafe_total}Kg")
print(f"\tExtrato de tomate -> {ext_tomate_total}Un")
print(f"\tMacarrão -> {macarrao_total}Un")
print(f"\tBolacha -> {bolacha_total}Pct") 
print(f"\tÓleo -> {oleo_total}L")
print(f"\tFarinha de Trigo -> {farinha_trigo_total}Kg")
print(f"\tFeijão -> {feijao_total}Kg")
print(f"\tSal -> {sal_total}Kg")
print(f"\tItens Extras -> {item_extra_total}Un")
print("-"*60)

#Total de itens (independente do tipo) doados por pessoas físicas e por pessoas jurídicas
print(f"\tTOTAL DE ITENS POR PESSOAS FÍSICAS -> {total_itens_pessoas_fisicas} Itens")   
print(f"\tTOTAL DE ITENS POR JURÍDICAS -> {total_itens_pessoas_juridicas} Itens") 
print("-"*60) 

#Formação de cestas
cond_formar_cesta = True
while cond_formar_cesta == True:
    if acucar_total >= 1 and arroz_total >= 4 and cafe_total >= 2 and ext_tomate_total >= 2 \
    and macarrao_total >= 3 and bolacha_total >= 1 and oleo_total >= 1 and farinha_trigo_total \
    >= 1 and feijao_total >= 4 and sal_total >= 1:
        cesta += 1
        acucar_total -= 1
        arroz_total -= 4
        cafe_total -= 2
        ext_tomate_total -= 2
        macarrao_total -= 3
        bolacha_total -= 1
        oleo_total -= 1
        farinha_trigo_total -= 1
        feijao_total -= 4
        sal_total -= 1

        #Adição do Item Extra à cesta (Caso houver)
        if item_extra_total > 0:
            cesta_com_item_extra += 1
            item_extra_total -= 1   
        cond_formar_cesta = True
    else:
        cond_formar_cesta = False 
cesta_sem_item_extra = cesta - cesta_com_item_extra 
        
#Informação sobre as cestas
print(f"\tCESTAS BÁSICAS FORMADAS -> {cesta}") 
print("-"*60)
print(f"\tCESTAS BÁSCIAS COM ITENS EXTRAS -> {cesta_com_item_extra}")
print("-"*60)
print(f"\tCESTAS BÁSICAS SEM ITENS EXTRAS -> {cesta_sem_item_extra}")
print("-"*60)

#Informação sobre os restos
print("\tSOBRARAM OS SEGUINTES ITENS:")
print(f"\tAçúcar -> {acucar_total}")
print(f"\tArroz -> {arroz_total}")
print(f"\tCafé -> {cafe_total}")
print(f"\tExtrato de Tomate -> {ext_tomate_total}")
print(f"\tMacarrão -> {macarrao_total}")
print(f"\tBolacha -> {bolacha_total}")
print(f"\tÓleo -> {oleo_total}")
print(f"\tFarinha de Trigo -> {farinha_trigo_total}")
print(f"\tFeijão -> {feijao_total}")
print(f"\tSal -> {sal_total}")
print(f"\tItem Extra -> {item_extra_total}")
