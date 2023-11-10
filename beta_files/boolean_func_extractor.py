import re

def extract_boolean_function(verilog_code, module_name):
    # Find the module definition
    module_pattern = re.compile(r'module\s+' + re.escape(module_name) + r'\s*\(.*?\);(.*?)endmodule', re.DOTALL)
    module_match = module_pattern.search(verilog_code)

    if module_match:
        module_body = module_match.group(1)

        # Find input and output declarations
        input_pattern = re.compile(r'input\s+(.*?);', re.DOTALL)
        output_pattern = re.compile(r'output\s+(.*?);', re.DOTALL)

        input_match = input_pattern.search(module_body)
        output_match = output_pattern.search(module_body)

        if input_match and output_match:
            input_declaration = input_match.group(1)
            output_declaration = output_match.group(1)

            # Extract input and output names
            input_names = re.findall(r'\b\w+\b', input_declaration)
            output_names = re.findall(r'\b\w+\b', output_declaration)

            # Create a Boolean function string
            boolean_function = f'{", ".join(output_names)} = f({", ".join(input_names)});'
            return boolean_function

    return None

# Example usage
verilog_code = """
module MyModule (
    input A,
    input B,
    wire C,
    Wire D,
    output Y
);
    AND2X(A,B,C);
    OR3X(A,B,C,D);
    NAND2X(A,D,Y);

endmodule
"""

module_name = "MyModule"
boolean_function = extract_boolean_function(verilog_code, module_name)

if boolean_function:
    print("Boolean Function:")
    print(boolean_function)
else:
    print("Module not found or invalid Verilog code.")
