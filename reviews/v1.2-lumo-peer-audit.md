# Peer Audit — Green Paper v1.2: *The Neuro-Architectural Substrate for a Terminal AI Development Environment*

**Auditor lens:** dual — ML Architecture (primary), Neuroscience (secondary)
**Scope audited:** Green Paper v1.2 + Consultation Response Form (template), as issued for consultation
**Stance entering:** sympathetic but unsentimental; the paper's own constitution is the grading standard

---

## Global Verdict (the paper's own grammar)

**ACCEPT WITH REVISIONS.** The v1.2 hemispheric derivation is a genuine strengthening of §5's internal coherence — but as issued, it also introduces the paper's most serious self-inflicted wound: **several clauses render the core count effectively unfalsifiable in the downward direction**, which is precisely the crime the paper accuses decorated metaphors of. Blocking items, in priority order: §4 division-count arithmetic, the router/pipeline reconciliation gap, the Chronicle substrate/tenant duality, and the one-directional falsifiability of the lobe count (D3, D4, D5, D1 below).

---

## Part I — Internal-Consistency Defects (editorial, but with trust-erosion blast radius)

A paper whose central rhetorical weapon is *exact arithmetic* ("total, complete, not approximate") cannot afford visible arithmetic errors. The Green Paper has them.

### D1. [CRITICAL] "Seven divisions" against an eight-row table
The Abstract and §4 both claim "seven divisions." The §4 anatomy table lists **eight**: Medulla, Midbrain, Pons, Locus coeruleus, Cerebellum, Thalamus, Basal ganglia, Cerebrum. Either the count is wrong or a merge is intended (e.g., midbrain/pons as one reflex-bridge division) that the table does not show. In a document that stakes its credibility on "the count is closed in both directions," an off-by-one in its own gross anatomy is the cheapest ammunition a hostile reviewer will ever find. **Fix:** pick the number and make table and prose agree; if a merge is intended, name it in the table.

### D2. [CRITICAL] Pathology numbering collides with a live section
The pathologies are table-numbered 10.1–10.10 but reside in **§9**. Every cross-reference — "§10.9" (tumor clause, cited twice in §5), "§10.4" (seizure, §2), "§10.5" (correlated monologue, §5.4), "§10.2" (reciprocal politeness, §8), "§10.10" (metaphor worship, §2) — points at **§10 Plasticity: The Myelination Ladder**, which contains none of them. §2's "metaphor worship (§10.10)" send a debugger at three in the morning to the wrong organ. **Fix:** renumber as 9.1–9.10 (+9.11 for split-brain drift, see D8).

### D3. [CRITICAL] Router and pipeline invariant are unreconciled
§8's macro router "emits one route: one role, one lens emphasis, one slot profile" per task bid, and "losers are silenced." The pipeline invariant of §5.3 requires claims to flow posterior-to-anterior across *four lobes* for a single task. These two mechanisms are never reconciled: does a winning route mean one lens acts while the mate merely hears (consistent with §6's pair-mate audience rule), or that one role executes the whole descent? If the latter, "one winner per bid" starves the pipeline; if the former, the **pair activation policy — who authors, who listens, and when both lenses of a non-frontal lobe act — is nowhere stated**. The frontal pair has an obvious division of labor (propose/veto); the parietal, temporal, and occipital pairs do not, and Law 3's *measurement* (pair disagreement rates, Q2) cannot even be defined without it. **Fix:** one paragraph specifying per-lobe authorship policy and the router's scope (action arbitration vs. event dispatch), before blueprint compression.

### D4. [CRITICAL] The Chronicle is both substrate and tenant — a Law 5 shadow-violation
§6: the blackboard's "substrate is the Chronicle." §5.3: the Chronicle is simultaneously one of the eight tenanted roles, with subscriptions, a laterality mandate, and Law 4 accountability. This duality is unresolved and it is constitutional, not cosmetic: *who appends* decides what the Chronicle is. If any slot may append, the Chronicle is infrastructure masquerading as cognition — a funded role with no workload (violating Law 4), and the append-only guarantee belongs to the substrate, not the tenant. If only the Chronicle role appends, then **all inter-slot communication is mediated by a single deliberative-positioned organ** — a de facto gate over everything, in tension with Law 5 and with "the protocol has no moderator anywhere inside it." **Fix:** split the concepts explicitly — name the substrate (e.g., "the Ledger," append-only, dumb transport, medullary hard-fail on tampering) and grant the Chronicle role read/annotate duties over it — or show why the duality is lawful.

