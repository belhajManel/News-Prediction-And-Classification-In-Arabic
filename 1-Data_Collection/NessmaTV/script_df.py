import json
import os
path_to_json = '.'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files)
def merge_JsonFiles(filename):
    result = list()
    result_name = input("Output file name : ")

    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open(result_name, 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(json_files)