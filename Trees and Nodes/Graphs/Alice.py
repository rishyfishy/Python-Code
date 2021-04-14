class Node:
	def __init__(self,n):
		self.name=n
		self.neighboors=set()
		self.totalDistance=float('inf')
		self.prevNode=None
	def addNeighbor(self,v):
		if v not in self.neighbors:
			self.neighbors.add(v)
class Maze:
	def __init__(self):
		self.nodes={}

	def addNode(self,node):
		if node.name not in self.nodes:
			self.nodes[node.name]=node
			return True
		return False
	
	def addPath(self,node:str,dist:str):
		name=eval(node.name) 	#list of coords
		offset=eval(dist) 		#list of coords
		neighbor=str([a+b for a,b in zip(name,offset)])
		if node.name in nodes and neighbor in nodes:
			node.addNeighbor(nodes[neighbor])
			return True
		return False

	def printGraph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key +":"+ str(self.vertices[key].neighbors))

g=Maze()
a=Node('[0,0,0]')
g.addNode(a)
g.addNode(Node('[0,0,1]'))
g.addNode(Node('[1,0,1]'))
g.addNode(Node('[1,1,1]'))


g.addPath('[0,0,1]','[1,0,0]')
g.addPath('[1,0,1]','[0,1,0]')

g.printGraph()


# directions={'up':(0,-1),		
# 			'upright':(1,-1),	
# 			'right':(1,0),	
# 			'downright':(1,1),	
# 			'down':(0,1),	
# 			'downleft':(-1,1),	
# 			'left':(-1,0),	
# 			'upleft':(-1,-1)}

# colours={'red':1,'black':0,'yellow':-1}
