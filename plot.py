import json

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import seaborn as sns

WINDOW_SIZE = 5

sac_hyperparams = {
     1: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 1, 'domain': 'cartpole-swingup', 'action_repeat': 8},
     2: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 2, 'domain': 'cartpole-swingup', 'action_repeat': 8},
     3: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 3, 'domain': 'cartpole-swingup', 'action_repeat': 8},
     4: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 1, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
     5: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 2, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
     6: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 3, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
     7: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4},
     8: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4},
     9: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4},
    10: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 1, 'domain': 'finger-spin', 'action_repeat': 2},
    11: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 2, 'domain': 'finger-spin', 'action_repeat': 2},
    12: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 3, 'domain': 'finger-spin', 'action_repeat': 2},
    13: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 1, 'domain': 'reacher-easy', 'action_repeat': 4},
    14: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 2, 'domain': 'reacher-easy', 'action_repeat': 4},
    15: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 3, 'domain': 'reacher-easy', 'action_repeat': 4},
    16: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2},
    17: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2},
    18: {'alg': 'state-sac', 'markov_lr': 0, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2},
}

rad_hyperparams = {
   1: {'alg': 'rad', 'markov_lr': 0, 'seed': 1, 'domain': 'ball_in_cup-catch', 'action_repeat': 4, 'backup_file': 'tmp/rad/ball_in_cup-catch-01-30-im108-b128-s1-pixel-tuning-rad_1/eval.log'},
   2: {'alg': 'rad', 'markov_lr': 0, 'seed': 2, 'domain': 'ball_in_cup-catch', 'action_repeat': 4, 'backup_file': 'tmp/rad/ball_in_cup-catch-01-30-im108-b128-s2-pixel-tuning-rad_2/eval.log'},
   3: {'alg': 'rad', 'markov_lr': 0, 'seed': 3, 'domain': 'ball_in_cup-catch', 'action_repeat': 4, 'backup_file': 'tmp/rad/ball_in_cup-catch-01-30-im108-b128-s3-pixel-tuning-rad_3/eval.log'},
   4: {'alg': 'rad', 'markov_lr': 0, 'seed': 1, 'domain': 'cartpole-swingup', 'action_repeat': 8, 'backup_file': 'tmp/rad/cartpole-swingup-01-30-im108-b128-s1-pixel-tuning-rad_4/eval.log'},
   5: {'alg': 'rad', 'markov_lr': 0, 'seed': 2, 'domain': 'cartpole-swingup', 'action_repeat': 8, 'backup_file': 'tmp/rad/cartpole-swingup-01-30-im108-b128-s2-pixel-tuning-rad_5/eval.log'},
   6: {'alg': 'rad', 'markov_lr': 0, 'seed': 3, 'domain': 'cartpole-swingup', 'action_repeat': 8, 'backup_file': 'tmp/rad/cartpole-swingup-01-30-im108-b128-s3-pixel-tuning-rad_6/eval.log'},
   7: {'alg': 'rad', 'markov_lr': 0, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad/cheetah-run-01-30-im108-b128-s1-pixel-tuning-rad_7/eval.log'},
   8: {'alg': 'rad', 'markov_lr': 0, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad/cheetah-run-01-30-im108-b128-s2-pixel-tuning-rad_8/eval.log'},
   9: {'alg': 'rad', 'markov_lr': 0, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad/cheetah-run-01-30-im108-b128-s3-pixel-tuning-rad_9/eval.log'},
  10: {'alg': 'rad', 'markov_lr': 0, 'seed': 1, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad/finger-spin-01-31-im108-b128-s1-pixel-tuning-finger_1/eval.log'},
  11: {'alg': 'rad', 'markov_lr': 0, 'seed': 2, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad/finger-spin-01-31-im108-b128-s2-pixel-tuning-finger_2/eval.log'},
  12: {'alg': 'rad', 'markov_lr': 0, 'seed': 3, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad/finger-spin-01-31-im108-b128-s3-pixel-tuning-finger_3/eval.log'},
  13: {'alg': 'rad', 'markov_lr': 0, 'seed': 1, 'domain': 'reacher-easy', 'action_repeat': 4, 'backup_file': 'tmp/rad/reacher-easy-01-31-im108-b128-s1-pixel-tuning-reacher_1/eval.log'},
  14: {'alg': 'rad', 'markov_lr': 0, 'seed': 2, 'domain': 'reacher-easy', 'action_repeat': 4, 'backup_file': 'tmp/rad/reacher-easy-01-31-im108-b128-s2-pixel-tuning-reacher_2/eval.log'},
  15: {'alg': 'rad', 'markov_lr': 0, 'seed': 3, 'domain': 'reacher-easy', 'action_repeat': 4, 'backup_file': 'tmp/rad/reacher-easy-01-31-im108-b128-s3-pixel-tuning-reacher_3/eval.log'},
  16: {'alg': 'rad', 'markov_lr': 0, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad/walker-walk-01-31-im84-b128-s1-pixel-tuning-rad_1/eval.log'},
  17: {'alg': 'rad', 'markov_lr': 0, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad/walker-walk-01-31-im84-b128-s2-pixel-tuning-rad_2/eval.log'},
  18: {'alg': 'rad', 'markov_lr': 0, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad/walker-walk-01-31-im84-b128-s3-pixel-tuning-rad_3/eval.log'},
}

markov_hyperparams = {
   1: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 1, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
   2: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 1, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
   3: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 1, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
   4: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 2, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
   5: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 2, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
   6: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 2, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
   7: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 3, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
   8: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 3, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
   9: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 3, 'domain': 'ball_in_cup-catch', 'action_repeat': 4},
  10: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 1, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  11: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 1, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  12: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 1, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  13: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 2, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  14: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 2, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  15: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 2, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  16: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 3, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  17: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 3, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  18: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 3, 'domain': 'cartpole-swingup', 'action_repeat': 8},
  19: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-2, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4},
  20: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-3, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4},
  21: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-4, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4},
  22: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-2, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4},
  23: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-3, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4},
  24: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-4, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4},
  25: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-2, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4},
  26: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-3, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4},
  27: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-4, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4},
  61: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-5, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s1-pixel-tuning-rad-markov-cheetah_1/eval.log'},
  62: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-5, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s2-pixel-tuning-rad-markov-cheetah_2/eval.log'},
  63: {'alg': 'rad+markov-inv_coef=1', 'markov_lr': 1e-5, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s3-pixel-tuning-rad-markov-cheetah_3/eval.log'},
  64: {'alg': 'rad+markov-inv_coef=6', 'markov_lr': 1e-5, 'inverse_coef': 6, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s1-pixel-tuning-rad-markov-cheetah_4/eval.log'},
  65: {'alg': 'rad+markov-inv_coef=6', 'markov_lr': 1e-5, 'inverse_coef': 6, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s2-pixel-tuning-rad-markov-cheetah_5/eval.log'},
  66: {'alg': 'rad+markov-inv_coef=6', 'markov_lr': 1e-5, 'inverse_coef': 6, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s3-pixel-tuning-rad-markov-cheetah_6/eval.log'},
  67: {'alg': 'rad+markov-inv_coef=6', 'markov_lr': 1e-4, 'inverse_coef': 6, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s1-pixel-tuning-rad-markov-cheetah_7/eval.log'},
  68: {'alg': 'rad+markov-inv_coef=6', 'markov_lr': 1e-4, 'inverse_coef': 6, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s2-pixel-tuning-rad-markov-cheetah_8/eval.log'},
  69: {'alg': 'rad+markov-inv_coef=6', 'markov_lr': 1e-4, 'inverse_coef': 6, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s3-pixel-tuning-rad-markov-cheetah_9/eval.log'},
  28: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 1, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s1-pixel-tuning-rad-markov_28/eval.log'},
  29: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 1, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s1-pixel-tuning-rad-markov_29/eval.log'},
  30: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 1, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s1-pixel-tuning-rad-markov_30/eval.log'},
  31: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 2, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s2-pixel-tuning-rad-markov_31/eval.log'},
  32: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 2, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s2-pixel-tuning-rad-markov_32/eval.log'},
  33: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 2, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s2-pixel-tuning-rad-markov_33/eval.log'},
  34: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 3, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s3-pixel-tuning-rad-markov_34/eval.log'},
  35: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 3, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s3-pixel-tuning-rad-markov_35/eval.log'},
  36: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 3, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/finger-spin-01-30-im108-b128-s3-pixel-tuning-rad-markov_36/eval.log'},
  37: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 1, 'domain': 'reacher-easy', 'action_repeat': 4},
  38: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 1, 'domain': 'reacher-easy', 'action_repeat': 4},
  39: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 1, 'domain': 'reacher-easy', 'action_repeat': 4},
  40: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 2, 'domain': 'reacher-easy', 'action_repeat': 4},
  41: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 2, 'domain': 'reacher-easy', 'action_repeat': 4},
  42: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 2, 'domain': 'reacher-easy', 'action_repeat': 4},
  43: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 3, 'domain': 'reacher-easy', 'action_repeat': 4},
  44: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 3, 'domain': 'reacher-easy', 'action_repeat': 4},
  45: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 3, 'domain': 'reacher-easy', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/reacher-easy-01-30-im108-b128-s3-pixel-tuning-rad-markov_45/eval.log'},
  46: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s1-pixel-tuning-rad-markov_1/eval.log'},
  47: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s1-pixel-tuning-rad-markov_2/eval.log'},
  48: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s1-pixel-tuning-rad-markov_3/eval.log'},
  49: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s2-pixel-tuning-rad-markov_4/eval.log'},
  50: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s2-pixel-tuning-rad-markov_5/eval.log'},
  51: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s2-pixel-tuning-rad-markov_6/eval.log'},
  52: {'alg': 'rad+markov', 'markov_lr': 1e-2, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s3-pixel-tuning-rad-markov_7/eval.log'},
  53: {'alg': 'rad+markov', 'markov_lr': 1e-3, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s3-pixel-tuning-rad-markov_8/eval.log'},
  54: {'alg': 'rad+markov', 'markov_lr': 1e-4, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-01-31-im84-b128-s3-pixel-tuning-rad-markov_9/eval.log'},
  71: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-4, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-01-im84-b128-s1-pixel-tuning-rad-markov-big-inv_7/eval.log'},
  72: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-4, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-01-im84-b128-s2-pixel-tuning-rad-markov-big-inv_8/eval.log'},
  73: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-4, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-01-im84-b128-s3-pixel-tuning-rad-markov-big-inv_9/eval.log'},
  74: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-4, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-01-im84-b128-s1-pixel-tuning-rad-markov-big-inv_10/eval.log'},
  75: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-4, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-01-im84-b128-s2-pixel-tuning-rad-markov-big-inv_11/eval.log'},
  76: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-4, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-01-im84-b128-s3-pixel-tuning-rad-markov-big-inv_12/eval.log'},
  81: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-4, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s1-pixel-tuning-rad-markov-big-inv_1/eval.log'},
  82: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-4, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s2-pixel-tuning-rad-markov-big-inv_2/eval.log'},
  83: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-4, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s3-pixel-tuning-rad-markov-big-inv_3/eval.log'},
  84: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-4, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s1-pixel-tuning-rad-markov-big-inv_4/eval.log'},
  85: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-4, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s2-pixel-tuning-rad-markov-big-inv_5/eval.log'},
  86: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-4, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-01-31-im108-b128-s3-pixel-tuning-rad-markov-big-inv_6/eval.log'},
  91: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-3, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-02-im84-b128-s1-pixel-tuning-rad-markov-big-inv2_7/eval.log'},
  92: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-3, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-02-im84-b128-s2-pixel-tuning-rad-markov-big-inv2_8/eval.log'},
  93: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-3, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-02-im84-b128-s3-pixel-tuning-rad-markov-big-inv2_9/eval.log'},
  94: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-3, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-02-im84-b128-s1-pixel-tuning-rad-markov-big-inv2_10/eval.log'},
  95: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-3, 'seed': 2, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-02-im84-b128-s2-pixel-tuning-rad-markov-big-inv2_11/eval.log'},
  96: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-3, 'seed': 3, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': 'tmp/rad-markov/walker-walk-02-02-im84-b128-s3-pixel-tuning-rad-markov-big-inv2_12/eval.log'},
  101: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-3, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-02-02-im108-b128-s1-pixel-tuning-rad-markov-big-inv2_1/eval.log'},
  102: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-3, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-02-02-im108-b128-s2-pixel-tuning-rad-markov-big-inv2_2/eval.log'},
  103: {'alg': 'rad+markov-inv_coef=10', 'inverse_coef': 10, 'markov_lr': 1e-3, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-02-02-im108-b128-s3-pixel-tuning-rad-markov-big-inv2_3/eval.log'},
  104: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-3, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-02-02-im108-b128-s1-pixel-tuning-rad-markov-big-inv2_4/eval.log'},
  105: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-3, 'seed': 2, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-02-02-im108-b128-s2-pixel-tuning-rad-markov-big-inv2_5/eval.log'},
  106: {'alg': 'rad+markov-inv_coef=30', 'inverse_coef': 30, 'markov_lr': 1e-3, 'seed': 3, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': 'tmp/rad-markov/cheetah-run-02-02-im108-b128-s3-pixel-tuning-rad-markov-big-inv2_6/eval.log'},

}

curl_hyperparams = {
    1: {'alg': 'curl', 'markov_lr': 0, 'seed': 1, 'domain': 'ball_in_cup-catch', 'action_repeat': 4, 'backup_file': '../gridworlds/dmcontrol/experiments/dm2gym-Ball_in_cupCatch-v0/curl-paper-results/curl/seed_001/scores.csv'},
    2: {'alg': 'curl', 'markov_lr': 0, 'seed': 1, 'domain': 'cartpole-swingup', 'action_repeat': 8, 'backup_file': '../gridworlds/dmcontrol/experiments/dm2gym-CartpoleSwingup-v0/curl-paper-results/curl/seed_001/scores.csv'},
    3: {'alg': 'curl', 'markov_lr': 0, 'seed': 1, 'domain': 'cheetah-run', 'action_repeat': 4, 'backup_file': '../gridworlds/dmcontrol/experiments/dm2gym-CheetahRun-v0/curl-paper-results/curl/seed_001/scores.csv'},
    4: {'alg': 'curl', 'markov_lr': 0, 'seed': 1, 'domain': 'finger-spin', 'action_repeat': 2, 'backup_file': '../gridworlds/dmcontrol/experiments/dm2gym-FingerSpin-v0/curl-paper-results/curl/seed_001/scores.csv'},
    5: {'alg': 'curl', 'markov_lr': 0, 'seed': 1, 'domain': 'reacher-easy', 'action_repeat': 4, 'backup_file': '../gridworlds/dmcontrol/experiments/dm2gym-ReacherEasy-v0/curl-paper-results/curl/seed_001/scores.csv'},
    6: {'alg': 'curl', 'markov_lr': 0, 'seed': 1, 'domain': 'walker-walk', 'action_repeat': 2, 'backup_file': '../gridworlds/dmcontrol/experiments/dm2gym-WalkerWalk-v0/curl-paper-results/curl/seed_001/scores.csv'},
}

dfs = []

#%%
for i in range(1,18):
    filepath = 'logs/state-sac_%d.g' % i
    params = sac_hyperparams[i]
    data = pd.read_csv(filepath, names=['steps', 'reward'])
    data['episode'] = data.steps / 1000 * params['action_repeat']
    data = data.set_index('steps')
    data['cumulative_reward'] = (data.reward*10).cumsum()
    data['cumulative_reward_per_episode'] = data.cumulative_reward / data.episode * params['action_repeat']
    for k, v in params.items():
        data[k] = v
    dfs.append(data)

#%%
for i in range(1,18):
    filepath = 'logs/tuning-rad_%d.g' % i
    params = rad_hyperparams[i]
    if params.get('backup_file', False):
        data = pd.read_json(params['backup_file'], lines=True)
        data = data.rename(columns={'step': 'steps', 'mean_episode_reward': 'reward'}).drop(columns=['episode_reward', 'eval_time', 'best_episode_reward']).set_index('steps')
    else:
        data = pd.read_csv(filepath, names=['steps', 'reward'])
        data['episode'] = data.steps / 1000 * params['action_repeat']
        data = data.set_index('steps')
    data['cumulative_reward'] = data.reward.cumsum()
    data['cumulative_reward_per_episode'] = data.cumulative_reward / data.episode * params['action_repeat']
    data.reward = data.reward.rolling(WINDOW_SIZE).mean()
    for k, v in params.items():
        if k == 'backup_file':
            continue
        data[k] = v
    dfs.append(data)

#%%

for i in list(range(1,55))+list(range(61,70))+list(range(81,87))+list(range(71,77))+list(range(101,107))+list(range(91,97)):
    filepath = 'logs/tuning-rad-markov_%d.g' % i
    params = markov_hyperparams[i]
    if params.get('backup_file', False):
        data = pd.read_json(params['backup_file'], lines=True)
        data = data.rename(columns={'step': 'steps', 'mean_episode_reward': 'reward'}).drop(columns=['episode_reward', 'eval_time', 'best_episode_reward']).set_index('steps')
    else:
        data = pd.read_csv(filepath, names=['steps','reward'])
        data['episode'] = data.steps / 1000 * params['action_repeat']
        data = data.set_index('steps')
    data['cumulative_reward'] = data.reward.cumsum()
    data['cumulative_reward_per_episode'] = data.cumulative_reward / data.episode * params['action_repeat']
    data.reward = data.reward.rolling(WINDOW_SIZE).mean()
    for k, v in params.items():
        if k == 'backup_file':
            continue
        data[k] = v
    dfs.append(data)

#%%
for i in range(1,7):
    params = curl_hyperparams[i]
    data = pd.read_csv(params['backup_file'])
    data = data.rename(columns={'step': 'steps'})
    data = data.set_index('steps')
    for k, v in params.items():
        if k == 'backup_file':
            continue
        data[k] = v
    dfs.append(data)

#%%
data = pd.concat(dfs, axis=0)
data.loc[data.inverse_coef.isnull() & (data.markov_lr > 0), 'inverse_coef'] = 1
data.loc[data.inverse_coef.isnull() & (data.markov_lr == 0), 'inverse_coef'] = 0
data.loc[((data['inverse_coef'] == 1) & (data['alg'] == 'rad+markov')), 'alg'] = 'rad+markov-inv_coef=1'
#%%
# for d in ['cartpole-swingup']:#list(data.domain.unique()):
subset = data
subset = subset.query("alg != 'curl'")
# subset = subset.query("domain == 'ball_in_cup-catch'")
# subset = subset.query("domain == 'cartpole-swingup'")
# subset = subset.query("domain == 'cheetah-run'")
# subset = subset.query("domain == 'finger-spin'")
# subset = subset.query("domain == 'reacher-easy'")
# subset = subset.query("domain == 'walker-walk'")
# subset = subset.query("domain in ['walker-walk', 'cheetah-run']")
subset = subset.query("domain != 'ball_in_cup-catch' or ((markov_lr == 0.001 or alg in ['state-sac', 'rad', 'curl']) and steps <= 100e3)")
subset = subset.query("domain != 'cartpole-swingup' or ((markov_lr == 0.0001 or alg in ['state-sac', 'rad', 'curl']) and steps <= 100e3)")
subset = subset.query("domain != 'finger-spin' or markov_lr == 0.001 or alg in ['state-sac', 'rad', 'curl']")
subset = subset.query("domain != 'reacher-easy' or markov_lr == 0.001 or alg in ['state-sac', 'rad', 'curl']")
subset = subset.query("domain != 'cheetah-run' or (markov_lr == 0.0001 and inverse_coef == 10.0) or alg in ['state-sac', 'rad', 'curl']")
# subset = subset.query("domain != 'cheetah-run' or (markov_lr == 0.0001 and inverse_coef == 30.0) or alg in ['state-sac', 'rad', 'curl']")
# subset = subset.query("domain != 'cheetah-run' or (markov_lr == 0.001 and inverse_coef == 30.0) or alg in ['state-sac', 'rad', 'curl']")
# subset = subset.query("domain != 'cheetah-run' or (markov_lr == 0.0001 and inverse_coef == 10.0) or (markov_lr == 0.0001 and inverse_coef == 30.0) or (markov_lr == 0.001 and inverse_coef == 30.0) or (markov_lr == 0.001 and inverse_coef == 10.0) or alg in ['state-sac', 'rad', 'curl']")
subset = subset.query("domain != 'walker-walk' or (markov_lr == 0.001 and inverse_coef == 10.0) or alg in ['state-sac', 'rad', 'curl']")
# subset = subset.query("domain != 'walker-walk' or (markov_lr == 0.0001 and inverse_coef == 30.0) or alg in ['state-sac', 'rad', 'curl']")
# subset = subset.query("domain != 'walker-walk' or (markov_lr == 0.0001 and inverse_coef == 30.0) or (markov_lr == 0.001 and inverse_coef == 10.0) or alg in ['state-sac', 'rad', 'curl']")

subset.loc[subset.alg.isin(['rad+markov-inv_coef=30', 'rad+markov-inv_coef=10', 'rad+markov-inv_coef=6', 'rad+markov-inv_coef=1']), 'alg'] = 'Markov+RAD'
subset.loc[subset.alg.isin(['rad']), 'alg'] = 'RAD'
subset.loc[subset.alg.isin(['state-sac']), 'alg'] = 'SAC (Expert)'

# subset = subset.query("steps <= 100e3")
# subset = subset.query("alg in ['rad', 'state-sac'] or (domain == 'cartpole-swingup' and markov_lr == 0.0001) or (domain != 'cartpole-swingup' and markov_lr == 0.001) or (domain == 'cheetah-run')")
# subset = subset[subset.index % 5000 == 0]

p = sns.color_palette('viridis', n_colors=len(subset['alg'].unique()), desat=0.5)
p[-1] = (.60,.57,.57)
# p[-1] = (.5,.3,.3)
sns.relplot(
    data=subset,
    x='steps',
    y='reward',
    hue='alg',
    hue_order=['Markov+RAD', 'RAD', 'SAC (Expert)'],
    style='alg',
    # style='markov_lr',
    col='domain',
    col_wrap=3,
    style_order=['Markov+RAD', 'RAD', 'SAC (Expert)'],
    kind='line',
    # units='seed',
    # estimator=None,
    # height=10,
    palette=p,
    facet_kws={'sharex': False, 'sharey': True},
)
# plt.title(d)
# plt.ylim([0,300])
plt.tight_layout()
plt.show()
