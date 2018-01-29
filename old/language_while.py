import re

A_OPS=["+","*","-"]

def parenthesis_block(input:str):
    res=None,None
    i=0
    n=len(input)
    open_parenthesis=False
    while i<n:
        if input[i]=="(":
            open_parenthesis=True
            break
        i+=1

    if open_parenthesis:
        j=i+1
        closing_parenthesis=False
        nb_open_parenthesis=0
        while j<n:
            if input[j]=="(":
                nb_open_parenthesis+=1
            elif input[j]==")":
                if nb_open_parenthesis==0:
                    closing_parenthesis=True
                    break
                else:nb_open_parenthesis-=1
            j+=1

        if closing_parenthesis:
            res=i+1,j-1

    return res


def parenthesis_block_len(input:str):
    i=1
    n=len(input)
    nb_open_parenthesis = 0
    while i < n:
        if input[i] == "(":
            nb_open_parenthesis += 1
        elif input[i] == ")":
            if nb_open_parenthesis == 0:
                break
            else:
                nb_open_parenthesis -= 1
        i += 1
    return i

def block_split(input:str):
    i=0
    n=len(input)
    res=[]
    buffer=""
    while i<n:
        if input[i] in A_OPS:
            res+=[buffer,input[i]]
            buffer=""
            i += 1
        elif input[i]=="(":
            b_len=parenthesis_block_len(input[i:])
            res+=[input[i+1:i+b_len]]
            i+=b_len+1
        else:
            buffer+=input[i]
            i+=1
    return res

def arithmetic_AST(input:str):
    pass



def is_Arithmetic(input:str, values):
    parse_tree=block_split(input)
    parenthesis_presence=True
    while parenthesis_presence:
        parenthesis_presence=False
        parse_tree_1=[]
        for block in parse_tree:
            if "(" in block:
                parse_tree_1+=[[block_split(block)]]
                parenthesis_presence=True
            else:
                parse_tree_1+=block
        parse_tree=parse_tree_1
    return parse_tree



def eval_Arithmetic(a_exp,values):
    pass

class B_Exp:
    pass


class C_Exp:
    pass


if __name__=="__main__":
    print("1+(2*3*(4+1)+1)")
    print(is_Arithmetic("1+(2*3*(4+1)+1)",None))