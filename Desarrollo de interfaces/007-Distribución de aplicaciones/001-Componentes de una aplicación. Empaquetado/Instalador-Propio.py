import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import zipfile
import os
import threading
import subprocess
import sys
import platform
from ttkthemes import ThemedTk
import pygame

try:
    import winshell
    from win32com.client import Dispatch
    WINDOWS_SHORTCUT_AVAILABLE = True
except ImportError:
    WINDOWS_SHORTCUT_AVAILABLE = False

class Installer(ThemedTk):
    def __init__(self):
        super().__init__(theme="equilux")
        self.title("Professional Installer")
        self.geometry("800x600")
        self.resizable(False, False)
        self.install_path = tk.StringVar(value=os.getcwd())
        self.frames = {}

        for F in (WelcomeScreen, TermsAndConditionsScreen, ReadmeScreen,
                 SelectFolderScreen, ProgressScreen, SuccessScreen):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomeScreen)
        pygame.mixer.init()
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play(-1)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        if hasattr(frame, 'on_show'):
            frame.on_show()

    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def uninstall_application(self):
        folder_to_uninstall = filedialog.askdirectory(
            title="Select Folder to Uninstall",
            initialdir=os.path.expanduser("~")
        )
        
        if not folder_to_uninstall:
            return
            
        if not os.path.exists(folder_to_uninstall):
            messagebox.showerror("Error", "Selected folder doesn't exist!")
            return

        confirm = messagebox.askyesno(
            "Confirm Uninstall",
            f"THIS WILL PERMANENTLY DELETE:\n{folder_to_uninstall}\n\nContinue?",
            icon="warning"
        )
        
        if not confirm:
            return

        try:
            for root, dirs, files in os.walk(folder_to_uninstall, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(folder_to_uninstall)
            messagebox.showinfo("Success", "Uninstallation completed!")
        except Exception as e:
            messagebox.showerror("Error", f"Uninstall failed:\n{str(e)}")

class WelcomeScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        title_label = tk.Label(self, text="Welcome to the Professional Installer", 
                             font=("Arial", 20, "bold"))
        title_label.pack(pady=30)

        description_label = tk.Label(self,
            text="This installer will guide you through the steps\n"
                 "to install the application on your system.", 
            font=("Arial", 12))
        description_label.pack(pady=15)

        uninstall_btn = ttk.Button(self, text="Uninstall", 
                                  command=parent.uninstall_application)
        uninstall_btn.pack(pady=10)

        music_btn = ttk.Button(self, text="Toggle Music", 
                             command=parent.toggle_music)
        music_btn.pack(pady=10)

        next_btn = ttk.Button(self, text="Next", command=self.go_next)
        next_btn.pack(pady=20)

    def go_next(self):
        self.master.show_frame(TermsAndConditionsScreen)

class TermsAndConditionsScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        title_label = tk.Label(self, text="Terms and Conditions", 
                            font=("Arial", 18, "bold"))
        title_label.pack(pady=20)

        terms_text = """
        By clicking "Accept", you agree to the following terms:

        1. License: Provided 'as-is' without warranty
        2. Usage: Allowed for personal/commercial use
        3. Liability: No liability for damages
        4. Modification: Allowed with original license
        5. Distribution: Must include original agreement
        """
        terms_label = tk.Label(self, text=terms_text, justify=tk.LEFT, 
                             font=("Arial", 12))
        terms_label.pack(pady=15)

        self.accept_var = tk.BooleanVar()
        accept_check = tk.Checkbutton(self, 
                                    text="I accept the terms and conditions",
                                    variable=self.accept_var, 
                                    font=("Arial", 12))
        accept_check.pack(pady=15)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)
        
        back_btn = ttk.Button(btn_frame, text="Back",
                            command=lambda: self.master.show_frame(WelcomeScreen))
        back_btn.pack(side=tk.LEFT, padx=10)

        self.next_btn = ttk.Button(btn_frame, text="Next", command=self.go_next)
        self.next_btn.pack(side=tk.RIGHT, padx=10)
        self.next_btn.config(state="disabled")

        self.accept_var.trace_add('write', self.on_accept_change)

    def on_accept_change(self, *args):
        self.next_btn.config(state="normal" if self.accept_var.get() else "disabled")

    def go_next(self):
        self.master.show_frame(ReadmeScreen)

class ReadmeScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        title_label = tk.Label(self, text="Application Documentation", 
                             font=("Arial", 18, "bold"))
        title_label.pack(pady=15)

        readme_content = """
        APPLICATION OVERVIEW
        --------------------
        This program provides advanced file management capabilities with:
        - Cross-platform compatibility
        - Batch processing
        - Custom workflows
        - Detailed analytics

        KEY FEATURES
        ------------
        1. File Management:
           - Organize files efficiently
           - Advanced search & filtering
        2. Processing:
           - Automated workflows
           - Custom scripting
        3. Exporting:
           - Multiple format support
           - Cloud integration

        GETTING STARTED
        --------------
        1. Complete installation
        2. Launch from Start Menu
        3. Follow setup wizard
        4. Import your files
        5. Configure workflows

        SUPPORT
        -------
        Email: support@example.com
        Documentation: docs.example.com
        Community Forum: forum.example.com
        """

        self.text_area = scrolledtext.ScrolledText(self,
                                                 wrap=tk.WORD,
                                                 font=("Arial", 12),
                                                 width=70,
                                                 height=20)
        self.text_area.insert(tk.INSERT, readme_content)
        self.text_area.configure(state='disabled')
        self.text_area.pack(padx=20, pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=15)
        
        back_btn = ttk.Button(btn_frame, text="Back",
                            command=lambda: self.master.show_frame(TermsAndConditionsScreen))
        back_btn.pack(side=tk.LEFT, padx=10)

        next_btn = ttk.Button(btn_frame, text="Next",
                            command=lambda: self.master.show_frame(SelectFolderScreen))
        next_btn.pack(side=tk.RIGHT, padx=10)

class SelectFolderScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        instruction_label = tk.Label(self, text="Select Installation Folder", 
                                   font=("Arial", 16, "bold"))
        instruction_label.pack(pady=25)

        folder_frame = tk.Frame(self)
        folder_frame.pack(pady=10)

        self.folder_entry = tk.Entry(folder_frame, 
                                   textvariable=parent.install_path, 
                                   width=50, font=("Arial", 12))
        self.folder_entry.pack(side=tk.LEFT, padx=(0, 10))

        browse_btn = ttk.Button(folder_frame, text="Browse...", 
                              command=self.browse_folder)
        browse_btn.pack(side=tk.LEFT)

        self.error_label = tk.Label(self, text="", fg="red", font=("Arial", 12))
        self.error_label.pack(pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=25)
        
        back_btn = ttk.Button(btn_frame, text="Back",
                            command=lambda: self.master.show_frame(ReadmeScreen))
        back_btn.pack(side=tk.LEFT, padx=10)

        self.next_btn = ttk.Button(btn_frame, text="Next", command=self.go_next)
        self.next_btn.pack(side=tk.RIGHT, padx=10)
        self.next_btn.config(state="disabled")

        parent.install_path.trace_add('write', self.on_path_change)
        self.check_folder_empty()

    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=os.getcwd(), 
                                       title="Select Installation Folder")
        if folder:
            self.master.install_path.set(folder)

    def on_path_change(self, *args):
        self.check_folder_empty()

    def check_folder_empty(self):
        path = self.master.install_path.get()
        if os.path.isdir(path):
            try:
                if not os.listdir(path):
                    self.next_btn.config(state="normal")
                    self.error_label.config(text="")
                else:
                    self.next_btn.config(state="disabled")
                    self.error_label.config(text="Folder must be empty!")
            except PermissionError:
                self.next_btn.config(state="disabled")
                self.error_label.config(text="Permission denied!")
            except Exception as e:
                self.next_btn.config(state="disabled")
                self.error_label.config(text=f"Error: {str(e)}")
        else:
            self.next_btn.config(state="disabled")
            self.error_label.config(text="Invalid directory!")

    def go_next(self):
        self.master.show_frame(ProgressScreen)

class ProgressScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        title_label = tk.Label(self, text="Installing...", 
                             font=("Arial", 18, "bold"))
        title_label.pack(pady=25)

        self.progress = ttk.Progressbar(self, orient="horizontal", 
                                      length=500, mode="determinate")
        self.progress.pack(pady=15)

        self.status_label = tk.Label(self, text="Preparing to install...", 
                                   font=("Arial", 12))
        self.status_label.pack(pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)
        
        back_btn = ttk.Button(btn_frame, text="Back",
                            command=lambda: self.master.show_frame(SelectFolderScreen))
        back_btn.pack(side=tk.LEFT, padx=10)

        self.next_btn = ttk.Button(btn_frame, text="Next", command=self.go_next)
        self.next_btn.pack(side=tk.RIGHT, padx=10)
        self.next_btn.config(state="disabled")

        self.installation_started = False

    def on_show(self):
        if not self.installation_started:
            self.installation_started = True
            threading.Thread(target=self.start_extraction, daemon=True).start()

    def start_extraction(self):
        zip_file = "paquete.zip"
        install_dir = self.master.install_path.get()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        zip_path = os.path.join(script_dir, zip_file)

        if not os.path.isfile(zip_path):
            messagebox.showerror("Error", "Missing installation package!")
            self.status_label.config(text="Installation failed!")
            return

        try:
            with zipfile.ZipFile(zip_path, 'r') as zipped:
                total_files = len(zipped.namelist())
                
                for i, file in enumerate(zipped.namelist(), 1):
                    zipped.extract(file, install_dir)
                    progress = int((i / total_files) * 100)
                    self.progress["value"] = progress
                    self.status_label.config(text=f"Extracting {file} ({i}/{total_files})")
                    self.master.update_idletasks()

            self.status_label.config(text="Installation complete!")
            self.next_btn.config(state="normal")

        except Exception as e:
            messagebox.showerror("Error", f"Installation failed:\n{str(e)}")
            self.status_label.config(text="Installation failed!")

    def go_next(self):
        self.master.show_frame(SuccessScreen)

class SuccessScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        success_label = tk.Label(self, text="Installation Successful!", 
                               font=("Arial", 18, "bold"))
        success_label.pack(pady=25)

        detail_label = tk.Label(self, 
                              text="Your application is ready to use!", 
                              font=("Arial", 12))
        detail_label.pack(pady=15)

        self.launch_var = tk.BooleanVar(value=True)
        self.shortcut_var = tk.BooleanVar(value=True)

        tk.Checkbutton(self, text="Launch Now", 
                     variable=self.launch_var, font=("Arial", 12)).pack(pady=15)
        tk.Checkbutton(self, text="Create Shortcut", 
                     variable=self.shortcut_var, font=("Arial", 12)).pack(pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)
        
        back_btn = ttk.Button(btn_frame, text="Back",
                            command=lambda: self.master.show_frame(ProgressScreen))
        back_btn.pack(side=tk.LEFT, padx=10)

        ttk.Button(btn_frame, text="Finish", 
                 command=self.finish_installation).pack(side=tk.RIGHT, padx=10)

    def finish_installation(self):
        if self.shortcut_var.get():
            threading.Thread(target=self.create_shortcut, daemon=True).start()

        if self.launch_var.get():
            self.launch_main_py()

        self.master.destroy()

    def create_shortcut(self):
        target_path = os.path.join(self.master.install_path.get(), "main.py")
        shortcut_name = "My App"
        os_type = platform.system()

        if not os.path.isfile(target_path):
            messagebox.showerror("Error", "Main file missing!")
            return

        try:
            if os_type == "Windows":
                self.create_windows_shortcut(target_path, shortcut_name)
            elif os_type == "Darwin":
                self.create_macos_shortcut(target_path, shortcut_name)
            elif os_type == "Linux":
                self.create_linux_shortcut(target_path, shortcut_name)
        except Exception as e:
            messagebox.showerror("Error", f"Shortcut failed:\n{str(e)}")

    def create_windows_shortcut(self, target, name):
        if not WINDOWS_SHORTCUT_AVAILABLE:
            return

        desktop = winshell.desktop()
        shortcut_path = os.path.join(desktop, f"{name}.lnk")
        with winshell.shortcut(shortcut_path) as link:
            link.path = sys.executable
            link.arguments = f'"{target}"'
            link.icon_location = (sys.executable, 0)

    def create_macos_shortcut(self, target, name):
        desktop = os.path.expanduser("~/Desktop")
        applescript = f'''
        tell application "Finder"
            make alias file to POSIX file "{target}" at POSIX file "{desktop}"
            set name of result to "{name}"
        end tell
        '''
        subprocess.run(['osascript', '-e', applescript], check=True)

    def create_linux_shortcut(self, target, name):
        desktop = os.path.expanduser("~/Desktop")
        shortcut_path = os.path.join(desktop, f"{name}.desktop")
        
        desktop_entry = f'''[Desktop Entry]
Type=Application
Name={name}
Exec={sys.executable} "{target}"
Terminal=false
'''
        with open(shortcut_path, 'w') as f:
            f.write(desktop_entry)
        os.chmod(shortcut_path, 0o755)

    def launch_main_py(self):
        main_py = os.path.join(self.master.install_path.get(), "main.py")
        if os.path.isfile(main_py):
            try:
                subprocess.Popen([sys.executable, main_py], 
                               cwd=self.master.install_path.get())
            except Exception as e:
                messagebox.showerror("Error", f"Launch failed:\n{str(e)}")

if __name__ == "__main__":
    app = Installer()
    app.mainloop()
