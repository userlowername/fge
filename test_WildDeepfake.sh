#!/bin/bash

CUDA_VISIBLE_DEVICES='0' python test.py \
--dataset 'FaceForensics++' \
--text-type 'class_descriptor' \
--contexts-number 8 \
--class-token-position "end" \
--class-specific-contexts 'True' \
--seed 1 \
--temporal-layers 1 \
--load_and_tune_prompt_learner 'True'


