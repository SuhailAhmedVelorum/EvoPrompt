#!/bin/bash

set -ex

export CUBLAS_WORKSPACE_CONFIG=:16:8  
export CUDA_VISIBLE_DEVICES=0

BUDGET=5
POPSIZE=5
INITIAL_MODE=topk
LLM_TYPE=davinci
EVO_MODE=pso

for DATASET in sam
do
OUT_PATH=outputs/sum/$DATASET/alpaca/all/$EVO_MODE/bd${BUDGET}_top${POPSIZE}_${INITIAL_MODE}_init/$LLM_TYPE
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
    --position pro \
    --evo_mode $EVO_MODE \
    --llm_type $LLM_TYPE \
    --setting default \
    --initial all \
    --initial_mode $INITIAL_MODE \
    --output $OUT_PATH/seed$SEED \
    --cache_path data/sum/$DATASET/seed${SEED}/prompts_batched.json
done
python get_result.py -p $OUT_PATH > $OUT_PATH/result.txt 
done