### D5. [WARNING] Split-brain drift is buried as a corollary of its own prediction
Split-brain drift (§9 closing) is the *expected* failure mode of v1.2's headline addition — §5.2's lateralization mandate — and it is demoted to an unnumbered coda while the paper's own taxonomy requires named pathologies with theorems. The form (Part D) obligingly counts it among the eleven, but the paper text does not. **Fix:** promote to 9.11 with its theorem stated in the table row.

### D6. [WARNING] Embryology violates its own hindbrain-first ordering
§4 and §11 both claim boot order follows neural-tube closure, "hindbrain before forebrain." Epoch 3 funds pineal + hypothalamus (diencephalic — forebrain derivatives) **before** Epoch 4 funds the cerebellum (metencephalic — hindbrain). The justification for this inversion (sleep and hunger before motor calibration) is fine operationally, but the paper pretends the biology licenses the order when it does not. §2's own standard — metaphor as specification, not ornament — is violated here by the paper itself. **Fix:** either swap epochs 3 and 4 or state the deviation and own it.

### D7. [SUGGESTION] "Ten expected diseases" plus an unnumbered eleventh
Cosmetic companion to D5: §9 announces ten, names eleven.

---

## Part II — Structural Logic Audit (the deep findings)

### F1. [CRITICAL] One-directional falsifiability: the theory can only grow
§5.1 grants the lobe count a falsifier that operates "in only one direction": a fifth stage forces a new role *pair*, and §5.5 adds that a ninth role alone is the tumor clause in organizational form. Examine what this does to falsifiability: **any conceivable countering evidence either expands the theory symmetrically (new stage → +2 roles) or is classified as pathology (extra role → tumor).** The lobe count cannot fail downward because the tumor clause converts would-be refutations into diagnoses. This is the classic absorption escape hatch — it is pseudo-falsifiability, and by the paper's own evidence-delta standard it should be flagged as such. Additionally, the closure argument conflates *definitional* closure (the role namespace is 8 by construction) with *empirical* adequacy (workload evidence justifies the namespace) — Law 4's map/slots separation is correct and should be the whole story; §5.5 instead sells arithmetic closure as if it were evidence-derived, which it is not and does not need to be. **Fix:** specify in advance the downward falsifier — e.g., "if a funded lobe's pair agreement exceeds threshold X on the golden set across N sessions, the stage merges and its pair retires" — and state plainly that eight is a prior lattice awaiting workload confirmation, not an arithmetic proof of adequacy.

### F2. [WARNING] Law 3 is enforced pair-locally; cross-lobe error correlation is unlegislated
Every Law 3 mechanism in the paper — laterality mandates, the §5.4 decorrelation ladder, disagreement measurement, split-brain drift detection — operates **within** a lobe's pair. Nothing guards against correlation *across* lobes: Spotlight and Reader both consume the same upstream artifacts; if a context slice is corrupt or an upstream claim wrong, both members of every downstream pair inherit the error and their "independent witnessing" testifies identically from poisoned premises — while looking maximally decorrelated by pair-level metrics. Worse, the pipeline invariant *guarantees* this propagation: posterior-to-anterior flow means an early-stage error reaches every subsequent witness by design, and out-of-order correction is defined as noise. See Pathology Proposal P1 below.

### F3. [WARNING] The callosal floor is unpriced — read amplification is a doubling minimum
§6: "Default audience for every claim: its hemispheric mate, always." Every published claim therefore costs author tokens *plus* at minimum one mate's read of it, a floor amplification factor of 2 across the organism, before any cross-lobe subscribers. Law 1 makes cost the constitution, yet no section or consultation question prices this. Q11 (interoception formulas) cannot be answered without a ledger schema that includes subscriber read costs — see the form audit, below. **Fix:** make callosal read-amplification a named line item in the cost ledger and in Q11's premises.

