import giphypop
g = giphypop.Giphy()
print(g)
results = [x for x in g.search('kitten')]
print(results[0])
