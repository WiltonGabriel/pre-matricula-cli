from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Input, Button
import csv


class MatriculaApp(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    TITLE = "Sistema de Pré-Matrículas"
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Input(placeholder="Nome completo do aluno", id="input_nome")
        yield Input(placeholder="CPF do Aluno", id="input_cpf")
        yield Input(placeholder="CEP do Aluno",id="input_cep")
        yield Input(placeholder="Data de Nascimento do Aluno (DD/MM/AAAA)",id="input_nascimento")

        yield Input(placeholder="Nome do Responsável", id="input_responsavel")
        yield Input(placeholder="Telefone/WhatsApp do Responsável",id="input_telefone")
        yield Input(placeholder="Série (Ex: 1º Ano do Ensino Médio)",id="input_serie")

        yield Button("Salvar", id="btn_salvar")

        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    def on_button_pressed(self, event) -> None:
        nome_digitado = self.query_one("#input_nome", Input).value
        cpf_digitado = self.query_one("#input_cpf", Input).value
        cep_digitado = self.query_one("#input_cep", Input).value
        Nascimento_digitado = self.query_one("#input_nascimento", Input).value

        nomeR_digitado = self.query_one("#input_responsavel", Input).value
        Telefone_digitado = self.query_one("#input_telefone", Input).value
        serie_digitado = self.query_one("#input_serie", Input).value

        aluno={
        "Nome completo":nome_digitado,
        "CPF": cpf_digitado,
        "CEP": cep_digitado,
        "Nascimento":  Nascimento_digitado,
        "Responsável": nomeR_digitado,
        "Telefone": Telefone_digitado,
        "Série": serie_digitado
        }

        colunas = ["Nome completo", "CPF", "CEP", "Nascimento", "Responsável", "Telefone", "Série"]

        nome_arquivo= "matricula_" + aluno["Nome completo"]+".csv"

        with open(nome_arquivo, mode="w",newline="") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas)
            escritor.writeheader()
            escritor.writerow(aluno)
            
if __name__ == "__main__":
    app = MatriculaApp()
    app.run()
