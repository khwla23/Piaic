#data use for fast communication, is like dictionary.
#in the form of dictionary write karwate hein but saves in the form of json.
import json
#2 methods, dump(insert) and load (get)
alphabets = [ "a", "b","c"]
with open("alpha.json","w") as f:
    json.dump(alphabets,f)

    
