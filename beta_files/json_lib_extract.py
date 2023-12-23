import re 
import json

data = {}

def get_libdef(txt):
    gate_def = txt.split("/cell(")
    gate_def.pop(0)

    gate_dict = {}
    for gate in gate_def:
        gate_name,gate=gate.split("){drive_strength")
        gate = gate.split("}pin(")[1:]
        input=[]
        output = []
        func = {}
        for pin in gate:
            pin_name=pin.split("){direction:")[0]
            direction = re.search(r'direction:\s*([a-zA-Z]+);', pin).group(1).strip()
            if direction == "output":
                temp = re.search(r'function:"(.*?)"', pin).group(1).strip()
                output.append(pin_name)
                func[pin_name]=temp

            elif direction == "input":
                input.append(pin_name)

        data[gate_name]={"input": input, "output": output, "func": func}
    
    json_file_path = "nangate_typical.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)







file = "beta_files/nangate_typical.lib"


try:
    with open(file, "r") as verilog_file:
        verilog_code = verilog_file.read()

except FileNotFoundError:
    print(f"Error: File '{file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

get_libdef(''.join(verilog_code.split()))