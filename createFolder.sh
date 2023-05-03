#!/bin/bash
# 作るフォルダの番号の最大値
max=175
# ディレクトリ移動
cd ABC151-175
for ((i=166; i <= $max; i++)); do
   echo abc${i}
   acc new abc${i}
done
