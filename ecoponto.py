__version__ = "1.0.0"
print(f"EcoPonto Inteligente - Versão {__version__}")

import json
from datetime import datetime

class EcoPonto:
    def __init__(self):
        self.materiais = {
            "1": {"nome": "Plástico", "eco_pontos": 10, "dica": "Lave para remover resíduos orgânicos."},
            "2": {"nome": "Papel", "eco_pontos": 5, "dica": "Não pode estar sujo de gordura."},
            "3": {"nome": "Vidro", "eco_pontos": 15, "dica": "Embale se estiver quebrado."},
            "4": {"nome": "Metal", "eco_pontos": 12, "dica": "Amasse as latas."},
            "5": {"nome": "Eletrônico", "eco_pontos": 50, "dica": "Nunca descarte no lixo comum."},
            "6": {"nome": "Óleo", "eco_pontos": 40, "dica": "Armazene em garrafas PET."}
        }

        self.total_pontos = 0
        self.historico = []
        self.carregar_dados()

    # -------------------------
    # Persistência
    # -------------------------
    def salvar_dados(self):
        dados = {
            "total_pontos": self.total_pontos,
            "historico": self.historico
        }
        with open("ecoponto.json", "w") as f:
            json.dump(dados, f)

    def carregar_dados(self):
        try:
            with open("ecoponto.json", "r") as f:
                dados = json.load(f)
                self.total_pontos = dados["total_pontos"]
                self.historico = dados["historico"]
        except:
            pass

    # -------------------------
    # Sistema de nível
    # -------------------------
    def calcular_nivel(self):
        if self.total_pontos < 100:
            return "🌱 Iniciante"
        elif self.total_pontos < 500:
            return "🌿 Consciente"
        elif self.total_pontos < 1000:
            return "🌳 Sustentável"
        else:
            return "🌎 Guardião do Planeta"

    # -------------------------
    # Interface
    # -------------------------
    def exibir_menu(self):
        print("\n" + "="*40)
        print("🌿 ECOPONTO INTELIGENTE 🌿")
        print("="*40)
        print(f"Pontuação: {self.total_pontos:.1f} | Nível: {self.calcular_nivel()}")
        print("\n[1-6] Registrar descarte")
        print("[7] Ver histórico")
        print("[8] Ver relatório")
        print("[0] Sair")
        print("-" * 40)

    # -------------------------
    # Funcionalidades
    # -------------------------
    def escolher_material(self):
        print("\nMateriais disponíveis:")
        for k, v in self.materiais.items():
            print(f"[{k}] {v['nome']}")
        return input("Escolha o material: ")

    def processar_descarte(self):
        opcao = self.escolher_material()

        if opcao not in self.materiais:
            print("❌ Material inválido.")
            return

        item = self.materiais[opcao]

        try:
            peso = float(input("Peso (kg): "))
            if peso <= 0:
                raise ValueError

            pontos = peso * item["eco_pontos"]
            self.total_pontos += pontos

            registro = {
                "material": item["nome"],
                "peso": peso,
                "pontos": pontos,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            }

            self.historico.append(registro)
            self.salvar_dados()

            print("\n✅ Descarte registrado!")
            print(f"💡 Dica: {item['dica']}")
            print(f"⭐ +{pontos:.1f} pontos")

        except ValueError:
            print("❌ Peso inválido.")

    def ver_historico(self):
        if not self.historico:
            print("\nNenhum registro ainda.")
            return

        print("\n📜 HISTÓRICO:")
        for h in self.historico:
            print(f"{h['data']} - {h['material']} ({h['peso']}kg) → {h['pontos']} pts")

    def relatorio(self):
        if not self.historico:
            print("\nSem dados para relatório.")
            return

        total_kg = sum(h["peso"] for h in self.historico)

        print("\n📊 RELATÓRIO:")
        print(f"Total descartado: {total_kg:.1f} kg")
        print(f"Total de pontos: {self.total_pontos:.1f}")
        print(f"Nível atual: {self.calcular_nivel()}")

    # -------------------------
    # Execução
    # -------------------------
    def iniciar(self):
        while True:
            self.exibir_menu()
            op = input("Escolha: ")

            if op == "1":
                self.processar_descarte()
            elif op == "7":
                self.ver_historico()
            elif op == "8":
                self.relatorio()
            elif op == "0":
                print("\n🌎 Obrigado por contribuir com o planeta!")
                break
            else:
                print("❌ Opção inválida.")


if __name__ == "__main__":
    app = EcoPonto()
    app.iniciar()