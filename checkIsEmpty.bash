#!/bin/bash

# 026から050までの範囲でループ
for num in {26..50}; do
    # 対応するフォルダ名を生成
    ABC_FOLDER="ABC026-050"
    abc_FOLDER="abc0${num}"

    # 対応するaフォルダ内のmain.pyのパスを指定
    MAIN_PY_PATH="${ABC_FOLDER}/${abc_FOLDER}/b/main.py"

    # main.pyが存在し、中身が空である場合にフォルダ名を出力
    if [ -f "$MAIN_PY_PATH" ] && [ ! -s "$MAIN_PY_PATH" ]; then
        echo "$abc_FOLDER"
    fi
done
echo "Checking Completed!"
