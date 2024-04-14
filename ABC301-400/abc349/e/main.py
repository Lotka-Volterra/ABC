import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)


def check_winner(board):
    # 横、縦、斜めのラインをチェック
    lines = [
        board[0],
        board[1],
        board[2],  # 横ライン
        [board[0][0], board[1][0], board[2][0]],  # 縦ライン
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],  # 斜めライン
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in lines:
        if all(x == "Takahashi" for x in line):
            return "Takahashi"
        if all(x == "Aoki" for x in line):
            return "Aoki"
    return None  # 勝者なし


def best_move(board, turn, scores, current_score):
    if not any(" " in row for row in board):  # もう空きマスがない場合
        return current_score
    # Aのターンの場合、best-scoreを負の無限大にする。Bのターンの場合、best-scoreを正の無限大にする
    best_score = -float("inf") if turn == "Takahashi" else float("inf")
    # next_turnに次のターンのプレイヤーを保存
    next_turn = "Aoki" if turn == "Takahashi" else "Takahashi"
    # 盤面を探索
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = turn
                score = scores[i][j] if turn == "Takahashi" else -scores[i][j]
                winner = check_winner(board)
                if winner:
                    new_score = (
                        current_score + score
                        if winner == "Takahashi"
                        else current_score - score
                    )
                else:
                    new_score = best_move(
                        board, next_turn, scores, current_score + score
                    )

                board[i][j] = " "
                if turn == "Takahashi":
                    best_score = max(best_score, new_score)
                else:
                    best_score = min(best_score, new_score)
    return best_score


def tic_tac_toe_game(scores):
    # 初期状態のボード（すべて空きマス）
    board = [[" " for _ in range(3)] for _ in range(3)]
    result = best_move(board, "Takahashi", scores, 0)
    return "Takahashi" if result > 0 else "Aoki"


scores = [list(map(int, input().split())) for _ in range(3)]
print(tic_tac_toe_game(scores))
