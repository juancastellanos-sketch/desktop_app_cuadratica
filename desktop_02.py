import math
import tkinter as tk
from tkinter import messagebox, ttk


class QuadraticSolverApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Quadratic Solver v1.0")
        self.root.geometry("680x560")
        self.root.minsize(640, 520)
        self.root.configure(bg="#D9E1E8")

        # Configuración de Paleta de Colores (Basada en el mockup)
        self.COLOR_TOP_BAR = "#004B9B"
        self.COLOR_SIDEBAR_BG = "#EAEAEA"
        self.COLOR_SIDEBAR_ACTIVE = "#004B9B"
        self.COLOR_CONTENT_BG = "#F5F5F5"
        self.COLOR_BOX_BG = "#EAEAEA"
        self.COLOR_BTN_CALC = "#005A9C"
        self.COLOR_BTN_CLEAR = "#E0E0E0"
        self.COLOR_TEXT_MAIN = "#111111"
        self.COLOR_TEXT_MUTED = "#555555"

        # Inicializar variables de placeholders
        self.placeholders = {"a": "Ej: 1", "b": "Ej: -5", "c": "Ej: 6"}

        # Construir la interfaz
        self._build_ui()

    def _build_ui(self):
        # ==========================================
        # 1. CONTENEDOR PRINCIPAL (Split Horizontal)
        # ==========================================
        self.frame_main = tk.Frame(self.root, bg=self.COLOR_CONTENT_BG)
        self.frame_main.pack(fill="both", expand=True)

        # ------------------------------------------
        # A. BARRA LATERAL (Sidebar Frame)
        # ------------------------------------------
        self.frame_sidebar = tk.Frame(
            self.frame_main, bg=self.COLOR_SIDEBAR_BG, width=150
        )
        self.frame_sidebar.pack(side="left", fill="y")
        self.frame_sidebar.pack_propagate(False)

        # Encabezado del Sidebar
        lbl_tools = tk.Label(
            self.frame_sidebar,
            text="Tools",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_SIDEBAR_BG,
            fg=self.COLOR_TEXT_MAIN,
            anchor="w",
        )
        lbl_tools.pack(fill="x", padx=15, pady=(15, 0))

        lbl_subtools = tk.Label(
            self.frame_sidebar,
            text="Engineered Precision",
            font=("Segoe UI", 8),
            bg=self.COLOR_SIDEBAR_BG,
            fg=self.COLOR_TEXT_MUTED,
            anchor="w",
        )
        lbl_subtools.pack(fill="x", padx=15, pady=(0, 15))

        # Opciones del Menú Lateral
        btn_solver = tk.Label(
            self.frame_sidebar,
            text="🧮 Solver",
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_SIDEBAR_ACTIVE,
            fg="white",
            padx=15,
            pady=8,
            anchor="w",
            cursor="hand2",
        )
        btn_solver.pack(fill="x")

        btn_history = tk.Label(
            self.frame_sidebar,
            text="🕒 History",
            font=("Segoe UI", 9),
            bg=self.COLOR_SIDEBAR_BG,
            fg=self.COLOR_TEXT_MAIN,
            padx=15,
            pady=8,
            anchor="w",
            cursor="hand2",
        )
        btn_history.pack(fill="x")

        btn_constants = tk.Label(
            self.frame_sidebar,
            text="∑ Constants",
            font=("Segoe UI", 9),
            bg=self.COLOR_SIDEBAR_BG,
            fg=self.COLOR_TEXT_MAIN,
            padx=15,
            pady=8,
            anchor="w",
            cursor="hand2",
        )
        btn_constants.pack(fill="x")

        # ------------------------------------------
        # B. ÁREA DE CONTENIDO (Content Frame)
        # ------------------------------------------
        self.frame_content = tk.Frame(
            self.frame_main, bg=self.COLOR_CONTENT_BG, padx=25, pady=20
        )
        self.frame_content.pack(side="right", fill="both", expand=True)

        # Frame B1: Encabezado del contenido
        self.frame_header = tk.Frame(
            self.frame_content, bg=self.COLOR_CONTENT_BG
        )
        self.frame_header.pack(fill="x")

        lbl_title = tk.Label(
            self.frame_header,
            text="Resolutor de Ecuaciones\nCuadráticas",
            font=("Segoe UI", 16, "bold"),
            bg=self.COLOR_CONTENT_BG,
            fg=self.COLOR_TEXT_MAIN,
            justify="left",
            anchor="w",
        )
        lbl_title.pack(fill="x")

        separator = ttk.Separator(self.frame_header, orient="horizontal")
        separator.pack(fill="x", pady=8)

        lbl_subtitle = tk.Label(
            self.frame_header,
            text="Formato: ax² + bx + c = 0",
            font=("Segoe UI", 10),
            bg=self.COLOR_CONTENT_BG,
            fg=self.COLOR_TEXT_MUTED,
            anchor="w",
        )
        lbl_subtitle.pack(fill="x", pady=(0, 10))

        # Frame B2: Formulario de Entradas
        self.frame_inputs = tk.Frame(
            self.frame_content,
            bg=self.COLOR_BOX_BG,
            bd=1,
            relief="solid",
            padx=15,
            pady=15,
        )
        self.frame_inputs.pack(fill="x", pady=5)

        # Campos de entrada
        self.entry_a = self._create_input_row("Coeficiente\na:", "a", 0)
        self.entry_b = self._create_input_row("Coeficiente\nb:", "b", 1)
        self.entry_c = self._create_input_row("Coeficiente\nc:", "c", 2)

        # Frame B3: Botones de Acción
        self.frame_actions = tk.Frame(
            self.frame_content, bg=self.COLOR_CONTENT_BG
        )
        self.frame_actions.pack(fill="x", pady=15)

        btn_calc = tk.Button(
            self.frame_actions,
            text="▶  Calcular",
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_BTN_CALC,
            fg="white",
            activebackground="#004070",
            activeforeground="white",
            relief="flat",
            padx=15,
            pady=6,
            cursor="hand2",
            command=self.calcular,
        )
        btn_calc.pack(side="left", padx=(0, 10))

        btn_clear = tk.Button(
            self.frame_actions,
            text="⌫  Limpiar",
            font=("Segoe UI", 9),
            bg=self.COLOR_BTN_CLEAR,
            fg=self.COLOR_TEXT_MAIN,
            activebackground="#D0D0D0",
            relief="groove",
            padx=15,
            pady=5,
            cursor="hand2",
            command=self.limpiar,
        )
        btn_clear.pack(side="left")

        # Frame B4: Contenedor de Resultados
        self.frame_results = tk.Frame(
            self.frame_content, bg=self.COLOR_CONTENT_BG
        )
        self.frame_results.pack(fill="both", expand=True)

        lbl_res_header = tk.Label(
            self.frame_results,
            text="Resultados:",
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_CONTENT_BG,
            fg=self.COLOR_TEXT_MAIN,
            anchor="w",
        )
        lbl_res_header.pack(fill="x", pady=(0, 5))

        # Caja visual de texto para el resultado
        self.txt_output = tk.Text(
            self.frame_results,
            font=("Consolas", 10),
            bg="white",
            fg="#444444",
            bd=1,
            relief="solid",
            height=4,
            padx=10,
            pady=10,
        )
        self.txt_output.pack(fill="both", expand=True)
        self.txt_output.insert("1.0", "Esperando entrada de datos...")
        self.txt_output.config(state="disabled")

        # ==========================================
        # 2. PIE DE PÁGINA (Footer Frame)
        # ==========================================
        self.frame_footer = tk.Frame(
            self.root,
            bg=self.COLOR_SIDEBAR_BG,
            bd=1,
            relief="solid",
            padx=15,
            pady=8,
        )
        self.frame_footer.pack(side="bottom", fill="x")

        lbl_copy = tk.Label(
            self.frame_footer,
            text="© 2026 Industrial Systems Engineering",
            font=("Segoe UI", 8),
            bg=self.COLOR_SIDEBAR_BG,
            fg=self.COLOR_TEXT_MUTED,
        )
        lbl_copy.pack(side="left")

        lbl_links = tk.Label(
            self.frame_footer,
            text="Documentation   License   Source",
            font=("Segoe UI", 8),
            bg=self.COLOR_SIDEBAR_BG,
            fg=self.COLOR_TEXT_MUTED,
            cursor="hand2",
        )
        lbl_links.pack(side="right")

    # ----------------------------------------------------------------------
    # MÉTODOS AUXILIARES Y LÓGICA MATEMÁTICA
    # ----------------------------------------------------------------------
    def _create_input_row(self, label_text, key, row_idx):
        """Crea una fila de entrada estandarizada en el Frame de Inputs."""
        lbl = tk.Label(
            self.frame_inputs,
            text=label_text,
            font=("Segoe UI", 9),
            bg=self.COLOR_BOX_BG,
            fg=self.COLOR_TEXT_MAIN,
            justify="left",
            anchor="w",
            width=12,
        )
        lbl.grid(row=row_idx, column=0, sticky="w", pady=4)

        entry = tk.Entry(
            self.frame_inputs,
            font=("Segoe UI", 10),
            bd=1,
            relief="solid",
            fg="gray",
        )
        entry.grid(row=row_idx, column=1, sticky="ew", padx=(10, 0), pady=4)
        entry.insert(0, self.placeholders[key])

        # Manejo de Placeholders dinámicos
        entry.bind(
            "<FocusIn>",
            lambda e: self._on_focus_in(entry, self.placeholders[key]),
        )
        entry.bind(
            "<FocusOut>",
            lambda e: self._on_focus_out(entry, self.placeholders[key]),
        )

        self.frame_inputs.grid_columnconfigure(1, weight=1)
        return entry

    def _on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def _on_focus_out(self, entry, placeholder):
        if entry.get().strip() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    def _get_val(self, entry, placeholder):
        val = entry.get().strip()
        if val == placeholder or val == "":
            raise ValueError("Campo incompleto")
        return float(val)

    def calcular(self):
        """Realiza el cálculo matemático de la ecuación cuadrática."""
        try:
            a = self._get_val(self.entry_a, self.placeholders["a"])
            b = self._get_val(self.entry_b, self.placeholders["b"])
            c = self._get_val(self.entry_c, self.placeholders["c"])
        except ValueError:
            messagebox.showwarning(
                "Entrada inválida",
                "Por favor, ingresa valores numéricos válidos para a, b y c.",
            )
            return

        if a == 0:
            messagebox.showerror(
                "Error Matemático",
                "El coeficiente 'a' no puede ser 0 en una ecuación cuadrática.",
            )
            return

        discriminante = (b**2) - (4 * a * c)

        # Formateo de salida
        res_text = f"Discriminante (Δ): {discriminante:.2f}\n"

        if discriminante > 0:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            res_text += f"Raíces reales y distintas:\n  ▶ x₁ = {x1:.4f}\n  ▶ x₂ = {x2:.4f}"
        elif discriminante == 0:
            x = -b / (2 * a)
            res_text += f"Raíz real única (Doble):\n  ▶ x₁ = x₂ = {x:.4f}"
        else:
            real_part = -b / (2 * a)
            imag_part = math.sqrt(-discriminante) / (2 * a)
            res_text += f"Raíces complejas conjugadas:\n  ▶ x₁ = {real_part:.4f} + {abs(imag_part):.4f}i\n  ▶ x₂ = {real_part:.4f} - {abs(imag_part):.4f}i"

        self._update_output(res_text, is_result=True)

    def limpiar(self):
        """Restablece los campos de entrada y la caja de resultados."""
        for entry, key in [
            (self.entry_a, "a"),
            (self.entry_b, "b"),
            (self.entry_c, "c"),
        ]:
            entry.delete(0, tk.END)
            entry.insert(0, self.placeholders[key])
            entry.config(fg="gray")

        self._update_output("Esperando entrada de datos...", is_result=False)

    def _update_output(self, text, is_result=False):
        self.txt_output.config(state="normal")
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert("1.0", text)
        self.txt_output.config(fg="#000000" if is_result else "#666666")
        self.txt_output.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuadraticSolverApp(root)
    root.mainloop()