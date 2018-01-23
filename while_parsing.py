import re

from control_graph import Graph, Vertice

def convert_file(filename):
    #Function that takes a file as entry and return the content
    #of the file as a string
    content = ""
    with open(filename, 'r') as f:
        for line in f:
            content += (line.replace("\x14","")).replace("\n", "") + " "
    
    content = content.replace("  ","")
    return content

def convert_block_to_graph(content):
    buffer_block=""
    vertices = {} #List of the vertices
    for elt in content:
        if re.match(r".*[0-9]+ :\s[A-Za-z]+\s",buffer_block):
            vertice = Vertice((buffer_block.split(" "))[-4])
            cmd = (buffer_block.split(" "))[-2]
            vertices[vertice] = cmd
            buffer_block = ""
        else:
            buffer_block += elt
    return vertices

def detect_command(string):
    if string == "if":
        

def main():
    filename = "/Users/alexandresioufi/Documents/Projets infos/IVF/verifformelle/prog.txt"
    content = convert_file(filename)
    graph = convert_block_to_graph(content)
    return graph

"""Iterate over """

