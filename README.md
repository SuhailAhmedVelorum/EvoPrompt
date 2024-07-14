# 🧬 SwarmPrompt

This is the modified implementation of the paper [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://arxiv.org/abs/2309.08532) to work on Swarm Optimization Algorithms in the paper SwarmPrompt: Swarm Intelligence-Driven Prompt
Optimization using Large Language Models

## 📃 Abstract

 The advancement of Generative AI and Large Language Models (LLMs) has made developing effective text prompts challenging, particularly for less experienced users. LLMs often struggle with nuances, tone, and context, requiring precise prompt engineering for generating high-quality prompts. Previous research uses approaches such as gradient descent, reinforcement learning, and evolutionary algorithms for optimizing prompts. This paper introduces SwarmPrompt, a novel approach that utilizes swarm intelligence-based optimization techniques, specifically Particle Swarm Optimization and Grey Wolf Optimization, to enhance and optimize prompts. SwarmPrompt leverages LLMs' language processing capabilities and swarm operators to iteratively modify prompts, identifying the best-performing ones. This method reduces human intervention, outperforms human-engineered prompts, and decreases the time and resources needed for prompt optimization. Experimental results show that SwarmPrompt outperforms human-engineered prompts by 4\% for classification tasks and by 2\% for simplification and summarization tasks. 

## 🚀 Quick Start

### ⚙️ Preparation

1. **Environmental** settings: `pip install -r requirements.txt`
2. **Data** download: The test data for the language understanding task can be found [here](https://nlp.cs.princeton.edu/projects/lm-bff/datasets.tar). Put the test file in the folder `./data/cls/{dataset_name}`. For datasets of BBH, download from the repo [CoT-hub](https://github.com/FranxYao/chain-of-thought-hub/tree/main/BBH/data) and put them in the folder `BBH/data/{dataset_name}`.
3. **OpenAI API key** required: add your OpenAI API key and other related settings in the file `auth.yaml`

### ♻ Evolution

We instanciate two evolutionary algorithms, PSO (Particle Swarm Optimization) and GWO (Gray Wolf Optimization) to evolve upon the initial population. Evolve your prompts using the following commands:

Customize the parameter `--llm_type` to use `text-davinci-003`, `gpt-3.5-turbo`, `gpt-4`.

```bash
# understanding task on Alpaca
bash scripts/cls/run_pso_alpaca.sh  # Genetic algorithm
bash scripts/cls/run_gwo_alpaca.sh  # Differential evolution

# simplification task on Alpaca
bash scripts/sim/run_pso_alpaca.sh
bash scripts/sim/run_gwo_alpaca.sh

# summarization task on Alpaca
bash scripts/sum/run_pso_alpaca.sh
bash scripts/sum/run_gwo_alpaca.sh
```

### 🤔 Inference

To evaluate a single instruction, run the following, set the argument `--content` to evaluate a performance of a specific prompt

```bash
bash scripts/cls/eval_single_alpaca.sh  # understanding task on alpaca
bash scripts/sim/eval_single_alpaca.sh  # simplification
bash scripts/sum/eval_single_alpaca.sh  # summarization
```

### 📌 Notes

Note that we have two language models used in our framework, one is for evolution (argument `--llm_type`), the other for the task implementation (`--language_model`).

#### 💡Tips for Usage

The number of iteration and the population size effect the performance of EvoPrompt. There exists a trade-off between the cost and the performance. For relative simple tasks, a size of 10 and 10 iterative steps are enough, or even less. While for complex tasks, a larger population with diversity is required.

#### 🔢 Arguments

You may need to set the following arguments to customize your own configuration.

- `task`: the task category, such as `sim` (simplification), `cls`(classification), `sum`(summarization). If you need to extend this to other tasks, you may override the metric to evaluate
- `dataset`: the dataset you want to evolve prompt on
- `dev_file`: the path of the devlopment set
- `language model`: the model used for task implementation
- `llm_type`: the LLM used to evolve prompts
- `position`: this argument mainly indicates whether to use demonstration (zero-shot or few-shot)
- `sample_num`: the size of dev set, mainly used for generation task where there is no need to set the `dev_file`
- `prompt_num`: number of examples for few-shot demonstrations

## 📎 Framework

For the pipeline of SwarmPrompt, there are mainly three steps as follows, while for each of them algorthms, there exists slight differences to instantiate.

- **Initialization**: We apply prompts generated manually written or generated by GPT as the initial population. (see in the `prompts.txt` and `prompts_auto.txt` under the path of each dataset)
- **Evolution** (mutation and crossover): For templates used for DE and GA, see the file `./data/templates_ga` and `./data/templates_de`. We use a demonstration including one example of the algorithm implementation to get precise and expected prompt following the steps of evolution. To avoid the LLMs copying the demonstration,the demonstration of the task is different from the task of implementation.

- **Evaluation and update**: After each iteration, we need select which prompts should be maintained in the population to update. For GA, we maintain top-$N$ prompts in each iteration while for DE, we replace the old prompt if the newly generated is better.

## 🌳 Code Strucutre

```python
.
├── args.py
├── auth.yaml
├── BBH  # code for BBH tasks
├── data  # dataset, templates used
│   ├── cls
│   ├── sim
│   ├── sum
│   ├── template_pso.py  # templates of prompt evolution by PSO
│   ├── template_gwo.py  # templates of prompt evolution by GWO
│   └── template_v2.json  # templates for task implementation
├── dataset.py  # dataset class
├── evaluator.py  # evaluators on different tasks
├── evoluter.py  # DE, GA, APE
├── evolution.py  # DE, GA, APE
├── get_result.py
├── infer.py  # main file for inference
├── llm_client.py  # LLM query
├── metrics.py  # metric calculation
├── requirements.txt
├── run.py  # main file for evolution
├── scripts  # scripts to run the code
└── utils.py  # auxiliary functions
```

## 🧩 Possible Extension

- **Aggregation**: Based on the final population of high quality, ensembling strategies can be effectively applied upon the prompts.
- **More fine-grained metrics**: to select prompt maintained in the population, we need to evaluate the performance on dev set. However, for understanding tasks, metrics such as accuracy or F1 are coarse-grained, sometimes it's not accurate anough to select which to keep in the population since the performances of them are the same.
- **More complex tasks** are left to explore.
- **Tuning coefficients** by modifying the template to tweak the coefficients as another parameter could help in making our evolution process within the llm to be a lot more aligned to the original algorithm for these swarm optimizers.


## Acknowledgements

We'd like to thank the authors of the paper [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://arxiv.org/abs/2309.08532) for laying a solid base through their paper and well crafted testing framwork which helped us immensely while experimenting with our own paper.

The base framework is based on the following repos. Thanks for open-sourcing!

- [CoT-hub](https://github.com/FranxYao/chain-of-thought-hub)
- [APE](https://github.com/keirp/automatic_prompt_engineer)
- [LM-BFF](https://github.com/princeton-nlp/LM-BFF)

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
