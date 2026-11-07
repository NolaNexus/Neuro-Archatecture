# Green Paper: The Neuro-Architectural Substrate for a Terminal AI Development Environment

**Status:** GREEN PAPER — FOR CONSULTATION
**Version:** 2.2 (OpenCode substrate mapping appended; revision-memo provenance retired to the revision log; supersedes v2.1 and all earlier editions)
**Classification of contents:** Proposals. Nothing herein is binding, implemented, or settled.
**Disposition of prior reviews:** Every finding of the Green Paper Peer Audit (v1.2) and the Dual-Lens Peer Review (v1.4) is adopted or explicitly overruled in the Revision Log (Appendix C).
**Substrate grounding:** Dell Precision Tower 7910 — 2× Xeon E5-2630 v3 (16 cores / 32 threads, AVX2), 256 GiB DDR4, ZIP 59804 (NorthWestern Energy territory; residential electricity ~14–16¢/kWh in recent reporting; the bill is the constant).

---

## Abstract

This paper proposes the reconstruction of a Terminal AI Development Environment (TAIDE) as a *computational organism* whose architecture is derived — deliberately, and with its biological deviations publicly inventoried — from the human brain. The metaphor is method: generative engine of the design, organizing vocabulary of its documentation, and standard against which components are named, judged, promoted, and deleted. The proposal rests on five laws — Metabolism, Sparse Activation, Decorrelated Errors, Earned Existence, and Substrate Silence — elaborated into a complete anatomy of **eight divisions**, a cerebrum of four pipeline stages with two witnesses per stage (**eight roles**), a single append-only signal medium split into a dumb substrate (the **Ledger**) and a tenanted witness (the **Chronicle**), an endocrine tier for chronic metabolic control, a bandit-trained macro router for action selection, and a reflexively-triggered dispute interrupt whose inputs are mechanically computable numbers, never interpretations. The stage count carries falsifiers in **both** directions. Development proceeds embryologically from Epoch 0 — a census of the physical host and its **live model registry** — through hindbrain to forebrain, each epoch required to beat its predecessor's cost-quality point on the pinned golden set.

On this substrate the constitution acquires an unexpectedly literal reading. The host's abundant RAM and scarce CPU threads mean that **many models may reside but few may act**: residency is cheap and activity is dear, so Sparse Activation (Law 2) stops being a cognitive preference and becomes the physics of the machine. And the registry's heavyweights are mixture-of-experts architectures whose weights dominate memory while their sliding-window and grouped-query attention cap KV growth — so **RAM cannot be converted into context through them**, and the organism's memory strategy must spend its surplus on lanes and one context-heavy resident rather than on a second heavyweight.

The paper closes with consultation questions that remain genuinely open; questions earlier editions asked rhetorically have been settled in text, because consulting on what the paper already suspects is deference theater.

**Keywords:** agent orchestration; multi-model systems; neuro-inspired architecture; hemispheric specialization; cost-constrained inference; substrate-instrumented metabolism; mixture-of-experts residency; winner-take-all selection; complementary learning systems

---

## 1. Purpose of this Paper

A Green Paper proposes before it prescribes. This one proposes a substrate — an arrangement of live and dormant components, of models and reflexes and budgets — and submits the arrangement itself to the criticism it anticipates. The paper does not ask to be believed. It asks to be *answered*: every mechanism named herein carries the condition of its own falsification, and every organ must earn occupancy of its slot with evidence, never with the elegance of its metaphor. Elegance justifies nothing. Metabolism justifies everything.

The proposal responds to the death of the prior TAIDE rig. Its autopsy — nine classes of verified failure, itemized in Section 13 — is inherited here not as regret but as curriculum. An architecture that cannot account for its predecessor's lesions has no claim on its predecessor's ambitions.

The lineage's two prior reviews are fully dispositioned in the revision log (Appendix C); nothing here is defended against them. The defects they caught — a one-directional falsifier (an absorption hatch dressed as arithmetic), decorative lateralization warrants, a pineal organ falsely credited with a hypothalamic job, a locus-coerulean selector wearing borrowed anatomy, a "column" name importing exactly the persistence connotation the tumor clause forbids, and a jerk trigger whose inputs quietly violated Substrate Silence — are corrected in the text where they matter. A deviations ledger (Appendix B) marks every departure from biology as a departure, because unmarked inversions are where metaphor worship begins.

## 2. The Methodological Commitment: Metaphor as Specification

We state our epistemological position plainly, because readers accustomed to treating biological analogy as decoration will otherwise misread what follows.

**The neuroanatomical vocabulary of this paper is load-bearing.** Where this document names an organ after a brain structure, that name is a *specification constraint*, not a flourish. A component called thalamic is forbidden from judging what it gates. A component called medullary is forbidden from thinking at all. A component called cerebellar must calibrate work already decided, never initiate it. To rename an organ casually is to break a contract with every engineer who will ever debug the organism at three in the morning; the metaphor exists so that behavioral expectations arrive for free with every name.

**And the same clause applies to this paper itself.** Cortical lobes are gross anatomical conventions, not functional modules: the real frontal lobe does far more than action, and the real temporal lobe does far more than memory. The eight roles of Section 5 are *good role design standing on deliberate scaffolding* — the anatomy generates the roles, the evidence funds the slots, and nowhere does the anatomy vouch for the roles. This is the headline of the cerebral theory, not its caveat. The theory gains more credibility by shedding borrowed authority it does not need than it ever held by renting authority it could not repay.

Where the design *deviates* from the biology it honors, the deviation is inventoried in Appendix B with its engineering rationale. Deviation is not apostasy; unmarked deviation is. The commitment carries a risk we name in advance: metaphor worship, the pathology of architectures that fund every named organ because it has a name. Our guard is Law 4. Names are free; metabolism is not.

**The architecture is grounded twice.** First in the physics of its host, measured at Epoch 0 (§12, Appendix A). Second in the implementation substrate it will be built on — OpenCode, whose native primitives (primary and subagent agents, skills, permissions, tools) the design is mapped onto in Appendix E. Where the substrate cannot honor the biology, the gap is logged as a deviation in Appendix B, not papered over.

## 3. First Principles

Five laws constitute the constitution of the organism. Nothing in the sequel may contradict them; where a proposal and a law appear to conflict, the law wins and the proposal is defective.

**Law 1 — Metabolism.** Compute is energy; every token is a calorie. The organism's fitness is measured as quality delivered per unit energy per *completed, verified task* — not per token. Token economics is a telemetry variable, not the fitness function; a cheap organism that half-completes tasks wins the metric while losing the mission. Local inference is the baseline metabolism — electricity already priced into the host's fixed capacity. Paid dispatch to remote inference is an *emergency ration*, consumed only under the operator's explicit, recorded authority. An expenditure without such a record is an incident, not a purchase. On this substrate, the law is not a preference: with no accelerator, CPU-class token velocity, and residential-priced electricity, the organism *cannot* graze; scarcity is the physics.

**Law 2 — Sparse Activation.** At any instant, most of the organism is silent. Components activate in response to signal classes, never globally. Total synchronous activation is not a superpower; it is a seizure — and on a dual-socket air-cooled tower, it is also a thermal event. On this host the law is enforced by hardware arithmetic: **residency is RAM (abundant), activation is threads (scarce)**. The registry can hold many tenants; the scheduler can feed few. Sparse activation is here a scheduling necessity before it is a cognitive virtue.

**Law 3 — Decorrelated Errors.** The value of paired components lies in the independence of their mistakes. Two reasoners that fail identically are one reasoner billed twice. Enforcement operates at every scope, not only within a pair: pairing, context slicing, perspective diversity, and guards against correlated inheritance across pipeline stages (§5.5, Pathology 9.12). Ensembles, not committees, are the aspiration.

**Law 4 — Earned Existence.** The architecture defines roles; evidence funds slots. A role instantiates when its absence demonstrably harms, grows when its workload persists, and dies when its falsifier fires. This law applies to the paper itself and to every guard the paper proposes: guards are tenants too, pay rent against the ledger they protect, and are deleted when their alarms stop distinguishing cases. No dormant reflexes, no unfalsified instrumentation — and, on this substrate, no resident model that is never routed to: **a model that occupies RAM and never acts is dead weight wearing a role's name**; its residency rent is audited per epoch like every other tenant.

**Law 5 — Substrate Silence.** Infrastructure never deliberates. Transport routes, gates evaluate, daemons supervise. The bright line, published here as constitutional text rather than left implicit: **a predicate is lawful when, and only when, its output is a computable function of claim fields — no free-text inference anywhere in the path. A number produced by a deterministic function is a computation; a judgment produced over meaning is an interpretation, and interpretations belong to cerebrum or operator alone.** Any component empowered to arbitrate a contested question is a judge organ, and judge organs are prohibited everywhere except the operator and the unconditional reflexes.

## 4. Gross Anatomy

The organism comprises **eight divisions**, ordered from most to least ancient. The count is eight in the table, eight in the prose, eight in the Abstract.

