"""BGM機能：ゲームプレイ中、バックグラウンドでずっと音楽を流し続ける！"""

import threading
import time

# 音楽が再生中かどうかの合図（フラグ）
_is_playing = False


def _play_loop():
    """裏側でずっとゲームメロディを繰り返し再生する処理"""
    try:
        import winsound

        # ピコピコゲーム風のループメロディ♪（音階のヘルツと長さ）
        melody = [
            (523, 200),  # ド
            (587, 200),  # レ
            (659, 200),  # ミ
            (698, 200),  # ファ
            (784, 400),  # ソ
            (659, 400),  # ミ
            (523, 600),  # ド
        ]
        while _is_playing:
            for freq, duration in melody:
                if not _is_playing:
                    break
                winsound.Beep(freq, duration)
                time.sleep(0.1)  # 音と音の少しの間隔
    except Exception:
        pass


def start_bgm():
    """ゲーム開始時に呼び出すと、裏側でBGMループをスタートする！"""
    global _is_playing
    if _is_playing:
        return
    _is_playing = True

    # ここが魔法の技術！「裏側の作業員（別スレッド）」に音楽再生をお任せする
    thread = threading.Thread(target=_play_loop, daemon=True)
    thread.start()
    print("🎵 BGMスタート！（ゲームプレイ中、裏側で音楽が流れます♪）")


def stop_bgm():
    """ゲームクリア時に呼び出すと、BGMをストップする！"""
    global _is_playing
    _is_playing = False
    print("🔇 BGMストップ！")