### F4. [WARNING] Rule 1 and rule 4 of the blackboard are in tension
"Claims, not chatter" bars reasoning-in-progress from the board; the evidence-delta rule demands each objection round carry *new evidence — a citation, a measurement, a named line.* If evidence must be attached to every rebuttal, the board's bandwidth approaches chatter (every objection round ships citations, diffs, excerpts); if evidence is merely *cited*, the objector cannot verify what it did not receive, and the evidence-delta check reduces to trusting the author's summary — the exact capitulation surface the rule exists to seal. The rigid-predicate answer to Q1 (transport-evaluated predicates) can only check citation *fields* syntactically; it cannot check whether the named line is load-bearing. State the resolution the paper actually intends: attachment scope (what travels with an objection), because it determines both Q1's implementation and the ledger cost model.

### F5. [WARNING] Operator as throughput bottleneck — the escalation storm
The organism escalates to its single judge organ (the operator) on: every ~two-round unresolved objection, every jerk round that fails to converge, every paid dispatch (requires recorded authority), every hard-bound draw. On a dense build day with several funded pairs, the operator queue *is* the critical path, and nothing in §7 or §8 throttles it. The endocrine tier throttles token velocity; nothing throttles operator attention velocity. Absent batching/coalescing semantics, "mandatory post-jerk escalation" converts to a denial-of-service on the human. **Fix:** an operator-queue budget/coalescing rule belongs in the endocrine tier's remit (a throttle that is allowed to be slow), and the pineal's sleep window may need to be the only guaranteed escalation-drain interval.

### F6. [SUGGESTION] The basal-ganglia/locus-coeruleus "same WTA, disjoint schemas" homology is inverted biology
In the organ being honored, the dopaminergic and noradrenergic systems are famous for *crosstalk*, not disjointness. The computational design — disjoint input schemas as the structural guarantee that routing can never adjudicate — is good engineering, but the paper presents it as an inherited biological warrant when it is a deliberate deviation from the biology. By §2's own standard, deviations should be marked as deviations; unmarked inversions are exactly how metaphor worship (§10.10/9.10) begins.

### F7. [SUGGESTION] Behavioral falsifiers are Goodhart-exposed; anchor to the lesion ledger
Disagreement-rate (Q2), "maximal specificity, zero politeness" (the jerk reflex), evidence-delta thickness — every one of these observable metrics is *performable* by models trained to satisfy evaluators. A pair can manufacture disagreement for show; an agent can perform commitment theater; a debater can ship thin-but-novel citations indefinitely. The paper's one non-gameable asset is the fixed inherited lesion set (§12), which cannot flatter its grader. Where possible, falsifiers should anchor to golden-set recurrence/cost outcomes rather than to in-flight behavioral observables, with behavioral metrics demoted to screening signals. The form's Q2 already anticipates manufactured disagreement — generalize that suspicion to the reflex and the delta rule themselves.

---

## Part III — Neuroscience Warrant Audit, Lobe by Lobe

The paper's §2 promise is that names import "millions of years of tested defaults." Audit each hemispheric warrant for whether it imports defaults or decorates guesses.

| Lobe | Claimed warrant | Actual state of the literature | Verdict |
|---|---|---|---|
| Frontal | Approach-left / withdrawal-right; "among the most robust findings of affective neuroscience" | Directionally robust as *population-level correlational* asymmetry (frontal EEG/affect literature). The paper legislates it as *categorical* — "constitutionally incapable of its mate's mode." Overreads the warrant it imports. | **Strongest overall, overstated in degree.** Keep the mandate, drop the absolutism or mark it as legislated design rather than inherited default. |
| Parietal | Focal-left / global-right attention dissociation | Solid: patient and imaging work on global/local processing ties left-sided damage to local deficits and right-sided (especially right posterior) damage to global deficits. | **Strong — but see collision under Occipital.** |
| Temporal | Episodic-right / semantic-left; "as in the organ it is named for" | Misattributed. The episodic/semantic dissociation is best established as a *systems-level* phenomenon (hippocampal vs. neocortical networks) with the classic amnesia evidence showing semantic learning surviving episodic impairment. The famous hemispheric asymmetry in episodic memory (HERA) is *frontal*, not temporal-lobe. Evidence for right temporal dominance in episodic memory exists but is partial and mixed. | **The hidden weakest warrant, weaker than the occipital pair the paper volunteers.** The paper flags Q3 on occipital but walks past temporal. Revise the derivation: derive the pair from the episodic/semantic systems distinction without the left/right claim, or cite the actual lateralization literature and soften "as in the organ it is named for." |
| Occipital | Reader-left (content) / Surveyor-right (gestalt) | Confuses two orthogonal dissociations. Content-vs-geometry maps cleanly onto **ventral/dorsal streams**, which are *not* hemispheric — both occupy occipital cortex bilaterally. The literature that *would* support a hemispheric left/right split here (global/local deficits after unilateral posterior damage) is substantially the **same literature already spent on the parietal pair**. | **Fails as derived, and double-spends a warrant.** See revision below. |

