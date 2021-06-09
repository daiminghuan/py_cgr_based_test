contacts = range(100, 1100, 100)
nodes = range(10, 110, 10)
pairs = {}
for i in range(10):
    pair = {contacts[i] : nodes[i]}
    pairs.update(pair)
for x, y in pairs.items():
    print(x, y)
