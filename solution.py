def version_key(version):
    # Split the version string into parts using '.' as the delimiter
    parts = version.split('.')

    # Pad each part with leading zeros to ensure they have the same length (8 digits in this case)
    padded_parts = [part.zfill(8) for part in parts]  # Pad with leading zeros

    # Convert the padded parts to integers and return them as a tuple
    return tuple(map(int, padded_parts))

def solution(input_list):
    """
    Expected return value is a list
    """
    # Sort the input list using the version_key function as the key for sorting
    sorted_versions = sorted(input_list, key=version_key)
    
    # Return the sorted list of versions
    return sorted_versions

input_list = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
result = solution(input_list)
print(result)

    # # FEL
    # return ["1.0.1 1.0 1 2.0.0"]

    # # RÄTT
    # return ["1.0.1", "1.0", "1"]
