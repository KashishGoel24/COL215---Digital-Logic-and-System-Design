import copy
def nonecount(a):
    #INPUT --> Any term corresponding to n variables.
    #OUTPUT --> The number of 'None' in the term i.e. number of variables from which the term is independent.
    nonecount = 0
    for i in range(len(a)):
        if a[i] == None:
            nonecount += 1
    return nonecount

def convert(P,n):
    #INPUT --> Term P as a string of literals and the number of variables corresponding to the minterm
    #OUTPUT --> Term P as a list of 1,0 and 'None'
    b = [None] * n
    if (P=='None'):
        return b
    nums=[]
    dist={}
    for i in range(26):
        nums.append(chr(i+ord('a')))
        dist.update({chr(i+ord('a')):i})

    for i in range(len(P)):
        if P[i] in nums:
            b[dist[P[i]]] = 1
        elif P[i] == "'":
            b[dist[P[i - 1]]] = 0
    return b

def conversion(P,n):
    #INPUT --> List of Terms P as a string of literals and the number of variables corresponding to the minterm
    #OUTPUT --> List of Terms P where each term is a list of 1,0 and 'None'
    a=[]
    for i in range(len(P)):
        a.append(convert(P[i],n))
    return a

def inverse(P):
    #INPUT --> Term P as a list of 1,0 and 'None'
    #OUTPUT --> Term P as a string of literals
    b = ""
    dict = {}
    for i in range(26):
        dict.update({i:chr(i + ord('a'))})
    for i in range(len(P)):
        if (P[i] == None):
            pass
        else:
            if (P[i] == 1):
                b += dict[i]
            else:
                b += dict[i] + "'"
    if (b==''):
        return 'None'
    return b

def inverse_conversion(P):
    #INPUT --> List of Terms P as a list of 1,0 and 'None'
    #OUTPUT --> List of Terms P where each term is a string of literals
    a=[]
    for i in range(len(P)):
        a.append(inverse(P[i]))
    return a

def generate_minterm(term):
    #OUTPUT --> For every term, return list of all the possible minterms which can be added to it by converting 'None' to 1 and 0
    #Generates minterms which when expanded give us term
    if (nonecount(term)==0):
        return [term]
    else:
        i = 0
        while (i < len(term)):
            if (term[i] != None):
                i += 1
            else:
                break
            #i= index of first None
        reducedterm1=copy.deepcopy(term)
        reducedterm2=copy.deepcopy(term)
        reducedterm1[i]=0
        reducedterm2[i]=1
        list1=generate_minterm(reducedterm1)
        list2=generate_minterm(reducedterm2)
        return list1+list2

def next_possible_mintermsforexpansion(term):
    #OUTPUT--> For every term, returns all the possible minterms with which the term can be combined and the region can be expanded
    #gives us the set of minterms that can be possibly used for the next expansion for a given term by tryying to remove exactly one bit
    list=[]
    for i in range(len(term)):
        if(term[i]==0 or  term[i]==1):
            newterm=copy.deepcopy(term)
            newterm[i]= int(not newterm[i])
            list.append((i, generate_minterm(newterm)))  #appending the minterm along with the literal which has been changed to otin the terms of possible expansion 
        else:
            pass
    return list

def list_subset(A,B):
    # checks is A is a Subset of B
    for i in range(len(A)):
        if (A[i] in B):
            pass
        else:
            return False
    return True

def update(i,term):
    #A helper function for function 'exhausted addition', it updates the term once it is added to some other term
    #it expands the term by removing the variable at ith position
    a=copy.deepcopy(term)
    a[i]=None
    return a

