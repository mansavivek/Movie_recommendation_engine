with open('100K_movielens_baskets.txt', 'r') as f:
    baskets = [line.strip() for line in f if line.strip()]
with open('100K_movielens_baskets.arff', 'w') as f:
    f.write('@RELATION movielens_baskets\n\n')
    f.write('@ATTRIBUTE basket STRING\n\n')
    f.write('@DATA\n')
    for basket in baskets:
        f.write("'" + basket + "'\n")
        
print("ARFF file created and saved to 100K_movielens_baskets.arff")