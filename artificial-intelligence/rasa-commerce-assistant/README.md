# Rasa Commerce Assistant

An English-language conversational shopping assistant created for the
Artificial Intelligence Methods course at MISIS in 2023.

## What was implemented

The assistant uses Rasa to recognize customer intents and manage dialogue
forms, entities, and slots. Custom Python actions connect the conversation to a
small SQLite store supporting:

- registration and sign-in;
- inventory checks and shoe reservations;
- cart operations;
- order status, cancellation, and returns;
- feedback and product-update flows.

The project structure follows a standard Rasa application: training examples,
stories, and rules live in `data/`; dialogue definitions are in `domain.yml`;
and business logic is in `actions/actions.py`.

## Technologies

- Python
- Rasa 3.2 and Rasa SDK 3.2
- SQLite
- Duckling entity extraction

## Running the project

This project uses an older dependency set and is best treated as an archival
Rasa 3.2 application.

```bash
pip install -r requirements.txt
python initialize_db.py
rasa train
```

Run the custom-action server in one terminal:

```bash
rasa run actions
```

Then start an interactive conversation in another:

```bash
rasa shell
```

`config.yml` expects a Duckling service at `http://localhost:8000` for number
and email extraction.

## Known limitations

- The dependency lock reflects the original environment and may not install on
  current Python versions without adjustment.
- Passwords are stored as plain text because this is a classroom prototype,
  not a production authentication system.
- Some user-facing responses remain in Russian.
- Generated Rasa caches and trained model archives were omitted because they
  can be reproduced from the source.

## Authors

Michael Ratke and Daria Sergeeva, fourth-year students in group BPM-20-4.

## Historical note

The project was written by hand before generative AI coding assistants became
widely available. It is preserved as historical student work.
