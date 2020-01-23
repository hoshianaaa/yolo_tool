#!/usr/bin/env python
# -*- coding: utf8 -*-
import os

NAME = 'neji6'
CLASS_NUM = 1

dir_path = './' + NAME
backup_dir_path = dir_path + '/backup'

os.makedirs(backup_dir_path, exist_ok=True)

with open(backup_dir_path + '/empty_file','w') as f:
  pass

with open(dir_path + '/config.data','w') as f:
  text = 'class=' + str(CLASS_NUM) + '\n'
  text += 'train=' + '/' + NAME + '/' + 'data/train.list' + '\n'
  text += 'valid=' + '/' + NAME + '/' + 'data/test.list' + '\n'
  text += 'names=' + '/' + NAME + '/' + 'names.list' + '\n'
  text += 'backup=' + '/' + NAME + '/' + 'backup' + '\n'
  f.write(text)

with open(dir_path + '/names.list','w') as f:
  pass


