"""Minimal HTTP server that renders the TriboFit prototype as HTML."""
from __future__ import annotations

from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Iterable

from .app import TriboFitApp, build_demo_app


def _render_list(items: Iterable[str]) -> str:
    return "".join(f"<li>{escape(item)}</li>" for item in items)


def render_homepage(app: TriboFitApp) -> str:
    """Return an HTML page representing the TriboFit experience."""

    user = app.user.username if app.user else "Visitante"
    objective = app.user.objective.name if app.user and app.user.objective else "Nenhum"
    avatar = app.user.avatar.name if app.user and app.user.avatar else "Nenhum"
    completed = app.user.completed_workouts if app.user else []

    objectives = _render_list(
        f"{item.name} — {item.description}" for item in app.objectives
    )
    avatars = _render_list(
        f"{item.name} ({item.archetype}) — {item.description}" for item in app.avatars
    )
    workouts = _render_list(
        f"{item.name} ×{item.repetitions}: {item.instructions}" for item in app.workouts
    )
    feed = _render_list(
        [
            "@diana_f concluiu o Desafio Nitro.",
            "@mauro.fit compartilhou um novo WOD.",
            "@bianca_runs comemorou 30 dias de streak!",
        ]
    )
    communities = _render_list(
        f"{item.name} — {item.focus} ({item.members} membros)" for item in app.communities
    )
    ranking = _render_list(
        f"{index}. {entry.username} — {entry.workouts_completed} treinos · {entry.streak_days} dias"
        for index, entry in enumerate(app.ranking, start=1)
    )
    store = _render_list(
        f"{item.name} ({item.category}) — R$ {item.price:.2f}" for item in app.store_items
    )
    completed_workouts = (
        _render_list(completed)
        if completed
        else '<li class="placeholder">Nenhum treino concluído ainda</li>'
    )

    return f"""
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <title>TriboFit — protótipo web</title>
    <style>
      :root {{
        color-scheme: light dark;
        font-family: 'Segoe UI', system-ui, sans-serif;
        background: #0b0d16;
        color: #f5f5f5;
      }}
      body {{
        margin: 0;
        padding: 0;
        background: radial-gradient(circle at top, #111831 0%, #05070d 70%);
        min-height: 100vh;
      }}
      header {{
        padding: 2.5rem 1.5rem 1rem;
        text-align: center;
      }}
      h1 {{
        letter-spacing: 0.2rem;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
      }}
      .tagline {{
        color: #9fb4ff;
        font-weight: 500;
        margin: 0;
      }}
      main {{
        display: grid;
        gap: 1.5rem;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        padding: 0 1.5rem 2.5rem;
      }}
      section {{
        background: rgba(17, 24, 49, 0.75);
        border: 1px solid rgba(159, 180, 255, 0.15);
        border-radius: 18px;
        padding: 1.5rem;
        box-shadow: 0 20px 40px rgba(3, 8, 24, 0.45);
        backdrop-filter: blur(12px);
      }}
      h2 {{
        font-size: 1.125rem;
        margin-top: 0;
        color: #9fb4ff;
        text-transform: uppercase;
        letter-spacing: 0.1rem;
      }}
      ul {{
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
      }}
      li {{
        background: rgba(5, 7, 13, 0.55);
        border-radius: 12px;
        padding: 0.75rem 1rem;
        line-height: 1.4;
        box-shadow: inset 0 0 0 1px rgba(159, 180, 255, 0.08);
      }}
      .summary-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.75rem;
      }}
      .summary-card {{
        background: linear-gradient(140deg, rgba(90, 120, 255, 0.4), rgba(3, 8, 24, 0.4));
        border-radius: 14px;
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(159, 180, 255, 0.25);
      }}
      .summary-card span {{
        display: block;
        font-size: 0.75rem;
        letter-spacing: 0.08rem;
        text-transform: uppercase;
        color: rgba(245, 245, 245, 0.75);
      }}
      .summary-card strong {{
        font-size: 1.25rem;
      }}
      .placeholder {{
        color: rgba(245, 245, 245, 0.55);
        font-style: italic;
      }}
      footer {{
        text-align: center;
        padding: 1.5rem;
        color: rgba(245, 245, 245, 0.55);
        font-size: 0.875rem;
      }}
      a {{
        color: #9fb4ff;
      }}
    </style>
  </head>
  <body>
    <header>
      <h1>TriboFit</h1>
      <p class="tagline">Energia da tribo com foco no seu progresso diário</p>
    </header>
    <main>
      <section>
        <h2>Resumo</h2>
        <div class="summary-grid">
          <div class="summary-card">
            <span>Usuário</span>
            <strong>{escape(user)}</strong>
          </div>
          <div class="summary-card">
            <span>Objetivo</span>
            <strong>{escape(objective)}</strong>
          </div>
          <div class="summary-card">
            <span>Avatar</span>
            <strong>{escape(avatar)}</strong>
          </div>
        </div>
      </section>
      <section>
        <h2>Objetivos</h2>
        <ul>{objectives}</ul>
      </section>
      <section>
        <h2>Avatares</h2>
        <ul>{avatars}</ul>
      </section>
      <section>
        <h2>Treino do Dia</h2>
        <ul>{workouts}</ul>
      </section>
      <section>
        <h2>Feed da Tribo</h2>
        <ul>{feed}</ul>
      </section>
      <section>
        <h2>Comunidades</h2>
        <ul>{communities}</ul>
      </section>
      <section>
        <h2>Ranking</h2>
        <ul>{ranking}</ul>
      </section>
      <section>
        <h2>Loja</h2>
        <ul>{store}</ul>
      </section>
      <section>
        <h2>Treinos Concluídos</h2>
        <ul>{completed_workouts}</ul>
      </section>
    </main>
    <footer>
      Visualização web do protótipo TriboFit. Ajuste os dados no servidor para testar novos cenários.
    </footer>
  </body>
</html>
"""


class _TriboFitRequestHandler(BaseHTTPRequestHandler):
    """Serve the TriboFit homepage for any GET request."""

    demo_app: TriboFitApp = build_demo_app()

    def do_GET(self) -> None:  # noqa: N802 (keep signature from BaseHTTPRequestHandler)
        html = render_homepage(self.demo_app)
        encoded = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, *_: object) -> None:  # pragma: no cover - silence default logs
        return


def run_web_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Start a simple HTTP server that renders the TriboFit prototype."""

    server = HTTPServer((host, port), _TriboFitRequestHandler)
    print(f"TriboFit web disponível em http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:  # pragma: no cover - manual shutdown
        print("Encerrando servidor TriboFit...")
    finally:
        server.server_close()


if __name__ == "__main__":
    run_web_server()
