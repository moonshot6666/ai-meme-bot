def read_api_key(file_path):
    """
    Reads the API key from a specified file.
    """
    with open(file_path, 'r') as file:
        return file.read().strip()

def write_output_to_file(bot1_response, bot2_response, file_path='output.txt'):
    """
    Writes the responses of both bots to an output file.
    """
    with open(file_path, 'a') as f:  # Open in append mode
        f.write(f"<Bot1>\n{bot1_response}\n")
        f.write(f"<Bot2>\n{bot2_response}\n\n")