| Division | Biological warrant | Computational instantiation | Deliberative capacity |
|---|---|---|---|
| **Medulla** | Autonomic life support | Serving daemon, process supervision, residency management, automatic context degradation; tamper hard-fails | None — autonomic |
| **Midbrain** | Reflex arcs | Unconditional guards: spend caps, syntax gates, permission walls, trap handlers | None — reflexive |
| **Pons** | Relay bridge | Transport bus carrying claims, objections, results, provenance stamps | None — a cable |
| **Locus coeruleus** | Phasic interruption (warrant held loosely; see App. B) | Jerk reflex: hardening orders issued mid-dispute by infrastructure, recipient chosen by an embedded winner-take-all sub-selector over a quarantined schema of *mechanically computable* features | None — reflexive |
| **Cerebellum** | Forward models; motor error correction | Sidecars: retrieval (embedding index), warm-context, residency governors calibrating decided work | None — corrective |
| **Thalamus** | Gating *and* transthalamic relay | Subscription gate: determines which slot hears which signal class, enforces Law 2, and performs light non-judging transformation on passed signals (denormalization, ranking, redaction) | None — selective |
| **Basal ganglia** | Action selection (Redgrave/Gurney selection thesis) | Macro router: a contextual-bandit-trained selector over routes; structurally blind to dispute state | None — selective |
| **Cerebrum** | Cognition (scaffolding, not warrant; see App. B) | All reasoning: four stages × two witnesses = eight roles (§5), instantiated into funded slots | **The only thinker** |

Three auxiliary structures complete the anatomy.

- **The endocrine tier (§7)** supplies slow, cascading, system-wide adjustment — the hormonal counterpart to the brainstem's hard reflexes. The circadian pacemaker lives in the hypothalamic axis, where the biology actually puts it: the hypothalamus bundles budget homeostasis with the sleep/wake scheduler, exactly as the real hypothalamus sits adjacent to the suprachiasmatic clock it serves.
- **The corpus callosum** is honored as what it biologically is: not an organ but a fiber tract — the interhemispheric bridge carrying disagreement between paired lenses, pure transport, never judging. Callosal traffic volume is a vital sign, and its read-amplification is a priced line in the cost ledger (§7): every published claim costs its author plus at minimum one mate's read, a floor amplification of ×2 before any cross-stage subscriber.
- **The Ledger/Chronicle pair (§6)** is the substrate–tenant split: the substrate is dumb append-only storage with medullary hard-fails on tampering; the Chronicle is the tenanted right lens of memory that witnesses and annotates it. Neither may do the other's job.

One designed homology is retained, *marked as a deviation*: the basal ganglia and the locus-coeruleus sub-selector implement the same winner-take-all algorithm over strictly disjoint input schemas — task features for the former, mechanically-computed dispute-local features for the latter. The disjointness is the structural guarantee that routing and adjudication can never contaminate each other. In the biological organ, the dopaminergic and noradrenergic systems are famous for crosstalk, not disjointness; ours is deliberate engineering wearing anatomical dress, and the dress is hereby labeled.

## 5. Cerebral Theory: Four Stages, Two Witnesses, Eight Roles

The cerebrum's structure remains an exact multiplication: **four pipeline stages × two obligatory witnesses = eight roles — total, complete, not approximate.** The count is a derived arithmetic to be enforced, and *falsifiable in both directions*.

Organization resolves onto two orthogonal axes. The **authority axis** is a property of the role (author claims, spawn assemblies, hold subscriptions); the **funding axis** is a property of the slot (persistent, transient, fixed). The granularities are diagonal pairings:

- **Areas** (persistent): the eight roles themselves, funded while workload and Law 4 sustain them.
- **Assemblies** (transient): task-scoped sub-workers born at decomposition and destroyed at delivery — never the permanent anatomical units of cortical columns, whose persistence connotation the tumor clause forbids. Assemblies never author claims; their digest returns to their parent, which owns and answers for the work. Sub-agents give areas hands; they do not give them alibis.
- **Circuits** (fixed): compiled, single-purpose bindings answering one signal class in milliseconds at negligible cost, so that no area burns contemplative context on a mechanical question.

### 5.1 Why Four Stages

Four because the pipeline invariant demands four abstraction levels: perception decodes, situation situates, comprehension interprets, decision commits. Fewer stages collapse transformations that must remain separable so their claims can be checked against a different transformation; more insert out-of-order consultations, which the invariant defines as noise. The stage count is a claim about the depth of abstraction.

### 5.2 Why Two Witnesses — and the Both-Direction Falsifier

Two because no stage may have only one witness: every stage houses exactly two lenses, each the adversarial complement of the other, so that no single mode of attention can be the only witness to its own task.

A count armed in only one direction is not falsifiable: a fifth stage would force a ninth-and-tenth-role pair, while an extra role within a stage could always be absorbed by the tumor clause — converting every would-be refutation into a diagnosis. That was the shape of the earlier editions' count: pseudo-falsifiability, an absorption escape hatch. The count is falsifiable downward, and the falsifier is stated in advance:

> **Downward falsifier (stage merger).** If a funded stage's pair exhibits agreement rate exceeding threshold X on the pinned golden set across N consecutive sessions — that is, if the two witnesses of a stage reliably say the same thing about the same inputs — the stage has failed the independence it exists to provide. The stage merges with its nearest neighbor, and its pair retires. Threshold X and window N are set in Epoch 0 and published in the ledger schema; they are not tunable in flight.

Eight is stated honestly for what it is: **a prior lattice awaiting workload confirmation, not an arithmetic proof of adequacy.** Definitional closure (the role namespace is 4×2 by construction) is separate from empirical adequacy (workload evidence justifying the namespace). Law 4's map/slots separation is the whole truth of the matter, and the paper no longer sells the multiplication table as if it were evidence.

### 5.3 The Eight Roles — Complete Enumeration

| Stage | Lens | Role | Function | Constitutional disposition |
|---|---|---|---|---|
| Frontal (decision) | Left | **Driver** | Decomposition, sequencing, proposing | Approaches the task; optimism is structural |
| Frontal (decision) | Right | **Sentinel** | Cost/risk/irreversibility evaluation of bids; unconditional veto | Withdraws from danger; pessimism is structural |
| Parietal (situation) | Left | **Spotlight** | Focal, task-relative salience | Sees the part; forgets the field |
| Parietal (situation) | Right | **Cartographer** | Global state, terrain, drift detection, re-derivation of state from source artifacts | Sees the whole; also the integrity poller (§5.5) |
| Temporal (comprehension) | Right | **Chronicle** | Episodic, situated, narrative record; witnesses and annotates the Ledger; never edited by anyone | Context-bound testimony |
| Temporal (comprehension) | Left | **Canon** | Distilled conventions; decontextualized rule | Context-free doctrine; learns from Chronicle, never touches it |
| Occipital (perception) | Ventral-stream | **Reader** | Decodes focal artifact content: the word, the line, the diff-intent | Blind to the shape that changes meaning |
| Occipital (perception) | Dorsal-stream | **Surveyor** | Reads artifact geometry: gestalt, spread, clustering | Sees the pattern; interprets no content |

**The per-lobe warrants, restated honestly:**

- **Frontal.** The approach-left / withdrawal-right affective asymmetry is directionally robust as population-level correlational findings (frontal EEG/affect literature), and the pair keeps its mandate: Driver approaches, Sentinel withdraws. But the claim that each lens is "constitutionally incapable of its mate's mode" overreads a correlational warrant as a categorical law. The disposition is owned as *legislated design* informed by biology — a mandate the organism enforces on itself, not a fact the organism inherits.
- **Parietal.** The local/global attention dissociation (focal-left, global-right) is solidly grounded in patient and imaging work, and the pair retains it — *augmented* by parietal's actual specialty: egocentric spatial updating and state integration. This re-derivation also ends the warrant double-spend between parietal and occipital, which previously leaned on the same local/global literature twice.
- **Temporal.** The right-temporal episodic dominance this pair once leaned on is not cleanly supported — the famous hemispheric asymmetry in episodic memory (HERA) is frontal, not temporal. The pair is derived from **complementary learning systems theory** (McClelland et al.): a fast, episodic, interference-prone store (Chronicle) training a slow, semantic, generalizing one (Canon), with protection running in exactly one direction — episodic feeds semantic, never the reverse. This is the strongest biological mapping in the entire document, and the left/right labels on this pair are organizational labels, not anatomical claims.
- **Occipital — the declared exemption.** The content-versus-geometry dissociation maps onto **ventral and dorsal cortical streams**, which are bilateral, not hemispheric. Rather than consult on a fix the paper already possesses (deference theater), occipital is hereby declared the known exemption to the uniform lateralization rule: Reader is the ventral-stream lens (content decoding), Surveyor the dorsal-stream lens (spatial form). The load-bearing requirement — *two witnesses per stage* — survives intact; only the left/right décor is discarded. A theory that names its own exemption is falsifying itself in public, which is the entire brand.

The pipeline invariant governs signal flow posterior-to-anterior, binding both lenses of every stage: bytes become state, state becomes meaning, meaning becomes action. Out-of-order consultation is noise by definition.

### 5.4 Authorship and Activation Policy — the Router Reconciliation

The macro router ("one route, one role, one lens emphasis; losers silenced") and the pipeline invariant ("claims flow through four stages for one task") must be reconciled, or the non-frontal pairs have no authorship policy. The reconciliation is constitutional:

