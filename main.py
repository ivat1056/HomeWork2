import matplotlib.pyplot as plt
import networkx as nx

print("Вариант №2 ИУ4-23Б Матвеев И.С.")
print("Визуализация графа, заданного списком рёбер")

class graf(): # класс создает объект граф с набором методов 
    def __init__(self,allvertex,edgess):
        self.vertex = allvertex
        self.edges = edgess
    def output(self):
        print(f'Вершины: {self.vertex}')
        print(f'Ребра: {self.edges}')

def read_txt(name_of_txt): # считывает данные из файла в строку
    string=""
    for i in open(name_of_txt):
        string+=i
    return string
def split(string): # разделяет строку по пробела и энтарам 
    list_before= string.split("\n")
    del list_before[-1]
    for i in range(0,len(list_before)):
        list_before[i] = list_before[i].split(" ")
    return list_before
def edges(list_before): #  преобразует лист бефо в лист афтер 
    list1 = []
    list2 = []
    for i in range(0,len(list_before)):
        if(len(list_before[i])==2):
            list1.append(int(list_before[i][0]))
            list2.append(int(list_before[i][1]))
    list_after=zip(list1,list2)
    return list(set(list_after))
def vertex(list_after): # формирует список вершин (кроме одиночных)
    listvertex =[]
    for i in range(0,len(list_after)):
        listvertex.append(list_after[i][0])
        listvertex.append(list_after[i][1])
    return listvertex
def alonevertex(list_before): # формирует список одиночных вершин
    alonev = []
    for i in range(0,len(list_before)):
        if(len(list_before[i]) == 1 ):
            alonev.append(int(list_before[i][0]))
    return alonev
def allvert(listvertex,alonev): # формирует список всех вершин 
    for i in range(0,len(alonev)):
        listvertex.append(alonev[i])
    return list(set(listvertex))
string = read_txt("list_of_edges15.txt")
list_before = split(string)
list_after = edges(list_before)
edgess = list_after
listvertex =  vertex(list_after)
alonev = alonevertex(list_before)
allvertex = allvert(listvertex,alonev)
G = nx.Graph()
exgraf = graf(allvertex, list_after)
vertex = [1,2,3,4,5]
G.add_nodes_from(exgraf.vertex)
G.add_edges_from(exgraf.edges)
exgraf.output()
nx.draw(G, with_labels=1)
plt.show()
