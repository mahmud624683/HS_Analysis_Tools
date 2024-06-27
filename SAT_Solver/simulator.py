import itertools
import re

def parse_verilog(verilog_code):
    lines = verilog_code.split('\n')
    gates = {}
    inputs = []
    outputs = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("INPUT"):
            inputs.append(re.findall(r'\((.*?)\)', line)[0])
        elif line.startswith("OUTPUT"):
            outputs.append(re.findall(r'\((.*?)\)', line)[0])
        elif '=' in line:
            left, right = line.split('=')
            left = left.strip()
            right = right.strip()
            gates[left] = right
    
    return inputs, outputs, gates


def get_expression(gates, inputs, target):
    if target in gates:
        expression = gates[target]
        parts = re.findall(r'\((.*?)\)', expression)[0].split(',')
        parts_len = len(parts)
        for i in range(parts_len):
            target_gate = parts[i].strip()
            target_expression = get_expression(gates, inputs, parts[i].strip())
            if target_expression != "":
                expression = expression.replace(target_gate,target_expression)
        return expression
    elif target in inputs:
        return target
    
    return ""

def extract_output_expressions(verilog_file_path):
    with open(verilog_file_path, 'r') as file:
        verilog_code = file.read()
    
    inputs, outputs, gates = parse_verilog(verilog_code)
    expressions = {}
    
    for output in outputs:
        if output in gates:
            expressions[output] = get_expression(gates, inputs, output)
    
    return expressions,inputs


verilog_file_path = 'E:\\Personal\\SAT_Solver\\verilog_file.v'
outputs_expression, inputs = extract_output_expressions(verilog_file_path)
inputs = list(itertools.product([0, 1], repeat=len(inputs)))
for inp in inputs:
    G1gat,G4gat,G8gat,G11gat,G14gat,G17gat,G21gat,G24gat,G27gat,G30gat,G34gat,G37gat,G40gat,G43gat,G47gat,G50gat,G53gat,G56gat,G60gat,G63gat,G66gat,G69gat,G73gat,G76gat,G79gat,G82gat,G86gat,G89gat,G92gat,G95gat,G99gat,G102gat,G105gat,G108gat,G112gat,G115gat = inp
    for output, expression in outputs_expression.items():
        print(f"{output} = {eval(expression)}")