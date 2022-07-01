# WN18RR

## Dataset Description

WN18RR is a link prediction dataset created from WN18, which is a subset of WordNet (a large lexical database of English). It has a total of 93,003 triplets with 40,943 entities and 18 unique relationships.

Statistics:
- Nodes: 40943
- Edges: 93003

#### Citation

```
@inproceedings{dettmers2018convolutional,
  title={Convolutional 2d knowledge graph embeddings},
  author={Dettmers, Tim and Minervini, Pasquale and Stenetorp, Pontus and Riedel, Sebastian},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={32},
  number={1},
  year={2018}
}
```

## Available Tasks

### Knowledge Graph Completion

+ Task type: `EntityLinkPrediction`
    - Predict the tail (head) entity given a pair of relation and head (tail).
+ Task type: `RelationLinkPrediction`
    - Predict the relation edge given a pair of head and tail entities.

#### Citation

##### Link Prediction Task

```
@article{padia2019knowledge,
    title={Knowledge graph fact prediction via knowledge-enriched tensor factorization},
    author={Padia, Ankur and Kalpakis, Konstantinos and Ferraro, Francis and Finin, Tim},
    journal={Journal of Web Semantics},
    volume={59},
    pages={100497},
    year={2019},
    publisher={Elsevier}
}
```

##### Train, Validation, Test Split

```
@inproceedings{han2018openke,
    title={OpenKE: An Open Toolkit for Knowledge Embedding},
    author={Han, Xu and Cao, Shulin and Lv Xin and Lin, Yankai and Liu, Zhiyuan and Sun, Maosong  and Li, Juanzi},
    booktitle={Proceedings of EMNLP},
    year={2018}
}
```

## Preprocessing

The data files and task config file in GLB format are transformed from the [OpenKE](https://github.com/thunlp/OpenKE) implementation.

### Requirements

The preprocessing code requires the following packages.

```
scipy==1.7.1
```