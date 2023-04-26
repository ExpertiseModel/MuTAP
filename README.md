# MuTAP

`MuTAP` is a prompt-based learning technique to generate effective test cases with Large Language Models (LLMs). This is an implementation of a method described in 
'<strong>Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing</strong>'
The paper aims to encode the expertise of developers, learned from different source of information, into embedding vectors.<br />
These vectors are learned based on doc2vec model that is trained on three different sources of information: repository meta data, issue resolving history and API calls.<br />
![](https://github.com/ExpertiseModel/MuTAP/blob/master/diagram_mutant.png)


We name these models: dev2vec:repos, dev2vec:Issues and dev2vec:APIs <br />

### Download dev2vec:
You can download the two models dev2vec:repos and dev2vec:Issues from <a href="https://doi.org/10.5281/zenodo.7580313"><strong>here</strong></a> <br />
### Run the initial prompt on LLMC:

```
$ python generate_test_oracle.py [prompt type] [dataset] [task_num] [script name] [output prefix name] [csv report filename (.csv)]
```

### Run the semantic fix:

```
$ python semantic_err_correction.py [dataset] [task_num] [input prefix name] [output prefix name] [csv report filename (.csv)]
```

### Run generate mutants:

```
$ python Mutants_generation.py [dataset] [task_num] [input prefix name] [csv report filename (.csv)]
```

### calculte mutation score:

```
$ python Mutation_Score.py [dataset] [task_num] [testfile prefix name] [csv report filename (.csv)]
```

### prompt augmentation:

```
$ python augmented_prompt.py [prompt type] [dataset] [task_num] [input prefix name] [output prefix name] [csv report filename (.csv)]
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

    
