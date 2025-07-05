import tkinter as tk
from tkinter import messagebox, scrolledtext, font
import groq
import threading
from datetime import datetime

GROQ_API_KEY = "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"
client = groq.Groq(api_key=GROQ_API_KEY)

APP_TITLE = "Brainy"
WINDOW_SIZE = "900x700"


BG_COLOR = "#0a0a12"  
SIDEBAR_COLOR = "#121220" 
TEXT_COLOR = "#ffffff" 
INPUT_BG = "#1a1a2a"   
BTN_COLOR = "#2a2a4a"
BTN_HOVER = "#3a3a6a" 
ACCENT_COLOR = "#4a4a8a"  
CHAT_BG = "#0f0f1a"  
USER_MSG_COLOR = "#2a2a4a" 
AI_MSG_COLOR = "#1a1a2a"  


VALID_IDS = [f"{i:04}" for i in range(1, 93)]

class BrainyAI:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(True, True)
        self.setup_fonts()
        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def setup_fonts(self):
        self.title_font = font.Font(family="Segoe UI", size=20, weight="bold")
        self.subtitle_font = font.Font(family="Segoe UI", size=12)
        self.chat_font = font.Font(family="Segoe UI", size=12)
        self.input_font = font.Font(family="Segoe UI", size=12)
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")
        
    def create_widgets(self):
        self.sidebar = tk.Frame(self.root, bg=SIDEBAR_COLOR, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        self.main_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        

        tk.Label(self.sidebar, text="BRAINY", font=self.title_font, fg=TEXT_COLOR, 
                bg=SIDEBAR_COLOR, pady=20).pack(fill=tk.X)
        
        tk.Label(self.sidebar, text="AI Assistant", font=self.subtitle_font, 
                fg="#aaaaaa", bg=SIDEBAR_COLOR).pack(fill=tk.X, pady=(0, 30))
        
        tk.Label(self.sidebar, text="Developed by Affan", font=self.subtitle_font, 
                fg="#888888", bg=SIDEBAR_COLOR).pack(side=tk.BOTTOM, fill=tk.X, pady=20)
        

        model_frame = tk.Frame(self.sidebar, bg=SIDEBAR_COLOR)
        model_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(model_frame, text="Model:", font=self.subtitle_font, 
                fg="#aaaaaa", bg=SIDEBAR_COLOR, anchor="w").pack(fill=tk.X)
        tk.Label(model_frame, text="Llama 3 70B", font=self.subtitle_font, 
                fg=TEXT_COLOR, bg=SIDEBAR_COLOR, anchor="w").pack(fill=tk.X)
        

        id_frame = tk.Frame(self.sidebar, bg=SIDEBAR_COLOR)
        id_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(id_frame, text="Student ID:", font=self.subtitle_font, 
                fg="#aaaaaa", bg=SIDEBAR_COLOR, anchor="w").pack(fill=tk.X)
        
        self.student_id_entry = tk.Entry(id_frame, font=self.input_font, 
                                       bg=INPUT_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                                       relief=tk.FLAT)
        self.student_id_entry.pack(fill=tk.X, pady=(5, 0))
        

        self.chat_history = scrolledtext.ScrolledText(
            self.main_frame, 
            bg=CHAT_BG, 
            fg=TEXT_COLOR,
            font=self.chat_font,
            relief=tk.FLAT,
            padx=15,
            pady=15,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.chat_history.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        

        self.add_message("Brainy", "Hello! I'm Brainy, your AI assistant. How can I help you today?", False)
        

        input_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        self.question_input = tk.Text(
            input_frame, 
            height=3, 
            font=self.input_font, 
            bg=INPUT_BG, 
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.question_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.question_input.bind("<Return>", self.on_enter_pressed)
        

        btn_container = tk.Frame(input_frame, bg=BG_COLOR)
        btn_container.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))
        

        self.send_btn = tk.Button(
            btn_container, 
            text="Send", 
            font=self.button_font,
            bg=BTN_COLOR, 
            fg=TEXT_COLOR, 
            relief=tk.FLAT, 
            command=self.generate_script,
            width=8,
            padx=10,
            pady=5
        )
        self.send_btn.pack(fill=tk.BOTH, expand=True)
        self.send_btn.bind("<Enter>", lambda e: self.send_btn.config(bg=BTN_HOVER))
        self.send_btn.bind("<Leave>", lambda e: self.send_btn.config(bg=BTN_COLOR))

        self.status_bar = tk.Label(self.main_frame, text="Ready", font=self.subtitle_font, 
                                 fg="#888888", bg=BG_COLOR, anchor="w")
        self.status_bar.pack(fill=tk.X, padx=10, pady=(0, 5))
    
    def on_enter_pressed(self, event):
 
        if event.state == 0: 
            self.generate_script()
            return "break"  
        return None
    
    def validate_student_id(self, sid):
        return sid in VALID_IDS
    
    def add_message(self, sender, message, is_user=True):
        self.chat_history.config(state=tk.NORMAL)
        

        timestamp = datetime.now().strftime("%H:%M")
        

        self.chat_history.tag_configure("user", background=USER_MSG_COLOR, lmargin1=50, lmargin2=50, 
                                       rmargin=10, spacing2=5, relief=tk.FLAT, borderwidth=5)
        self.chat_history.tag_configure("ai", background=AI_MSG_COLOR, lmargin1=10, lmargin2=10, 
                                      rmargin=50, spacing2=5, relief=tk.FLAT, borderwidth=5)
        self.chat_history.tag_configure("timestamp", foreground="#888888", font=("Segoe UI", 9))
        self.chat_history.tag_configure("sender", font=("Segoe UI", 10, "bold"))

        tag = "user" if is_user else "ai"
        sender_tag = "User" if is_user else "Brainy"
        
        self.chat_history.insert(tk.END, f"{timestamp} ", "timestamp")
        self.chat_history.insert(tk.END, f"{sender_tag}\n", "sender")
        self.chat_history.insert(tk.END, f"{message}\n\n", tag)
        
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.see(tk.END)
    
    def call_groq_api(self, student_id, question):
        try:
            prompt = f"Student ID: {student_id}. Question: {question}"
            

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama3-70b-8192",
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )
            
            return chat_completion.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"
    
    def generate_script(self):
        student_id = self.student_id_entry.get().strip()
        question = self.question_input.get("1.0", tk.END).strip()
        
        if not self.validate_student_id(student_id):
            messagebox.showerror("Invalid ID", "Student ID must be between 001 and 092.")
            return
        
        if not question:
            messagebox.showerror("Missing Question", "Please enter your question.")
            return
        

        self.add_message("User", question, True)

        self.question_input.delete("1.0", tk.END)

        self.send_btn.config(state=tk.DISABLED, bg="#555555")
      
        threading.Thread(target=self.process_query, args=(student_id, question), daemon=True).start()
    
    def process_query(self, student_id, question):
        try:
            response = self.call_groq_api(student_id, question)
            self.add_message("Brainy", response, False)
            self.status_bar.config(text="Ready")
        except Exception as e:
            self.status_bar.config(text=f"Error: {str(e)}")
            self.add_message("Brainy", f"Sorry, I encountered an error: {str(e)}", False)
        finally:
            self.send_btn.config(state=tk.NORMAL, bg=BTN_COLOR)
    
    def on_close(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = BrainyAI(root)
    root.mainloop()