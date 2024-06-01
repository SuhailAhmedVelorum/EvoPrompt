#!/bin/bash

set -ex

export CUBLAS_WORKSPACE_CONFIG=:16:8  
export CUDA_VISIBLE_DEVICES=0

BUDGET=5
POPSIZE=5
SEED=5
INITIAL_MODE=topk
LLM_TYPE=turbo

for DATASET in sst-5
do
OUT_PATH=outputs/cls/$DATASET/alpaca/all/pso/bd${BUDGET}_top${POPSIZE}_${INITIAL_MODE}_init/$LLM_TYPE
for SEED in 5
do
python run.py \
    --seed $SEED \
    --dataset $DATASET \
    --task cls \
    --batch-size 8 \
    --prompt-num 0 \
    --sample_num 5 \
    --language_model alpaca \
    --budget $BUDGET \
    --popsize $POPSIZE \
    --position demon \
    --evo_mode pso \
    --llm_type $LLM_TYPE \
    --setting default \
    --write_step 1 \
    --initial all \
    --initial_mode $INITIAL_MODE \
    --output $OUT_PATH/seed$SEED \
    --cache_path data/cls/$DATASET/seed${SEED}/prompts_batched.json \
    --dev_file ./data/cls/$DATASET/seed${SEED}/dev.txt \
    --test_file ./data/cls/$DATASET/seed${SEED}/test.txt
done
python get_result.py -p $OUT_PATH > $OUT_PATH/result.txt 
done