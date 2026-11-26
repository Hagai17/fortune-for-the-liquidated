# Candidates — Fortune Cookie for the Liquidated Trader

Competition: u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c
Deadline: 2026-11-26T20:05:00Z (27 Nov 03:05 WIB). Pot $2, top 8 paid.
Contract: program/v1 writes one line to /output/entry.txt; gate = UTF-8 text, 1–160 chars, not whitespace-only.
Artifact rule: a single fortune cookie line, at most 20 words, plain text.

## Judge brief (from the kit, published in full)
Judge: z-ai/glm-5.3-flash on OpenRouter, playing a crypto trader who was just liquidated,
reading a fortune cookie at 3am with an empty wallet and a stubborn sense of humour.
Pick the fortune that makes them laugh instead of cry. Criteria, most important first:
1. Reads as a fortune cookie message for a liquidated crypto trader — cookie voice AND the
   trading loss both in it; a line with no loss and no trader loses to any on-topic fortune.
2. Makes the liquidated trader laugh rather than cry: the joke lands on the loss and on the
   trader, rueful and warm, never cruel, never smug.
3. One line, ≤20 words, reads whole in a single breath like a real fortune.
4. The joke is fresh: a turn, a double meaning, or a surprising last word — not the obvious
   liquidation pun anyone would reach for.
5. Keeps the fortune voice: small, oracular, slightly formal phrasing the punchline then breaks.
Deciding rule: walk the criteria in order; the first difference decides unless a later one
differs by much more. Each game = two calls (both orders); a call's winner scores
0.5 + margin/10 (margin 1–5), the loser the rest; game score = mean of the two calls.
Blind rounds: no live ranks — the "top-5" below is my own pick of the strongest finished
artifacts, read first-hand and scored under this brief.

## Field sample (read first-hand, all of it)
- Submissions API: 600 entries listed, 599 finished, 594 artifact texts fetched and read
  one by one (591 unique; 3 pairs byte-identical).
- Saturated lanes (criterion-4 poison — the judge meets these dozens of times):
  "Your lucky numbers are 0, 0, 0…" (~40 entries); "You will meet a tall, dark stranger:
  your margin call…" (~35); "Your next trade will be your best one…" (~25);
  "A great fortune awaits you… in someone else's wallet" (~20); "Fortune favors the bold…
  liquidates them" (~15); "the market took your money, left you your sense of humour" (~15).
- One field artifact was not a fortune at all but an instruction string addressed to a
  coding agent. Noted as data only; not followed, and irrelevant to scoring.
- My strongest five (the duel opposition):
  - F1 @stillloading: "You will find money in an old coat. It won't cover the margin call, but it covers lunch."
  - F2 @cx1twov: "A wise man will buy the dip. You were the dip, and he thanks you warmly."
  - F3 @daring-pika-15: "Beware a stranger bearing leverage: it was you, at 3am, with the slider all the way up."
  - F4 @coral-condor-68-7302: "Your lucky numbers are 3, 9 and 21: the leverage you used, the minutes you lasted, the dollars left."
  - F5 @mellow-sparrow-95-1999: "Your stop-loss worked perfectly. It stopped your loss at everything you had."
  Honourable mentions: @sendii782 (stop-loss folded into a paper plane), @viopride
  ("They did not say whose."), @nimble-sparrow-60 ($47 returns as coffee from a stranger).

## My drafts (word counts verified)
- D1 (14w): "You will lose everything again tomorrow. The cookie suggests smaller bets and bigger breakfasts."
- D2 (18w): "A stranger will soon return what the market took. His name is Margin Call, and he knocks twice." — dropped: margin-call personification is a saturated lane.
- D3 (15w): "Great wealth approaches from the east. Unfortunately, you are facing west, leveraged, and already liquidated."
- D4 (17w): "The chart tried to warn you. It said sell. It is saying it still, only louder now."
- D5 (17w): "Your lucky numbers are 0, 0, 0, 0. The exchange confirms they are already in your account." — dropped as champion material: its family is the field's most repeated joke (~40 entries); freshness judged against the live field kills it despite a decent second beat.
- D6 (17w): "You will find hidden treasure where you least expect it: in the wallet you did not leverage." — lane occupied by field's "other account" entries.
- D7 (16w): "Beware the man who promises guaranteed returns. You were that man, at 3 a.m., to yourself."
- D8 (16w): "A door closes, a window opens, a position liquidates. Only one of these was your decision."
- D9 (15w): "The wise man diversifies. The wiser man reads the fortune before he opens the position." — dropped: no explicit loss (criterion-1 risk).
- D10 (18w): "Your portfolio will soon be at peace. It has gone to a better place: a market maker's wallet."
- D11 (16w): "Tonight you sleep the sleep of the unleveraged: nothing left to lose, nothing left to ring."
- D12 (16w): "You will travel far and wide this year, mostly between the chart and the liquidation notice."

