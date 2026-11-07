# Peer Review — TAIDE Neuro-Architecture Foundational Theory (v1.4)

**Reviewed from dual lenses:** computational neuroscience + ML architecture.
**Scope:** conceptual review of the v1.4 foundational theory. This is a simulated dual-lens review; it is informed and evidence-grounded but is not a substitute for credentialed human peer review.
**Overall verdict:** APPROVE WITH REVISIONS. The theory is unusually self-aware (the open-problems list alone puts it above most cognitive architectures), but it carries two genuine internal contradictions (M1, N1/N2 below) that must be resolved before blueprint compression, because both sit on load-bearing joints.

---

## A. Neuroscience Lens

### A.1 What maps well (keep and defend these)

**Chronicle → Canon = complementary learning systems theory.** Your episodic-log to distilled-semantics one-way consolidation (§3.1, §7.6) is essentially the hippocampus↔neocortex systems-consolidation dialogue described by McClelland et al. — fast episodic store trains a slow semantic one, with interference protection running in exactly one direction. This is the strongest biological mapping in the document. Cite it; it will carry weight.

**Sparse activation (Law 2).** Roughly 1–2% of neurons fire concurrently at any instant, and most of the brain's energy budget goes to signaling rather than idle state. Sparse activation as a *design requirement rather than optimization* is defensible from biology.

**Basal ganglia as action selection (§6).** The Redgrave/Gurney selection thesis — competitive convergence via direct/indirect inhibitory pathways, winner-take-all, losers suppressed — is mainstream and well-mapped to your macro router. Structurally blinding the router to dispute fields is a genuinely elegant enforcement of the judge-organ ban.

**Cerebellum as forward models (§2).** Wolpert-style internal models predicting consequences of commands, correcting rather than deliberating — matches your sidecar/governor framing faithfully.

**LC as interruption (§7.2, core idea only).** The *idea* of a phasic arousal burst breaking perseveration is well grounded (the Bouret & Sara network-reset account; Aston-Jones & Cohen adaptive-gain theory). The *targeting mechanism* is the problem — see A.2.

### A.2 Findings

#### N1 [HIGH] Pineal is not the pacemaker — the SCN is
**§5, §8 epoch 3.** The master circadian clock in mammals is the suprachiasmatic nucleus — which is *hypothalamic*, not pineal. The pineal is the melatonin effector downstream of SCN control, and its role in human cognition/circadian regulation is far smaller than pop-neuroscience implies. Your "pineal = consolidation scheduler" is a fine *engineering* organ but a false *anatomical* warrant. Fix: either relabel the consolidation scheduler as hypothalamic (bundling it with the budget homeostat is actually fine — sleep and hunger are adjacent in the real hypothalamus), or keep the pineal name and openly file it under "engineering metaphor, not anatomy" the way you did with the occipital pair.

#### N2 [HIGH] LC targeting is overstated; the biology grants reset, not sniper fire
**§2, §7.2.** Locus coeruleus projections are predominantly *diffuse* — phasic NE acts as a global gain/reset signal biasing the entire network toward exploitation or disengagement, with regional biases but not party-selective message delivery. Your claim that "targeting of bursts is LC-local, not striatal" borrows the plausibility of LC *interruption* to justify an LC *selector*. You don't need the warrant: an embedded quarantined WTA circuit choosing a jerk recipient is good engineering on your own terms (disjoint input schemas, Law 5 compliance). Drop the anatomical justification and keep the engineering one — as written, this is the document's most citation-vulnerable sentence.

#### N3 [MEDIUM-HIGH] "Column" is a naming collision that will bite
**§3.2.** Real cortical columns (Mountcastle minicolumns) are *permanent* anatomical units that persist for the lifetime of the organism. Your columns are transient, born-at-decomposition workers. What you actually built is closer to Hebbian cell assemblies / transient coalitions. This matters operationally: your own §7.9 tumor clause depends on maintainers *not* mentally granting columns persistence — and the name you chose imports exactly that connotation. Rename the granularity (e.g., "assembly," "cohort") or accept drift risk in every future reader.

#### N4 [MEDIUM] The lobe mapping is decorative — promote it from claim to admission
**§3.1, open problem #3.** You already flag the occipital pair as weakest-fit, but the honest move is stronger: cortical lobes are gross anatomical conventions, not functional modules. Frontal does far more than action; temporal does far more than memory. The eight roles are *good role design* standing on *bad anatomical scaffolding*. Open problem #6 already concedes roles are "anatomically generated, not workload-derived" — make that the headline of §3.1, not the caveat. The theory gains credibility by shedding borrowed authority it doesn't need.

#### N5 [LOW-MEDIUM] The 20W framing overcredits architecture
**§0.** The brain's efficiency also derives from analog/chemical computation, synaptic miniaturization, and ~10¹⁴ synapse-level parallelism that silicon routing cannot replicate. "Steal all four tricks" is rhetorically great but the tricks you list (sparse activation, layered autonomy, error-correcting pairs, gating) are the *transferable subset* — say so, and the premise gets more robust, not less.