def exhausted_addition(term,checklist):
    # OUTPUT --> For every term which is a minterm, return the maximum region to which it can be expanded
    n = len(term)
    a = next_possible_mintermsforexpansion(term)    
    possibleaddition = False
    i=0
    while (i<len(a)) :  #checking whether it is possible to expand the region at all 
        if (list_subset(a[i][1],checklist)):
            possibleaddition=True
            break
        else:
            i+=1
    if (not possibleaddition) :
        return term
    else:
        j = 0
        while (j<len(a)):
            if(list_subset(a[j][1],checklist)):
                break
            else:
                j+=1
                # j is the index of the first instance of a possible expansion in the set of all possible expansions
        maxaddition = exhausted_addition(update(a[j][0],term),checklist)  #adding the first possible term of addition to the term.
        for i in range(len(a)):   #checking all the possible combinations of expansion and keeping the region which has the maximum size
            if(list_subset(a[i][1],checklist)):
                addition=exhausted_addition(update(a[i][0],term),checklist)
                if(nonecount(addition)>nonecount(maxaddition)):
                    maxaddition=addition
        return maxaddition


def expansion(checklist):
    #INPUT --> Any term corresponding to which we wnat to check the possible terms to which it can be expanded
    #OUTPUT --> The next legal terms of expansion for a current term and the expanded term.
    n = len(checklist[0])                      # assert n = number of variables
    while True:
        string = input("Enter Term: ")
        term = convert(string,n)
        a = next_possible_mintermsforexpansion(term)
        possibleaddition = False
        i = 0
        while (i < len(a)):
            if (list_subset(a[i][1], checklist)):
                possibleaddition = True
                break
            else:
                i += 1
        if (not possibleaddition):   #If it isn't possible to further exapnd the region cprresponding to the K-Map function given
            print("Current Term Expansion: ",string)
            print("Maximum Expansion Reached ")
            return None
        else:
            j = 0
            while (j < len(a)):
                if (list_subset(a[j][1], checklist)):
                    break
                else:
                    j += 1
            maxaddition = exhausted_addition(update(a[j][0], term), checklist)  #adding the first possible term of addition to the term.
            largestindex = j
            for i in range(len(a)):  #checking all the possible combinations of expansion and keeping the region which has the maximum size
                if (list_subset(a[i][1], checklist)):
                    addition = exhausted_addition(update(a[i][0], term), checklist)
                    if (nonecount(addition) > nonecount(maxaddition)):
                        maxaddition = addition
                        largestindex = i
            expandedterm =(update(a[largestindex][0],term))
            expansion=inverse_conversion(a[largestindex][1])
            print("Current Term Expansion: ",string)
            print("Next Legal Terms for Expansion: ",end="")
            for s in expansion:
                print(f"{s}, ",end="")
            print("\n","Expanded Term: ",inverse(expandedterm))
    return None


def show_expansion(func_TRUE,func_DC):
    #INPUT --> List of minterms which are 1 and x corresponding to the k-map given
    #OUTPUT --> The next legal terms of expansion for a current term and the expanded term.
    n = 0
    for i in range(len(func_TRUE[0])):
        if (func_TRUE[0][i]!="'"):
            n+=1
    checklist=conversion(func_TRUE+func_DC,n)
    expansion(checklist)
    return None


def comb_function_expansion(func_TRUE, func_DC):
    """
    determines the maximum legal region for each term in the K-map function
    Input Arguments: func_TRUE: list containing the terms for which the output is '1' ; func_DC: list containing the terms for which the output is 'x'
    Return: a list of terms: expanded terms in form of String literals
    """
    n = 0
    for i in range(len(func_TRUE[0])):
        if (func_TRUE[0][i] != "'"):
            n += 1
    # n is the number of variables that are being considered
    expandedterms=[]
    func_TRUE_modified=[]
    for i in range(len(func_TRUE)):
        func_TRUE_modified.append(convert(func_TRUE[i],n))      # converts terms present in func_TRUE as string literals to boolean lists
    func_DC_modified = []
    for i in range(len(func_DC)):
        func_DC_modified.append(convert(func_DC[i],n))          # converts terms present in func_DC as string literals to boolean lists
    checklist = func_DC_modified + func_TRUE_modified
    for i in range(len(func_TRUE)):
        expandedterms.append(exhausted_addition(func_TRUE_modified[i],checklist)) # for each term in func_TRUE, we give the max region using exhausted addition
    expandedterms_literals=[]
    for i in range(len(expandedterms)):
        expandedterms_literals.append(inverse(expandedterms[i])) # converting the boolean list into string literals

    return expandedterms_literals