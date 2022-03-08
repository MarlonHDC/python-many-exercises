
import shutil

def escrever_arquivo(texto):
    ## CRIANDO ARQUIVO
    arquivo = open('teste.txt', 'w') ## para criar usa-se "w". Para acrescentar usa-se "a"
    ## ESCREVENDO EM ARQUIVO
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    ## ATUALIZANDO ARQUIVO
    arquivo = open(nome_arquivo, 'a')  ## para criar usa-se "w". Para acrescentar usa-se "a"
    arquivo.write(texto)
    arquivo.close()

## LER ARQUIVOS
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

## MANIPULANDO ARQUIVOS DE NOTAS
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
## FAZENDO SPLIT EM UMA STRING. TRANSFORMANDO EM UMA LISTA
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
## FAZENDO NOVO SPLIT PARA SEPARAR NOME DE NOTA
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        notas = lista_notas.pop(0)
        print(aluno)
        print (lista_notas)
        media = lambda notas: sum (int(i) for i in notas) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

## COPIAR ARQUIVO
def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/DIO/')

## MOVER ARQUIVO
def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/DIO/')



if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha. \n')
    #aluno = 'Cezar, 7, 9, 3, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')