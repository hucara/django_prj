# django_prj

# fakenews

Small Django project with a fake news classifier via REST.
Dataset: https://www.kaggle.com/c/fake-news/data

A test example project with django framework that includes:
* Different web views for checking the documents stored in sqlite.
* REST api for consumption of documents.
* A classifier of fake news documents based on the dataset in kaggle.


# ntral

## Semantic search test with gensim and LsiModel

Small Django project with a semantic search engine via REST.

This is only for testing. Expect to find crappy code.
Dataset: https://www.kaggle.com/rmisra/news-category-dataset

1. Download and place the specified dataset in the ntral/data folder.
2. Run notebooks/genism_semantic_search.ipynb to create corpus, dictionary and indexes.
3. Run the server and query the search engine like done in query_example.py.

Results:

For the query "boat" and results = 10:

It's obvious that the result shows the first document with the word "boat" in it, but following documents all contain related themes like beach, water, ship. Results that would never show up in a boolean Bag of Words model.

1. ((40531, 0.72241807), 'Four Migrants Drown Off Coast Of Morocco', 'They were in an inflatable boat.')
2. ((81065, 0.6100451), "Hundreds Of Unwanted Pets Dumped On 'Dead Dog Beach'", 'A dog with a broken leg and pellet wound in his neck limps along a beach, helpless, wondering if he will ever be safe again')
3. ((40433, 0.60876673), 'Thousands Of Snow Geese Thought Dead After Landing On Toxic Mining Pit', 'Berkeley Pit is nearly 700 acres of acidic, deadly water.')
4. ((93370, 0.6077832), 'Walking With My Ancestors On Cannon Beach', ''),
5. ((75909, 0.60237277), '6 Infants Drown When Migrant Boat Capsizes Off Greek Island', 'ATHENS, Nov 1 (Reuters) - Eleven migrants including six infants drowned when their boat capsized off the Greek island of'),
6. ((78568, 0.59833413), 'Dozens Of Endangered Seals Wash Up Dead, Starving On California Beaches', 'The threatened Guadalupe fur seal could be the latest victim of the unusually warm waters in the eastern Pacific Ocean.'),
7. ((47225, 0.58883095), 'More Than 130 Bodies Recovered From Migrant Boat Capsized Off Egypt', 'The ship was carrying Africans headed for Italy.'),
8. ((76253, 0.5884743), 'Coast Guard Crew Travels Thousands Of Miles To Rescue 36 Stranded Fishermen', 'The fishermen spent more than 10 hours in skiffs after abandoning ship.'),
9. ((25472, 0.5865745), 'Blue Whale Found Dead On Northern California Beach Likely Struck By Ship', '79-foot female suffered blunt force trauma and several broken bones.'),
10. ((98799, 0.5863053), 'About 700 Migrants Rescued Off Coast Of Libya', '')]
