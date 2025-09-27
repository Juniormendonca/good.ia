"""Command line interface for the TriboFit simulation."""
from __future__ import annotations

from typing import Callable, Dict

from .app import TriboFitApp


MENU_OPTIONS: Dict[str, Callable[[TriboFitApp], str]] = {
    "1": TriboFitApp.objectives_screen,
    "2": TriboFitApp.avatars_screen,
    "3": TriboFitApp.training_screen,
    "4": TriboFitApp.feed_screen,
    "5": TriboFitApp.community_screen,
    "6": TriboFitApp.ranking_screen,
    "7": TriboFitApp.store_screen,
    "8": TriboFitApp.get_summary,
}


def run_cli() -> None:
    """Launch an interactive text-based session."""
    app = TriboFitApp()
    username = input("Digite seu usuário TriboFit: ")
    print(app.login(username))

    while True:
        print()
        print(app.welcome_screen())
        print("Escolha uma opção:")
        print("1) Ver objetivos")
        print("2) Escolher avatar")
        print("3) Ver treino do dia")
        print("4) Abrir feed")
        print("5) Explorar comunidades")
        print("6) Ver ranking")
        print("7) Visitar loja")
        print("8) Resumo do perfil")
        print("9) Registrar treino concluído")
        print("0) Sair")

        choice = input("> ").strip()

        if choice == "0":
            print("Até logo, continue firme nos treinos!")
            break

        if choice == "2":
            print(app.avatars_screen())
            avatar_name = input("Digite o nome do avatar escolhido: ").strip()
            try:
                selected = app.choose_avatar(avatar_name)
                print(f"Avatar selecionado: {selected.name}")
            except ValueError as exc:
                print(exc)
            continue

        if choice == "1":
            print(app.objectives_screen())
            objective_name = input("Digite o nome do objetivo: ").strip()
            try:
                selected = app.select_objective(objective_name)
                print(f"Objetivo definido: {selected.name}")
            except ValueError as exc:
                print(exc)
            continue

        if choice == "9":
            print(app.training_screen())
            workout_name = input("Qual treino você completou? ").strip()
            try:
                workout = app.complete_workout(workout_name)
                print(f"Parabéns! Você concluiu {workout.name} x{workout.repetitions}.")
            except ValueError as exc:
                print(exc)
            continue

        action = MENU_OPTIONS.get(choice)
        if not action:
            print("Opção inválida, tente novamente.")
            continue

        try:
            print(action(app))
        except ValueError as exc:
            print(exc)


if __name__ == "__main__":
    run_cli()
