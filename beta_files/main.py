import re
from visLib import Node
import json
import fileDir

#method to extract input & output pins name
def extract_inputs_outputs(verilog_code):
    input_pattern = re.compile(r'\binput\b\s*(.*?);', re.DOTALL)
    output_pattern = re.compile(r'\boutput\b\s*(.*?);', re.DOTALL)

    inputs = re.search(input_pattern, verilog_code).group(1)
    outputs = re.search(output_pattern, verilog_code).group(1)

    input_list = re.findall(r'(\w+)\s*,?', inputs)
    output_list = re.findall(r'(\w+)\s*,?', outputs)

    return input_list, output_list

#method for creating node
def create_node(name,node_type="",inputs=[],outputs=[],functn=""):
    new_node = Node(name, node_type)
    new_node.input_list= inputs
    new_node.output_list= outputs
    new_node.func = functn
    return new_node

#method for updating node
def update_node(node,name="",node_type="",input="",output="",inputs=[],outputs=[],functn=""):
    if name !="":
        node.name = name
    
    if node_type != "":
        node.node_type = node_type

    if input != "":
        node.add_input(input)

    if output != "":
        node.add_output(output)

    if len(inputs)>0:
        node.append_inputlist(inputs)

    if len(outputs)>0:
        node.append_outputlist(outputs)

    if functn != "":
        node.func = functn
    
        

#method for building gate tree
def get_node_tree(code):
    node_dict={}
    inputs, outputs = extract_inputs_outputs(code)
    #creating input and output nodes
    for input in inputs:
        input = input.strip()
        node_dict[input] = create_node(input, "input")

    for output in outputs: 
        output = output.strip()
        node_dict[output+"_reg"] = create_node(output+"_reg","output")
    
    #getting code inside the module
    code = re.search(r'module\s+(\w+)\s*\(([^)]*)\)\s*;([\s\S]*?)endmodule',code).group(3)
    codes = code.split(";")
    
    #loading nandgate_typical gate definition
    with open(fileDir.gate_lib_json, 'r') as file:
        gate_lib = json.load(file)
    
    gates_in_lib = list(gate_lib.keys())

    #iterating over the statements of the codes
    for code in codes:
        code = code.replace("\n","")
        code = code.strip()
        gate_type = code.split(" ")[0]
        
        node_inputs = []

        #Processing only the gates are defined in nandgate_typical library
        if gate_type in gates_in_lib:
            #getting input pins of the gate
            gate_inputs = gate_lib[gate_type]["input"]
            for i in range(len(gate_inputs)):
                temp = re.search(rf'\.{gate_inputs[i]}\s*\(\s*([^)]*)\s*\)',code).group(1)
                if "connect" not in temp.lower():
                    node_inputs.append(temp)

            #getting active outputs and creating nodes against each nodes
            gate_outputs = gate_lib[gate_type]["output"]
            for i in range(len(gate_outputs)):
                temp = re.search(rf'\.{gate_outputs[i]}\s*\(\s*([^)]*)\s*\)',code).group(1)
                if "connect" not in temp.lower():
                    if temp in node_dict.keys():
                        update_node(node_dict[temp],node_type=gate_type,inputs=node_inputs,functn=gate_lib[gate_type]["func"][gate_outputs[i]])
                    else:     
                        node_dict[temp] = create_node(temp,gate_type, node_inputs,functn=gate_lib[gate_type]["func"][gate_outputs[i]])

                    #update the nodes from where the inputs are came.
                    for node_input in node_inputs:
                        if node_input in node_dict.keys():
                            update_node(node_dict[node_input],output=temp)
                        else:
                            node_dict[node_input]=create_node(node_input,outputs=[temp])
    
    return node_dict

    

if __name__ == "__main__":
    file_path = "benchmark_ALL/resources/s27.v"
    try:
        with open(file_path, "r") as verilog_file:
            verilog_code = verilog_file.read()
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
  
    gate_tree = get_node_tree(verilog_code)

    for key in gate_tree.keys():
        gate_tree[key].print_node()
