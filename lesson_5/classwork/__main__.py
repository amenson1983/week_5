import json
def get_json_data(filename):
    with open(filename, "r") as myfile:
        data_str = myfile.read()
    return data_str

if __name__ == '__main__':
    data = get_json_data('info.json')
    datastr = json.loads(data)
    count_hob = 0
    child_count = 0
    for i in datastr["hobbies"]:
        count_hob +=1
    for i in datastr["children"]:
        child_count +=1
    for child in datastr['children']:
        child1 = child["age"]
    #child2 = datastr["children"]["Bob"]

    print("String:", datastr, "\n",
          "Hobbies:", datastr["hobbies"],
          "\n Quantity: ", count_hob,
          "\n Children quant: ", child_count,
          "\n")