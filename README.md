# EvoPrompt
This is the implementation of the paper [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers]()

## Abstract

Large Language Models (LLMs) excel in various tasks, but they rely on carefully crafted prompts that often demand substantial human effort. To automate this process, in this paper, we propose a novel framework for discrete prompt optimization, called EvoPrompt, which borrows the idea of evolutionary algorithms (EAs) as they exhibit good performance and fast convergence. To enable EAs to work on discrete prompts, which are natural language expressions that need to be coherent and human-readable, we connect LLMs with EAs. This approach allows us to simultaneously leverage the powerful language processing capabilities of LLMs and the efficient optimization performance of EAs. Specifically, abstaining from any gradients or parameters, EvoPrompt starts from a population of prompts and iteratively generates new prompts with LLMs based on the evolutionary operators, improving the population based on the development set. We optimize prompts for both closed- and open-source LLMs including GPT-3.5 and Alpaca, on 31 datasets covering language understanding, generation tasks, as well as BIG-Bench Hard (BBH) tasks. EvoPrompt significantly outperforms human-engineered prompts and existing methods for automatic prompt generation (e.g., up to 25% on BBH). Furthermore, EvoPrompt demonstrates that connecting LLMs with EAs creates synergies, which could inspire further research on the combination of LLMs and conventional algorithms.

## Quick Start

### Preparation

1. Environmental settings: `pip install -r requirements.txt`
2. Dataset download: the test data for the language understanding task can be found [here](https://nlp.cs.princeton.edu/projects/lm-bff/datasets.tar). Put the test file in the folder `./data/cls/{dataset}`

### Evolution

We instanciate two evolutionary algorithms, GA (genetic algorithm) and DE (diffenrential evolution) to evolve upon the initial population. Evolve your prompts using the following commands: 

```bash
bash scripts/cls/run_ga_alpaca.sh  # Genetic algorithm 
bash scripts/cls/run_de_alpaca.sh  # Differential evolution
```

### Inference

To evaluate a single instruction, run the following:

```bash
bash scripts/cls/eval_single_alpaca.sh  # cls
```

## Framework

For the pipeline of EvoPrompt, there are mainly three steps as follows, while for each of them algorthms, there exists slight differences to instantiate.

* Initialization: We apply prompts generated by GPT and APE as the initial population. (see in the `prompts_pre.txt` and `prompts_pre_ape.txt` under the path of each dataset)
* Evolution (mutation and crossover):  For templates used for DE and GA, see the file `./data/templates_ga` and `./data/templates_de`. We use a demonstration including one example of the algorithm implementation to get precise and expected prompt following the steps of evolution. To avoid the LLMs copying the demonstration,the demonstration of the task is different from the task of implementation. 

* Update: After each iteration, we need select which prompts should be maintained in the population to update.  For GA, we maintain top-$N$ prompts in each iteration while for DE, we replace the old prompt if the newly generated is better. 

### Genetic Algorithm

* **Selection strategy**: in each iteration, we need to select parents for mutation and crossover, as donors to child prompts. Set the argument `sel_mode` to apply different strategy. There are three choices: `["wheel", "random", "tour"]`, we use `wheel` by default.
* **Update**: After generating a population with the same size of the original population, $N$, we select top-$N$ as the new population.

### Differential Evolution

* **Design in DE**: We apply different DE templates for ablations. Specify the argument `template` to use different settings.
  * Eliminate Prompt 3: `--template v2`
  * Prompt 3 (random): add the argument `--donor_random`
  * Prompt 3 (best): `--template v1` (default setting)
  * Different part: `--template v3`
* **Update**: Different from GA, in each iteration for each prompt `p`, several donor prompts are used for the new prompt `p'`, if `p'` is better than `p`, `p` will  be replaced by `p'`. Otherwise, it will be maintained. 

## Code Strucutre

```
- automatic_prompt_engineer
    |- configs
    |- evaluation
    |- ape.py
    |- config.py
    |- evaluate.py
    |- generate.py
    |- llm.py
    |- template.py
- experiments: scripts for experiments
    |- configs
    |- data
    |- evaluation
    |- run_instruction_induction.py
    |- run_truthful_qa.py
```

## Comments

Our codebase is based on the following repo. Thanks for open-sourcing!

- [CoT-hub](https://github.com/FranxYao/chain-of-thought-hub)
- [APE](https://github.com/keirp/automatic_prompt_engineer)
- [LM-BFF](https://github.com/princeton-nlp/LM-BFF)

## ☕️ Citation

If you find this repository helpful, please consider citing our paper:

```
@article{guo2023connecting,
  title={Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers},
  author={Guo, Qingyan and Wang, Rui and Guo, Junliang and Li, Bei and Song, Kaitao and Tan, Xu and Liu, Guoqing and Bian, Jiang and Yang, Yujiu},
  journal={arXiv preprint arXiv:2309.08532},
  year={2023}
}
```
