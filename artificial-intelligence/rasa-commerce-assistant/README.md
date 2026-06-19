# Rasa Commerce Assistant

Laboratory project for the Artificial Intelligence Methods course at the
National University of Science and Technology MISIS.

The project implements a conversational shopping assistant using Rasa. It
recognizes customer intents, manages dialogue forms and slots, and uses custom
Python actions with SQLite for registration, authentication, inventory checks,
reservations, cart operations, order status, cancellation, and returns.

## Main components

- `data/` contains NLU examples, stories, and dialogue rules.
- `domain.yml` defines intents, entities, slots, forms, and responses.
- `actions/actions.py` contains the custom business actions.
- `initialize_db.py` creates the demonstration inventory, users, and orders.
- `tests/` contains Rasa conversation tests.

Generated Rasa caches and trained model archives were intentionally omitted from
the consolidated archive because they can be reproduced from the source files.

## Authors

Michael Ratke and Daria Sergeeva, fourth-year students in group BPM-20-4.

This is historical coursework written manually without generative-AI-produced
code.
