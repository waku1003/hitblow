"""GUI版ゲーム画面：BGM・評定・AI対戦がすべて詰まった完全版！"""

import tkinter as tk
from tkinter import messagebox
import random  # AIの予想生成用に追加

# チームで作った部品をすべてインポート！
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
        self.root.title("Hit & Blow - 完全版")
        self.root.geometry("450x600")
        self.root.configure(padx=20, pady=20)

        # タイトル
        tk.Label(root, text=f"Hit & Blow ({digits}桁)", font=("Helvetica", 18, "bold")).pack(pady=10)

        # 履歴表示エリア（テキストボックス）
        self.history_text = tk.Text(root, height=18, width=45, state="disabled", font=("Courier", 12))
        self.history_text.pack(pady=10)

        # ＝＝＝ 入力・操作エリア ＝＝＝
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # 入力ボックス
        self.guess_var = tk.StringVar()
        self.entry = tk.Entry(input_frame, textvariable=self.guess_var, font=("Helvetica", 16), width=10)
        self.entry.pack(side=tk.LEFT, padx=10)
        self.entry.bind("<Return>", lambda e: self.check_player_guess())

        # プレイヤー予想ボタン
        submit_btn = tk.Button(input_frame, text="自分で予想", font=("Helvetica", 12), bg="#e0f7fa", command=self.check_player_guess)
        submit_btn.pack(side=tk.LEFT, padx=5)

        # AI予想ボタン（AI対戦システム）
        ai_btn = tk.Button(input_frame, text="🤖 AIに任せる", font=("Helvetica", 12), bg="#ffe0b2", command=self.check_ai_guess)
        ai_btn.pack(side=tk.LEFT, padx=5)

        # ヒント（気分転換）ボタン
        hint_btn = tk.Button(root, text="🎵 気分転換ミュージック（BGM機能）", font=("Helvetica", 10), command=self.play_hint)
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
        """ヒント機能（BGMモジュール連携）"""
        self.log_history("🎵 応援ミュージック再生中...")
        play_hint_music()

    def check_player_guess(self):
        """プレイヤーが予想した時の処理"""
        guess = self.guess_var.get().strip()
        self.guess_var.set("")  # 入力欄をクリア
        self.process_guess(guess, "あなた")

    def check_ai_guess(self):
        """AI対戦システム：AIが自動で予想する処理"""
        # ランダムで重複のない数字を生成（AIの思考ロジック）
        ai_guess = "".join(random.sample("0123456789", self.digits))
        self.process_guess(ai_guess, "AI🤖")

    def process_guess(self, guess, player_name):
        """予想を判定し、ゲーム進行とスコア（評定）を管理する共通処理"""
        # 入力チェック（プレイヤーのみ警告を出す）
        if len(guess) != self.digits or not guess.isdigit():
            if player_name == "あなた":
                messagebox.showwarning("エラー", f"{self.digits}桁の数字を入力してね！")
            return

        self.tries += 1
        hit, blow = judge(self.secret, guess)
        
        # 画面に結果を表示（誰が予想したかも表示）
        self.log_history(f"[{self.tries}回目] {player_name}: {guess} ➔ Hit:{hit} Blow:{blow}")

        # 正解時の処理（評定システムと勝利音の統合）
        if hit == self.digits:
            stop_bgm()
            celebrate()
            score, grade = calculate_score_and_grade(self.digits, self.tries)
            
            # 結果発表テキスト
            result_msg = (
                f"🎉 {player_name}の正解！ {self.tries} 回で当たり！\n"
                f"答えは「{self.secret}」でした。\n\n"
                f"★ 獲得スコア: {score} 点！\n"
                f"★ 評定：（{grade}）"
            )
            
            # プレイヤーが負けた（AIが当てた）場合
            if player_name == "AI🤖":
                result_msg += "\n\nAIに先を越されてしまいました…！"
                
            messagebox.showinfo("ゲーム終了！", result_msg)
            self.root.destroy()  # ウィンドウを閉じる

def main():
    root = tk.Tk()
    app = HitBlowGUI(root)
    root.mainloop()
