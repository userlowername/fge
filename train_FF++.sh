#!/bin/bash

CUDA_VISIBLE_DEVICES="0,1" python main1.py \
--dataset 'FaceForensics++' \
--workers 8 \
--epochs 50 \
--batch-size 4 \
--lr 1e-3 \
--lr-image-encoder 1e-6 \
--lr-prompt-learner 1e-4 \
--weight-decay 1e-3 \
--momentum 0.9 \
--print-freq 10 \
--milestones 40 60 \
--contexts-number 8 \
--class-token-position "end" \
--class-specific-contexts 'True' \
--text-type 'class_descriptor' \
--seed 1 \
--temporal-layers 1 \
--load_and_tune_prompt_learner 'True'