1. **The router arbitrates action, not attendance.** Its winning route names the *leading lens* per stage for the task: Driver or Sentinel in decision, Spotlight or Cartographer in situation, Chronicle or Canon in comprehension, Reader or Surveyor in perception. "Losers are silenced" means losers forfeit *authorship* on this task, never audience.
2. **The mate is the mandatory first reader.** The leading lens publishes; its pair-mate receives by callosal right (§6, rule 2) with objection rights and no counter-authorship for that task. A stage's two witnesses therefore always both participate — one as author, one as adversarial reader — in every task the stage touches.
3. **Leading-lens selection is signal-class-driven, not performance-contested.** The Reader leads content tasks and the Surveyor geometry tasks; the Spotlight leads scoped edits and the Cartographer repo-wide operations; the Chronicle leads situated-witness tasks and the Canon convention-application tasks; the Driver leads proposals and the Sentinel hazard evaluations. Contests between pair-mates for lead position are forbidden — a pair that competes internally is a fusion pathology (9.11) in progress.
4. **Both lenses may act as authors in the same waking period, never on the same claim.** Concurrent authorship on different claims is lawful and desirable; concurrent authorship on one claim is a dispute by construction and enters the objection loop (§6, rule 3).

With this policy, Law 3's *measurement* (pair disagreement rates) becomes definable: it is measured on the mate's objection behavior against the leader's claims, per stage, per epoch — and it lives inside the two-sided band of §7.5.

### 5.5 Integrity Polls — the Cartographer's Second Duty

Posterior-to-anterior flow guarantees that an error admitted at stage *n* is inherited by every downstream witness, while per-stage pair independence decorrelates only against within-stage single-witness failure. Pair-level disagreement metrics read *maximally healthy* precisely when this pathology is worst: a contaminated early claim produces vigorous, decorrelated, unanimous downstream error. Nothing within the pipeline can witness against the pipeline's shared input.

The guard is a **ground-truth channel that bypasses the pipeline**: the Cartographer periodically re-derives state directly from source artifacts — not from situated upstream claims — and flags divergence between re-derived and inherited state. Re-perception is a scheduled integrity poll, priced as a ledger line (§7), and its alarm history is itself subject to Law 4: a poll whose alarms never distinguish true divergences from noise on the golden set is deleted. Without this channel, the golden set can pass through the organism while the organism confidently mis-executes exactly like its predecessor did, with better posture.

### 5.6 The Decorrelation Ladder — Ordered by Divergence

Ordered cheap-first (instruction divergence → context slices → backbone divergence), the ladder would put the *least effective* mechanism first: same-backbone, different-persona pairs correlate heavily — persona diversity buys stylistic variance, not error variance — which walks straight into correlated monologue. Ordered by genuine divergence, the ladder gains teeth:

> **Rung 1 — Divergent context slices.** Pair-mates receive materially different views of the same artifacts: different windows, different orderings, different retrieval sets. Divergent evidence is the cheapest genuinely divergent thing two lenses can carry.
> **Rung 2 — Divergent lateralized instruction.** Attention-mode mandates ride atop the slices, as the floor supplement — never mistaken for sufficient decorrelation on its own.
> **Rung 3 — Divergent backbones.** Different local models, purchased only when workload evidence shows Rungs 1–2 failing; on this substrate, backbone divergence costs memory residency and thread share, not license fees.
>
> **Automatic promotion clause:** any pair whose golden-set disagreement rate falls below the band floor (§7.5) is promoted to the next rung regardless of cost preference. Cost-first instincts are correct everywhere except where they collide with Law 3, and this is that place.

### 5.7 The Substrate Economy — Residency, Lanes, and Context

The host enforces a two-axis economy that the registry (Appendix D) makes concrete:

- **Residency is cheap; activation is dear.** 256 GiB can hold several heavyweight residents simultaneously (two ~65 GiB MoE checkpoints, a mid-weight, two small lanes, an embedding index, and their KV caches sum comfortably inside the budget), but 32 hardware threads feed roughly two concurrent heavyweight inference lanes at interactive latency. **The organism's true maximum simultaneous cognition is set by threads, not by RAM.** This is Law 2 as hardware fact, and the Epoch 0 census measures the exact lane/thread curve.
- **MoE residency starves KV.** The registry's heavyweights are mixtures-of-experts: weights dominate their footprint, while their attention designs (sliding-window layers, grouped-query heads, hybrid local/global interleaves) deliberately cap KV growth. Per published architecture documentation, a flagship 117B-total / ~5.1B-active MoE carries ~65 GiB of MXFP4 weights but only ~4.5 GiB of KV cache even at its full 128K window. The lesson generalizes: **spending this machine's RAM surplus on a second heavyweight does not buy long-context capability; it buys redundancy in the dimension the organism already has.** Long context must be purchased through an architecture whose attention permits it, and it is cheaper to fund one context-heavy resident than to over-provision context on every lane.
- **The minimalist corollary.** On a CPU-only host, token velocity scales chiefly with *active* parameters per token, not total — which is precisely why the registry leans MoE. But velocity is shared across lanes: every concurrently-active resident dilutes every other's throughput. The organism therefore prefers *few heavyweight lanes at high duty cycle* over many at low duty cycle, and the bandit router (§8) must learn a bias against route spreads that thrash the thread pool (Pathology: routing thrash, §8).

## 6. Signal Theory: The Board

All inter-slot communication passes through a single append-only medium. The medium is **split into two entities**, substrate and tenant:

- **The Ledger** — the substrate: append-only storage, dumb transport, medullary hard-fail on tampering attempts, provenance stamps affixed at append time by the transport itself — each claim carries origin slot, generation, and jurisdiction fields, so that downstream selectors can be audited to read only fields within their own remit. The Ledger judges nothing, funds nothing, and is not a tenant.
- **The Board** — the protocol that runs over the Ledger, governed by five rules. The protocol has no moderator anywhere inside it.

**Rule 1 — Claims, not chatter.** Only finished claims reach the board; reasoning-in-progress never leaves private context. The board is a laboratory notebook of conclusions, not a meeting transcript.

**Rule 2 — Subscription hearing.** A slot cannot address others; it can only hear the claim-classes to which it is subscribed. Default audience for every claim: its stage-mate, always — the callosal channel made formal. Cross-stage subscribers, rarely, by manifest. Rule 2 is priced: mate-read is a mandatory ledger line at ×2 floor amplification per published claim.

**Rule 3 — Pairwise objection loops.** A subscriber objects on stated grounds; the author corrects or counters; the objector re-evaluates. Two peers, exchanged evidence, no audience.

**Rule 4 — The evidence-delta rule, as a commitment.** Each objection round must carry new evidence. The check is **committed** rather than consulted on: a *deterministic predicate over claim fields, evaluated by dumb transport* — citation-present, measurement-attached, line-identified, and an embedding-distance floor between the objector's successive positions. A number is a computation, not an interpretation (Law 5's bright line). The attachment-scope tension is resolved by rule: an objection must *carry the cited material itself* (excerpt or hash within a size bound), never merely reference it — an objector who cannot quote what it contests cannot contest it, and the transport's hash check makes quoting mechanically verifiable. Convergence must be information-driven, never confidence-driven; this is the anti-capitulation clause.

**Rule 5 — Bound, coalesced escalation.** After approximately two unresolved exchanges, the claim joins the operator queue. A human-visible draw is a success state — biology offers no court of appeal; this organism does. But escalations are cheap to manufacture and the operator is the organism's single judge organ, so the endocrine tier (§7) owns an **escalation-rate budget with coalescing**: a run of unresolved draws over one topic coalesces into a single operator session, and the sleep window is the guaranteed drain interval — escalations batch at the maintenance window unless urgent-class. Escalations-per-completed-task is a first-class epoch metric with an alarm.

**The claim schema, enumerated.** Rule 4's predicates need a fixed field set to operate over; here it is, so the checks are computable and nothing rides on free text: `claim_id`; `signal_class`; `author_slot` (origin); `generation`; `jurisdiction`; `timestamp`; `author_tokens`; `position_vectors` (successive positions, for embedding-distance and slope); `citation_present` (boolean); `measurement_attached` (boolean); `line_identified` (boolean); `excerpt_hash` (within the size bound of Rule 4); `status` (`draft` → `published` → `objected` → `conceded`/`escalated`). The evidence-delta and jerk predicates read these fields only — numbers and booleans, never meaning. Everything else is prose, and prose belongs to cerebrum or operator alone (Law 5).

**Constitutional silences.** Two claim-classes admit no *objection loop*: they are read, never disputed. The Sentinel's `veto` is a terminal class — broadcast so the halt is visible and auditable, but lawfully answered only by cessation, for an appealable veto is a judge organ reborn. The Chronicle's `record_append` is read by Canon (its sole training input) and by downstream witnesses — argument with memory is confabulation, so the only lawful response is assimilation; tampering attempts are medullary hard-fails, not debates.

## 7. Metabolic Control: The Endocrine Tier

Acute control is reflexive and unconditional — spend caps fire without weighing, without appeal. Chronic control is hormonal and advisory: a system in which soft signals act like hard ones is a gland impersonating a brainstem; a system in which hard limits can be argued away is a brainstem with a public-relations department.

### 7.1 The Hypothalamic Axis — Budget Homeostat and Pacemaker

Continuous measurement of cumulative spend, token velocity, projected runway, *and* the circadian schedule — sleep/wake windows for consolidation and maintenance live here, adjacent to hunger, exactly where the real diencephalon puts them: the SCN is hypothalamic; the pineal was never the clock. It suggests; it never forbids.

### 7.2 The Pituitary — Cascade Controller

Translates hypothalamic signals into executed adjustment: batch sizing, routing weights, consolidation scheduling, operator-queue coalescing. Autonomous cascades, suppressible at will by the operator.

### 7.3 Interoception — Literal Formulas

