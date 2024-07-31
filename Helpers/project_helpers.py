import re

def color_code_to_hex(color_code):
    """
    Convert an RGB or RGBA color code to HEX format.

    Args:
    - color_code (str): The color code in RGB or RGBA format. For example, 'rgb(255, 0, 0)' or 'rgba(255, 0, 0, 1)'.

    Returns:
    - str: The color code in HEX format. For example, '#FF0000'.
    """
    # Define a function to convert individual values to a 2-digit hex
    def rgb_to_hex(r, g, b):
        return '#{:02X}{:02X}{:02X}'.format(r, g, b)
    
    # Define a function to extract and convert the values
    def parse_color_code(color_code):
        # Regex pattern to match RGB or RGBA
        pattern = re.compile(r'rgb(a?)\((\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d*\.?\d+))?\)')
        match = pattern.match(color_code)
        
        if match:
            # Extract values
            r, g, b = map(int, match.groups()[1:4])
            # Convert to HEX
            return rgb_to_hex(r, g, b)
        else:
            raise ValueError("Invalid color code format")

    # Normalize and convert the color code
    color_code = color_code.lower().strip()
    return parse_color_code(color_code)
