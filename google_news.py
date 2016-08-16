import gensim


print "Start..."
# Load Word2Vec model.
# the data can be download here: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/
model = gensim.models.Word2Vec.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)

## basic test
print model.most_similar(positive=['woman', 'king'], negative=['man'])[0]
# queen
print model.similarity('woman', 'man')
# 0.7664012231
print model.similarity('woman', 'woman')
# 1.0
## which wore from the given list doesn't go with the others?
print model.doesnt_match("breakfast cereal dinner lunch".split())
# cereal



## word-vector analogies
## City1 : State containing City1 : : City2 : State containing City2
print "City : State..."
print model.most_similar(positive=['Chicago', 'Houston'], negative=['Illinois'])[0]
# Dallas
print model.most_similar(positive=['Chicago', 'Philadelphia'], negative=['Illinois'])[0]
# Philly
print model.most_similar(positive=['Chicago', 'Phoenix'], negative=['Illinois'])[0]
# Los_Angeles
print model.most_similar(positive=['Chicago', 'Dallas'], negative=['Illinois'])[0]
# Houston
print model.most_similar(positive=['Chicago', 'Jacksonville'], negative=['Illinois'])[0]
# Tampa
print model.most_similar(positive=['Chicago', 'Indianapolis'], negative=['Illinois'])[0]
# Milwaukee
print model.most_similar(positive=['Chicago', 'Austin'], negative=['Illinois'])[0]
# Dallas
print model.most_similar(positive=['Chicago', 'Detroit'], negative=['Illinois'])[0]
# Detriot
print model.most_similar(positive=['Chicago', 'Memphis'], negative=['Illinois'])[0]
# Atlanta
print model.most_similar(positive=['Chicago', 'Boston'], negative=['Illinois'])[0]
# Seattle

## Capital City 1 : Country 1 : : Capital City 2 : Country 2

## superlative adjectives
print "Superlative Adjectives..."
print model.most_similar(positive=['bad', 'big'], negative=['worst'])[0]
# good
print model.most_similar(positive=['bad', 'bright'], negative=['worst'])[0]
# good
print model.most_similar(positive=['bad', 'cold'], negative=['worst'])[0]
# chilly
print model.most_similar(positive=['bad', 'cool'], negative=['worst'])[0]
# good
print model.most_similar(positive=['bad', 'dark'], negative=['worst'])[0]
# gray
print model.most_similar(positive=['bad', 'easy'], negative=['worst'])[0]
# good
print model.most_similar(positive=['bad', 'fast'], negative=['worst'])[0]
# quick
print model.most_similar(positive=['bad', 'good'], negative=['worst'])[0]
# nice
print model.most_similar(positive=['bad', 'great'], negative=['worst'])[0]
# good

## past tense
print "Past Tense..."
print model.most_similar(positive=['dancing', 'decreasing'], negative=['danced'])[0]
# increasing
print model.most_similar(positive=['dancing', 'enhancing'], negative=['danced'])[0]
# enhance
print model.most_similar(positive=['dancing', 'falling'], negative=['danced'])[0]
# dropping
print model.most_similar(positive=['dancing', 'feeding'], negative=['danced'])[0]
# feed
print model.most_similar(positive=['dancing', 'flying'], negative=['danced'])[0]
# fly
print model.most_similar(positive=['dancing', 'generating'], negative=['danced'])[0]
# generate
print model.most_similar(positive=['dancing', 'going'], negative=['danced'])[0]
# gonna
print model.most_similar(positive=['dancing', 'hiding'], negative=['danced'])[0]
# hidden
print model.most_similar(positive=['dancing', 'hitting'], negative=['danced'])[0]
# Hitting




print "End..."