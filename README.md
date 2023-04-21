# MuTAP

This is a replication package for the article 
<a href=""><strong>Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing</strong></a>
    
The paper aims to encode the expertise of developers, learned from different source of information, into embedding vectors.<br />
These vectors are learned based on doc2vec model that is trained on three different sources of information: repository meta data, issue resolving history and API calls.<br />
![](https://github.com/ExpertiseModel/MuTAP/blob/master/diagram_mutant.png)


We name these models: dev2vec:repos, dev2vec:Issues and dev2vec:APIs <br />

### Download dev2vec:
You can download the two models dev2vec:repos and dev2vec:Issues from <a href="https://doi.org/10.5281/zenodo.7580313"><strong>here</strong></a> <br />
### Load our trained model:

```
model = Doc2Vec.load("dev2vec_repos")
model = Doc2Vec.load("dev2vec_issues")
```

The model that is used to generated embedding vectors for dev2vec:APIs is the pretrained model from the article <a href="https://ieeexplore.ieee.org/abstract/document/9401957?casa_token=G8DjJLSm2sQAAAAA:3h8AEP8d0XLzSgHaVkSal9k7AyQ1pfXt18uuCCeIyiCMEmEKqlkgR1xsaoJj-iJIbGVP-hbeRg"><strong>Representation of Developer Expertise in Open Source Software</strong></a> <br />

-------------------------------------------------------------------------------------------------------------------------------------------------
## Citation
<a href="https://arxiv.org/abs/2207.05132"><strong>Dev2vec: Representing Domain Expertise of Developers in an Embedding Space</strong></a>
```
@article{dakhel2022dev2vec,
  title={Dev2vec: Representing Domain Expertise of Developers in an Embedding Space},
  author={Dakhel, Arghavan Moradi and Desmarais, Michel C and Khomh, Foutse},
  journal={arXiv preprint arXiv:2207.05132},
  year={2022}
}
```

    
