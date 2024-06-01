#!/bin/bash

set -ex

# ACTUAL ARGS - untested

export CUBLAS_WORKSPACE_CONFIG=:16:8
export CUDA_VISIBLE_DEVICES=0

BUDGET=1
POPSIZE=4
TEMPLATE=v1
LLM_TYPE=davinci

for dataset in asset
do
OUT_PATH=outputs/cls/$dataset/alpaca/all/pso/bd${BUDGET}_top${TEMPLATE}_template/$LLM_TYPE
for SEED in 5 10 15
do
python run.py \
    --seed $SEED \
    --dataset $dataset \
    --task cls \
    --batch-size 8 \
    --prompt-num 0 \
    --sample_num 100 \
    --language_model alpaca \
    --budget $BUDGET \
    --popsize $POPSIZE \
    --position pre \
    --evo_mode pso \
    --llm_type $LLM_TYPE \
    --initial all \
    --initial_mode para_topk \
    --template $TEMPLATE \
    --cache_path data/sim/$dataset/seed${SEED}/prompts_batched.json \
    --output $OUT_PATH/seed$SEED
done
python get_result.py -p $OUT_PATH > $OUT_PATH/result.txt
done


############
############
############
############ NEED TO PULL SOME STUFF FROM HERE
############
############

POPSIZE=10
BUDGET=10
template=v1
initial=all

for dataset in asset
do
OUT_PATH=outputs/sim/$dataset/gpt/$initial/de/bd${BUDGET}_top${POPSIZE}_topk_para_init/$template/davinci
for SEED in 5 10 15
do
python run.py \
    --seed $SEED \
    --do_test \
    --dataset $dataset \
    --task sim \
    --batch-size 20 \
    --prompt-num 0 \
    --sample_num 100 \
    --language_model gpt \
    --budget $BUDGET \
    --popsize $POPSIZE \
    --position pre \
    --evo_mode de \
    --llm_type davinci \
    --initial $initial \
    --initial_mode para_topk \
    --template $template \
    --cache_path data/sim/$dataset/seed$SEED/prompts_gpt.json \
    --output $OUT_PATH/seed${SEED}
done
python get_result.py -p $OUT_PATH > $OUT_PATH/result.txt
done