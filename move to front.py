data = 'DCDEAABEB'
symbol = 'ABCDE'
mtfEncode = []
mtfDecode = []

def encode(data, symbol):
    print("---==[ENCODING]==---")
    listSymbol = list(symbol.strip())
    for i in range(len(data)):
        for j in range(len(symbol)):
            if data[i] == listSymbol[j]:
                mtfEncode.append(j)
                listSymbol.insert(0, listSymbol.pop(j))
        print(listSymbol)
    print("MTF encode: " + ''.join(str(x) for x in mtfEncode) + '\n')

def decode(mtfEncode, symbol):
    print("---==[DECODING]==---")
    listSymbol = list(symbol.strip())
    for i in range(len(mtfEncode)):
        for j in range(len(symbol)):
            if mtfEncode[i] == j:    
                mtfDecode.append(listSymbol[mtfEncode[i]])
                listSymbol.insert(0, listSymbol.pop(mtfEncode[i]))
        print(listSymbol)
    print("MTF decode: " + ''.join(str(x) for x in mtfDecode) + '\n')

encode(data, symbol)
decode(mtfEncode, symbol)