For each metabolic signal, **surprise = |observed burn rate − predicted burn rate|**, where the prediction is an exponentially-weighted moving average over the trailing window. Appetite is thresholded precision on that residual; throttle is proportional action on the same. Constants — window length, thresholds, gain — are Epoch 0 measurements published in the ledger schema, not free parameters. The residual-throttled variant must beat flat-rate throttling on the golden set or be deleted (Law 4 applies to formulas too).

### 7.4 Consolidation Trigger — Hybrid

Chronicle→Canon distillation runs when (cumulative `record_append` volume > V) **∧** (dispatch activity below idle threshold), where V is a pinned Epoch 0 constant (Appendix A), mirroring the conjunction of accumulated plasticity markers and offline state that licenses biological replay. Falsify hybrid against batch-only and volume-only on Canon-retrieval quality per distillation joule. Distillation direction remains fixed: episodic feeds semantic, never the reverse. The offline gate governs *when* distillation runs, not *whether* its products may be reviewed: distilled `convention_claims` enter the board as ordinary claims, subject to the objection loop like any other — consolidation's offline guarantee protects the run from interference, not its products from dispute.

### 7.5 The Pair-Health Band

Pair disagreement rate is measured per stage, per epoch, on the mate's objection behavior against the leader's claims (§5.4). The mechanism survives only inside a two-sided band:

- **Floor violation** (agreement ≈ unanimity on the golden set): capitulation theater with tenure — the pair is fused; automatic decorrelation promotion fires (§5.6), and persistent violation triggers the stage-merger falsifier (§5.2).
- **Ceiling violation** (persistent disagreement on resolved-known-answer items): noise manufactured for show — correlated disagreement is still correlation; the pair is diagnosed, not congratulated.
- **Healthy band**: disagreement present, information-driven (per Rule 4 deltas), and resolving within bound on known-answer items.

Band parameters X and N are Epoch 0 constants, published in Appendix A, and identical for both violation classes in absolute-value form so that the band cannot be gamed by manufacturing disagreement (behavioral metrics are screening signals; binding verdicts anchor to golden-set recurrence and cost outcomes, which cannot flatter their grader).

### 7.6 The Cost Ledger

