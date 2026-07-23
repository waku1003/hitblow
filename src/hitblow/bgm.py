"""BGM機能：ゲームプレイ中、バックグラウンドでずっと音楽を流し続ける！"""

import threading
import time

# 音楽が再生中かどうかの合図（フラグ）
_is_playing = False

def _play_loop():
    """ファミコン風の「高速アルペジオ技法」で、音を重ねているように錯覚させるラスボス決戦BGM"""
    try:
        import winsound

        boss_melody = [
            # --- フェーズ1：不穏に音が重なり合うイントロ（高速アルペジオ） ---
            (220, 50), (329, 50), (440, 50), (329, 50),
            (220, 50), (329, 50), (440, 50), (329, 50),
            (208, 50), (311, 50), (415, 50), (311, 50),
            (208, 50), (311, 50), (415, 50), (311, 50),
            
            # --- フェーズ2：激しい戦闘ビート（重いベースと鋭い攻撃音） ---
            (165, 70), (165, 70), (330, 120), (247, 70),
            (262, 120), (247, 80), (220, 180),
            
            # --- フェーズ3：AIに追い詰められるクライマックス（怒涛の上昇和音） ---
            (330, 50), (440, 50), (660, 50), (440, 50),
            (349, 50), (466, 50), (698, 50), (466, 50),
            (330, 250),
        ]

        while _is_playing:
            for freq, duration in boss_melody:
                if not _is_playing:
                    break
                winsound.Beep(freq, duration)
                time.sleep(0.01)
    except Exception:
        pass

def start_bgm():
    """ゲーム開始時に呼び出すと、裏側でBGMループをスタートする！"""
    global _is_playing
    if _is_playing:
        return
    _is_playing = True

    thread = threading.Thread(target=_play_loop, daemon=True)
    thread.start()
    print("🎵 ラスボス決戦BGMスタート！")

def stop_bgm():
    """ゲームクリア時に呼び出すと、BGMをストップする！"""
    global _is_playing
    _is_playing = False
    print("🔇 BGMストップ！")