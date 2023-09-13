#!/bin/bash
# 作るフォルダの番号の最大値
max=225
# ディレクトリ移動
cd ABC201-225
for ((i=213; i <= $max; i++)); do
   echo abc${i}
   acc new abc${i}
done
