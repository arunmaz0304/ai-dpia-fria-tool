# AI System DPIA & FRIA Assessment Tool

An interactive tool for running a combined Data Protection Impact Assessment (GDPR Art. 35) and Fundamental Rights Impact Assessment (EU AI Act Art. 27) on an AI system, with a companion framework document.

## What's in here

| File | What it is |
|---|---|
| `index.html` | The assessment tool. Single self-contained page, open it in any browser. No install, no server. |
| `docs/DPIA_FRIA_Framework_AI_Systems.docx` | The written framework the tool is based on: Stages 0–7 with checklists and sign-off gates. |

## Coverage

- Screening: GDPR applicability, Art. 35(3) mandatory categories, EDPB/WP29 nine criteria, IMY list, AI Act classification, Art. 27 FRIA trigger
- Scoping and data mapping (training vs inference data, flows, transfers, vendor/supply chain)
- Necessity and proportionality, legal basis by phase
- AI-specific risk register (bias, hallucination, automation bias, model inversion, function creep…)
- Measures, residual risk, sign-off, monitoring schedule
- Summary report

## Using it

Open `index.html` in a browser. Nothing is sent anywhere; the page runs fully offline.

- **Autosave:** answers are kept in your browser as you go, so a refresh doesn't lose them.
- **Save to file:** downloads the assessment as a `.json` file. Use this to keep a record, move to another computer, or hand over to a colleague.
- **Open file:** loads a saved `.json` back in.
- **New assessment:** clears the current answers (save first if you need them).
- **Print report:** on the Report tab; the save/open buttons are hidden in print.

Autosave lives in one browser on one computer only. Treat the `.json` file as the real record, and remember it will contain whatever you typed, possibly personal data about the system under review.

## Caveat

Reflects the legal position as understood at drafting. Check against the current GDPR/AI Act texts, latest EDPB guidance, Commission guidelines, any changes to the AI Act timetable (incl. the digital omnibus), and IMY guidance before relying on it. Not legal advice.

---
Maintained by Aru Mazumder (Yellow Elk Law & Technology).
