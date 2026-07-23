"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    from .bgm import start_bgm
    start_bgm()  # ゲーム開始と同時にBGMスタート！♪

    # --- AIの難易度選択を呼び出す！ ---
    from .ai import select_ai_difficulty, get_initial_candidates
    select_ai_difficulty()
    ai_candidates = get_initial_candidates(digits)
    print("🤖 [AI] 準備完了です。どちらが先に当てるか勝負開始！")

    tries = 0
    while True:
        # --- 👤 プレイヤーのターン ---
        guess = input("あなたの予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        from .hint import give_hint

        if guess == "h" or guess == "hint":
            give_hint()
            continue

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"👤 あなた: Hit={hit}  Blow={blow}")
        
        if hit == digits:
            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            from .bgm import stop_bgm
            stop_bgm()  # クリアしたらBGMを止める！
            
            # --- スコア・評定の計算と表示 ---
            from .score import calculate_score_and_grade
            score, grade = calculate_score_and_grade(digits, tries)
            print(f"★ あなたは{score}点です！評定：（{grade}）")

            from .win import celebrate
            celebrate()  # お祝いのファンファーレ♪

            print(f"🎉 正解！ {tries} 回で当たり（答え {secret}）")
            break

        # --- 🤖 AIのターン ---
        from .ai import ai_turn, filter_candidates
        
        # AIが考えて予想を出す
        ai_guess = ai_turn(ai_candidates)
        ai_hit, ai_blow = judge(secret, ai_guess)
        
        print(f"🤖 AIの予想 > {ai_guess}")
        print(f"🤖 AI: Hit={ai_hit}  Blow={ai_blow}")

        if ai_hit == digits:
            from .bgm import stop_bgm
            stop_bgm()  # AIが勝った時もBGMを止める
            print(f"💀 残念... AIの勝ち！ {tries} 回で当てられました（答え {secret}）")
            break
            
        # AIが外した場合、情報を元に頭の中の候補を論理的に絞り込む
        ai_candidates = filter_candidates(ai_candidates, ai_guess, ai_hit, ai_blow)
        print(f"   (AIは理詰めで残り {len(ai_candidates)} 個の候補まで絞り込んだ...)")