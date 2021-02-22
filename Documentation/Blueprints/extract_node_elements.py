import json
import sys

class CommentNode:
	def __init__(self):
		self.x = None
		self.y = None
		self.x2 = None
		self.y2 = None
		self.members = []
		self.comment = ""

class EventNode:
	def __init__(self):
		self.x = None
		self.y = None
		self.event = ""

class GenericNode():
	def __init__(self):
		self.x = None
		self.y = None
		self.name = ""
		self._class = ""

class FunctionCallNode():
	def __init__(self):
		self.x = None
		self.y = None
		self.name = ""
		self._class = ""
		self.function_name = ""

def node_in_comment(node, comment_node):
	if (node.x > comment_node.x and node.y > comment_node.y):
		if (node.x < comment_node.x2 and node.y < comment_node.y2):
			return True
	return False

comments = []
events = []
generics = []
functions = []

with open('BattleshipPlayerController.JSON', 'r') as f:
	jso = json.load(f)
	for super_node in jso['_data']:
		node_json = super_node['_data']
		if ("NodePosX" not in node_json.keys()) or ("NodePosY" not in node_json.keys()):
			print("ERROR ================================")
			print("Could not find either posx or posy for:")
			print(node_json["Name"])
		elif node_json["Class"] == "/Script/UnrealEd.EdGraphNode_Comment":
			node = CommentNode()
			node.x = node_json["NodePosX"]
			node.y = node_json["NodePosY"]
			node.x2 = node_json["NodeWidth"] + node.x
			node.y2 = node_json["NodeHeight"] + node.y
			node.name = node_json["Name"]
			node._class = node_json["Class"]
			node.comment = node_json["NodeComment"]
			node.members = []
			comments.append(node)
		elif "EventReference" in node_json.keys():
			try:
				node = EventNode()
				node.x = node_json["NodePosX"]
				node.y = node_json["NodePosY"]
				node.event = node_json["EventReference"]["MemberName"]
				events.append(node)
			except KeyError:
				print(node_json)
				print(node_json.keys())
				break
		elif "FunctionReference" in node_json.keys():
			try:
				node = FunctionCallNode()
				node.x = node_json["NodePosX"]
				node.y = node_json["NodePosY"]
				node.function_name = node_json["FunctionReference"]["MemberName"]
				node.name = node_json["Name"]
				node._class = node_json["Class"]
				functions.append(node)
			except KeyError:
				print(node_json)
				print(node_json.keys())
				break
		elif "NodePosY" in node_json.keys():
#			print(node_json, "\n\n")
			node = GenericNode()
			node.x = node_json["NodePosX"]
			node.y = node_json["NodePosY"]
			node.name = node_json["Name"]
			node._class = node_json["Class"]
			generics.append(node)

for comment_node in comments:
	for node in events:
		if (node_in_comment(node, comment_node)):
			comment_node.members.append(node)
	for node in functions:
		if (node_in_comment(node, comment_node)):
			comment_node.members.append(node)
	for node in generics:
		if (node_in_comment(node, comment_node)):
			comment_node.members.append(node)

original_stdout = sys.stdout

with open('output.md', 'w') as output:
	sys.stdout = output
	for comment_node in comments:
		print(
			"##", comment_node.comment, "\n"
			"- Name: ", comment_node.name, "\n"
			"- Class: ", comment_node._class, "\n"
			"- Members: ",
			)

		print("  - Events")
		for member_node in comment_node.members:
			if isinstance(member_node, EventNode):
				print("    - EVENT",member_node.event)

		print("  - Function Calls")
		for member_node in comment_node.members:
			if isinstance(member_node, FunctionCallNode):
				#print("\tFunction call:", member_node.function_name, "\tName:", member_node.name,"\tClass:", member_node._class)
				line = "    - Call:%-28s Name:%-28s Class:%-28s" % (member_node.function_name, member_node.name, member_node._class)
				print(line)

		print("  - Others")
		for member_node in comment_node.members:
			if isinstance(member_node, GenericNode):
				line = "    - Name:%-28s Class:%-28s" % (member_node.name, member_node._class)
				print(line)
		print()
		
sys.stdout = original_stdout
#			if "CustomFunctionName" in member_node.keys():
#				print(
#					"\tFunctionName: ", member_node['CustomFunctionName'], "\n"
#					"\tNodeName: ", member_node['Name'], "\n",
#					"\tClass: ", member_node['Class'], "\n",
#					)
		

		#if "NodeComment" in node.keys():
		#	print(
		#		"Name: ", node['Name'], "\n",
		#		"Class: ", node['Class'], "\n",
		#		"Comment: ", node["NodeComment"], "\n"
		#		)
		#elif "CustomFunctionName" in node.keys():
		#	print(
		#		"FunctionName: ", node['CustomFunctionName'], "\n"
		#		"NodeName: ", node['Name'], "\n",
		#		"Class: ", node['Class'], "\n",
		#		)