Two structural conclusions follow:

**First: the double-count.** The parietal and occipital pairs both lean on the local/global literature — "sees the part vs. whole" (Spotlight/Cartographer) and "content vs. gestalt" (Reader/Surveyor) are adjacent readings of one dissociation, licensed twice. As defined, Spotlight and Reader risk functional redundancy, and Cartographer and Surveyor likewise: two pairs chosen to fail together is a Law 3 deficit *between* pairs, currently unmeasured.

**Second: the uniform rule does not hold — and the paper half-knows it.** §5.2 legislates the same lateralization geometry over all four lobes, then Q3 concedes occipital is the most exposed application. The honest conversion is not to consult on Q3 but to settle it in text: either (a) **declare occipital the known exemption** — stream-structured (ventral Reader, dorsal Surveyor) rather than hemisphere-structured — costing the uniformity of §5.2 but preserving the per-stage two-witness requirement intact (the load-bearing part is the *witness count*, not the *left/right decor*); or (b) rescue occipital hemispherically via the global/local patient literature and *simultaneously* re-derive parietal away from local/global toward what parietal actually dominates — egocentric spatial updating and state integration — so each lobe spends a distinct warrant. Option (a) is cheaper, truer to the biology, and strengthens the paper: a theory that names its own exemption is falsifying itself in public, which is the entire brand.

**The hemispheric derivation, net verdict:** rhetorically strengthening, epistemically redecorative at two of four lobes. The eight-role arithmetic holds either way (two witnesses per stage carries the count); the left/right paint peels at temporal and occipital without structural damage. Say so in §5.3 and the derivation gains more from disclosure than the uniform rule ever bought.

---

## Part IV — Pathology Proposals (Part D2-shaped: theorem supplied)

### P1. **Pipeline inheritance** — the missing twelfth disease
**Theorem:** the posterior-to-anterior invariant guarantees that any error admitted at stage *n* is inherited by every witness at stages *n+k*, because out-of-order consultation is defined as noise and per-stage pair independence decorrelates only against *within-stage* single-witness failure. Paired lenses witness against each other; nothing witnesses against their shared input. Corollary: pair-level disagreement metrics are maximally healthy exactly when this pathology is worst — an early contaminated claim produces vigorous, decorrelated, unanimous downstream error.
**Guard:** a ground-truth channel that bypasses the pipeline — the Cartographer (or a medullary circuit) periodically re-derives state from source artifacts rather than from situated upstream claims, and flags divergence between re-derived and inherited state. Re-perception as a scheduled integrity poll, priced per F3. Without this guard, the golden set will pass through the organism while the organism confidently mis-executes exactly like the prior rig did, with better posture.

### P2. **Ledger obesity** — every guard breeds a surcharge
**Theorem:** each proposed guard (callosal traffic as a vital sign, disagreement telemetry, evidence-delta records, read-amplification, re-perception polls) is itself a consumer with a standing cost; guards are additive, unfalsified guards accumulate (they cannot fire, or they would already be known), and the organism slowly pays for its immune system more than its cognition — Law 4 has no clause forcing guards to earn existence, only organs. **Guard:** guards are tenants too — each telemetry channel carries a standing rent against the very ledger it protects, and myelination must apply to guards (a guard whose alarm never distinguishes cases across the golden set is deleted).

---

## Part V — Audit of the Five Laws (form Part B4-shaped)

