# CITESEER

## Dataset Description

The CITESEER dataset contains a citation network with with documents as nodes and citations as edges. Each node has bag-of-words features of the document and a class label represents the research area this document belongs to.

Statistics:
- Nodes: 3327
- Edges: 9228
- Number of Classes: 6

#### Citation

```
@article{sen2008collective,
  title={Collective classification in network data},
  author={Sen, Prithviraj and Namata, Galileo and Bilgic, Mustafa and Getoor, Lise and Galligher, Brian and Eliassi-Rad, Tina},
  journal={AI magazine},
  volume={29},
  number={3},
  pages={93--93},
  year={2008}
}
```

## Available Tasks

### Planetoid

- Task type: `NodeClassification`

This is a node classification task with fixed split from [planetoid](https://github.com/kimiyoung/planetoid).

#### Citation

```
@inproceedings{yang2016revisiting,
  title={Revisiting semi-supervised learning with graph embeddings},
  author={Yang, Zhilin and Cohen, William and Salakhudinov, Ruslan},
  booktitle={International conference on machine learning},
  pages={40--48},
  year={2016},
  organization={PMLR}
}
```

## Preprocessing

The data files and task config file in GLB format are transformed from the DGL implementation. Run `python transform_citeseer.py` to generate the GLB format files.


### Requirements

The preprocessing code requires the following packages.

```
scipy==1.7.1
dgl-cuda11.3==0.7.2
```