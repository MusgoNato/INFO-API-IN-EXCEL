from classes.ConectAPI import ConectApi
from classes.HeadersInExcel import WriteHeaders
from classes.WriteInfoInExcel import WriteinExcel
import openpyxl as opy

url = "https://rickandmortyapi.com/api/character"
response = ConectApi(url)

# Requisição da API
responseDataApi = response.returnAllCharacteres()
data_List = responseDataApi['results']

# Criação da planilha
workbook = opy.Workbook()
worksheet = workbook.active

# Coleta os cabeçalhos únicos do primeiro personagem e os adiciona na planilha
cabecalhos = []
primeiro_personagem = data_List[0]
objHeaders = WriteHeaders(primeiro_personagem)
cabecalhos = objHeaders.EscreveCabecalhos()

# Insere os cabeçalhos na primeira linha
worksheet.append(cabecalhos)

# Escrevo as informações consumidas da API em meu arquivo Excel
objWriteinExcel = WriteinExcel(data_List, worksheet)
objWriteinExcel.Write()
    
# Salva a planilha
workbook.save("data.xlsx")