"""GUI版ゲーム画面：ウィンドウとボタンで直感的に遊べるモード！"""

import tkinter as tk
from tkinter import messagebox

# 今までチームで作った「音」や「ロジック」の部品をそのまま使い回します！
from .core import judge, make_secret
from .bgm import start_bgm, stop_bgm
from .score import calculate_score_and_grade
from .win import celebrate
from .hint import play_hint_music

class HitBlowGUI:
    def __init__(self, root, digits=3):
        self.root = root
        self.digits = digits
        self.secret = make_secret(digits)
        self.tries = 0

        # ウィンドウの基本設定
        self.root.title("Hit & Blow - GUI Edition")
        self.root.geometry("400x550")
        self.root.configure(padx=20, pady=20)

        # タイトル
        tk.Label(root, text=f"Hit & Blow ({digits}桁)", font=("Helvetica", 18, "bold")).pack(pady=10)

        # 履歴表示エリア（テキストボックス）
        self.history_text = tk.Text(root, height=15, width=40, state="disabled", font=("Courier", 12))
        self.history_text.pack(pady=10)

        # 入力エリアのフレーム
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # 入力ボックス
        self.guess_var = tk.StringVar()
        self.entry = tk.Entry(input_frame, textvariable=self.guess_var, font=("Helvetica", 16), width=10)
        self.entry.pack(side=tk.LEFT, padx=10)
        # Enterキーを押したときも予想ボタンと同じ動きをするように紐付け
        self.entry.bind("<Return>", lambda e: self.check_guess())

        # 予想ボタン
        submit_btn = tk.Button(input_frame, text="予想する！", font=("Helvetica", 12), command=self.check_guess)
        submit_btn.pack(side=tk.LEFT)

        # ヒント（気分転換）ボタン
        hint_btn = tk.Button(root, text="🎵 気分転換ミュージック", font=("Helvetica", 10), command=self.play_hint)
        hint_btn.pack(pady=10)

        # 起動時にBGMスタート
        start_bgm()

    def log_history(self, message):
        """履歴エリアにテキストを追加する関数"""
        self.history_text.config(state="normal")
        self.history_text.insert(tk.END, message + "\n")
        self.history_text.see(tk.END)  # 一番下まで自動スクロール
        self.history_text.config(state="disabled")

    def play_hint(self):
        """ヒントボタンが押された時の処理"""
        self.log_history("🎵 応援ミュージック再生中...")
        play_hint_music()

    def check_guess(self):
        """予想ボタンが押された時の処理（これまでの whileループの中身に相当）"""
        guess = self.guess_var.get().strip()
        self.guess_var.set("")  # 入力欄を空にする

        # 入力チェック
        if len(guess) != self.digits or not guess.isdigit():
            messagebox.showwarning("エラー", f"{self.digits}桁の数字を入力してね！")
            return

        self.tries += 1
        hit, blow = judge(self.secret, guess)
        
        # 画面に結果を表示
        self.log_history(f"[{self.tries}回目] {guess} ➔ Hit:{hit} Blow:{blow}")

        # 正解時の処理
        if hit == self.digits:
            stop_bgm()
            celebrate()
            score, grade = calculate_score_and_grade(self.digits, self.tries)
            
            # ポップアップウィンドウで結果発表！
            result_msg = (
                f"正解！ {self.tries} 回で当たり！\n"
                f"答えは「{self.secret}」でした。\n\n"
                f"★ 獲得スコア: {score} 点！\n"
                f"★ 評定：（{grade}）"
            )
            messagebox.showinfo("ゲームクリア！🎉", result_msg)
            self.root.destroy()  # ウィンドウを閉じる

def main():
    root = tk.Tk()
    app = HitBlowGUI(root)
    root.mainloop()  # GUIのイベントループ（待機状態）に入る
