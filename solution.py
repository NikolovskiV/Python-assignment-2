def version_key(version):
    parts = version.split('.')
    padded_parts = [part.zfill(8) for part in parts]  # Pad with leading zeros
    return tuple(map(int, padded_parts))

def solution(input_list):
    """
    Expected return value is a list
    """
    sorted_versions = sorted(input_list, key=version_key)
    return sorted_versions

input_list = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
result = solution(input_list)
print(result)

    # # FEL
    # return ["1.0.1 1.0 1 2.0.0"]

    # # RÄTT
    # return ["1.0.1", "1.0", "1"]
