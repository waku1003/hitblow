"""AI対戦機能：難易度（初級・中級・上級）を選べるAI！"""

import itertools
import random
from .core import judge

# AIのうっかり度（初期値は中級）
_forget_rate = 0.30

def select_ai_difficulty():
    """ゲーム開始時にAIの強さ（難易度）を選ぶ機能"""
    global _forget_rate
    print("\n🤖 AIの難易度を選んでください！")
    print("  1: 初級（のんびりAI・ミス多め）")
    print("  2: 中級（いい勝負・少しミスする）")
    print("  3: 上級（最強・一切ミスしないプロ棋士）")
    
    while True:
        choice = input("難易度 (1/2/3) > ").strip()
        if choice == "1":
            _forget_rate = 0.70  # 70%の確率で見落とす（弱め）
            print("🤖 [初級] お手柔らかにお願いしますね！")
            break
        elif choice == "2":
            _forget_rate = 0.30  # 30%の確率で見落とす（程よい）
            print("🤖 [中級] 全力でいい勝負をしましょう！")
            break
        elif choice == "3":
            _forget_rate = 0.00  # 0%＝一切見落とさない（最強）
            print("🤖 [上級] 100%理詰めで潰しにいきます。覚悟してください！")
            break
        else:
            print("1, 2, 3 のどれかを入力してください。")

def get_initial_candidates(digits):
    """最初の全パターンのリストを作る（3桁なら720通り）"""
    return ["".join(p) for p in itertools.permutations("0123456789", digits)]

def filter_candidates(candidates, guess, hit, blow):
    """AIの推理ターン：選ばれた難易度に応じた確率でうっかりミスをする！"""
    valid_candidates = []
    for cand in candidates:
        h, b = judge(cand, guess)
        if h == hit and b == blow:
            valid_candidates.append(cand)
        else:
            # 難易度で決まった確率（_forget_rate）で消し忘れて残してしまう！
            if random.random() < _forget_rate:
                valid_candidates.append(cand)
    return valid_candidates

def ai_turn(candidates):
    """残った候補の中から、AIが予想を決定する"""
    if not candidates:
        return "012"  # 万が一候補が消えた場合のフェイルセーフ
    return random.choice(candidates)