| Law | Verdict | Remark |
|---|---|---|
| 1 — Metabolism | **AMEND** | The ledger is incomplete: callosal read-amplification (floor ×2 per claim), guard rents (P2), and per-slot idle context-residency costs must be named lines before Q11 is answerable. |
| 2 — Sparse Activation | **UPHOLD** | Coherent as written; the router/pipeline reconciliation (D3) is the one hole in its enforcement story. |
| 3 — Decorrelated Errors | **AMEND** | Enforced only pair-locally; cross-lobe correlation and pipeline inheritance (P1) are unlegislated, and the parietal/occipital warrant double-spend manufactures correlated pairs at birth. |
| 4 — Earned Existence | **UPHOLD, with caution** | Sound map/slots separation, but: (i) the lobe count needs its downward falsifier restored (F1), and (ii) behavioral falsifiers are Goodhart-exposed (F7) — anchor to the lesion ledger. |
| 5 — Substrate Silence | **AMEND** | The Chronicle substrate/tenant duality (D4) is an unresolved shadow violation, and the Law 5 boundary "evaluate predicates" vs. "interpret outcomes" needs its bright line published: a predicate is lawful when its output is a computable function of claim fields with no free-text inference anywhere in the path. State that line in §3, not implicitly in Q1/Q9. |

---

## Part VI — Consultation Question Audit (well-posed vs. malformed)

Well-posed and blocking: **Q1** (predicate/prose — but add the attachment-scope premise of F4), **Q2** (already anticipates Goodhart; generalize per F7), **Q11** (currently unanswerable — see form audit), **Q12** (needs golden-set version pinning).

Noted defects: **Q3** should be settled in text, not consulted on — the paper has the evidence to revise occipital itself; consulting on what you already suspect is deference theater, and the form is right to hate it. **Q5** smuggles "cheapest-first" as presumptive; ensemble literature supports backbone-divergence as strongest decorrelator and persona/instruction divergence as weakest, so the ladder *ordering* is plausible as a prior — but the form rightly demands local measurements, and none exist for this stack; plan them, don't cite intuition. **Q6** is half-answered by §5.5 already — the residual question is purely the downward falsifier (F1), so reduce it to that. **Q10** has an unexplored third resolution: **quarantine gating** — distill offline ungated, publish `convention_claims` as *provisional*, and subject them to the objection loop upon promulgate at next wake; the pineal's offline guarantee survives intact and bad-night doctrine faces the light before use.

---

## Part VII — Consultation Response Form Audit

The form is well-designed (graded falsifiability, stance declaration, the E1 "most likely to be wrong" field is excellent). Three defects:

1. **Q11 demands formulas over a ledger the paper has not published.** Respondents are asked for "windows, residuals, thresholds" over a cost-ledger schema that is never specified — fields, units, sampling cadence unknown. Nobody can propose appetite/satiety math against an unlisted schema. Attach a cost-ledger schema appendix to the form (including read-amplification and guard-rent lines per F3/P2) or the response space is fictional rigor.
2. **Undefined lifecycle vocabulary.** Q2's "promotion, divorce, or unfunding" introduce lifecycle verbs the paper never defines. Define the tenant lifecycle verb set once (fund, promote, demote, retire, expel?) or rephrase in the paper's own terms.
3. **No golden-set version pin.** Multiple falsifiers reference the lesion ledger / golden set; without pinning which iteration is graded against, epoch-to-epoch comparisons (the paper's own success criterion, §11) are incommensurable.

Minor: the form and paper disagree in no substance; the file title of the form itself misspells "Architecture" — fitting evidence that typos are load-bearing in this ecosystem, see D1.

---

## Part VIII — Closing Statement

The paper's spine is sound: witness-count-per-stage and the consolidation direction are its two genuinely strong derivations, and Law 4's application of the theory to itself is the best clause in the document. Its weakness is that in exactly two places it behaves like the thing it legislates against: the one-directional lobe-count falsifier is an absorption hatch (F1), and the uniform lateralization rule decorates two lobes with borrowed or misattributed warrants rather than importing tested defaults (Part III). Both are curable by disclosure, and both are curable *now*, before any respondent can weaponize them.

Everything the theory trusts arrives hostile. This audit complies.

**Confidence:** medium-high that these findings survive contact with the paper; the finding most likely to be wrong is the occipital "exemption" remedy — the parietal re-derivation alternative (option b) may ultimately produce a better organism.

**One sentence to quote back if the blueprint ships:** *the count earned its witnesses; the left-right paint was always optional.*
