#!/bin/bash
# 作るフォルダの番号の最大値
max=25
# ディレクトリ移動
cd ABC001-025
for ((i=10; i <= $max; i++)); do
   echo abc${i}
   acc new abc0${i}
done
