"""スコア機能：少ない手数でクリアするほど高い点数がもらえるシステム！"""

def calculate_score_and_grade(digits, tries):
    """
    スコアと評定（秀・優・良・可・不可）を計算して返す関数。
    """
    # --- スコアの計算 ---
    base_score = 100
    difficulty_bonus = digits * 50
    penalty = (tries - 1) * 10
    
    score = base_score + difficulty_bonus - penalty
    score = max(0, score)  # 0点以下にならないようにする
    
    # --- 評定の計算 ---
    # その桁数での「満点（1回で正解した時の点数）」を計算
    max_score = base_score + difficulty_bonus
    ratio = score / max_score  # 満点に対する割合を出す
    
    # 割合に応じて大学風の成績をつける
    if ratio >= 0.9:     # 9割以上
        grade = "秀"
    elif ratio >= 0.8:   # 8割以上
        grade = "優"
    elif ratio >= 0.7:   # 7割以上
        grade = "良"
    elif ratio >= 0.6:   # 6割以上
        grade = "可"
    else:                # 6割未満
        grade = "不可"
        
    return score, grade