"""ヒント機能：ゲーム中に音楽（メロディ）を流して気分転換する！"""

import time


def play_hint_music():
    """Windowsのビープ音機能を使って、ゲームっぽいピコピコメロディを流す♪"""
    try:
        import winsound

        # 音階の周波数（ヘルツ）と長さ（ミリ秒）の設定：ド・ミ・ソ・高いド！♪
        melody = [
            (523, 150),  # ド
            (659, 150),  # ミ
            (784, 150),  # ソ
            (1046, 300),  # 高いド
        ]
        for freq, duration in melody:
            winsound.Beep(freq, duration)
            time.sleep(0.05)  # 音と音の間の短い間隔
    except ImportError:
        # 万が一Windows以外のパソコンで動かしたとき用の安全対策
        print("♪〜（メロディが流れています）〜♪")


def give_hint():
    """音楽だけを鳴らす関数（答えのネタバレは一切しない！）"""
    print("\n🎵 応援ミュージック、スタート！！ 🎵")
    play_hint_music()  # メロディを再生♪
    print("🎶 気分転換完了！次の予想を集中して入力してね！\n")