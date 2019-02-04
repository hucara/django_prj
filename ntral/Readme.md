# Semantic search test with gensim and LsiModel

Small Django project with a semantic search engine via REST.

This is only for testing. Expect to find crappy code.
Dataset: https://www.kaggle.com/rmisra/news-category-dataset

1. Download and place the specified dataset in the ntral/data folder.
2. Run notebooks/genism_semantic_search_lsi_tfidf.ipynb to create corpus, dictionary and indexes.
3. Run the server and query the search engine like done in query_example.py.

## Results:

For the query "illness" and results = 10:

It's obvious that the result shows the first and second document with the word "illness" in it, but the third document just contains related themes. Results that would never show up in a simple boolean Bag of Words model.

| Similarity    | DocId   | Headline  | Short description |
| ------------- |---------|-----------|-------------------|
| 0.8559768199920654 | 104044 | Staring Into the Abyss of the Criminalization of Persons With Mental Illness |  |
| 0.8063535690307617 | 120903 | Suspected Seattle Gunman Suffers From Severe Mental Illness: Lawyers |  |
| 0.8037028312683105 | 199133 | Does Depression Exist? | If you call your sadness, irritability, loneliness, disappointments, and overwhelm "the mental disorder of depression," does calling all that pain make it "the mental disorder of depression"? |
| 0.7922694683074951 | 100521 | 'There's No Shame' In Talking About Mental Illness |  |
| 0.7846556901931763 | 92275 | Mental Illness and Identity: Would I Shed My Bipolar Disorder Skin? |  |
| 0.7507518529891968 | 96541 | My Mental Collection |  |
| 0.7361612319946289 | 74773 | The Psychological Toll Of Racism In The Wake Of Mizzou | How writing about racism everyday interacts with my mental illness. |
| 0.695318341255188 | 133521 | How to Get Rid of Secrets? Tell Them | by guest blogger Cristina Negrón It took my own mental illness to fully embrace the fact that mental illness is just that |
| 0.6931425333023071 | 125753 | Finding Hope and Help in Tragedy | Whenever a person with a mental disorder (or assumed to have a mental disorder), veteran or civilian, commits a violent act that makes headlines, there is a call to address the "mental health issue" in violent crimes. However, what is meant by the "mental health issue" is generally unclear. The fact is that killings and overall violence are extremely rare by people with serious mental illness. |
| 0.6643341779708862 | 89698 | Being Vocal for Mental Health | What does it mean to be "aware" of mental health though? Of what should we be aware? |
