"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from itertools import permutations
from .core import judge, make_secret
import threading
import time

_is_playimg = False

def play_loop():
    try:
        import winsound

        melody = [
            {523,200},
            {587,200},
            {659,200},
            {698,200},
            {784,400},
            {659,400},
            {523,600},
        ]
        while _is_playing:
            for freq, duration in melody:
                if not _is_playing:
                    break
                    winsound.Beep(freq,duration)
                    time.sleep(0.1)
    except Exception
        pass

def
def make_candidates(digits=3):
    return [
        "".join(p)
        for p in permutations("0123456789", digits)
    ]

def play(digits=3):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits}桁・重複なし）")

    tries = 0

    while True:
        guess = input("予想 > ").strip()

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits}桁の数字で入力してください")
            continue

        tries += 1

        hit, blow = judge(secret, guess)

        print(f"Hit={hit} Blow={blow}")

        if hit == digits:
            print(f"正解！ {tries}回でクリア！（答え {secret}）")
            return tries


def ai_play(digits=3):
    candidates = make_candidates(digits)

    print("あなたが秘密の数字を決めてください。")
    input("決めたらEnterを押してください。")

    tries = 0

    while True:
        guess = candidates[0]
        tries += 1

        print(f"\nAIの予想：{guess}")

        hit = int(input("Hit > "))
        blow = int(input("Blow > "))

        if hit == digits:
            print(f"\nAIが {tries} 回で正解しました！")
            return tries

        candidates = [
            c
            for c in candidates
            if judge(c, guess) == (hit, blow)
        ]

        if not candidates:
            print("入力されたHit・Blowが矛盾しています。")
            return None

def versus():
    print("======================")
    print("      AI対戦モード")
    print("======================")

    print("\n【AIのターン】")
    ai_tries = ai_play()

    if ai_tries is None:
        return

    print("\n======================")
    print("   今度はあなたの番！")
    print("======================")

    player_tries = play()

    print("\n====== RESULT ======")
    print(f"AI      : {ai_tries} 回")
    print(f"Player  : {player_tries} 回")

    if ai_tries < player_tries:
        print("🤖 AIの勝ち！")

    elif ai_tries > player_tries:
        print("🎉 あなたの勝ち！")

    else:
        print("🤝 引き分け！")

mode = input("""
1 : 通常モード
2 : AI対戦モード

> """).strip()

if mode == "1":
    play()

elif mode == "2":
    versus()

else:
    print("1 または 2 を入力してください。")