
class WriteinExcel:

    def __init__(self, data_list, _worksheet):
        self.data_list = data_list
        self.worksheet = _worksheet

    def Write(self):
        for lista in self.data_list:
            
            # A cada novo personagem
            lista_valores = []

            for i, (chave, valor) in enumerate(lista.items()):
                
                # Tratando dicionarios internos
                if isinstance(valor, dict):
                    for dictKey, dictValue in valor.items():
                        lista_valores.append(dictValue)
                
                # Tratando listas internas
                if(isinstance(valor, list)):
                    ListainString = " + ".join(valor)
                    lista_valores.append(ListainString)

                # Tipos comuns
                if(isinstance(valor, int) or isinstance(valor, str)):
                    lista_valores.append(valor)
            
            # Nova linha na planilha
            self.worksheet.append(lista_valores)