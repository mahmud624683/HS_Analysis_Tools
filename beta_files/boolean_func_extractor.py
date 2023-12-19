import re


def verilog_to_boolean(verilog_code, module_name):
    # Extract the module instance connections
    module_instance_pattern = re.compile(rf'\b{module_name}\s*\(\s*(.*?)\s*\);', re.DOTALL)
    module_instance_match = module_instance_pattern.search(verilog_code)

    if module_instance_match:
        # Extract module connections
        connections = module_instance_match.group(1)

        # Use re.findall to handle multiple inputs correctly
        inputs_match = re.findall(r'\b(\w+)\s*,?', connections)

        # The last match is the output
        output = inputs_match[-1]

        # Store the inputs
        inputs = inputs_match[:-2]

        if inputs and output:
            # Create a Boolean function string
            boolean_function = f'{", ".join(output)} = f({", ".join(inputs)});'
            return boolean_function

    else:
        return None

# Example Verilog code
verilog_code = """
module MyModule (
    input A,
    input B,
    wire C,
    wire D,
    output Y
);
    AND2X(A,B,C);
    OR3X(A,B,C,D);
    NAND2X(A,D,Y);
endmodule
"""

# Specify the module name for which you want the boolean function
module_name = "MyModule"

# Convert Verilog to boolean function
boolean_function = verilog_to_boolean(verilog_code, module_name)

if boolean_function:
    print(f"The boolean function for {module_name} is: {boolean_function}")
else:
    print(f"No boolean function found for {module_name}")