#### N6 [SUGGESTION] Thalamus is undersold
**§2.** Beyond sensory gating, a large fraction of cortico-cortical traffic is transthalamic — the thalamus is a relay and processing node, not merely a gate. For your purposes this is free good news: it legitimizes the subscription mechanism doing light transformation on signals (e.g., denormalizing, ranking) without becoming a judge organ.

---

## B. ML Architect Lens

### B.1 What holds up (keep)

The Role/Slot/Tenant ontology (§0) is the document's best engineering asset — it converts staffing decisions into a typed grid, and §7.9's sharp tumor definition falls out of it mechanically. The evidence-delta rule (§4.4) is a genuinely good anti-sycophancy mechanism. The refusal to instantiate the jerk reflex before its falsifier data exists (§8, epoch 5) is the single most disciplined paragraph in the document. The lesion-as-curriculum stance (§9) mirrors how real postmortems should drive architecture.

### B.2 Findings

#### M1 [HIGH] The jerk trigger quietly violates Law 5
**§7.2 vs. §1 Law 5.** Law 5: "Infrastructure never deliberates… none of them interpret, argue, or decide anything contested." The jerk trigger requires infrastructure to measure **concession slope ≈ 0**, **evidence-delta violations**, and **position volatility** — all semantic judgments about the *content* of arguments. Detecting a restated opinion is interpretation. As written, either (a) the LC measurements become deterministic proxies (string overlap, citation-field checks — weaker fidelity, but Law 5 survives), or (b) some substrate component is an unlicensed interpreter. The theory must pick a fork *before* the blueprint, because the entire §6/§7.2 disjointness architecture depends on it. Recommended: restrict LC inputs to mechanically computable features (round count, citation-presence fields, embedding-distance between successive positions — a number is a computation, not an interpretation, if you rule it so explicitly).

#### M2 [HIGH] The decorrelation ladder orders cheap-first into your own pathology
**Open problem #5, §7.5.** The cost-ordered ladder (personae → slices → backbones) puts the *least effective* decorrelation mechanism first. Empirically, same-backbone, different-persona LLM pairs correlate heavily — persona diversity produces stylistic variance, not error variance. That means the recommended default ordering walks straight into §7.5 correlated monologue: one reasoner billed twice, with extra prompt tokens. Either invert the default (slices first, since divergent context produces genuinely divergent evidence), or state an explicit falsifier rung: any pair whose disagreement rate on the golden set falls below a floor is automatically promoted to the next decorrelation tier regardless of cost preference. Your cost-first instinct is right for *metabolism* but this is the one place it conflicts with Law 3.

#### M3 [MEDIUM-HIGH] Router credit assignment has an obvious cheap answer you left on the table
**Open problem #9.** You correctly call this the highest-leverage open problem, but the resolution space is smaller than implied: a contextual bandit (or even epsilon-greedy with counts) over route choices, rewarded by the epoch cost-quality delta, needs no paid dispatch, tiny state, and — critically — *deletes the roster-drift lesion (§9) structurally* because routing weights become learned state rather than duplicated config. The biological warrant is dopamine-like reward-prediction error on route outcomes. This should move from open problem to design commitment pending the falsifier.

#### M4 [MEDIUM] "Restated opinion terminates the loop" needs a terminator
**§4.4.** Who evaluates whether round *n* carried new evidence? If a disputing slot evaluates it, you've handed a party to the dispute a micro-judge role — precisely the organ you retired. This resolves *together with* M1 and open problem #1: deterministic predicates over claim fields (citation present? measurement attached? line cited?) give you a lawful evidence-delta check evaluated by dumb transport. Push your existing "start rigid, relax on evidence" tilt into a commitment.

#### M5 [MEDIUM] Jerk + mandatory escalation serializes the organism on operator availability
**§7.2, §4.5, §6.** Combination: bounded loops (~2 rounds) + jerk on stall + *mandatory* operator escalation after failed jerk + WTA routing means the whole pipeline can block on a human inbox. Unresolved disputes are expensive but *cheap to create*: any pair with a true disagreement or a noisy evidence-delta channel manufactures escalations. Add an **escalation-rate metric** (escalations per completed task per epoch) to the epoch cost-quality point, with a budget alarm — otherwise the theory has no pressure sensor for its own appeal path.

#### M6 [MEDIUM] You reinvented Mixture-of-Experts; mine that literature
**§1 Law 2, §6.** Sparse activation + gated expert routing + winner-take-all selection *is* the MoE pattern. The MoE literature has already catalogued your pathologies with mitigations: router collapse (your tumor growth / roster drift) → load-balancing objectives; expert under-use → auxiliary losses; routing thrash → hysteresis. Importing those as named guards (even unimplemented, as falsifier targets) is cheaper than rediscovering them in production.

