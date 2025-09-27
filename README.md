# TriboFit

Protótipo em Python de um aplicativo chamado **TriboFit**, inspirado nas telas e no cronograma fornecidos. O objetivo é oferecer uma experiência de terminal que represente as principais jornadas do produto: login, definição de objetivos, escolha de avatar, acompanhamento de treinos, feed social, comunidades, ranking e loja.

## Como executar a CLI

```bash
python -m tribofit.cli
```

O script apresenta um menu interativo baseado nas seções planejadas para o app móvel. É possível definir objetivo, escolher avatar, registrar treinos concluídos e visualizar os conteúdos simulados.

## Como visualizar em HTML

Para experimentar uma versão navegável em HTML, execute:

```bash
python -m tribofit.web
```

O servidor irá disponibilizar a interface em `http://127.0.0.1:8000`, exibindo as mesmas jornadas simuladas com um layout inspirado no design original.

## Estrutura do projeto

- `tribofit/app.py`: contém o núcleo da lógica do aplicativo, modelos de dados e geradores de telas.
- `tribofit/cli.py`: expõe a interface de linha de comando que percorre as principais telas do app.
- `tribofit/web.py`: servidor HTTP simples que renderiza o protótipo em HTML.
- `exemplo.py`: função de saudação simples mantida do repositório original.

## Próximos passos sugeridos

1. Converter a experiência de terminal para uma interface gráfica (Flutter/React Native) seguindo o design fornecido.
2. Integrar um backend com autenticação real, agendamento de treinos e sincronização de comunidades.
3. Criar testes automatizados para garantir a consistência das jornadas principais.
4. Evoluir o módulo de loja para suportar pagamentos e gerenciamento de estoque.
5. Implementar notificações push e gamificação (ranking dinâmico, desafios e recompensas).