**Schema in Appendix A.** It includes every line the cost model needs — authorship tokens, callosal mate-read amplification (floor ×2), cross-stage subscriber reads, guard rents, assembly spawn costs, circuit invocation costs, escalation handling, idle residency — plus the two substrate lines this hardware demands: **model residency** (a resident checkpoint's RAM share, audited against routing frequency per Law 4) and **KV growth** (actual cache consumption per active lane, which caps usable context on CPU lanes regardless of nominal windows). Ledger obesity remains a pathology (9.13): guards accumulate additively because unfired guards look wise; therefore guards myelinate and die like everything else.

## 8. Selection and Interruption

**Action selection — a bandit, not a table.** The macro router reads task features (signal class, artifact type, budget context) and emits one route: one leading lens per touched stage (per §5.4), one slot profile, and — on this substrate — one **lane assignment**, binding the route to a resident model and a thread budget. Training is a lightweight contextual bandit over route choices, rewarded by the epoch cost-quality delta — tiny state, no paid dispatch, learned rather than hand-maintained, which *structurally deletes the roster-drift lesion*: routing weights are learned state, not duplicated configuration. The biological warrant is dopamine-like reward prediction on route outcomes; the engineering warrant is that it is falsifiable per-epoch.

Winner-take-all remains lawful here and only here: losers are silenced (as authors), not blended — a weighted blend of two minds doing one job is a committee, and committees launder anomalies.

**MoE-inherited guards.** Sparse activation + gated routing + WTA selection is the mixture-of-experts pattern, and the MoE literature has already catalogued our failure modes. Imported as named, falsifiable guards: **router collapse** (route diversity decays onto one path; load-balance alarm), **expert under-use** (a funded role or resident model never selected across an epoch; under-use alarm triggering Law 4 review — on this substrate this alarm also catches resident-never-routed waste), **routing thrash** (route or lane oscillation across retried steps; hysteresis requirement, with special force on this host where lane switching evicts warm KV caches).

**Dispute interruption — the jerk reflex, lawful by construction.** The reflex detects stalled convergence and serves one party a hardening order: produce genuinely new evidence or refuse concession with maximal specificity — zero hedging, full commitment. Three properties keep it lawful:

1. **Its inputs are numbers, not meanings.** Stall detection reads the three mechanically-computed features of the input schema — **concession slope** (rate of position movement across rounds), **citation-presence** (evidence-delta field compliance), and **position volatility** (embedding distance between successive positions). A number is a computation, not an interpretation — the bright line of Law 5, now with a concrete input schema.
2. **Its recipient is chosen by the embedded WTA sub-selector** over a quarantined schema scoring the three named features with a seeded pseudorandom tie-break recorded in the transcript. The warrant for recipient-selection is engineering (disjoint input schemas, disjoint provenance — the sub-selector may read only fields written within the dispute's own jurisdiction, stamped at append); *the anatomical LC-sniper justification is withdrawn*. The biology grants reset, not party-selective message delivery; the design deviates, and Appendix B says so.
3. **It never decides.** A jerk round that fails to converge escalates mandatorily — the reflex forces honesty or forces appeal; it cannot manufacture resolution.

**The reflex ships only against its control arm.** Before the hardening variant earns its organ, a mirror control — *force concession-or-maximal-specificity* at equal budget — runs on the golden set. If hardening and concession-forcing resolve disputes at the same rate, the machinery halves at no quality cost: mediocre reasons to keep an organ is the definition of a Law 4 deletion. The epoch-5 bias test (same party repeatedly targeted) is retained as the fairness falsifier.

## 9. Pathology

An organism is defined as much by what kills it as by what it does. The register is numbered 9.1–9.13, with split-brain drift and pipeline inheritance full citizens rather than codas. Each disease carries its structural theorem and its guard:

| # | Pathology | Theorem and guard |
|---|---|---|
| 9.1 | **Capitulation theater** — convergence via confidence, not information | Theorem: flip-rates track persuaders, not evidence, wherever convergence is graded on agreement. Guard: deterministic evidence-delta predicates (§6 R4); flip-rate audited against citation density. |
| 9.2 | **Infinite politeness** — courteous rounds until budget death | Theorem: unresolved disputes spend unbounded tokens. Guard: hard exchange bound (not arguable mid-flight, because it is not an argument); jerk reflex; mandatory post-jerk escalation into the coalesced queue. |
| 9.3 | **Committee blindness** — broad participation averages away tail anomalies | Theorem: blending witnesses launders outliers. Guard: pairwise objections only; subscription scarcity; WTA authorship. |
| 9.4 | **Seizure** — full synchronous activation; correlated convergence on a shared confident error | Theorem: total activation is epileptic in brain and thermal in tower alike. Guard: thalamic Law 2 enforcement; **tested empirically at Epoch 2: one golden-set task run sparse-audience vs. all-slots-hear; if full-audience wins anywhere, the theory's spine is weaker than claimed — better known at Epoch 2 than Epoch 6.** |
| 9.5 | **Correlated monologue** — paired lenses sharing slices, instructions, backbone; one reasoner billed twice | Theorem: cheap decorrelation is stylish variance, not error variance. Guard: decorrelation ladder (§5.6) with automatic promotion on band-floor violation. |
| 9.6 | **Confabulation** — semantic memory editing episodic memory to flatter belief | Theorem: consolidation that runs backward destroys the interference protection that makes CLS work. Guard: one-way Chronicle→Canon flow; Ledger immutability; the most load-bearing invariant in the organism. |
| 9.7 | **Rumination** — memory gaining veto over action | Theorem: a memory organ that overrides decision is a judge organ. Guard: temporal stages inform the frontal pair through the pipeline; they never overrule it. |
| 9.8 | **Undirected escalation** — paid dispatch without operator record | Theorem: unwatched emergency rations become the diet. Guard: 1:1 correspondence between paid ledger rows and recorded operator confirmations. |
| 9.9 | **Tumor growth** — transient roles squatting persistent slots; orphan lenses without stage or mate | Theorem: authority without workload persists by inertia. Guard: assembly mortality; authority contracts; myelination as the sole sanctioned promotion path; occupancy legality rule (§11). |
| 9.10 | **Metaphor worship** — funding every named organ because it has a name | Theorem: names are free and metabolism is not, so name-driven funding metastasizes. Guard: Law 4 applied to this paper — the deviations ledger (App. B) exists to make worship impossible to hide. |
| 9.11 | **Split-brain drift** — a stage's lenses converge into mirror copies; traffic still flows, but nothing crosses the midline the other side lacks | Theorem: the expected failure of any implementation that treats witness-diversity as décor. Guard: two-sided disagreement band (§7.5) with automatic decorrelation promotion; persistent band-floor violation triggers the stage-merger falsifier (§5.2). |
| 9.12 | **Pipeline inheritance** — an early-stage error inherited unanimously and decorrelatedly by every downstream witness | Theorem: posterior-to-anterior flow guarantees propagation, and pair metrics read healthiest exactly when poisoning is worst. Guard: Cartographer re-perception integrity polls (§5.5) — a ground-truth channel that bypasses the pipeline, priced and rent-paying. |
| 9.13 | **Ledger obesity / guard fatigue** — the immune system outbilling the cognition | Theorem: guards are additive, unfired guards look wise, so instrumentation accumulates until it eats the budget. Guard: every telemetry channel carries a standing rent against the ledger it protects; guards myelinate and die like organs; alarm-distinguishing-power is audited on the golden set at every epoch review. |

Goodhart caution, generalized: every *behavioral* observable — disagreement rates, jerk responsiveness, evidence-delta thickness — is performable by a model that has learned what its evaluator rewards. Behavioral metrics are screening signals; the **binding falsifiers anchor to the lesion ledger and golden-set recurrence/cost outcomes**, which cannot flatter their grader.

**Invariant vs. falsifier.** Not every §9 guard is a falsifier. Structural invariants — the paid-dispatch 1:1 correspondence (9.8), the one-way Chronicle→Canon flow (9.6), the hard exchange bound (9.2) — are *enforced* rather than graded: they hold or they are violated, and a violation is an incident to repair, not evidence that retires an organ. Under Law 4 an organ dies only on a measurable falsifier anchored to golden-set recurrence or cost outcomes. Invariants defend the constitution; falsifiers judge the organs — and only the latter can kill.

## 10. Plasticity: The Myelination Ladder

Behavior descends a ladder as it becomes routine: a repeated assembly is promoted to a standing circuit; a circuit whose outputs prove reliably deterministic is *myelinated* — rewritten as plain script, exiting model inference entirely, exiting the set of things that have tenants at all. Every demotion purchases metabolism: area slots are the costliest compute in the organism; deterministic code is free. The end-state of a sufficiently learned behavior is to stop thinking about it — literally.

**Promotion runs on credit, not counting.** Each circuit invocation logs cost and a coarse outcome flag; promotion fires when the expected value of standing compilation beats expected transient cost with a confidence bound (Wilson/Hoeffding bounds keep the trigger deterministic-friendly); demotion is the same inequality inverted over a decay window. Promotion triggers on observed history, never anticipation — pre-compiling a circuit "because it will obviously be needed" is the exact tier that overpromises — and the ladder as a whole remains subject to the golden-set falsifiers of Q4.

On this substrate the ladder has a concrete top rung in reach: the registry's small lanes make excellent *first quantization targets* for myelination trials — a hot circuit candidate (greeting parsing, trivial diff summarization) measured against the smallest resident before it is ever rewritten as script.

## 11. Occupancy, Identity, and Lifecycle

**Occupancy legality.** A role-kind × funding-kind cell is lawful iff (authority is grant-compatible) ∧ (funding is repetition-justified). Named consequences: persistent circuit = *cache* — legal and valuable; transient area = *surgeon* — legal but suspicious, reserved for rare-event cognition (incident response), and must auto-expire with its event class or become the next tumor taxonomy; assembly-with-subscriptions — impossible (violates inheritance); circuit-with-spawn — impossible.

**Tenant identity.** Identity is engineering, not philosophy: a tenant *is* the tuple (role, model-class, funding-generation) together with the Ledger entries authored under it. Attribution, decorrelation history, and falsifier ledgers bind to that tuple; whether a re-funded slot is "the same agent" dissolves into bookkeeping, which is exactly what an ontology should do. Lens identity (left-of-its-stage, right-of-its-stage) is a stable attribution key across generations.

**Lifecycle verbs, defined once:** **fund** (a role gains a slot on workload or lesion evidence), **promote** (a behavior descends the myelination ladder), **demote** (the inversion), **divorce** (a pair is decorrelation-promoted or rebuilt under the band rules), **retire** (a slot ends without prejudice, per falsifier or workload), **expel** (a tenant ends *with* prejudice, per pathology verdict). No other lifecycle vocabulary exists in this ecosystem.

## 12. Development: Embryology, from Census to Graduation

Neural tubes close hindbrain-first; forebrains develop last. Boot order obeys — and where it deviates, the deviation is owned in the text, not smuggled into the metaphor.

**Epoch 0 — the substrate census (new).** Before any organ, the organism knows its physics. On the named host: baseline token velocity per registry model per lane/thread allocation; watts per lane and per system state via on-board energy counters (RAPL) and a wall meter; memory ceilings, residency footprints, and measured KV growth curves per model per context length; thermal envelope under sustained load; the utility rate from the local bill, entered as the ledger's `$/joule` constant (recent reporting for this territory puts residential electricity around 14–16¢/kWh; the bill, not the blog post, is the constant). No organ exists yet; every constant in Appendix A gets its measured value here, including the pair-band thresholds X and N of §7.5. **An epoch with a guessed constant is not an epoch; it is debt.**

**Epoch 1 — Medulla.** Serving daemon, supervision, Ledger substrate with tamper hard-fails (largely inherited from the prior rig's one functioning organ).

**Epoch 2 — Midbrain, and the seizure experiment.** Reflexes: spend caps, syntax gates, permission walls. *The jerk reflex is excluded from this epoch by its own prerequisites: it presupposes disputes, which presuppose funded pairs.* Also this epoch: the sparse-audience vs. all-slots-hear experiment on one golden-set task settles Law 2 empirically before anything expensive is built on it.

**Epoch 3 — Cerebellum.** One calibration sidecar: the embedding/retrieval index resident, serving and warming. *(The cerebellum is metencephalic — hindbrain — and precedes the diencephalic homeostats, so the hindbrain-first claim is honored by the boot sequence itself.)*

**Epoch 4 — Hypothalamic axis.** Budget homeostat, circadian scheduler, cost ledger with measured constants. The organism learns to feel hunger and to sleep before it learns to think; the biology that licenses this is diencephalic, and we say so.

**Epoch 5 — One frontal pair.** Driver and Sentinel in their first funded slots, plus the Board. Two slots, one board, zero dollars: the minimal sentient organism — something that proposes and something that doubts. The callosal channel opens with the pair, because a pair that cannot hear each other is two organisms, not one. The jerk reflex may join here and only here, contingent on its mirror-control falsifier (§8) being measured in the same epoch.

**Epoch 6 — Graduation.** Each remaining stage funds only when the pinned lesion ledger or workload evidence shows the organism limping without it; posterior before anterior, because decoding precedes deciding. **A stage funds both lenses together or stays unfunded** — a half-paired stage has no callosal channel and therefore no testimony. The stage, not the role, is the unit of graduation.

On this substrate, the realistic minimum viable organism is plausibly the frontal pair plus Reader-as-circuit for a long while — 32 threads and CPU-class token velocity argue for graduating slowly and measuring constantly. The workload evidence of Epochs 5–6, not this paper's affection for symmetry, decides.

At every epoch the evaluation question is identical: *can the pinned golden set pass through this organism without recurrence, at what cost-quality point?* An epoch that cannot beat its predecessor's is not an epoch; it is debt.

## 13. The Inherited Lesions — the Golden Set, Pinned

The prior rig's verified failures constitute the golden set, and the golden set is **version-pinned**: the ledger records which iteration every falsifier grades against, and epoch-to-epoch comparisons are incommensurable without the pin. Nine classes, each charged to its detector organ: presence-only selftests against value-level evaluation (Reader/Sentinel); parse drift against validated-output parsers (Reader); word-splitting template bugs against falsifier fixtures (Circuits); fail-late sweeps against cheap-gates-first ordering (Midbrain); roster drift against the Cartographer's single source of truth (and structurally, against the bandit router's learned state); state wipes against round-trip selftests (Medulla/Cerebellum); unmeasured spending against prerequisite gates (Hypothalamus/Midbrain); deployment drift against byte-comparison at bringup (Medulla); and speculative middleware shipped dormant against Law 4 in its entirety. These are not bug reports. They are the entrance examination each organ must pass before claiming a slot.

## 14. Consultation Questions — Reduced and Honest

Questions earlier editions asked rhetorically are settled in the text (occipital fit → §5.3 exemption; evidence-delta mechanics → §6 R4; claim schema → §6; temporal witnessing under the constitutional silences → §6; bandit routing → §8; consolidation gating → §7.4; identity and lifecycle → §11; interoception schema → §7.3 + Appendix A; guard-vs-falsifier → §9). What remains genuinely open:

**Q1. Band parameters.** What values of X and N (disagreement thresholds and windows, §5.2/§7.5) best serve the stage-merger and pair-health falsifiers, given Epoch 0 measurements on this substrate?

**Q2. Escalation budget shape.** What coalescing window and escalation-rate alarm threshold keep the operator queue off the critical path without starving genuine draws? Is the sleep window as sole guaranteed drain interval tolerable, or must urgent-class exceptions be defined — and if defined, how bounded?

**Q3. Jerk feature weights.** Which weights over the three mechanically-computed features (concession slope, citation-presence, position volatility) and the seeded roll should the Epoch-5 sub-selector ship with, and what mirror-control result would falsify the whole organ (§8)?

**Q4. Myelination bounds.** What confidence bounds and decay windows should fire promotion/demotion on the plasticity ladder, and against what golden-set variant?

**Q5. Hybrid consolidation constants.** What V (distillation volume threshold) and idle-threshold implement the §7.4 conjunction, and which competing trigger loses on Canon-retrieval quality per distillation joule?

**Q6. Surgeon-area expiry.** Which transient-area event classes justify surgeon funding, and what auto-expiry discipline prevents the next tumor taxonomy?

**Q7. Minimum viable organism.** Given Epoch 0's measured lane curve on 32 threads and the registry's residency footprints, what is the smallest workload-honest funding lattice — frontal pair plus Reader-circuit, or more? Workload evidence, not symmetry, decides; respondents with measured alternatives are especially welcome.

**Q8. The frontal pair on one machine.** Which two registry residents should Driver and Sentinel instantiate on — and at what thread split — such that the pair achieves Rung-1 decorrelation (context slices) without starving the other's velocity? Candidates include the heavyweight trio of Appendix D; the paper's provisional tilt is that a same-backbone frontal pair with divergent slices and lateralized instructions should precede any two-heavyweight arrangement, because two concurrent heavyweight lanes halve each other's tokens-per-second on this host. Measured counter-proposals welcome.

**Q9. Lane discipline under contention.** When two or more residents act concurrently, what lane-switch hysteresis prevents routing thrash (§8) from evicting warm KV caches — and at what measured cache-eviction cost does switching lanes become more expensive than waiting?

---

*Issued for consultation. The theory declares its own fallibility as a founding term: nothing here earns existence by being written, and the blueprint this paper may someday inspire must be shorter than this paper — because blueprints are for builders, and this is for architects. Where blueprint and theory disagree, theory wins until the lesion ledger says otherwise.*

**End of Green Paper v2.2.**

---

## Appendix A — Cost-Ledger Schema (published)

Constants measured at Epoch 0 and pinned per epoch; every line carries units and sampling cadence.

| Field | Unit | Cadence | Notes |
|---|---|---|---|
| `author_tokens` | tokens | per claim | generation cost of the authoring lens |
| `mate_read_tokens` | tokens | per claim | mandatory callosal read; floor ×2 amplification with author |
| `subscriber_reads` | tokens | per claim | cross-stage subscribers, by manifest |
| `assembly_spawn_cost` | tokens + MiB·s | per assembly | transient worker lifecycle cost |
| `circuit_invoke_cost` | µs | per invocation | near-zero target; myelination erases it |
| `guard_rent_<name>` | J + tokens | per interval | standing rent of each guard/telemetry channel (P2) |
| `poll_rent_perception` | J + tokens | per poll | Cartographer re-derivation integrity polls (§5.5) |
| `escalation_cost` | tokens + operator-mins | per draw | coalesced operator queue events |
| `idle_residency_context` | MiB·s | continuous | resident context per lane |
| `model_residency_<model>` | MiB | continuous | resident checkpoint footprint; audited against routing frequency (Law 4) |
| `kv_usage_<lane>` | MiB | continuous | measured KV cache growth; caps usable context regardless of nominal window (§5.7) |
| `paid_dispatch` | USD | per dispatch | requires 1:1 operator confirmation record; incident if absent |
| `joules_task` | J | per task | RAPL-instrumented; the Law 1 denominator multiplier |
| `usd_per_joule` | USD/J | per billing cycle | from the utility bill; locality-pinned |
| `burn_rate_actual` | tokens/s, J/s | continuous | hypothalamic input |
| `burn_rate_predicted` | tokens/s, J/s | continuous | EWMA over trailing window (window = pinned constant) |
| `surprise` | \|Δ\| | per sample | \|actual − predicted\|; drives appetite/satiety/throttle |
| `interoception_window` | samples | pinned at Epoch 0 | EWMA trailing window for burn-rate prediction (§7.3) |
| `interoception_threshold` | \|Δ\| | pinned at Epoch 0 | appetite threshold on surprise residual (§7.3) |
| `interoception_gain` | unitless | pinned at Epoch 0 | throttle gain on the same residual (§7.3) |
| `pair_disagreement_rate` | ratio | per stage, per epoch | measured on mate objection behavior (§5.4); banded in §7.5 |
| `pair_band_threshold_X` | ratio | pinned at Epoch 0 | stage-merger and pair-health band threshold (§5.2, §7.5); identical in absolute value for both violation classes |
| `pair_band_window_N` | sessions | pinned at Epoch 0 | pair-health window (§5.2, §7.5); not tunable in flight |
| `distillation_volume_V` | records | pinned at Epoch 0 | cumulative `record_append` threshold in the §7.4 conjunction |
| `escalation_rate` | per completed task | per epoch | with alarm threshold |
| `golden_set_version` | hash | per epoch | the version pin (§13) |

*Fitness function (Law 1, M8): quality per joule per **completed, verified task**, graded against the pinned golden set. All other lines are telemetry.*

## Appendix B — Deviations Ledger (unmarked inversions are how metaphor worship begins)

| # | Site | Biology | Design | Status |
|---|---|---|---|---|
| B1 | Occipital pair (§5.3) | Ventral/dorsal streams are bilateral, not hemispheric | Reader = ventral-stream lens; Surveyor = dorsal-stream lens; left/right décor discarded | **Declared exemption** |
| B2 | Temporal pair (§5.3) | Episodic/semantic dissociation is systems-level (hippocampal/neocortical); HERA is frontal | Pair derived from complementary learning systems; left/right retained as organizational labels only | **Re-derived** |
| B3 | Frontal pair (§5.3) | Approach/withdrawal asymmetry is population-level correlational, not categorical | Mandate retained as legislated design; absolutism dropped | **Softened** |
| B4 | Parietal pair (§5.3) | Local/global dissociation robust; parietal also dominates egocentric spatial updating | Both imported; double-spend with occipital ended by B1 | **Augmented** |
| B5 | Pacemaker (§7.1) | Circadian pacemaker is the SCN — hypothalamic; pineal is a downstream effector | Pacemaker located in hypothalamic axis; pineal organ retired | **Corrected (N1)** |
| B6 | LC sub-selector (§8) | LC projections are diffuse network-reset, not party-selective | Party-selective WTA retained on engineering warrant only; anatomical justification withdrawn | **Warrant swapped (N2)** |
| B7 | BG/LC homology (§4) | Dopaminergic and noradrenergic systems crosstalk extensively | Strictly disjoint input schemas, deliberately | **Marked deviation (F6)** |
| B8 | "Columns" → "Assemblies" (§5) | Cortical columns are permanent anatomical units | Assemblies are transient coalitions; name imports no persistence connotation | **Renamed (N3)** |
| B9 | 20W framing (§3, Law 1) | Brain efficiency owes much to analog/chemical compute and synaptic parallelism silicon cannot copy | We steal the transferable subset only: sparse activation, layered autonomy, error-correcting pairs, gating | **Scoped (N5)** |
| B10 | Stage count (§5.2) | Lobes are anatomical convention, not functional modules | Eight = prior lattice; falsifiable downward via stage-merger; workload, not arithmetic, is the proof of adequacy | **Downgraded to lattice (F1)** |
| B11 | Callosal channel and record medium (§4, §6 R2) | Corpus callosum is a private, direct, un-tolled fiber tract; paired structures exchange disagreement with no third party | Pair exchange and the record medium are mediated by session plumbing; mate-read is a mandated step, not a metered ledger line; session records are per-session, not a tenanted append-only board | **Approximated (substrate)** |
| B12 | Sentinel veto (§5.3, §6) | No brain structure holds an absolute veto over the rest; withdrawal is graded | Unconditional veto approximated by permission `deny` rules plus refusal instruction; appeal-proof-ness is policy, and the operator retains ultimate override | **Approximated (substrate)** |
| B13 | Jerk reflex (§8) | The locus coeruleus is a diffuse network-reset (see B6), not a dispute interrupt | No native interrupt on the substrate; the reflex is provisional external tooling (watchdog or supervisor subagent) | **Missing (provisional)** |
| B14 | Thalamic gate (§4) | The thalamus gates by signal modality, non-judgingly, with light transformation | Permissions gate by action/resource type — mechanically non-judging (Law 5) but coarser than signal-class; transformation has no native primitive | **Approximated (substrate)** |
| B15 | Myelination (§10) | Biological myelination is continuous, graded, and reversible | Promotion to a compiled skill/command is a discrete boundary; demotion requires re-authoring | **Approximated (substrate)** |
| B16 | Sparse multi-organ concurrency (§5.7) | The brain sustains many parallel circuits within a sparse envelope | The substrate runs one primary agent per session and serializes child sessions; concurrent cognition is sequential | **Approximated (substrate)** |

## Appendix C — Revision Log (every prior finding, dispositioned)

| Finding | Disposition |
|---|---|
| Audit D1 (seven vs. eight divisions) | Fixed: eight everywhere (§4) |
| Audit D2 (§10.x numbering collisions) | Fixed: renumbered 9.1–9.13, cross-references repaired |
| Audit D3 (router/pipeline unreconciled) | Fixed: §5.4 authorship policy, router arbitrates action not attendance |
| Audit D4 (Chronicle substrate/tenant duality) | Fixed: Ledger (substrate) / Chronicle (tenant) split (§4, §6) |
| Audit D5/D7 (split-brain drift demoted; ten-vs-eleven) | Fixed: promoted to 9.11 with in-register theorem |
| Audit D6 (embryology hindbrain violation) | Fixed: cerebellum precedes diencephalic epoch (§12) |
| Audit F1 (one-directional falsifiability) | Fixed: §5.2 downward falsifier + honest "prior lattice" framing |
| Audit F2/P1 (cross-stage error correlation) | Fixed: §5.5 integrity polls; Pathology 9.12 |
| Audit F3 (callosal floor unpriced) | Fixed: mate-read as mandatory ledger line (§6 R2, App. A) |
| Audit F4 (blackboard rule tension) | Fixed: §6 R4 attachment-scope resolution — objections carry cited material |
| Audit F5 (operator bottleneck) | Fixed: §6 R5 coalescing + escalation-rate alarm; sleep window as drain |
| Audit F6 (BG/LC inversion) | Fixed: Appendix B7 |
| Audit F7 (Goodhart exposure) | Fixed: §9 closing; behavioral metrics demoted to screening |
| Audit Part III (temporal/occipital warrants) | Fixed: B2 re-derivation (CLS); B1 occipital exemption |
| Audit Part V (Laws verdicts) | Law 1 amended (M8 denominator + ledger lines); Law 3 amended (ladder + 9.12); Law 5 bright line published (§3); Laws 2/4 upheld |
| Audit Part VI (Q3 deference theater) | Fixed: occipital settled in-text (§5.3); questions reduced and de-rhetoricized (§14) |
| Audit Part VII (form defects) | Fixed: ledger schema published (App. A); lifecycle verbs defined (§11); golden-set pin (§13) |
| Review N1 (pineal ≠ pacemaker) | Adopted: B5 |
| Review N2 (LC targeting overstated) | Adopted: B6 |
| Review N3 ("column" collision) | Adopted: B8 |
| Review N4 (lobe mapping decorative) | Adopted: promoted to headline admission (§2, B10) |
| Review N5 (20W overcredit) | Adopted: B9 |
| Review N6 (thalamus undersold) | Adopted: §4 transthalamic relay with light transformation |
| Review M1 (jerk trigger vs. Law 5) | Adopted: §8 mechanical-feature input schema; §3 bright line |
| Review M2 (decorrelation ladder inverted) | Adopted: §5.6 reordering + automatic promotion |
| Review M3 (router credit assignment) | Adopted: §8 contextual bandit, roster-drift structural deletion |
| Review M4 (evidence-delta terminator) | Adopted: §6 R4 commitment |
| Review M5 (operator serialization) | Adopted: §6 R5; escalation-rate metric |
| Review M6 (MoE literature) | Adopted: §8 named guards (collapse/under-use/thrash) |
| Review M7 (provenance walls) | Adopted: §6 Ledger provenance stamps + jurisdiction audit |
| Review M8 (quality per joule denominator) | Adopted: Law 1 restated (§3) |
| Review E1–E8 | All adopted: §7.3 interoception formulas; §10 credit-triggered plasticity; §11 occupancy/identity; §7.4 hybrid consolidation; §7.5 two-sided band; §8 mirror control; §9.4 Epoch-2 seizure test |
| **v2.0 errata** | "falliability" → fallibility; §6 R5 garbled phrase rewritten; missing §7.5 subsection created (was a dangling cross-reference patched only in a footnote); §12 epochs explicitly numbered; Appendix A gains `model_residency` and `kv_usage` lines |
| **MoE residency vs. KV ceilings (Epoch −1 analysis)** | Codified: §5.7 Substrate Economy; §7.6 ledger lines; Appendix D registry annotations |
| **Live model registry supplied** | Adopted: Appendix D; Q8/Q9 reframed around lane contention |
| **v2.2 structural corrections** | Q-01 fixed (§5.2: a fifth stage pairs roles 9–10, not 10–11); §5.4 leading-lens lists completed with the comprehension pair (Chronicle/Canon); §8 jerk inputs reconciled with §14 Q3 (concession slope / citation-presence / position volatility); §7.4 distillation threshold renamed N→V (collision with §7.5's window N ended); Appendix A gains the promised pinned constants (band X/N, interoception window/threshold/gain, distillation volume V); §6 Constitutional silences rewritten — read, never disputed, with `veto` and `record_append` read paths stated |
| **Form Q9 (claim schema)** | Settled: §6 claim schema enumerated; rigid-predicate fields published so evidence-delta checks are computable |
| **Form Q11 (consolidation gating)** | Settled: §7.4 offline gate constrains when distillation runs, not whether its products are disputable; distilled conventions enter the board as ordinary claims |
| **Form Q14 (guard vs. falsifier)** | Settled: §9 invariant-vs-falsifier distinction; only measurable falsifiers retire organs under Law 4 |
| **v2.2 de-Lumo (provenance retirement)** | Revision-memo voice and inline finding citations removed from the body; the review narratives of §1 and §5.2 condensed; "prior session" reference (§D.4) retired; provenance now lives only in Appendix C |
| **Appendix E (OpenCode substrate mapping)** | Added: the design is mapped onto OpenCode V2 primitives; verdicts are Faithful / Approximate / Missing (provisional); substrate gaps are logged as deviations B11–B16 |
| **Edition 2 form, full disposition (Q1–Q14)** | No question silently dropped: Q1 division count → §4; Q2 reference integrity → disposition of Audit D2 in this log; Q3 count arithmetic → §5.2 (+B10); Q4 temporal exemption → §6 Constitutional silences (rewritten in v2.2: `record_append` is read by Canon, never disputed); Q5 occipital → §5.3 (+B1); Q6 jerk vs. Law 5 → §8; Q7 split-brain detection → §7.5 band + 9.11; Q8 pair falsifiability → §7.5 floor/stage-merger; Q9 claim schema → §6 (v2.2); Q10 interoception → §7.3 + Appendix A; Q11 consolidation gating → §7.4 (v2.2); Q12 router credit → §8; Q13 sub-selector → §8; Q14 guard vs. falsifier → §9 (v2.2) |

## Appendix D — Model Registry (living; the organism's genotype as of Epoch −1)

The registry is the candidate set from which Epoch 0 census and every funding decision draws. Entries are annotated with what is **verified** (against published architecture documentation or the model card) versus what is **to be measured at Epoch 0** — vendor claims are priors, not constants. Registry order follows the host's lane economy: heavyweights first.

### D.1 Heavyweight lanes (the heavyweight comparison)

| Model | Class | Verified/known | Epoch 0 must measure | Provisional candidacy |
|---|---|---|---|---|
| **gpt-oss:120b** | MoE, 117B total / ~5.1B active, MXFP4, ~65 GiB weights | KV cache ~4.5 GiB even at full 128K window (half its 36 layers are 128-token sliding-window; the rest 8-KV-head GQA); Apache 2.0; Harmony response format | tokens/s on 16 and 32 threads; watts/lane; actual KV growth curve; output quality on golden set | **Frontal-lane contender.** Highest capacity-residency per active token in the registry; cannot convert RAM into context (sliding-window ceiling), so it proposes/decides but does not remember long |
| **minimax2.7** | Presumed heavyweight MoE successor in the MiniMax line; specifics **unverified** for this release | Family precedent (per published analyses of earlier MiniMax generations): hybrid full + linear attention, very high sparsity (~4–10B active at ~230B-class total), long windows | Same census battery; **verify the actual config before residency decisions** | **Frontal-lane contender; Sentinel-side diversity candidate** — hybrid linear attention would make it the family's context-capable heavyweight, complementing gpt-oss where KV-starved |
| **qwen3.5:122b** | Presumed Qwen3.5-class MoE (~122B total); specifics **unverified** | Family precedent: Apache 2.0, MoE with modest active parameters, hybrid attention in recent generations; 2026 reporting places Qwen3.5-class coding models above gpt-oss on coding indices | Same census battery; verify config; coding-quality sample against the golden set | **Reader/coder-lane contender.** If the family's coding-index reputation holds locally, it competes with gpt-oss for the perception stage's leading lane rather than duplicating it |

**The heavyweight verdict, provisionally.** The paper refuses to crown one from vendor benchmarks — that is exactly the Goodhart surface §9 warns about. Instead, the comparison is an Epoch 0 bake-off on the *golden set*, graded by the Law 1 fitness function (quality per joule per completed, verified task). The structural priors that shape the bake-off: (i) CPU token velocity follows active parameters, so the three contenders' active counts, not their totals, set their speed class; (ii) their attention designs set their KV ceilings, and therefore which of them can *also* serve as a context-heavy resident; (iii) two heavyweights may co-reside in 256 GiB but cannot co-act at interactive latency without halving each other — co-residency is for redundancy/diversity between epochs, not simultaneous cognition (§5.7). The expected outcome is **division of labor, not a winner**: one heavyweight as the always-on frontal lane; the other as sentinel-side or swap-in — but the lesion ledger decides, not this table.

### D.2 Mid-weight lanes

| Model | Class | Verified/known | Provisional candidacy |
|---|---|---|---|
| **nemotron 3.5 lightning** | MoE, ~30B total / ~3B active, reported 1M-token context; NVIDIA agent-tier release | Token velocity class (small active count); context architecture **to be verified locally** | **The Chronicle candidate.** The registry's one plausible context-heavy resident: if its long-window attention survives CPU deployment, it is the temporal stage's episodic witness — the only role that *needs* the window the heavyweights cannot provide. Epoch 0 must measure where its KV actually caps on this host |
| **qwen3 coder next** | Code-focused model, presumed Qwen coder lineage; specifics **unverified** | — | **Reader-circuit candidate.** Contends with qwen3.5:122b for perception-stage duties at a fraction of the residency; census measures whether its quality holds on diff/parse golden items |
| **laguna 2.1** | Unverified entry; treat as unidentified until Epoch −1 config pull | — | Reserved slot: census assigns it a lane class by measurement, not by name |
| **d1** | Unverified entry; likely small/decoder class | — | Circuit-tier candidate: small enough to serve as a myelination-trial baseline (§10) |

### D.3 Small lanes and organs

| Model | Class | Provisional candidacy |
|---|---|---|
| **north mini code v1** | Small code model | **Completion/circuit tier.** Fallback for autocomplete-class signal where a heavyweight would burn context; myelination trial bed |
| **mellum2.1** | MoE, 12B total / ~2.5B active; JetBrains code model; Apache 2.0; Q4-class GGUF ~7.5 GiB; vendor-reported ~47% SWE-bench (vendor-reported — screen, don't trust) | **FLEXPASS-equivalent: low-latency lane.** Verification by the census: tokens/s at low thread counts, quality on scoped-edit golden items. Its Thinking variant is a candidate assembly engine for the Driver's hands |
| **nomic-embed-text** | Embedding model | **Cerebellum sidecar.** The retrieval/warm-context organ — index builder for the Cartographer's re-perception polls (§5.5) and the Spotlight's salience beam; computes, never deliberates |

### D.4 Registry economy, summarized

Three conclusions follow from the registry read against the host, and they are part of the theory rather than notes about it:

1. **The registry is MoE-heavy, and that is correct** for this machine: active-parameter economy is the only way CPU-class token velocity serves frontier-adjacent quality — MoE residency maximizes quality per resident GiB.
2. **But MoE residency starves KV**, so long-context capability must come from an attention architecture that permits it, and the registry holds exactly one candidate built for that role. The organism should fund **one context-heavy resident (Chronicle-class)** and stop there; a second context-starved heavyweight adds redundancy in the rich dimension, not coverage in the poor one (§5.7).
3. **Lane count is the scarce resource.** The census determines how many residents can act concurrently at acceptable latency; the paper's expectation on 32 threads is *one heavyweight plus one mid-weight*, with small lanes interleave. Funding beyond that is not capacity — it is thrash (Q9).

*Registry updates are amendments to this appendix only; the theory proper changes only through the falsifiers it names. A model that leaves the registry retires like any tenant: without prejudice, with its ledger history preserved.*

---

## Appendix E — OpenCode Substrate Mapping (the implementation ground)

The design's second grounding (§2): the implementation substrate is **OpenCode (V2)** — a terminal-native coding agent with primary and child agents, skills, permissions, and tool plumbing. This appendix maps each organ onto OpenCode's native primitives, so the paper's mechanisms are buildable rather than merely imaginable. Three verdicts are used: **Faithful** (a native primitive carries the mandated behavior), **Approximate** (a primitive carries most of it; the gap is logged in Appendix B), and **Missing (provisional)** (no native primitive exists; the organ ships as external tooling until one does). This appendix is descriptive of a substrate, not normative for the theory: where OpenCode and the theory disagree, theory wins until the lesion ledger says otherwise.

### E.1 Division-by-division mapping

| Organ (§) | OpenCode primitive | Verdict | Notes and gaps |
|---|---|---|---|
| Medulla (§4) | The OpenCode service itself: session ownership, config reload, tool execution, process supervision | **Faithful** | The server owns lifecycle exactly as the medulla is specified to; tamper-hard-fail maps to permission `deny` and policy hard-deny |
| Midbrain (§4) | Permission rules (`allow`/`ask`/`deny` per action×resource) and policies | **Faithful** | Spend caps ≈ permission walls over `shell`/`edit`/`webfetch` resources; unconditional, mechanical, non-judging (Law 5) |
| Pons (§4) | Session message bus and tool-call plumbing between parent and child sessions | **Approximate (B11)** | Transport exists, but it is session plumbing, not a neutral shared append-only medium with provenance stamps |
| Locus coeruleus (§4, §8) | *(none native)* | **Missing (provisional)** | No interrupt-on-dispute primitive; provisional implementation is an external watchdog or supervisor subagent reading the dispute transcript (B13) |
| Cerebellum (§4) | Built-in tool ecosystem: `grep`/`glob` (retrieval index), `read` (warm context), formatters/LSP | **Approximate** | Sidecar functions exist as tools, but they are invoked ad hoc, not as resident calibration organs with rents |
| Thalamus (§4) | Permission actions + skill advertisement + config-scoped tool availability | **Approximate (B14)** | Gates by action/resource class (mechanically non-judging), but coarser than signal-class gating; no native light-transformation step |
| Basal ganglia (§4, §8) | Agent selection: the `subagent` tool's agent ID choice, plus primary-agent routing | **Approximate** | Route choice exists (which subagent to launch); the contextual bandit over routes is not native — it must be trained externally on epoch metrics |
| Cerebrum (§4–§5) | Primary agent + configured subagents with per-agent models and system prompts | **Faithful** | Roles = agents; the stage × lens lattice is directly expressible as named subagents |

### E.2 Role-by-role mapping (§5.3)

| Role | OpenCode instantiation | Verdict | Notes |
|---|---|---|---|
| **Driver** | Primary agent, build/plan mode, decomposing and sequencing work | **Faithful** | The orchestration loop is Driver-shaped by design |
| **Sentinel** | Permission `deny`/`ask` rules + a review subagent instructed to refuse unsafe work | **Approximate (B12)** | Mechanical refusals are native; the *unconditional veto* is policy, and the operator (the client replying to `ask`) retains override — which is exactly the constitutional design: the operator is the only judge |
| **Spotlight** | Scoped `edit`/`read` on narrow path resources | **Faithful** | Focal salience ≈ scoped tool calls on explicit paths |
| **Cartographer** | `grep`/`glob`/`read` sweeps from project root; re-derivation polls are fresh reads of source artifacts | **Faithful** | Re-perception polls are literally re-running `read`/`grep` on sources, bypassing inherited claims |
| **Chronicle** | Session logs (persistent, append-only conversation history) | **Approximate (B11)** | Sessions record everything and are never edited, but they are per-session, not a tenanted cross-session witness with annotation rights |
| **Canon** | Skills (`SKILL.md` + references) and `AGENTS.md` instructions: distilled, decontextualized rules | **Faithful** | Skill discovery/loading is precisely doctrine distilled from episodes and applied context-free |
| **Reader** | `read` tool on focal artifacts; validated-output parsers | **Faithful** | Content decoding is the read path |
| **Surveyor** | `glob` results, directory listings, diff-stat summaries | **Approximate** | Geometry-reading exists, but as ad hoc tool output, not a distinct witnessing lens with its own claims |

### E.3 Mechanism mapping

| Mechanism (§) | OpenCode primitive | Verdict | Notes |
|---|---|---|---|
| Board/Claim flow (§6) | Session messages + tool results in the transcript | **Approximate (B11)** | Claims are messages, but no structured claim schema with provenance stamps exists natively; the §6 schema must be layered on |
| Objection loop (§6 R3) | Subagent review + parent correction round-trips | **Approximate** | Two-party exchange exists (parent ↔ subagent); the evidence-delta predicate must be layered on as tooling |
| Escalation (§6 R5) | Permission `ask` → operator decision | **Faithful** | `ask` is literally the operator queue; "allow once/always/reject" is the operator's ruling |
| Endocrine tier (§7) | *(none native)* | **Missing (provisional)** | No budget homeostat; provisional implementation is epoch instrumentation outside the substrate (scripts measuring tokens, joules, cost) |
| Bandit router (§8) | Subagent selection + config `model` per agent | **Approximate** | The routing surface exists; reward-driven weight learning is external tooling fed by epoch metrics |
| MoE guards (§8) | Load-balance-like signals: route frequency logs, per-agent invocation counts | **Approximate** | Under-use is detectable from session logs; collapse/thrash alarms must be layered on |
| Jerk reflex (§8) | *(none native)* | **Missing (provisional)** | Same gap as the LC row in E.1: provisional watchdog tooling (B13) |
| Myelination (§10) | Skills + commands: repeated behavior → `SKILL.md` → scripts; permissions `deny` retires it | **Approximate (B15)** | The promotion boundary is real and discrete (behavior → skill → script), but graded demotion is not native |
| Ledger/Chronicle (§6) | Append-only session storage (Ledger) + the reviewing agent over it (Chronicle) | **Approximate (B11)** | Immutability is native (sessions are not edited); tenancy and annotation are layered |

### E.4 What the substrate cannot yet do

Three theory-mandated behaviors have **no native OpenCode primitive** and ship only as provisional external tooling: the **jerk reflex** (dispute interrupt with mechanical inputs), the **endocrine tier** (continuous budget homeostasis), and the **bandit-trained router** (reward-learned route weights). A fourth constraint is structural rather than behavioral: the substrate runs one primary agent per session and serializes child sessions (B16), so the organism's sparse-activation envelope (§5.7) is enforced *sequentially* — concurrent cognition is approximated, not sustained. Per Law 4, each provisional implementation is itself a tenant: it pays rent, faces its falsifier on the golden set, and dies if its alarms stop distinguishing cases. When OpenCode grows a native primitive for any of these, the provisional tooling retires in its favor — the substrate is upstream, the theory does not fork it.

*Appendix E is a living registry like Appendix D: it tracks the substrate's actual capabilities at the current OpenCode version, and the Faithful / Approximate / Missing (provisional) distinction is preserved so that "the paper says so" never substitutes for "the substrate does so."*

---

*v2.2 changelog: §5.2 role-pair arithmetic corrected (9th/10th, not 10th/11th); §5.4 comprehension-pair leading lenses added; §8 jerk inputs reconciled with Q3; §7.4 threshold renamed N→V; Appendix A gains the pinned constants; §6 claim schema enumerated and Constitutional silences rewritten; §9 invariant-vs-falsifier added; revision-memo provenance retired to Appendix C; Appendix E added with deviations B11–B16.*