#### M7 [MEDIUM] Provenance walls are missing around the shared Chronicle substrate
**§6 vs. §4.** Your §6 disjointness guarantee is enforced at the *input schema* level, but both selectors' features (task features, dispute-local features) are computed from the same underlying transcript. Schema separation without provenance separation permits leakage — e.g., concession-slope computations that incidentally surface task routing info. Specify feature provenance: each selector may only read fields written *within its own jurisdiction*, and the transport layer stamps claim origin at append time.

#### M8 [LOW-MEDIUM] "Quality per joule" under-specifies the denominator
**Law 1.** Per-token metrics reward token thrift, not task completion; a cheap organism that half-completes tasks wins the metric while losing the mission. Your §8 epoch criterion ("cost-quality point") is actually the better Law 1 definition — normalize cost per *completed, verified task*, not per token. Token economics becomes a telemetry variable, not the fitness function.

---

## C. Exploring It Further — Proposed Extensions (with experiment designs)

**E1 — Close open problem #11 with precision-weighted surprise.** Interoception metrics can be literal formulas tomorrow: for each hypothalamic signal, define *surprise* = |observed burn-rate − predicted burn-rate from trailing window|, and *appetite/throttle signals* as thresholded precision on that residual. This imports predictive-processing machinery (free-energy framing) into the one place the theory admits it is still metaphor, and every constant is measurable from your own cost ledger. Falsifier: does residual-thresholded throttling beat flat-rate throttling on the golden set?

**E2 — Give the plasticity ladder a dopamine channel.** Promotion/demotion (§3.4) currently runs on "observed repetition." Promote it from counting to credit: each circuit invocation logs cost + a coarse outcome flag; promotion fires when expected value of standing compilation beats expected transient cost with a confidence bound (Wilson/Hoeffding bounds keep it deterministic-friendly). Demotion is the same inequality inverted over a decay window. This kills two birds: the ladder gets a principled trigger, and the "two-paperclip"-style meta-tooling ambiguity about *when* to consolidate disappears.

**E3 — Seed the occupancy matrix (open problem #7).** Proposed legality rule: a cell is legal iff **(authority is grant-compatible)** ∧ **(funding is repetition-justified)**. Consequences: persistent circuit = *cache* (legal, valuable); transient area = *surgeon* (legal but suspicious — should fire Law 4 review); column-with-subscriptions = impossible (violates inheritance); circuit-with-spawn = impossible. Two rungs worth pre-naming: **surgeon areas** (rare-event transient cognition, e.g., incident response) are legitimate but must auto-expire with their event class, or they become the next tumor taxonomy.

**E4 — Resolve identity (open problem #8) as engineering, not philosophy.** Define tenant identity as `(role, model-class, funding-generation)` + the Chronicle entries authored under it. Attribution, decorrelation history, and falsifier ledgers all bind to that tuple. The question of whether a re-funded slot is "the same agent" dissolves into bookkeeping — which is exactly what an ontology should do.

**E5 — Consolidation trigger (open problem #4): go hybrid.** Biology's replay/consolidation (sharp-wave ripples, systems consolidation during sleep) is triggered by *both* accumulated plasticity markers and offline/idle state. Design: run Chronicle→Canon distillation when (cumulative `record_append` volume > N) ∧ (dispatch activity below idle threshold). Falsify hybrid against batch-only and volume-only on downstream Canon-retrieval quality per distillation joule.

**E6 — Pair falsifiability (open problem #2) as a two-sided band.** Measure pair disagreement rate on golden-set tasks. Floor violation (≈0 disagreements) = capitulation theater with tenure → forced decorrelation promotion (ties into M2). Ceiling violation (persistent disagreement on resolved-known-answer items) = correlated noise manufacturing, i.e., a pair that disagrees for show. The pair mechanism survives only inside the band.

**E7 — Symmetric control for the jerk protocol (open problem #12).** Before shipping the hardening variant, grade a **mirror control** — "force concession-or-maximal-specificity" — at equal budget. If hardening-out and concession-forcing resolve disputes at the same rate, the LC machinery halves at no quality cost (mediocre reasons to keep an organ: Law 4). Scoring function: start logistic over the three named features + seeded roll; the epoch-5 bias test you specified (same party repeatedly targeted) is a good falsifier — keep it.

**E8 — Test the seizure theorem empirically.** §7.4 asserts full synchronous activation is pathological. This is your single most testable structural claim: construct one golden-set task run in (a) sparse-subscription mode and (b) all-slots-hear mode and compare cost-quality plus error-correlation. If full-audience mode wins anywhere, the theory's spine is weaker than claimed — better to know at epoch 2 than epoch 6.

---

## D. Reviewer Statement

The theory's deepest strength is that it *wants to be attacked*: Law 4 applied to itself, falsifiers named next to mechanisms, open problems admitted rather than hidden. Its deepest risk is metaphor worship (§7.10) operating *inside* the document, not just outside it — N1, N2, and N4 are all cases where the biological warrant is doing rhetorical work the engineering doesn't need. Every finding above can be repaired without touching the five laws or the two-axes ontology, which is the sign of a foundation that survived its review. Compress to blueprint only after M1, M2, and N1/N2 are ruled.
