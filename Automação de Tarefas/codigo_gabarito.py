# Passo a passo do projeto
# Passo 1: Entrar  no Sistema da Empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui # para instalar: pip install pyautogui no prompt de comando
import time
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey-> atalho (combinação de teclas)n 
    

pyautogui.PAUSE = 0.3

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

# esperar o site carregar //importar a bilbioteca "import time"//
time.sleep(3)

# Passo 2: Fazer login 
pyautogui.click(x=3210, y=646)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab") #passa para o campo de senha 
pyautogui.write("<PASSWORD>")

pyautogui.press("tab") #passei para o botão de login
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de dados do produto
#pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    # Passo 4: Cadastrar 1 Produto
    pyautogui.click(x=3180, y=446)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]

    #preencher os campos 
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):        
           pyautogui.write(str("obs"))  


    #apertar para enviar 
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
# Passo 5: Repetir o cadastro para todos os produtos 
