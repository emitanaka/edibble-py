from treelib import Node, Tree

class Design:
    """
    Instantiate a edibble design object.

    :param title: An optional title.
    """
    def __init__(self, title):
        self.title = title
        self.graph = {
            "factor": {
                "nodes": [],
                "edges": []
            },
            "level": []
        }
    
    __last_ids = {
        "fct_nodes": 0,
        "fct_edges": 0,
        "lvl_nodes": 0,
        "lvl_edges": 0
    }

    def __str__(self):
        fnodes = self.fct_nodes()
        fedges = self.fct_edges()
        tree = Tree()
        tree.create_node(self.title, 0)
        for id, pclass, name in fnodes:
            parentList = [edge for edge in fedges if edge[1] == id]
            if len(parentList): 
                for parent in parentList:
                    tree.create_node(name, id, parent = parent[0])
            else: 
                tree.create_node(name, id, parent = 0)
        return(repr(tree.show()))
        
        

    def __iterate_id__(self, view: str, which: str):
        self.__last_ids[view + "_" + which] += 1

    def set_fcts(self, pclass, **fcts):
        for key, value in fcts.items():
            self.__iterate_id__(view = "fct", which = "nodes")
            self.fct_nodes().append((self.__last_ids["fct_nodes"], 
                                     pclass, 
                                     key))
        return(self)

    def set_units(self, **fcts):
        self.set_fcts("unit", **fcts)
        return(self)

    def set_trts(self, **fcts):
        self.set_fcts("trt", **fcts)
        return(self)

    def fct_nodes(self):
        return(self.graph['factor']['nodes'])

    def fct_edges(self):
        return(self.graph['factor']['edges'])

    def lvl_nodes(self):
        return(self.graph['level']['nodes'])
    
    def lvl_edges(self):
        return(self.graph['level']['edges'])
    
    def __new_fct_node__(self, pclass, name, attrs):
        new_id = max(self.fct_nodes()['id'])
        new_node = (new_id, pclass, name, attrs)
        self.fct_nodes().append(new_node)

    def __fct_id__(self, name, pclass):
        fnodes = self.fct_nodes()
        if pclass is None:
            None


 
des = Design("test")
(des.set_units(plot = 2)
    .set_units(block = 2)
    .set_units(patch = 10))

print(des.fct_nodes())
des
print(des)