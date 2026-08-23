🇬🇧 English | [🇫🇷 Version française](./Synthese-experiences-numeriques.fr.md)

# Synthesis of numerical experiments — toy models for emergent gravity

> **Document status:** exploratory numerical work synthesis, produced as a companion to the theoretical document [«Open Question: Can Gravitational Geometry Emerge from a Quantum Structure?»](./Question-ouverte-gravite-source.fr.md) and its [literature mapping](./Reflexion-ouverte-sur-la-gravite.en.md). This document does not claim to resolve any open problem in theoretical physics. It documents 28 numerical tests on toy models, with both positive and negative results, in the same methodological spirit as the source document.
> **Code:** every cited test is reproducible; the corresponding code is archived in this document or in the full project journal.

---

## 0. Methodological guardrails

- **A toy model is not a physical theory.** Nothing in this document establishes that gravity emerges from a phase-coherence mechanism — only that certain precise mathematical mechanisms do, or do not, produce certain sought-after properties in simplified models.
- **A negative result is documented on the same footing as a positive one.** Several avenues explored here failed explicitly (see §7); keeping them visible avoids repeating the same attempts.
- **No number is retained without reproducible code and a documented random seed.** A figure circulating among several AI assistants without a computational trace (see §6) is not retained as a result, however plausible it may seem.
- **Any quantity that is a candidate for universality is tested against the model's arbitrary parameters** (size, coupling, thresholds) before being presented as such.

---

## 1. Overview — current state

| Question | Status | Test(s) |
|---|---|---|
| Can a recall mechanism derived from amplitudes (not hand-postulated) produce a return to coherence after a perturbation? | 🟢 Confirmed | Test 9 |
| Can this same mechanism produce an effective energy suppression ($\rho_{\rm eff} \ll \rho_{\rm micro}$)? | 🟠 Partial, weak, and noisy | Tests 11-13 |
| Does a derived coupling width (not hand-tuned) exist, from the microscopic action? | 🟢 Yes (action curvature, Van Vleck-Morette) | Tests 14-15 |
| Does a universal scale-contraction factor $q$ exist between scales? | 🔴 No — depends on an arbitrary threshold as long as the selection criterion is not unified | Tests 17-18 |
| Does this same $q$ become stable once the selection criterion is unified with the dynamics? | 🟠 Converges in $N$ ($q\approx4.9$ at high $N$) but still depends on $K$ | Tests 19-21, independent reproduction |
| Is a geometric reconstruction (causal order, dimension) possible from the dynamics? | 🟢 Yes — Myrheim-Meyer dimension consistent with the model's known dimensionality | Test 24 (H25) |
| Does a phase-correlation distance yield a valid geometry? | 🔴 No — degenerate in this model | Test 26 |
| Does the sign of $R$ encode a causal orientation ("two symmetric cones")? | 🔴 Not confirmed — persistent asymmetry due to the model's dissipation | Test 27 |
| Does the sign of $R$ encode a topological frustration (torus)? | 🔴 No — but a real topological effect exists, on $C$, not on $R$ | Test 28 |
| Does a positive floor $R_\infty>0$ exist in the long run? | 🔴 Not demonstrated | Tests reviewed in §6 |

---

## 2. Thread 1 — Recall mechanism derived from amplitudes

**Question:** can a mechanism for returning to coherence after a perturbation be derived solely from interference between amplitudes $A_i=e^{iS(Q_i)/\hbar}$, without hand-writing a coherence gradient $\nabla_Q C$?

**Result (Test 9):** a Kuramoto-type coupling, $\dot\theta_i = \frac{K}{N}\sum_j \sin(\theta_j-\theta_i)$ — derived from $\mathrm{Im}(A_i^*A_j)$, not postulated — reproduces the return to coherence, with a gradual transition around $K_c\approx0.14$–$0.36$ (Kuramoto synchronization behavior, cf. Strogatz, *From Kuramoto to Crawford*, Physica D 143, 1 (2000)).

**Circularity precedent ruled out (Test 8):** a recall imposed directly as $\dot Q_i\propto\nabla_{Q_i}C$ "works" trivially by construction — this is not a discovery, just verification that a gradient ascent does what it's asked to do. Test 9 is the non-circular version.

