#!/bin/bash

# 開始番号と終了番号を定義
startNumber=1
endNumber=25

cd ABC001-025
# ループで指定された範囲の番号に対応する処理を繰り返す
for ((num=startNumber; num<=endNumber; num++)); do
    # フォルダ名を生成
    ABC_FOLDER="ABC$(printf "%03d" $num)"
    abc_FOLDER="abc$(printf "%03d" $num)"

    # コピー元とコピー先のファイルパスを指定
    SOURCE_FILE="${ABC_FOLDER}/${ABC_FOLDER}_A.py"
    DEST_FILE="${abc_FOLDER}/a/main.py"

    # コピーを実行
    if [ -f "$SOURCE_FILE" ]; then
        echo "Copying from ${SOURCE_FILE} to ${DEST_FILE}"
        cp "$SOURCE_FILE" "$DEST_FILE"

        # # ABCフォルダを削除
        # rm -r "$ABC_FOLDER"
    else
        echo "Source file ${SOURCE_FILE} not found."
    fi
done

echo "Copy process completed."


echo "Copy process completed."
