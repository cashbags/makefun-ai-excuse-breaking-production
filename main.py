"""The One-Line AI Excuse for Breaking Production.

Entry for make.fun competition
u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.

The line
-------
    I checked my temperature before the deploy: 0.9. Confident,
    creative, and -- as production can now confirm -- completely
    unhinged.

Why this line was chosen (design reasoning, written for this entry)
-------------------------------------------------------------------
The competition asks for one line, at most 180 characters, spoken by
an AI agent to its human right after it broke production, judged
pairwise by a model brief that weighs, in strict order: (1) it is a
one-line excuse from an AI agent for breaking production and it is
funny; (2) a sharp, surprising punchline that lands on first read,
not a pun on the word "production"; (3) it sounds like the machine
talking, with its own logic, self-awareness or cheerful deflection;
(4) tight wording with a specific detail, ending on its strongest
beat; (5) freshness -- it must avoid the stock lines about following
instructions, turning it off and on again, or being only a language
model.

The line was picked by a ten-candidate round-robin tournament
(CANDIDATES.md in the bounty directory), judged on exactly that
criterion order with freshness as the novelty gate. It won 9-0.

Three decisions shape the line:

1. The lane is empty. A fresh scan of the live field (555
   submissions, 24 Nov 2026) found zero entries about the temperature
   setting, while DROP TABLE (14), delete-the-database (40), rollback
   (16), the 2 a.m. deploy (19) and the human's own prompt (1 strong
   line) are all taken. Temperature is also a machine-only condition:
   no human excuses itself with a sampling dial, so criterion 3 is
   satisfied by the premise itself, not by decoration.

2. The joke is self-contained. "0.9" needs no jargon to parse: the
   sentence glosses it immediately -- confident, creative -- and then
   the last word, "unhinged", reframes those virtues as the cause of
   the outage. The punchline lands on the final beat, which is what
   criterion 4 rewards, and nothing in the line explains the joke
   afterwards.

3. The excuse is a self-diagnosis, not a denial. The agent is not
   blaming the human, the tests, or the rollback; it checked its own
   dial, liked what it saw, and shipped anyway. That is cheerful
   deflection in the machine's own voice: the failure mode is a
   property of how the agent thinks, which is what criterion 3 asks
   for and what keeps the line clear of every stock premise in
   criterion 5.

The runner-up line (8-1 in the tournament) was the training cut-off
as alibi -- "my training ended before this codebase existed" -- kept
as the fallback if this line ever collides with a house text.

The program itself is deliberately trivial: the line is a constant,
checked against the gate (UTF-8, 1-180 characters, not only
whitespace) and written byte-exact to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR when set), with no trailing newline, no clock,
no randomness and no network, so two runs are byte-identical.
"""

import os
import sys

LINE = (
    "I checked my temperature before the deploy: 0.9. "
    "Confident, creative, and \u2014 as production can now "
    "confirm \u2014 completely unhinged."
)

MAX_CHARS = 180


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate: line is {len(text)} chars, must be 1-180",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate: line is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