---

## 3. Thread 2 — Effective energy suppression (H10a/b/c criterion)

**Question:** can this mechanism produce $0 < \rho_{\rm eff} \ll \rho_{\rm micro}$ (calculated, not tuned)?

**Result (Test 11, uniform coupling):** clear failure. $\rho_{\rm eff}/\rho_{\rm micro} = 1.000$ exactly — uniform coupling synchronizes the entire population without any sorting by energy.

**Result (Tests 12-13, energy-localized coupling):** real but modest and noisy suppression. $\rho_{\rm eff}/\rho_{\rm micro}$ drops from $1.000$ to $\approx0.4$–$0.6$ for a localization width $\sigma\in[8,15]$, with large standard deviations (up to 0.4). Nowhere near the $10^{120}$ factor required by the cosmological validation criterion (mapping document, §11/47) — expected for a toy model, but never to be presented as an approach to that factor.

**Origin of the localization width (Tests 14-15):** an attempt to derive $\sigma$ from the raw interference formula ($\cos(\theta_i-\theta_j)$) fails — the phase, wrapped modulo $2\pi$, loses metric distance information once it winds several times. The correctly derived width comes from the **curvature of the action** ($S''(Q)=2s$ for $S(Q)=sQ^2$), via the Van Vleck-Morette determinant (Van Vleck 1928; Morette 1951): $\sigma_Q = 1/\sqrt{2s}$ — a standard result of the stationary-phase approximation, not an invented parameter.

---

## 4. Thread 3 — Universality and the search for a scale factor

**Question:** does a universal contraction factor $q$ exist between successive scales?

**Result (Tests 17-18, arbitrary threshold criterion):** no. $q$ varies by a factor of 12 (from 31.6 to 2.7) depending on the angular tolerance threshold chosen to define "belongs to the coherent sector" — a construction artifact, not a physical property.

**Result (Tests 19-21, unified criterion — H24):** replacing the arbitrary threshold with a criterion derived from the same weight as the dynamics ($r_i>0.5$, local coherence order) collapses the dispersion. Clear convergence in $N$: $q=4.707\pm0.561$ ($N{=}800$) → $4.886\pm0.037$ ($N{=}1600$) → $4.908$ ($N{=}3200$, one seed). **But $q$ still depends on $K$** even at high $N$: $5.026$ ($K{=}0.3$) → $4.535$ ($K{=}0.7$), a confirmed monotonic dependence. **$q\approx4.9$ is therefore not universal** — it is a local value, reproducible for a given $K$, not a constant.

**Independent reproduction (August 23, 2026):** a multi-seed campaign exactly confirming the above values and conclusion (relative deviation ~0.12% from the original values). Recommended and retained formulation: *"q≈4.9 is a locally reproducible value for K=0.4 and N=1600; it does not support the claim that q=4.9 is universal."*

**Search for an intrinsic $K_c$ (Tests 22-23, Binder crossing):** no clean crossing identified in the tested ranges ($K\in[0.05,0.4]$ then $[0.5,2.0]$) — an inconclusive search, a resumption point rather than a result.

---

## 5. Thread 4 — Geometric reconstruction (H25, "causal cone")

**Question:** can an effective geometry (causal order, dimension) be constructed directly from the microscopic dynamics, without presupposing it?

**Method (Test 24):** causal order derived from each configuration's locking time + a derived coupling weight (no external threshold added). **Myrheim-Meyer** dimension (Myrheim 1978; Meyer 1988 — standard causal-set estimator, Bombelli-Lee-Meyer-Sorkin 1987) estimated: $d\approx1.85$, consistent with the toy model's actual dimensionality (1 spatial variable + 1 emergent time = 1+1D). Sanity check passed: the method does not fall into the pathological regime of non-geometric random orders (Kleitman & Rothschild, 1975).

**Comparison with a correlation distance (Test 26):** the independently proposed alternative method (distance $d_{ij}=-\log|K_{ij}|$ from phase correlations) fails the non-degeneracy criterion — many synchronized pairs have $d_{ij}=0$ exactly, and the estimated dimension (Grassberger-Procaccia, 0.38-0.42) is inconsistent with Myrheim-Meyer. **Only the causal-order approach is retained** going forward.

