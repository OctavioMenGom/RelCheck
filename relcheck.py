class relation:
    def __init__(self,A,R):
        self.a = A
        self.r = R
        # Types of relationship declared
        self.reflexive()
        self.symmetric()
        self.antisymmetric()
        self.transitive()
        self.is_equivalence()
        self.is_order()

        # Partitions and class of equivalence declared
        self.eq_partitions()
        self.eq_clas()

    # Reflexive relationship check
    def reflexive(self):
        # We add a empyt list to add the missing ordered pairs so the relationship will be reflexive
        mis_rel_r = []
        # We check al the elements of the A set with a for cycle
        for a in self.a:
            # If there are not all the ordered pairs (a,a) for every a in A then we add the missing pair to the list
            if (a,a) not in self.r:
                m_rel = (a,a); mis_rel_r.append(m_rel)
                # We print that it is not reflexive and the list with the missing pairs
                return ("No es reflexiva porque faltan las relaciones: "+ str(mis_rel_r))
        # In case all the elements in the set A have ordered pairs in the relationship we return a True
        return True
    
    # Symmetric relationship check
    def symmetric(self):
        # Same as before we create an empty list to nest the missing pairs so R could be symmetric
        mis_rel_s = []
        for a, b in self.r:
            # For every ordered pair (a,b) there must exist an (b,a) pair
            if (b, a) not in self.r:
                # if there is not such pair (b,a) it will be added from the cycle to the list
                m_rel = (b,a); mis_rel_s.append(m_rel)
                # if there is a single ordered pair in the missing list it wont be symmetric
                return ("No es simétrica porque faltan las relaciones: "+str(mis_rel_s))
        # if all the pairs (a,b) have one (b,a) then we have a True 
        return True

    # Antisymmetric relationship check
    def antisymmetric(self):
        # Other empty list but this time we'll add the pairs that already exist in R
        mis_rel_as = []
        for a in self.a:
            # We check for every a in A if exist (a,a)
            for a, b in self.r:
                # and if for (a,b) there is no (b,a)
                if (a,b) in self.r and (b,a) in self.r and a != b:
                    m_rel = [(a,b),(b,a)]; mis_rel_as.append(m_rel)
                    return ("No es antisimétrica porque existen las relaciones: "+str(mis_rel_as))
        return True
    # Transitive relationship check
    def transitive(self):
        # in this case we must see if there is a (a,c) pair for (a,b) and (b,c) in R
        tran_rel = []
        mis_rel_t = []
        for a in self.a:
            # for every a and b in A we want to check if there is a transition (a,b) to (b,c) so exist (a,c)
            for b in self.a:
                if (a, b) in self.r:
                    for c in self.a:
                        # in case ther is no such (a,c) pair it will be added with the corresponding (a,b) and (b,c) pairs
                        if (b, c) in self.r and (a, c) not in self.r:
                            t_rel = [(a,b), (b,c)] ;m_rel = (a,c)
                            tran_rel.append(t_rel); mis_rel_t.append(m_rel) 
                            return ("No es transitiva porque para las relaciones "+str(tran_rel)+" faltan las relaciones "+str(mis_rel_t))
        return True

    # Equivalence relationship check 
    # an equivalence relation must be reflexive, symmetric and transitive
    def is_equivalence(self):
        # first we create a list with the values of reflexive, symmetric and reflexive check
        eq = [self.reflexive(), self.symmetric(), self.transitive()]
        # and we also have a empty list were it'll added the non checked type of relationship
        l_not =[]
        miss_not = []
        # if all the values inside the list are not True then the relationship is not of equivalence
        if eq != [True, True, True]:
            # for each check on the list we want to know the ones that are not True, then add them to a list
            if eq[0] != True:
                l_not.append("reflexiva")
                miss_not.append(self.reflexive())
            elif eq[1] != True:
                l_not.append("simétrica")
                miss_not.append(self.symmetric())
            elif eq[2] != True:
                l_not.append("transitiva")
                miss_not.append(self.transitive())
            return ("La relación no es de equivalencia por qué no es: " + str(l_not)+". "
            + str(miss_not))
        else:
            return True

    # print the equivalence graph
    def equivalence_graph(self):
        # for this task we will use the networkx library for python
        import networkx as nx
        # we declare a directed graph
        G = nx.DiGraph(directed= True)
        # and add its edges from R
        G.add_edges_from(self.r)
        # if the value of is_equivalence is not True we will say it's not of equivalene
        if self.is_equivalence() != True:
            p = "No es posible mostrar el grafo pues no es relación de equivalencia"
        else:
            # else we will print the graph
            p = nx.draw_networkx(G, node_color='black', node_size=600, font_size= 15, font_color='yellow', with_labels=True, arrowsize=18, edge_color='green')
        
        return p

    # partitions of equivalence relationship 
    def eq_partitions(self):
        import networkx as nx
        # for this we need to use once again networkx library
        G = nx.DiGraph()
        # we create a graph with egdes from R
        G.add_edges_from(self.r)

        # we create an empty list that will recieve the a of the (a,b) ordered pairs from R
        xs = []
        for x,y in self.r:
            xs.append(x)
        # to drop duplicates we turn the list to a set and back again to a list
        xs = list(set(xs))
        # the next step is create a list with the relations of A with its same elements, this is represente in R
        tex = []
        # in this cycle we create sublists of elements of A related to, same again, elements of A
        for i in xs:
            z = [n for n in G.neighbors(i)]
            tex.append(z)  
        # there are missing the dictionaries that relate the values on A to the list of relations in R
        parts = {}
        keys = range(len(tex))
        # this cycle adds the related values with their lists
        for j in keys:
            parts[j+1] = tex[j]
        # if the value of is_equivalence is not True it won't print the dictionary of partitions
        if self.is_equivalence() != True:
            return ("No es posible mostrar las particiones pues no es relación de equivalencia")
        
        return parts

    # equivalence class
    def eq_clas(self):
    # is a set of all partitions subsets
    # we will use once again networkx
        import networkx as nx

        G = nx.DiGraph()
        G.add_edges_from(self.r)
        # we use the same method for the partitions
        xs = []
        for x,y in self.r:
            xs.append(x)

        xs = list(set(xs))

        tex = []
        for i in xs:
            z = [n for n in G.neighbors(i)]
            tex.append(z)

        if self.is_equivalence() != True:
            return ("No es posible mostrar la clase de equivalencia pues no es relación de equivalencia")
        # this time we don't want a dictionary but a set of subsets
        # in the tex list we will have all the tuples turned into a set
        # and then we have a set of unique sets
        return {tuple(x) for x in tex}
    # partial order relationship
    def is_order(self):
        # for R to be of partial order 
        or_p = [self.reflexive(), self.antisymmetric(), self.transitive()]
        p_not = []
        p_mis = []
        if or_p != [True, True, True]:
            if or_p[0] != True:
                p_not.append("reflexiva")
                p_mis.append(self.reflexive())
            elif or_p[1] != True:
                p_not.append("antisimétrica")
                p_mis.append(self.antisymmetric())
            elif or_p[2] != True:
                p_not.append("transitiva")
                p_mis.append(self.transitive())
            return ("La relación no es de orden parcial por qué no es: " + str(p_not)+". "
            + str(p_mis))
        else:
            return True
       
    def order_graph(self):
        
        import networkx as nx
        import random
        
        result = {}
        for a,b in self.r:
            result.setdefault(a,[]).append(b)

        result_list = []
        for a,b in self.r:
            result_list.append(a and b)

        primes = []
        for num in result_list:
            prime = True
            for i in range(2,num):
                if (num%i == 0 ):
                    prime = False
            if prime:
                primes.append(num)

        edges = {}
        rl_reverse = list(result_list)
        for a in rl_reverse:
            for b in rl_reverse:
                if (a%b==0) and (a!=b):
                    edges.setdefault(a,[]).append(b)
        
        edges_list = [(x,y) for x,y in self.r if x!=y]
        for i in list(range(1,10)):
            for a,b in edges_list:
                if b in list(edges.keys()):
                    for z in edges[b]:
                        if (z!=a) and (z%a==0):
                            while (a,b) in edges_list:
                                edges_list.remove((a,b))

        pos = {}
        randlist = list(range(1,len(list(result.keys()))+1))
        for a in (list(result.keys())):
            if a==1:
                pos.setdefault(a, ((len(list(result.keys()))/2), -len(list(result.keys()))*2-4))
            elif a in primes:
                pos.setdefault(a, (a, -len(list(result.keys()))*2))
            elif len(list(result[a])) == 1:
                exitr = random.choice(randlist)
                pos.setdefault(a,(exitr, 0))
                randlist.remove(exitr)
            else:
                exitr = random.choice(randlist)
                pos.setdefault(a, (exitr, (-len(list(result[a])))*2))
                randlist.remove(exitr)

        T = nx.Graph()
        T.add_nodes_from(list(pos.keys()))
        T.add_edges_from(edges_list)
        
        if self.is_order() != True:
            p = "No es posible mostrar el grafo pues no es relación de orden"
        else: 
            p = nx.draw(T, pos, node_color='black', node_size=600, font_size= 15, font_color='yellow', with_labels=True, arrowsize=18, edge_color='green')
        return p
        
