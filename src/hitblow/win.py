"""勝利時の機能：正解したときにファンファーレ（音）を鳴らして祝福する！"""

import time


def celebrate():
    """ゲームクリアのお祝い音（システム音）を「タ・タ・ターン♪」と軽快に鳴らす！"""
    print("\n🎉🎉🎉 祝・ゲームクリア！！ ファンファーレ♪ 🎉🎉🎉")

    try:
        import winsound

        # 「タ・タ・ターン♪」と聞こえるように、少しリズムを変えて3回鳴らす！
        winsound.MessageBeep(winsound.MB_OK)
        time.sleep(0.15)  # 短い間隔
        winsound.MessageBeep(winsound.MB_OK)
        time.sleep(0.15)  # 短い間隔
        winsound.MessageBeep(winsound.MB_OK)
        time.sleep(0.5)   # 最後の音の余韻
    except Exception:
        # 万が一鳴らなかった時のバックアップ（画面を光らせるピー音）
        print("\a\a\a\a")

    print("✨ おめでとうございます！最高のプレイでした！ ✨\n")