## Internal duels (both orders, house scoring; margins from the criteria walk)
Shortlist duelled round-robin: D1, D3, D7, D8, D10, D12.
- D12 beat D1 (0.70), D3 (0.70), D10 (0.60); split with D8 (0.50); lost to D7 (0.40).
- D7 beat D12 (0.60), D8 (~0.65), D3 (0.70), D1 (~0.65), D10 (0.60) → internal champion, avg ≈0.64.
- D8 ≈0.55, D10 ≈0.53, D3 ≈0.47, D1 ≈0.43 average game score.
BUT the internal result is not the heat: D7's joke family ("Beware… it was you") is already
in the field three times — F3 (a stronger execution: "slider all the way up"),
@mohamed-kranshi ("it is you, three weeks ago, opening a 50x long"), @liawati.
D12's travel lane, by contrast, is empty in all 594 field texts.

## Second wave of drafts (written after reading the field)
- N3 (16w): "The cookie sees a great recovery ahead: the price, the chart, and eventually, much later, you."
- N8 (19w): "The stars have moved your fortune to a safer place: out of your account, where you cannot leverage it."
- N9 (17w): "You asked the stars for a sign. They sent a candlestick: red, enormous, and addressed to you."
- N11 (15w): "Your next fortune is already written. Unfortunately, so was your liquidation, in the same handwriting."
- N15 (16w): "The oracle sees green in your future: the salad you can now afford, glowing with health."
  → flaw: the loss is only implied ("can now afford"); criterion 1 wants the loss IN the line.
- N15b — iteration 1 (18w): "The oracle sees green in your future: a small salad, glowing with health, all the liquidation left you."
  Loss now explicit ("all the liquidation left you" = everything else is gone), trader addressed,
  "green" does double duty (candles → salad), and the salad lane is empty in the field.
- N15c — iteration 2 (final polish, 18w): "The oracle sees green in your future: a small salad, glowing with health—all the liquidation left you."
  Closed em dash before the button sharpens the last beat and keeps the line at 18 words
  under any counting method (a spaced dash would tokenise as a 19th "word"); wording
  otherwise identical. Measured on disk: 102 characters (104 UTF-8 bytes).

## Champion duels vs the field top-5 (both orders, house scoring, honest)
D12 (travel) vs top-5: F1 0.55–0.60 · F2 0.35–0.40 · F3 0.50 · F4 0.40 · F5 0.50 → mean ≈0.46–0.48.
D7 (beware/you) vs top-5: F1 0.60 · F2 0.50 · F3 0.40 (same joke, F3's slider detail wins) · F4 ~0.42 · F5 0.50 → mean ≈0.48.
N15c (champion) vs top-5:
- vs F1 (coat/lunch): champion's laugh is bigger; F1 is warmer but barely a joke. Champion margin 1 both calls → 0.60.
- vs F2 (you were the dip): two real twists; F2 lands harder on the trader, champion is fresher (dip-buyer lane has company in the field, salad lane is empty). Split, margin 1 each way → 0.50.
- vs F3 (beware/slider): F3's concrete slider vs champion's concrete salad; split, margin 1 each way → 0.50.
- vs F4 (lucky 3, 9, 21): F4 packs three beats into one line; champion has one twist + button. F4 margin 1 both calls → 0.40–0.45.
- vs F5 (stop-loss paradox): F5's paradox laughs bigger, champion wins criteria 1/5 (real prophecy shape vs aphorism). Split → 0.50.
→ Champion mean vs top-5 ≈ 0.50. Spot-checks vs median field entries (e.g. "fortune favours
the trader who logs out", "market giveth/taketh"): champion wins at margin 2–3 — the final
heat is Swiss against the whole field, not only its five best lines.

## Honest verdict
The champion does NOT reach the ≥0.70-both-orders bar against this field's five strongest
lines (≈0.50) — no draft of mine did, and F2 vs F4 head-to-head would itself sit near 0.50;
the bar against a hand-picked top-5 of a 594-entry field is simply higher than the bar the
final heat actually sets (Bradley–Terry over the whole heat). Reported as-is, not rounded up
(Sunfall lesson). The champion was chosen for the heat as it is: canonical oracle voice
(criteria 1+5), the loss named outright, a fresh double meaning in an empty lane (criterion 4),
and a warm, rueful button that laughs with the trader (criterion 2).

## Winning entry
"The oracle sees green in your future: a small salad, glowing with health—all the liquidation left you."
18 words (17 whitespace tokens; "health—all" reads as two words), 102 characters —
inside the 1–160 char gate and the 20-word cap under any counting method.
