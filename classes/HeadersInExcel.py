class WriteHeaders:

    responseHeaders = []

    def __init__(self, personagemDeReferencia):
        self.personagem = personagemDeReferencia

    def EscreveCabecalhos(self):
        # Contrução dos cabeçalhos
        for chave, valor in self.personagem.items(): 

            # Se caso for um dicionario, construo um placeholder com base na chave e subchave do dicionario, para evitar duplicação
            if isinstance(valor, dict):  
                for subchave in valor.keys():
                    self.responseHeaders.append(f"{chave}_{subchave}")
            else:
                # Adiciono a chave principal
                self.responseHeaders.append(chave)

        return self.responseHeaders