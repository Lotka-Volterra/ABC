#!/bin/bash

# 開始番号と終了番号を定義
startNumber=251
endNumber=275

cd ABC251-275
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

    else
        echo "Source file ${SOURCE_FILE} not found."
    fi

    # コピー元とコピー先のファイルパスを指定
    SOURCE_FILEB="${ABC_FOLDER}/${ABC_FOLDER}_B.py"
    DEST_FILEB="${abc_FOLDER}/b/main.py"

    # コピーを実行
    if [ -f "$SOURCE_FILEB" ]; then
        echo "Copying from ${SOURCE_FILEB} to ${DEST_FILEB}"
        cp "$SOURCE_FILEB" "$DEST_FILEB"

    else
        echo "Source file ${SOURCE_FILEB} not found."
    fi

     # コピー元とコピー先のファイルパスを指定
    SOURCE_FILEC="${ABC_FOLDER}/${ABC_FOLDER}_C.py"
    DEST_FILEC="${abc_FOLDER}/c/main.py"

    # コピーを実行
    if [ -f "$SOURCE_FILEC" ]; then
        echo "Copying from ${SOURCE_FILEC} to ${DEST_FILEC}"
        cp "$SOURCE_FILEC" "$DEST_FILEC"

    else
        echo "Source file ${SOURCE_FILEC} not found."
    fi

    # フォルダを削除
    rm -r "$ABC_FOLDER"
done

echo "Copy process completed."
