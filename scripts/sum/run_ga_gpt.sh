#!/bin/bash

set -ex

export CUBLAS_WORKSPACE_CONFIG=:16:8  

BUDGET=3
POPSIZE=3
GA=topk

for dataset in sam
do
OUT_PATH=outputs/sum/$dataset/gpt/all/ga/bd${BUDGET}_top${POPSIZE}_para_topk_init/$GA/davinci
for SEED in 5
do
python run.py \
    --seed $SEED \
    --dataset $dataset \
    --task sum \
    --batch-size 20 \
    --prompt-num 0 \
    --sample_num 100 \
    --language_model gpt \
    --budget $BUDGET \
    --popsize $POPSIZE \
    --position pre \
    --evo_mode ga \
    --llm_type turbo \
    --setting default \
    --initial all \
    --initial_mode para_topk \
    --ga_mode $GA \
    --cache_path data/sum/$dataset/seed$SEED/prompts_gpt.json \
    --output $OUT_PATH/seed$SEED
done
python get_result.py -p $OUT_PATH > $OUT_PATH/result.txt
done
done