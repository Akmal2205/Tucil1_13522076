import random

#FUNGSI TAMBAHAN=====================
def print_matriks(mat):
    for row in mat:
        for elem in row:
            if elem != "0":
                print(elem, end=" ")
        print()

def print_path(mat):
    for coord in mat:
        for point in coord:
            print(point,",", end=" ")
        print()

def print_token(mat, path):
    for coord in path:
        print(mat[coord[0],coord[1]], end=" ")

def indexof(elem, lst):
    for i in range(len(lst)):
        if lst[i]==elem:
            return i

def bobot_path(path, bobot, sekuens, mat):
    sum=0
    for coord in path:
        sum+=bobot[indexof(random.randint(0,len(sekuens)-1), sekuens)]
    return sum

def min_length(mat):
    min=len(mat[0])
    for row in mat:
        if len(row)<min:
            min = len(row)
    return min

def rep_combination(token, store, temp, size):#SEMUA KEMUNGKINAN SUSUNAN SEKUENS TOKEN
    if len(temp) + min_length(token) > size: 
        store+=[temp]
    else:
        for row in token:
            rep_combination(token, store, temp+row, size)

def path_finder(mat, ver, hor, sekuens, paths, iter, length, state, visited):
    if( ver < 0 or hor < 0 or ver == len(mat) or hor == len(mat[0]) or iter==length or [ver,hor] in visited):
        return
    else:
        if(mat[ver][hor] == sekuens[iter]):
            paths+=[[ver, hor]]
            iter+=1
            state = not state
        #Vertikal, true vertikal
        if state:
            path_finder(mat, ver+1, hor, sekuens, paths, iter, length, state, visited+[[ver,hor]])#bawah
            path_finder(mat, ver-1, hor, sekuens, paths, iter, length, state, visited+[[ver,hor]])#atas
        else:
            path_finder(mat, ver, hor+1, sekuens, paths, iter, length, state, visited+[[ver,hor]])#kanan
            path_finder(mat, ver, hor-1, sekuens, paths, iter, length, state, visited+[[ver,hor]])#kiri


                


#INPUT INTERFACE========================
print("Jenis input:")
print("1. File txt")
print("2. Command")
inp = int(input("Masukkan jenis input : "))

#PERCABANGAN INPUT======================
if(inp==1):
    filename=input("Masukkan nama file txt : ")
else:
    j_token = int(input())
    token_inp = input().split()
    buffer_size = int(input())
    dimension = input().split()
    j_sekuens = int(input())
    sekuens_size = int(input())

    token_mat = [[random.choice(token_inp) for _ in range(int(dimension[1]))]for _ in range(int(dimension[0]))] #MATRIKS TOKEN

    sekuens_token = [["0" for _ in range(sekuens_size)]for _ in range(j_sekuens)] #SEKUENS TOKEN

    for i in range(j_sekuens): #SEKUENS TOKEN
        for j in range(random.randint(2,sekuens_size)):
            sekuens_token[i][j]=random.choice(token_inp)
    
    for seq in sekuens_token:
        while '0' in seq:
            seq.remove('0')

    bobot = [random.randint(5, 10) for _ in range(len(token_inp))] #BOBOT PER TOKEN UNIK
    path_combinations=[]

    #ALGORITMA
    rep_combination(sekuens_token, path_combinations, [], buffer_size)
    final_path=[]
    print_matriks(token_mat)
    print(sekuens_token)
    print(path_combinations)
    for seq in path_combinations:
        for i in range(len(token_mat[0])):
            temp=[]
            lst = list(token_mat)
            path_finder(token_mat, 0, i, seq, temp, 0, buffer_size, False, [])
            final_path+=temp
    
    print(final_path)
    #print(bobot_path(final_path, bobot, token_inp, token_mat))
    #print_token(token_mat,final_path)
    #print_path(final_path)
            
        