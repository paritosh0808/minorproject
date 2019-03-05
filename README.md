# minorproject
In this project we explore Respresentational Learning in Multi-layer Networks. We aim to apply state-of-the-art feature learning
algorithms to a multi-layer blood tissue dataset whose nodes are Entrez gene IDs and edges represent protein protein interactions

The "embeddings" folder contains embeddings created with each algorithm

The "blood-data" folder contains the blood-tissue PPI dataset with the layers and the hierarchy

The "scripts" folder currently contains:
1. merge.py: Run this in the blood-data-ohmnet/edgelists folder to produce a combined file of all the layers
2. remove_dup.py: Run thus in the blood-data-ohmnet/edgelists folder to remove duplicate edgelists
3. addcol.py: Run this in the edgelists folder to bring to format required by mne
4. merge-new: merges the above newly created edgelists
