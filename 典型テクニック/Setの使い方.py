# setを作る
ans_set = set()
# {}でも作れる
ans_set2 = {1, 2, 3, 4}
# setに入れる
ans_set.add(1)
# setの要素数を数える(lenが使える)
len(ans_set)
# 要素を削除する(removeは存在しない値を指定するとエラーになる。discardは値が存在しない場合は何もしない)
ans_set.discard(1)
