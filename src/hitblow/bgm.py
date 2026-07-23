"""BGM機能：ゲームプレイ中、バックグラウンドでずっと音楽を流し続ける！"""

import threading
import time

# 音楽が再生中かどうかの合図（フラグ）
_is_playing = False

def _play_loop():
    """最初のシンプルなメロディ（ゆっくりしたテンポ）"""
    try:
        import winsound

        # ゆったりとした基本的なメロディの組み合わせ
        basic_melody = [
            (262, 500),  # ド (500ミリ秒 = 0.5秒)
            (294, 500),  # レ
            (330, 500),  # ミ
            (349, 500),  # ファ
            (392, 500),  # ソ
            (440, 500),  # ラ
            (494, 500),  # シ
            (523, 1000), # ド (少し長く)
        ]
        
        while _is_playing:
            for freq, duration in basic_melody:
                if not _is_playing:
                    break
                winsound.Beep(freq, duration)
                time.sleep(0.1)  # 音と音の間に少しだけ間隔を空ける
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
    print("🎵 BGMスタート！")

def stop_bgm():
    """ゲームクリア時に呼び出すと、BGMをストップする！"""
    global _is_playing
    _is_playing = False
    print("🔇 BGMストップ！")