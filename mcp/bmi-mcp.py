from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My BMI Server")

@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate the Body Mass Index (BMI) of a person.
    
    Args:
        weight_kg: The weight of the person in kilograms
        height_m: The height of the person in meters
        
    Returns:
        float: The BMI of the person
    """
    return weight_kg / (height_m ** 2)

# wasn't in original version
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')


