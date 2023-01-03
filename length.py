
length = {"ym":1e-24,"zm":1e-21,"am":1e-18,"fm":1e-15,"pm":1e-12,"angstrom":1e-10,"nm":1e-9,"microm":1e-6,"mm":0.001, "cm":0.01,"dm":0.1, "m":1, "Dm":10, "hm":100,"km":1000}
 
def convert_l (val, inputU, outputU):
    return val*length[inputU]/length[outputU]
