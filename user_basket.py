import pandas as pd

ratings = pd.read_csv('u.data', sep='\t', names=['userId', 'movieId', 'rating', 'timestamp'], engine='python')
liked = ratings[ratings['rating'] >= 4]

baskets = liked.groupby('userId')['movieId'].apply(list).reset_index()
baskets.columns = ['userId', 'movies']
with open('100K_movielens_baskets.txt', 'w') as f:
    for movie_list in baskets['movies']:
        line = ','.join(map(str, movie_list))
        f.write(line + '\n')

print('Baskets created and saved to 100K_movielens_baskets.txt')
print('Total users with liked movies: ', len(baskets))
print('Total liked ratings users: ', len(liked))
    