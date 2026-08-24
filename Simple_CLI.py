import shutil
import time 
import os   
import webbrowser


def centralizar(texto):
    linha = texto.split("\n")

    resultado = ""

    largura = shutil.get_terminal_size().columns

    for linha in linha:
        resultado += linha.strip().center(largura) + "\n"

    return resultado

titulo ="""

▀██▄   ▄██▀                             ▄█▀▄█           ▀██   ██               ▄
 █▀██▄▀ ██    ▄▄▄  ▄ ▄▄▄   ▄▄▄ ▄▄      ▐█▌  █  ▄▄▄    ▄▄ ██  ▄▄▄  ▄ ▄▄▄    ▄▄▄▀ 
 █  ▀   ██  ▄██ ██  ██ ██   ██ █       ██     ██ ██ ▄██ ▀██   ██   ██ ██  ██ ██ 
 █      ██  ██▀▀▀▀  ██ ██   ██ █       ▐█▌    ██ ██ ██▌  ██   ██   ██ ██  ▀█▄█▀ 
▄█▄    ▄██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀▄       ▀█▄▄▀ ▀█▄█▀  ▀█▄▀██▄ ▄██▄ ▄██ ██▄  ▄▀██▄
    
                          Versao Aprendendo Python
                            Primeiro prjeto sem ia 
                            
      
"""


largura = shutil.get_terminal_size().columns

def submenu_menu():
    titulo_submenu = """

 ▄▄▄▄▄▄▄▄▄  ▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄      ▄▄▄▄▄       ▄▄▄▄▄      ▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄ ▄▄▄▄ 
▐░░░░░░░░░▌▐░░░░▓░░░░▌▐░░░░░▀▀▄  ▐░░░░░▌     ▐░░░░░▌  ▄▀▀░░░░░▌▐░░░░░░░▀▀▄  ▐░░░░▓░░░░▌
▐░░░░▓░░░░▌▐░░░░▓░░░░▌▐░░░░░░░░▓ ▐░░░░░░▌   ▐░░░░░░▌ ▓░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░▓░░░░▌
▐▒▒▒▒▌▀▀▀▀ ▐▒▒▒▒▓▒▒▒▒▌▐▒▒▒▒█▒▒▒▒▌▐▒▒▒▒▒▒▒▌ ▐▒▒▒▒▒▒▒▌▐▒▒▒▒▌▀▀▀▀ ▐▒▒▒▒▒█▒▒▒▒▒▌▐▒▒▒▒▓▒▒▒▒▌
▐▓▓▓▓▌▄▄▄▄ ▐▓▓▓▓▓▓▓▓▓▌▐▓▓▓▓█▓▓▄▄▀▐▓▓▓▓▓▓▓▓▀▓▓▓▓▓▓▓▓▌▐▓▓▓▓▓▓▓▌  ▐▓▓▓▓▓█▓▓▓▓▓▌▐▓▓▓▓▓▓▓▓▓▌
▐░░░░░░░░░▌▐░░░░▓░░░░▌▐░░░░▄░░▀▄ ▐░░░░▄░░░░░░░▄░░░░▌▐░░░░▌▄▄▄▄ ▐░░░░░█░░░░░▌▐░░░░▓░░░░▌
 ▄▄▄▄▐░░░░▌▐░░░░▓░░░░▌▐░░░░█░░░░▌▐░░░░▌▐░░░░░▌▐░░░░▌▐░░░░▌░░░░▌▐░░░░░▓░░░░░▌▐░░░░▓░░░░▌
▐▒▒▒▒█▒▒▒▒▌▐▒▒▒▒▒▒▒▒▒▌▐▒▒▒▒▒▒▒▒█ ▐▒▒▒▒▌ ▐▒▒▒▌ ▐▒▒▒▒▌▐░▒▒▒▒▒▒▒▒▌▐▒▒▒▒▒▓▒▒▒▒▒▌▐▒▒▒▒▒▒▒▒▒▌
▐▓▓▓▓▓▓▓▓▓▌ ▀▄▓▓▓▓▓▄▀ ▐▓▓▓▓▓▓▄▀  ▐▓▓▓▓▌  ▐▓▌  ▐▓▓▓▓▌ ▀▀▒▒▓▓▓▓▓▌▐▓▓▓▓▓▓▓▓▓▓▓▌ ▀▄▓▓▓▓▓▄▀ 
 ▀▀▀▀▀▀▀▀▀     ▀▀▀     ▀▀▀▀▀▀     ▀▀▀▀    ▀    ▀▀▀▀     ▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀     ▀▀▀    
                                 Versao Aprendendo Python
                                    Primeiro prjeto sem ia 
                            

                                

    """


    print(centralizar(titulo_submenu))



