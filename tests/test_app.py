"""Unit tests for the TriboFit application core."""

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from tribofit.app import TriboFitApp, build_demo_app  # noqa: E402
from tribofit.web import render_homepage  # noqa: E402


def test_login_and_welcome_screen():
    app = TriboFitApp()
    message = app.login("@ana.fit")
    assert "@ana.fit" in message
    assert "@ana.fit" in app.welcome_screen()


def test_select_objective_and_avatar():
    app = TriboFitApp()
    app.login("@beta")
    selected_objective = app.select_objective("Força")
    selected_avatar = app.choose_avatar("Alpha")

    assert selected_objective.name == "Força"
    assert app.user and app.user.objective == selected_objective
    assert selected_avatar.name == "Alpha"
    assert app.user and app.user.avatar == selected_avatar


def test_complete_workout_updates_summary():
    app = build_demo_app()
    summary = app.get_summary()
    assert "@triber" in summary
    assert "Força" in summary
    assert "Alpha" in summary
    assert "Agachamento" in summary


def test_render_homepage_contains_sections():
    app = build_demo_app()
    html = render_homepage(app)

    assert "<h2>Objetivos</h2>" in html
    assert "<h2>Treino do Dia</h2>" in html
    assert "Loja" in html
    assert "@triber" in html


def test_invalid_options_raise_errors():
    app = TriboFitApp()
    app.login("@gamma")
    try:
        app.select_objective("Inexistente")
    except ValueError as exc:
        assert "não encontrado" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("ValueError esperado para objetivo inválido")

    try:
        app.choose_avatar("Fantasma")
    except ValueError as exc:
        assert "não encontrado" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("ValueError esperado para avatar inválido")
