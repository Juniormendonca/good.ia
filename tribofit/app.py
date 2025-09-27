"""Core application logic for the TriboFit CLI experience."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Objective:
    """Represents a training objective."""

    name: str
    description: str


@dataclass
class Workout:
    """Represents a workout exercise."""

    name: str
    repetitions: int
    instructions: str


@dataclass
class Avatar:
    """Represents a selectable avatar."""

    name: str
    archetype: str
    description: str


@dataclass
class Community:
    """Represents a TriboFit community."""

    name: str
    focus: str
    members: int


@dataclass
class RankingEntry:
    """Represents a ranking leaderboard entry."""

    username: str
    workouts_completed: int
    streak_days: int


@dataclass
class StoreItem:
    """Represents an item from the TriboFit store."""

    name: str
    category: str
    price: float


@dataclass
class User:
    """Represents a TriboFit user profile."""

    username: str
    avatar: Optional[Avatar] = None
    objective: Optional[Objective] = None
    completed_workouts: List[str] = field(default_factory=list)


class TriboFitApp:
    """A lightweight in-terminal simulation of the TriboFit experience."""

    def __init__(self) -> None:
        self.user: Optional[User] = None
        self.objectives = self._load_objectives()
        self.workouts = self._load_workouts()
        self.avatars = self._load_avatars()
        self.communities = self._load_communities()
        self.ranking = self._load_ranking()
        self.store_items = self._load_store()

    # ------------------------------------------------------------------
    # Data loading helpers
    # ------------------------------------------------------------------
    def _load_objectives(self) -> List[Objective]:
        return [
            Objective("Condicionamento", "Ganhe resistência com treinos focados em cardio."),
            Objective("Força", "Construa músculos com rotinas de força progressiva."),
            Objective("Equilíbrio", "Melhore sua postura e estabilidade com treinos funcionais."),
        ]

    def _load_workouts(self) -> List[Workout]:
        return [
            Workout("Agachamento", 15, "Agache mantendo as costas retas e os joelhos alinhados."),
            Workout("Flexão", 12, "Mantenha o core firme e desça até 90 graus."),
            Workout("Prancha", 1, "Sustente a posição de prancha por 60 segundos."),
        ]

    def _load_avatars(self) -> List[Avatar]:
        return [
            Avatar("Alpha", "Explorador", "Equilibrado, ótimo para quem gosta de desafios variados."),
            Avatar("Nitro", "Velocista", "Ideal para quem busca treinos explosivos e cardio intenso."),
            Avatar("FurBot", "Suporte", "Focado em mobilidade e treinos de recuperação."),
        ]

    def _load_communities(self) -> List[Community]:
        return [
            Community("Projeto Verão", "Resultados rápidos", 1820),
            Community("Crossfit Lovers", "WODs diários", 2450),
            Community("Yoga Mind", "Equilíbrio corpo e mente", 980),
        ]

    def _load_ranking(self) -> List[RankingEntry]:
        return [
            RankingEntry("@diana_f", 86, 21),
            RankingEntry("@mauro.fit", 64, 14),
            RankingEntry("@bianca_runs", 59, 11),
        ]

    def _load_store(self) -> List[StoreItem]:
        return [
            StoreItem("Bandas Elásticas", "Acessórios", 79.90),
            StoreItem("Garrafa Térmica", "Acessórios", 59.90),
            StoreItem("Camiseta TriboFit", "Roupas", 99.90),
        ]

    # ------------------------------------------------------------------
    # User actions
    # ------------------------------------------------------------------
    def login(self, username: str) -> str:
        """Simulate a login returning a welcome message."""
        self.user = User(username=username)
        return f"Bem-vindo de volta, {username}!"

    def select_objective(self, objective_name: str) -> Objective:
        if not self.user:
            raise ValueError("Nenhum usuário logado.")
        for obj in self.objectives:
            if obj.name == objective_name:
                self.user.objective = obj
                return obj
        raise ValueError(f"Objetivo '{objective_name}' não encontrado.")

    def choose_avatar(self, avatar_name: str) -> Avatar:
        if not self.user:
            raise ValueError("Nenhum usuário logado.")
        for avatar in self.avatars:
            if avatar.name == avatar_name:
                self.user.avatar = avatar
                return avatar
        raise ValueError(f"Avatar '{avatar_name}' não encontrado.")

    def complete_workout(self, workout_name: str) -> Workout:
        if not self.user:
            raise ValueError("Nenhum usuário logado.")
        for workout in self.workouts:
            if workout.name == workout_name:
                self.user.completed_workouts.append(workout_name)
                return workout
        raise ValueError(f"Treino '{workout_name}' não encontrado.")

    # ------------------------------------------------------------------
    # Screen builders (return textual representation)
    # ------------------------------------------------------------------
    def welcome_screen(self) -> str:
        username = self.user.username if self.user else "visitante"
        return (
            "TRIBO.FIT\n"
            f"Bem-vindo, {username}!\n"
            "Próximo treino em 3h\n"
            "1) Comunidade\n2) Lojas\n3) Ranking\n"
        )

    def objectives_screen(self) -> str:
        lines = ["Objetivos:"]
        for obj in self.objectives:
            lines.append(f"- {obj.name}: {obj.description}")
        return "\n".join(lines)

    def avatars_screen(self) -> str:
        lines = ["Escolha seu avatar:"]
        for avatar in self.avatars:
            lines.append(
                f"- {avatar.name} ({avatar.archetype}): {avatar.description}"
            )
        return "\n".join(lines)

    def training_screen(self) -> str:
        lines = ["Treino do dia:"]
        for workout in self.workouts:
            lines.append(f"- {workout.name} x{workout.repetitions}: {workout.instructions}")
        return "\n".join(lines)

    def feed_screen(self) -> str:
        return (
            "Feed:\n"
            "@diana_f concluiu o Desafio Nitro.\n"
            "@mauro.fit compartilhou um novo WOD.\n"
            "@bianca_runs comemorou 30 dias de streak!"
        )

    def community_screen(self) -> str:
        lines = ["Comunidades disponíveis:"]
        for community in self.communities:
            lines.append(
                f"- {community.name}: {community.focus} ({community.members} membros)"
            )
        return "\n".join(lines)

    def ranking_screen(self) -> str:
        lines = ["Ranking Fitness:"]
        for index, entry in enumerate(self.ranking, start=1):
            lines.append(
                f"{index}. {entry.username} - {entry.workouts_completed} treinos, {entry.streak_days} dias de streak"
            )
        return "\n".join(lines)

    def store_screen(self) -> str:
        lines = ["Loja TriboFit:"]
        for item in self.store_items:
            lines.append(f"- {item.name} ({item.category}) - R$ {item.price:.2f}")
        return "\n".join(lines)

    def get_summary(self) -> str:
        if not self.user:
            raise ValueError("Nenhum usuário logado.")
        objective = self.user.objective.name if self.user.objective else "Nenhum"
        avatar = self.user.avatar.name if self.user.avatar else "Nenhum"
        workouts = ", ".join(self.user.completed_workouts) or "Nenhum"
        return (
            "Resumo do perfil:\n"
            f"Usuário: {self.user.username}\n"
            f"Objetivo: {objective}\n"
            f"Avatar: {avatar}\n"
            f"Treinos concluídos: {workouts}"
        )


def build_demo_app() -> TriboFitApp:
    """Helper to build an app preloaded with demo selections."""
    app = TriboFitApp()
    app.login("@triber")
    app.select_objective("Força")
    app.choose_avatar("Alpha")
    app.complete_workout("Agachamento")
    return app
