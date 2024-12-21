#!/usr/bin/env bash

# スクリプトが配置されているディレクトリに移動(安全のため)
cd "$(dirname "$0")"

# 基本となるmain.cppのパス。スクリプトがあるディレクトリに移動し、相対パスがスクリプト基準になるようにしています。
BASE_MAIN_CPP="./template.cpp"

# TODO:適宜書き換えること
# 001〜200まで処理
for i in $(seq 1 200); do
    # 3桁0埋め
    DIR_NUM=$(printf "%03d" $i)
    TARGET_DIR="abc${DIR_NUM}"

    # ターゲットディレクトリが存在するかチェック(存在しない場合はスキップ)
    # -dでディレクトリの存在確認
    if [ ! -d "$TARGET_DIR" ]; then
        continue
    fi

    # d, e, f の各ディレクトリを処理
    for sub in d e f; do
        SUB_DIR="${TARGET_DIR}/${sub}"

        # サブディレクトリが存在しない場合はスキップ
        if [ ! -d "$SUB_DIR" ]; then
            continue
        fi

        # main.cppが存在しない場合はコピー
        # -fでファイルの存在確認
        if [ ! -f "${SUB_DIR}/main.cpp" ]; then
            cp "$BASE_MAIN_CPP" "${SUB_DIR}/main.cpp"
        fi

        # main.pyが存在する場合、内容が空かどうかチェック。空なら削除。
        if [ -f "${SUB_DIR}/main.py" ]; then
            # ファイルが空かどうかチェック: -sはファイルサイズが0でなければtrue
            # 空ファイルの場合、-sはfalseとなる
            if [ ! -s "${SUB_DIR}/main.py" ]; then
                rm "${SUB_DIR}/main.py"
            fi
        fi

    done
done