def submenu_linkedin():

    while True:
    
        print("1. abrir linkedin".center(largura))
        print("2. voltar".center(largura))
   

        opcao_linkedin = input("escolha uma opçao:  ")

        if opcao_linkedin == "1":
            print("abrindo linkedin...")
            webbrowser.open("https://www.linkedin.com")
            time.sleep(1)
            os.system("cls")
            submenu_menu()
            

        elif opcao_linkedin == "2":
            break

        else:
            print("opcao invalida")
        

def submenu_youtube():

    while True:
            print("1. abrir youtube".center(largura))
            print("2. abrir no canal do ET".center(largura))
            print("3. voltar".center(largura))

            opcao_youtube = input("escolha uma opcao:  ")

            if opcao_youtube == "1":
                print("abrindo youtube...")
                webbrowser.open("https://www.youtube.com")
                time.sleep(1)
                os.system("cls")
                submenu_menu()

            elif opcao_youtube == "2":
                print("abrindo no canal do ET...")
                webbrowser.open("https://www.youtube.com/@1155doET")
                time.sleep(1)
                os.system("cls")
                submenu_menu()

            elif opcao_youtube == "3":
                time.sleep(1)
                os.system("cls")
                print(centralizar(titulo))
                break
            else:
                print("opcao invalida")


def submenu_Vscode(): 

    while True:

        print("1. abrir VScode".center(largura))
        print("2. sair".center(largura))
    

        opcao_vscode = input("escolha uma opçao:  ")


        if opcao_vscode == "1":
            print("abrindo VScode...")
            os.system("code")
            time.sleep(2)
            os.system("cls")
            submenu_menu()

        elif opcao_vscode == "2":
            time.sleep(1)
            os.system("cls")
            print(centralizar(titulo))
            break

        else:
            print("opcao invalida")
   


def submenu_chatgpt():
    while True:
        print("1. abrir chatgpt".center(largura))
        print("2. sair".center(largura))
       

        opcao_chatgpt = input("escolha uma opçao:  ")


        if opcao_chatgpt == "1":
                print("abrindo chatgpt...")
                webbrowser.open("https://www.chatgpt.com")
                time.sleep(2)
                os.system("cls")
                submenu_menu()
                submenu_chatgpt()

        elif opcao_chatgpt == "2":
                os.system("cls")
                print(centralizar(titulo))
                break

        else:
            print("opcao invalida")


def submenu_github():   
    while True:
        print("1. abrir github".center(largura))
        print("2. voltar".center(largura))

        opcao_github = input("escolha uma opçao:  ")


        if opcao_github == "1":
                print("abrindo github...")
                webbrowser.open("https://www.github.com")
                time.sleep(2)
                os.system("cls")
                submenu_menu()
                submenu_github()
                


        elif opcao_github == "2":
                os.system("cls")
                print(centralizar(titulo))
                break

        else:
            print("opcao invalida")













                # parte de seleçao 

while True:


    print(centralizar(titulo))

    print()
    print("1. abrir Vscode".center(largura))
    print("2. abrir linkedin".center(largura))
    print("3. abrir youtube".center(largura))
    print("4. abrir chatgpt".center(largura))
    print("5. abrir github".center(largura))
    print("6. sair".center(largura))
    print()
    print()


    opcao = input("escolha uma opção :  ")
  

    if opcao == "1":  
        os.system("cls")
        submenu_menu()
        submenu_Vscode()
        

    elif opcao == "2": 
        os.system("cls")
        submenu_menu()
        submenu_linkedin()
        

    elif opcao == "3":
        os.system("cls")
        submenu_menu()
        submenu_youtube()


    elif opcao == "4":
        os.system("cls")
        submenu_menu()
        submenu_chatgpt()


    elif opcao == "5":
        print("abrindo github...")
        submenu_menu()
        submenu_github()

    elif opcao == "6":
        print("Saindo...".center(largura))
        break

    else:
        print("opção inválida, tente novamente.") 



    time.sleep(1)   
    os.system("cls")












      
    