**$R$ redefined geometrically (Test 25):** an $R_{\rm causal}(t)$ = rate of formation of new causal relations (rather than $dC/dt$) shows qualitatively different behavior — a near-monotonic decay from an active regime toward saturation near zero, without random oscillation. No positive floor established, but a cleaner temporal structure than previous definitions of $R$.

**"Double cone" structure test (Test 27, user intuition):** hypothesis of a future/past symmetry (opposite cones glued at each point) — **not confirmed**. Persistent systematic asymmetry ($+4.9\pm6.2$ in the central portion, 86% of configurations with more future than past relations), attributable to the dissipative nature of the microscopic dynamics used (Kuramoto), which has a built-in arrow of time. Two readings left open: (a) a reversible dynamics would give the sought symmetry, or (b) the asymmetry itself is the source of an emergent arrow of time.

---

## 6. Thread 5 — Compact topology (torus)

**Question tested (Test 28):** does the sign of $R$ encode a "topological frustration" on a compact domain (torus)?

**Result:** the winding number (standard quantized topological invariant — XY/Kuramoto physics on a periodic lattice) does **not** correlate with the sign of $R$. However, a non-trivial topological winding ($W\neq0$) does effectively suppress global coherence $C$ ($C_{\rm mean}=0.23$ versus $0.41$ for $W\approx0$) — a real effect, but carried by $C$, not by $R$. The topological intuition contained a correct seed, misidentified in its initial formulation.

---

## 7. What is NOT established (central point of vigilance)

- No positive long-run floor $R_\infty>0$ has been demonstrated — the tests available (from an external thread, not independently reproduced in this document) explicitly conclude the opposite: $\langle R\rangle_{\rm tail}\approx0$, with positive and negative signs nearly cancelling out.
- A "torus-cone model" featuring a coupled Friedmann-type equation system ($\dot C$, $\dot H$), a critical fixed point $C_c$, and a "universal" factor $q^*$ was proposed in an exchange with Gemini. **The coupled equation system, the fixed point $C_c$, and the factor $q^*$ were never constructed or tested in this work** — the numbers they cite ($q\approx4.908$, asymmetry $+4.9$) come from two distinct tests of a different nature (Test 20: population ratio; Test 27: causal asymmetry), merged solely on the basis of a numerical coincidence at the 3rd decimal place from a single run each — not retained as a result.

  **However, the underlying geometric idea — a compact spatial domain (torus) traversed by a causal structure (cone) — does originate from this exchange with Gemini.** It was taken up and reformulated into a rigorous, non-circular test in this document (Test 28, §6): winding number on a ring, a standard topological invariant, independent of the original document's fabricated equations. The result of this test (§6) is real and retained; the Friedmann equations coupled to $C$ are not.
- No complete Lorentzian metric, no effective action containing $\sqrt{-g}R$, no $G_{\rm eff}$ or $\Lambda_{\rm eff}$ calculated (as opposed to tuned) has been obtained at this stage.
- No test on a known physical system (Newtonian limit, Schwarzschild) has been attempted — deliberately, so as not to introduce the sought answer into the model before having a validated reconstruction rule.

---

## 8. Contributions register

This work was built in dialogue with several AI assistants (Claude, ChatGPT, Perplexity, Gemini), each having contributed distinct ideas or tests. In line with the no-attribution-without-verification principle (§0), no contribution is here labeled as "validated" by an assistant unless the corresponding test is reproducible in this document.

- The amplitude-derived recall mechanism (Thread 1) and the unified selection criterion (Thread 3) were developed and tested in this work thread.
- The question of a non-circular recall term, the multi-basin structure, and the third regime (return/transition/decoherence) were explored independently in another thread, whose qualitative results (not the non-reproducible numbers) guided Test 16 and subsequent ones.
- The independent reproduction in §4 (factor $q$) confirmed, without deviation, the results and limits already established here.
- A synthesis ("torus-cone model") combining figures from distinct tests into an untested theoretical framework was identified and explicitly excluded from this document (§7).

---

*Numerical working document — open deposit, corrections and replications welcome. Source code for each test available on request or in the project's full journal.*
