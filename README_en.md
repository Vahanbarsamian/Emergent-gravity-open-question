[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22068679.svg)](https://doi.org/10.5281/zenodo.22068679)
---
## Citation

If you reference this work, please use the following citation:

> Barsamian, V. (2026). *Emergent Gravity and Spacetime Geometry from a Phase Coherence Field C(x): An Exploratory Framework and Numerical Test Program*. Zenodo. https://doi.org/10.5281/zenodo.22064401
---
🇬🇧 English | [🇫🇷 Version française](README.fr.md)
# Open Question: Can Gravitational Geometry Emerge from a Quantum Structure?

> ⚠️ **Note:** this document evolves frequently. Please refresh the page to see the latest version.
> 📎 **Companion document:** [Literature Mapping](./Reflexion-ouverte-sur-la-gravite.en.md) — contains precise references to existing literature and the quantitative validation criterion (section 11), to be consulted and edited only there.

**Document status:** personal reflection note, produced with the assistance of several language models (Claude, ChatGPT, Perplexity) from exploratory exchanges.
**Author:** Vahan
**Context:** reflection carried out in parallel with the H2C V8.4-R project (open-source hydrogen reactor), with no technical link between the two.

> **Important:** this document does not claim any discovery, any new theory, or any experimental result. It seeks to formulate a theoretical physics question precisely enough to allow it to be confronted with existing literature and to gather opinions from researchers in the field.

---

## 1. Starting point

The initial question was deliberately broad:

> **Does a physical mechanism exist that could locally compensate the gravitational effect on an object?**

Several classical avenues were explored: air ionization, Lense-Thirring-type gravitomagnetism, exotic energy distributions, dark energy, etc. Within currently established physics, none of these avenues provides a mechanism capable of producing a controllable macroscopic gravitational compensation.

This inquiry gradually led to a different, more fundamental question:

> **Could gravity itself be an emergent property of a deeper quantum structure?**

The problem is therefore no longer to immediately look for an "antigravity force," but to ask about the effective origin of gravitational geometry and of the constant $G$.

---

## 2. What is established

General relativity describes gravitation through Einstein's equations:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

where $g_{\mu\nu}$ is the spacetime metric, $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$ the Einstein tensor, $\Lambda$ the cosmological constant, $G$ the gravitational constant, $T_{\mu\nu}$ the energy-momentum tensor. The full curvature tensor is the Riemann tensor $R^{\rho}{}_{\sigma\mu\nu}$.

> **Important clarification:** $G_{\mu\nu}$ is not the full curvature tensor. It is the Einstein tensor that appears directly in Einstein's equations.

---

## 3. Why care about the origin of $G$?

General relativity describes gravity remarkably well, but it does not by itself provide a microscopic description of the origin of the constant $G$.

> **Is the gravitational constant fundamental, or could it be an effective parameter resulting from a deeper dynamics?**

This question leads notably to the concept of **induced gravity**, historically associated with the work of Andrei Sakharov.

---

## 4. The induced-gravity avenue

In the induced-gravity picture, the Einstein-Hilbert gravitational term can appear as an effective term resulting from quantum fluctuations of fields coupled to a geometry:

$$S_{\mathrm{EH}} = \frac{c^3}{16\pi G} \int d^4x \sqrt{-g}\, R$$

After integrating out quantum degrees of freedom, one can schematically obtain:

$$S_{\mathrm{eff}}[g] = \int d^4x \sqrt{-g} \left[ \frac{c^3}{16\pi G_{\mathrm{eff}}} (R - 2\Lambda_{\mathrm{eff}}) + aR^2 + bR_{\mu\nu}R^{\mu\nu} + \cdots \right]$$

The key idea is that the coefficient of the curvature term $R$ can receive a contribution from the integrated-out quantum degrees of freedom.

---

## 5. A schematic relation for $1/G_{\mathrm{eff}}$

$$\frac{1}{G_{\mathrm{eff}}} \sim \sum_i c_i N_i \Lambda_i^2$$

where $N_i$ is the number of degrees of freedom in a sector, $\Lambda_i$ a cutoff scale, $c_i$ a coefficient depending on the theory, spin, couplings, and regularization scheme. This relation is **schematic and framework-dependent** — it does not demonstrate that $G$ is directly determined by the real quantum content of the Universe.

---

## 6. What this relation does NOT allow us to claim

### 6.1 The cutoff $\Lambda$ is not necessarily a physically manipulable parameter
A cutoff scale may depend on regularization or on the model's limit of validity — it is not a physical energy that could be experimentally altered to change $G$.

### 6.2 A variation of $G$ would be strongly constrained
$G \rightarrow G(x)$ would need to remain compatible with general covariance, conservation laws, and the many observations bounding possible variations of $G$.

---

## 7. The change of perspective

Modifying $G$ is not enough to explain gravity, which is a theory of **the dynamical geometry of spacetime**. The deeper question becomes:

> **Could geometry itself emerge from more fundamental quantum degrees of freedom?**

$$\text{microscopic quantum structure} \rightarrow \text{correlations} \rightarrow \text{effective geometry} \rightarrow \text{classical gravity}$$

---

## 8. Working hypothesis

> **The classical metric $g_{\mu\nu}$ could be an emergent collective variable resulting from the organization or correlations of a set of more fundamental quantum degrees of freedom** $\hat{\Phi}_i$.

This proposal constitutes a **research hypothesis**, not an established theory.

---

## 9. The central mathematical question

$$G_{\mu\nu}(x) = \mathcal{F}_{\mu\nu}\left[\langle\hat{\Phi}_i(x)\hat{\Phi}_j(x')\rangle\right]$$

This equation is **not proposed as an established physical equation**. It represents the mathematical shape of the problem to be identified in the literature.

---

## 10. A more general formulation

$$\mathcal{Q}\left[\langle\hat{\Phi}_i\hat{\Phi}_j\rangle, \langle\hat{\Phi}_i\hat{\Phi}_j\hat{\Phi}_k\rangle, \ldots\right] \rightarrow g_{\mu\nu} \rightarrow R_{\mu\nu}, R, G_{\mu\nu}$$

> **What structure of quantum correlations could produce an effective geometry possessing the properties of relativistic spacetime?**

---

## 11. The Macroscopic Limit: Emergence of the Semi-Classical Regime and the $10^{120}$ Resolution

The decisive test of any theory of emergent gravity lies in its ability to derive — not postulate — Einstein's field equations at the macroscopic scale, while resolving the "vacuum catastrophe" ($10^{120}$). This section details the passage from the microscopic regime of sub-quantum phases to the smooth metric of General Relativity.

```
   [ Phase Micro-fluctuations at the Planck Scale ]
                 ρ_micro ~ ρ_Planck ~ 10^114 J/m³
                           │
                           ▼  ( Ensemble averaging over N >> 1 modes )
         [ Destructive Phase Filter (R < 0) ]
                           │
                           ▼  ( Condensation of the critical background C_c )
           [ Emergent Macro Density ρ_vac = V(C_c) ]
                 ρ_macro ~ 10^-6 J/m³ (Factor 10^-120)
                           │
                           ▼

[ Effective Metric & Cosmological Einstein Equation ]
G_μν[g^eff] + Λ(C_c) g_μν^eff = (8π G_eff(C) / c_loc^4) T_μν^eff
```

### 11.1 The Origin of the $10^{120}$ Gap: The Naive Summation Error
In conventional Quantum Field Theory (QFT), the vacuum energy density is computed by summing the zero-point energy ($\frac{1}{2}\hbar\omega$) of all modes up to the Planck cutoff frequency ($\omega_{\text{Planck}}$):

$$\rho_{\text{QFT}} = \int_0^{k_{\text{Planck}}} \frac{\hbar c k}{2} \frac{d^3k}{(2\pi)^3} \approx 10^{114} \text{ J/m}^3$$

This approach unrealistically assumes that all quantum modes interfere **purely constructively and in phase** at all spacetime scales.

### 11.2 Phase Decoherence and the Volume Scale Factor
In our formalism, the macroscopic spacetime is not sensitive to the raw algebraic sum of individual modes, but to the **residual coherence density** of the field $C(\mathbf{x})$.

1. **Underlying interference:** At the microscopic scale ($r \sim \ell_{\text{Planck}}$), fluctuations have highly incoherent phase distributions. Nearly all contributions ($R < 0$) cancel through immense destructive interference patterns.
2. **Meso-spatial averaging:** Integrating fluctuations over a macroscopic volume $\Omega$ obeys the law of large numbers for random phases. The scale ratio between the elementary Planck volume $v_{\text{Planck}} = \ell_{\text{Planck}}^3$ and the mesoscopic coherence volume $V_{\text{coh}}$ naturally generates the attenuation factor:

$$\rho_{\text{vac}}^{\text{macro}} = \rho_{\text{QFT}} \cdot \left( \frac{\ell_{\text{Planck}}}{L_{\text{cohérence}}} \right)^4 \approx 10^{-120} \cdot \rho_{\text{QFT}}$$

The $10^{120}$ gap is therefore not a constant to be artificially tuned: it is the **dimensionless scale ratio** between the maximal Planck-level excitation and the stationary background level of the critical vacuum $C_c$.

### 11.3 Emergence of the Scalar $C(\mathbf{x})$ and of the Metric
When the number of degrees of freedom $N$ becomes macroscopic ($N \gg 1$), the ensemble statistical average operator $\langle \cdot \rangle_{\Omega}$ gives rise to the continuous field:

$$C(\mathbf{x}) \equiv \langle |\Psi(\mathbf{x})|^2 \rangle_{\Omega}$$

The classical metric $g_{\mu\nu}^{\text{eff}}$ then becomes the substrate's response tensor to variations of this averaged field:

$$g_{\mu\nu}^{\text{eff}}(\mathbf{x}) = \eta_{\mu\nu} + f\left( \frac{\nabla_\mu C(\mathbf{x}) \nabla_\nu C(\mathbf{x})}{C_c} \right)$$

### 11.4 Deriving Einstein's Equation
Applying the principle of least action to the effective action $S_{\text{eff}} = \int \mathcal{L}(C, g^{\text{eff}}) \sqrt{|g^{\text{eff}}|} \, d^4x$ gives rise to the macroscopic field equations:

$$G_{\mu\nu}\left[g^{\text{eff}}\right] + \Lambda(C_c) g_{\mu\nu}^{\text{eff}} = \frac{8\pi G_{\text{eff}}(C)}{c_{\text{loc}}^2(C)^2} T_{\mu\nu}^{\text{eff}}$$

Where the observed cosmological constant $\Lambda(C_c) \propto V(C_c) \sim 10^{-52} \text{ m}^{-2}$ follows directly from the critical vacuum energy *after* destructive phase cancellation, rather than from the raw Planckian sum.

### Conclusion of Section 11
The passage from micro-quantum dynamics to the macroscopic metric **suggests an avenue** for the paradox of modern cosmology: the $10^{120}$ would not represent missing matter or fine-tuning, but the statistical ratio between the maximal local fluctuation and the average condensed state of the coherence field $C(\mathbf{x})$. **This mechanism remains an untested conceptual framework at this stage** — the numerical tests available (see the [synthesis document](./Synthese-experiences-numeriques.en.md), §3) show a real but modest effective energy suppression (factor ~2-3×, not $10^{120}$) in a toy model considerably simpler than the one described here, against the rigorous quantitative validation criterion detailed in the companion document (§11/47 of the mapping document): no candidate mechanism satisfies it to date, including this one.

---

## 12. Why the question goes beyond a simple theory of variable $G$

$$\text{quantum correlations} \rightarrow \text{geometry} \rightarrow G_{\mu\nu} \rightarrow \text{gravity}$$

$G$ would be an **effective parameter of the emergent geometry**, rather than the starting point of the theory.

---

## 13. Theoretical obstacles to examine

| Obstacle | Description |
|---|---|
| **13.1 General covariance** | $G_{\mu\nu} = \mathcal{F}_{\mu\nu}[\text{correlations}]$ must respect general covariance. |
| **13.2 Bianchi identities** | $\nabla^\mu G_{\mu\nu} = 0$ must appear at the macroscopic level. |
| **13.3 Energy-momentum conservation** | $\nabla^\mu T_{\mu\nu} = 0$ must generalize if $G_{\mathrm{eff}}$/$\Lambda_{\mathrm{eff}}$ become dynamical. |
| **13.4 Emergence of the metric** | One must explain how $g_{\mu\nu}$ itself emerges from the fundamental degrees of freedom. |
| **13.5 Dynamics of geometry** | One must explain the emergence of the $\sqrt{-g}R$ term with the correct coefficient. |
| **13.6 Definition of the quantum vacuum** | Specify which quantum state and correlations are physically relevant. |
| **13.7 Locality / non-locality** | Understand how a local macroscopic geometry emerges from a possibly non-local microscopic description. |
| **13.8 Universality of gravitation** | Explain why the coupling remains universal despite the diversity of microscopic degrees of freedom. |

---

## 14. The problem of the spacetime "mesh"

Early intuitions considered the geometric "mesh" of spacetime as possibly corresponding, by analogy, to a microscopic structure of the quantum vacuum — a **heuristic metaphor**, not a claim that Einstein proposed a spacetime made of a physical network of points.

> **Could the continuous geometric structure described by $g_{\mu\nu}$ be a large-scale effective description of a discrete, relational, or otherwise structured quantum substrate?**

---

## 15. The question of the cosmological constant

The hierarchy often summarized by a factor on the order of $10^{120}$ between certain microscopic estimates of vacuum energy and the observed cosmological contribution must be treated with caution — see the companion document for the rigorous treatment of this factor.

> **What if this enormous hierarchy revealed a difference between two levels of physical description?**

---

## 16. What if intermediate quantum states were hidden by the macroscopic description?

> **What if microscopic calculations described a multiplicity of degrees of freedom, states, and configurations, while effective cosmological gravitation only gives us access to a collective macroscopic description?**

An early formulation represented this transition as a relaxation, **𝒬₀ → 𝒬₁ → ⋯ → 𝒬ₛₜₐᵦₗₑ** — **Logic A**.
This representation remains relevant for comparing different physical mechanisms, but it is no longer the preferred mechanism for the fundamental emergence of the geometry studied here (see **section 18**).

---

## 17. The analogy with a computer program

$$\text{quantum micro-states} \rightarrow \text{interactions} \rightarrow \text{correlations} \rightarrow \text{collective constraints} \rightarrow \text{coherent macroscopic state}$$

This analogy should not be taken as a physical equivalence — it only serves to distinguish microscopic dynamics, intermediate states, interactions, coherence constraints, and macroscopic description.

---

## 18. Two possible logics for emergence

**Logic A — Temporal relaxation:** the system genuinely evolves in time and progressively reaches a stable configuration: **𝒬₀ → 𝒬₁ → ⋯ → 𝒬ₛₜₐᵦₗₑ**

**Logic B — Sum over configurations and stationary phase:** all configurations contribute to a global amplitude with no temporal succession:

$$\Psi \sim \int \mathcal{D}[\text{configurations}]\; e^{iS/\hbar}$$

In the semi-classical limit, contributions whose phase varies rapidly cancel out, while regions where the action is stationary contribute constructively. This is the structure adopted here as the working mathematical analogy for the emergence of $g_{\mu\nu}$.

---

## 19. Why logic B is now favored

The example of a photon reflected by a mirror illustrates this logic: all trajectories contribute to the amplitude; paths far from the classical path interfere destructively; the neighborhood of the classical path ($\delta S = 0$) interferes constructively. The observed point is therefore not the trace of a single path genuinely taken, but the dominant macroscopic result of a sum over all possibilities.

---

## 20. Stationary phase and coherence criterion

$$\delta S = 0$$

An additional intuition comes from phase-closure conditions (Bohr-Sommerfeld, $n\lambda = 2\pi r$): when phases close coherently, certain contributions are reinforced through interference.

> **Does an analogous coherence condition exist for geometric configurations, favoring certain geometries as stable quasi-classical configurations?**

This formulation remains a heuristic analogy — it does not mean that quantum gravity is a classical mechanical resonance phenomenon.

---

## 21. A path-integral-type formulation

$$\Psi[G] = \int_{\mathcal{C}(G)} \mathcal{D}\Phi\; e^{iS_{\mathrm{micro}}[\Phi]/\hbar}$$

where $\Phi$ represents the fundamental degrees of freedom, $\mathcal{C}(G)$ the set of configurations compatible with a candidate effective geometry $G$, and $S_{\mathrm{micro}}$ a microscopic action yet to be defined. This expression is a formalization goal, not an already-derived equation.

---

## 22. Technical problems associated with logic B

The measure problem (covariant $\mathcal{D}[g_{\mu\nu}]$), convergence (oscillating Lorentzian weight), the conformal factor (problematic directions of the gravitational action), renormalization (perturbative non-renormalizability of quantized GR). The gravitational path integral is a powerful formal framework, not yet a complete and calculable microscopic theory.

---

## 23. Working hypotheses H1–H10

| ID | Question |
|---|---|
| **H1** | Nature of the summed degrees of freedom — what concretely are the $\hat{\Phi}_i$? |
| **H2** | Microscopic action $S[\hat{\Phi}_i]$, without presupposing $\sqrt{-g}R$. |
| **H3** | Integration measure — which class of configurations, which symmetries are respected. |
| **H4** | Signature and convergence — Euclidean vs. Lorentzian. |
| **H5** | Stationary-phase criterion, applied to the microscopic action. |
| **H6** | Decoherence mechanism, separate from the stationary phase itself. |
| **H7** | Origin of $G_{\mathrm{eff}}$ and $\Lambda_{\mathrm{eff}}$ from microscopic parameters. |
| **H8** | Boundary conditions. |
| **H9** | Domain of validity. |
| **H10** | Distinctive and testable prediction. |

---

## 24. H6bis — Parallel spacetime configurations

Instead of considering several intermediate states of a single spacetime, one envisions a multiplicity of possible spacetime configurations or histories: $\{H_1, H_2, \ldots, H_N\}$, each associated with its own effective geometry $g_{\mu\nu}^{(i)}$ and possibly an effective proper time.

> A multiplicity of spacetime configurations in a quantum description does not automatically imply the existence of several independent classical spacetimes in the ordinary sense.

---

## 25. H6bis.1 — Decoherence of histories

$$\{H_i\} \xrightarrow{\text{interferences}} \text{decoherence} \rightarrow \{H_k^{\mathrm{qc}}\}$$

A family of histories may become sufficiently decoherent from the others to be described as a quasi-classical sector — not necessarily a single history that "wins."

---

## 26. H6bis.2 — The soap-bubble analogy

$$\{B_1, B_2, \ldots\} \xrightarrow{\text{interactions}} \text{coalescence} \rightarrow B_{\mathrm{collective}}$$

For bubbles, the mechanism (surface tension) is physical and known. For the quantum problem, the sought mechanism is different (interference → stationary phase → decoherence). The analogy only concerns the conceptual transition: multiplicity → collective organization → macroscopic description.

---

## 27. H6bis.3 — Bubbles as a heuristic representation of spacetime configurations

> **Could the spacetime geometry we observe be the dominant quasi-classical sector arising from a multiplicity of possible quantum spacetime configurations?**

This formulation does not claim to demonstrate that several classical spacetimes really exist — it proposes to determine whether a quantum theory of gravitation can give mathematical meaning to this multiplicity.

---

## 28. H6bis.4 — The parallel with the photon and the mirror

All trajectories contribute to the amplitude; contributions with rapidly varying phase cancel out; near the classical path ($\delta S = 0$), contributions reinforce each other. The macroscopically observed point is not the manifestation of a single microscopic path actually taken, but of the region where contributions interfere constructively. The parallel with bubbles and with histories is structural, not literal.

---

## 29. H6bis.5 — A more precise formulation of "constructed reality"

It is more rigorous to speak of a **configuration or family of configurations whose constructive contribution and collective coherence dominate in the macroscopic limit considered**, rather than a configuration that would "absorb" the others.

---

## 30. H6bis.6 — Temporalities internal to histories

If $H_i \to g_{\mu\nu}^{(i)}$, then the associated proper time $\tau_i$ is determined by this geometry.

> **Could the time we observe be the proper time internal to the quasi-classical history within which our macroscopic description is defined?**

This link remains to be constructed mathematically.

---

## 31. H6bis.7 — Unified formulation of H6

$$\text{quantum spacetime configurations} \rightarrow \text{interferences} \rightarrow \text{stationary phase} \rightarrow \text{decoherence} \rightarrow \text{quasi-classical histories} \rightarrow (g_{\mu\nu}, \tau_{\mathrm{eff}})$$

> **What if the macroscopic reality we observe were not a single fundamental description, but the coherent quasi-classical sector of a multiplicity of quantum spacetime configurations simultaneously contributing to the amplitude?**

This formulation constitutes a research hypothesis, not an established interpretation.

---

## 32. Microscopic energy and effective gravitation

$$\rho_{\mathrm{micro}} \gg \rho_{\mathrm{eff}}$$

without assuming that microscopic energy "disappears."

$$\{\text{quantum states}, \text{correlations}, \text{histories}\} \to T_{\mu\nu}^{\mathrm{eff}} \to g_{\mu\nu}$$

---

## 33. The possible link with the cosmological constant

> **Could the cosmologically observed value of $\Lambda$ be an emergent property of a collective sector of quantum configurations rather than a simple sum of the zero-point energies of all fields?**

---

## 34. A distinction between three levels of description
Microscopic level ($\hat\Phi_i$) → quantum level of configurations/histories ($H_i$) → emergent classical level ($g_{\mu\nu}$, $\tau_{\mathrm{eff}}$, $G_{\mathrm{eff}}$, $\Lambda_{\mathrm{eff}}$). This separation avoids confusing fundamental degrees of freedom, possible configurations, and effective macroscopic variables.

---

## 35. Time, history, and geometry

If $H_i \to (g_{\mu\nu}^{(i)}, \tau_{\mathrm{eff}}^{(i)})$, geometry and time become two linked aspects of the same effective description. The possibility of a common mechanism remains an open question.

---

## 36. A hypothesis on the separation of timescales

$$\tau_{\mathrm{micro}} \ll \tau_{\mathrm{corr}} \ll \tau_{\mathrm{macro}}$$

Heuristic relation, which does not imply the existence of several fundamental times.

---

## 37. The possible role of the Casimir effect

$$\Delta E_{\mathrm{Casimir}} = E_{\text{constrained}} - E_{\text{reference}}$$

The Casimir effect should not be interpreted as a direct measurement of the absolute vacuum energy. This is not about proposing a "Casimir cosmological constant," but about asking: **does gravitation couple to an absolute energy, or could it respond to an effective quantity arising from differences between states or configurations?**

---

## 38. A geometric coherence constraint

$$\nabla^\mu G_{\mu\nu} = 0 \quad (\text{Bianchi identities})$$

An emergent theory must explain how this geometric coherence appears at the macroscopic scale. The analogy with a "cosmic compiler" is purely heuristic.

---

## 39. A general formulation of the dynamics sought

$$\text{quantum degrees of freedom} \rightarrow \text{configurations/histories} \rightarrow \text{correlations} \rightarrow \text{interferences} \rightarrow \text{stationary phase} \rightarrow \text{decoherence} \rightarrow \text{quasi-classical sector} \rightarrow (g_{\mu\nu}, \tau_{\mathrm{eff}}, G_{\mathrm{eff}}, \Lambda_{\mathrm{eff}})$$

This chain constitutes a conceptual architecture, not an established theory.

---

## 40. Open question on effective mass

$$m_{\mathrm{eff}} = \frac{E}{c_{\mathrm{loc}}^2}$$

Dimensionally consistent relation, physically non-trivial only if $c_{\mathrm{loc}}$ is an effective propagation speed derived from a microscopic dynamics.

> **Could the same quantum substrate that might produce geometry also produce inertia or effective mass?**

No common mechanism of this form is established here. *(See the companion document for the historical caution — Wheeler, geometrodynamics, 1955 — associated with this ambition.)*

---

## 41. What would need to be shown to turn the hypothesis into a theory

Define the fundamental degrees of freedom and their state space; define their dynamics and the relevant correlations; define the summed object and the integration measure; establish a stationary-phase criterion; show how decoherence produces quasi-classical histories; show how $g_{\mu\nu}$ and effective time emerge; determine whether an effective mass can arise; derive an effective action recovering $\sqrt{-g}R$; determine $G_{\mathrm{eff}}$ and $\Lambda_{\mathrm{eff}}$; recover Einstein's equations; reproduce known observations; produce a falsifiable prediction.

Without these steps, the idea remains a **heuristic hypothesis**.

---

## 42. Open question to the scientific community

Question submitted to researchers in quantum gravity, QFT in curved spacetime, induced and emergent gravity, holography, quantum information and gravity, renormalization, non-commutative geometry, emergent spacetime, and out-of-equilibrium systems:

> **Does a mathematical construction exist in the literature where the effective gravitational geometry is explicitly derived from a structure of quantum correlations, amplitudes, and possibly a sum over histories, whose macroscopic limit reproduces Einstein's equations?**
>
> **Does a mechanism exist for passing from a multiplicity of quantum configurations to a coherent quasi-classical sector whose effective parameters are calculated rather than postulated?**

(19 detailed technical sub-questions — exact mathematical formulation, degrees of freedom, correlations, measure, decoherence, emergence of the metric, of time, of mass, of $G_{\text{eff}}$, of $\Lambda_{\text{eff}}$, hypotheses, limits, locality, covariance, energy-momentum consistency, the $10^{120}$ hierarchy, distinctive prediction.)

If no construction satisfying these criteria exists: **what known structural obstacle prevents such a construction?**

---

## 43. What this research does NOT claim to demonstrate

That spacetime is made of "quantum vacuum points"; that several independent classical spacetimes really exist; that $G$ is necessarily emergent; that the $10^{120}$ orders of magnitude represent physical stabilization steps; that coarse-graining already explains this hierarchy; that Casimir is responsible for the cosmological constant; that several independent fundamental times exist; that microscopic time "flows faster"; that the stationary phase alone selects a single classical reality; that decoherence proves an emergent geometry; that mass is necessarily emergent; that the quantum vacuum allows control of gravity; that a new theory of quantum gravity has been discovered; that an antigravity or propulsion application follows from it.

This is purely a **theoretical research question**.

---

## 44. Five related but distinct problems

| Level | Question |
|---|---|
| **Geometry** | How could $g_{\mu\nu}$ emerge? |
| **Gravitation** | How could $G_{\mathrm{eff}}$ arise? |
| **Cosmology** | Why is $\Lambda_{\mathrm{eff}}$ so small? |
| **Time** | Could proper time itself be emergent? |
| **Inertia** | Could an effective mass emerge from the same substrate? |

These problems may be linked in a deeper theory, but no automatic implication is assumed.

---

## 45. Purpose of this repository

Document the path of the reflection; distinguish established results from speculative hypotheses; identify existing work; avoid rediscovering an already-published construction; gather criticism allowing the hypothesis to be falsified or reformulated; determine whether the problem is already solved, partially addressed, or genuinely open.

---

## 46. Methodological position

> **Hypothesis ≠ interpretation ≠ result ≠ established theory.**

The assistance of language models was used to explore the literature, reformulate hypotheses, and identify mathematical avenues. It does not constitute scientific validation. Any significant claim must be checked against original publications and the opinion of competent researchers.

---
---

## 47. Mathematical formalization and toy model: consolidated status

This section gathers the phenomenological formalism and the numerical results obtained after successive campaigns. It should be read as a **falsifiable research program**, not as an established derivation of general relativity.

### 47.1 Coherence field and fundamental variables

We consider a scalar phase-coherence field:

$$C(\mathbf{x})\in[0,1].$$

In collective-dynamics models, it is represented by the order parameter:

$$Z=\frac{1}{N}\sum_{j=1}^{N}e^{i\theta_j},\qquad C=|Z|^2.$$

This definition has an important property: $C$ is invariant under a global phase rotation, unlike $R=\mathrm{Re}(Z)$. Earlier campaigns therefore led to retaining $C$ as a robust coherence observable.

The structural framework remains fixed at **3+1 dimensions**:

$$d=3\quad\text{spatial dimensions},\qquad D=d+1=4.$$

### 47.2 Potential equation and regularized profile

The working model retains a modified Poisson-type equation:

$$\nabla^2\Phi(\mathbf{x})=\frac{4\pi c^2}{L_0^2}\left[C(\mathbf{x})-C_c\right].$$

The regularized reference profile used is:

$$C(r)=C_c+\frac{r_g^2}{r^2+r_g^2}(C_{\max}-C_c),$$

with $C_{\max}=1$ and $r_g=2GM/c^2$.

This profile has a useful property:

$$C(0)=C_{\max},\qquad C'(0)=0.$$

But it must not be directly identified with a mass density: its asymptotic $1/r^2$ behavior would make the integrated mass diverge. The reconstruction must therefore remain separate:

$$C(r)\rightarrow\rho(r)\rightarrow m(r)\rightarrow g(r)\rightarrow g_{\mu\nu}^{\mathrm{eff}}.$$

### 47.3 Collective dynamics tested

The weighted Kuramoto dynamics used in Tests 12–13 and in the Test 51 campaign is:

$$E_i=Q_i^2,$$

$$w_{ij}=\exp\left[-\frac{(E_i-E_j)^2}{2\sigma^2}\right],$$

$$\dot\theta_i=\frac{K}{N}\sum_jw_{ij}\sin(\theta_j-\theta_i).$$

The order parameter is then:

$$C=|Z|^2,\qquad Z=\frac1N\sum_j e^{i\theta_j}.$$

This dynamics allows an incoherent state ($C\sim1/N$) to be distinguished from a collectively coherent state ($C\gg1/N$).

For independent uniform phases:

$$\mathbb E[C]=\frac1N,$$

which provides an essential reference for interpreting small $C$ values at finite size.

### 47.4 Status of $R$

The sign of $R=\mathrm{Re}(Z)$ is not invariant under a global phase rotation. Earlier tests therefore ruled out its use as an absolute coherence criterion or as proof of a causal orientation.

The following specific hypotheses were not confirmed in their original form:

- $R<0$ as a necessarily destructive sector;
- $R$ as a direct code for a future/past causal cone;
- correlation between the sign of $R$ and a topological winding.

An alternative causal indicator $R_{\mathrm{causal}}$ remains a promising avenue, but with no demonstrated positive floor.

---

### 47.5 Deriving $K$: from a postulated parameter to a derived coupling constant

The dynamics described in 47.3 uses a coupling constant $K$ which, until now, was an external hand-tuned parameter. Two results establish that it can be reformulated, and then partly derived.

**Step 1 — $K$ is already, structurally, a coupling constant.** The dynamics $\dot\theta_i=\frac{K}{N}\sum_j w_{ij}\sin(\theta_j-\theta_i)$ is exactly the descending gradient flow of the potential:

$$V[\theta]=-\frac{K}{2N}\sum_{i,j}w_{ij}\cos(\theta_i-\theta_j)$$

verified numerically to machine precision ($\sim10^{-11}$) — $K$ is therefore not an arbitrarily added force, but the coupling constant of an XY-type interaction term.

**Step 2 — derivation via adiabatic elimination of a mediator field.** By coupling each phase $\theta_i$ to a complex mediator field $\psi$ (Hubbard-Stratonovich-type technique, formally analogous to Sakharov's induced gravity, §4-5):

$$\dot\psi = \mathrm{rate}\cdot(-m^2\psi+g\,\bar Z),\qquad \bar Z=\frac{1}{N}\sum_j e^{i\theta_j}$$

adiabatic elimination of $\psi$ (fast relaxation toward its equilibrium $\psi_{\mathrm{eq}}=(g/m^2)\bar Z$) reproduces the reduced Kuramoto dynamics with:

$$\boxed{K_{\mathrm{eff}}=\frac{g^2}{m^2}}$$

Verified numerically: the full system with an explicit mediator reproduces the reduced dynamics to within the 3rd-4th decimal, across five tested coupling values $g$ (from $g=0.05$ to $g=1.0$).

**Scope and limitation.** This is the first non-circular derivation of a parameter of this model, rather than a tuning — but $g$ (coupling to the mediator) and $m$ (mediator mass) remain themselves undeived external parameters. The problem is pushed back one level, not resolved.

> ⚠️ **Note on test numbering.** Several independent work threads (this one, and the companion numerical journal) each have their own "Test N" numbering, which do not coincide term for term — for example, "Test 43" in section 48.4 below (radii $R_{\mathrm{trans}}$, $R_{\mathrm{gentle}}$) is not the same calculation as "Test 43" in the [numerical experiments journal](./Journal-experiences-numeriques.en.md) (exponent search on the radial solution). Refer to each test's content, not just its number, in case of doubt.

---

## 48. Regularized geometry and recovery of the Newtonian limit

### 48.1 Why the global $4/3$ was abandoned

Early versions used a global scaling of the type $r\sim N^{4/3}$. Tests 39–40 showed that this unbounded growth cannot be maintained to infinity: it destroys the Newtonian limit.

The physical constraint therefore becomes:

$$\text{central/intermediate regime: correction possible}$$

$$\text{Large } r:\qquad |g(r)| \propto \frac{1}{r^2}.$$

### 48.2 Test 41 — success of the localized correction

Test 41 corrected a sign error: $g(r)$ is negative by convention, while $M_{\mathrm{tot}}>0$. The correct comparison is therefore between the magnitudes $|g(r)|r^2$.

Reported values:

| $r$ (kpc) | $|g(r)|r^2$ |
|---:|---:|
| 15 | 1183.9 |
| 20 | 1183.0 |
| 30 | 1182.0 |

The average is about $1183$, with a coefficient of variation of about $0.07\%$, and the relative deviation from $M_{\mathrm{tot}}=1196.7$ is about $1.15\%$.

The result establishes, in this toy model, a very clean recovery of the law:

$$|g(r)|r^2\rightarrow\mathrm{constant}.$$

**Status: 🟢 non-regression numerical result in the toy model.** It does not constitute an observational validation of emergent gravity.

### 48.3 Test 42 — robustness of the localized correction

A $4\times4$ grid was explored by independently varying $\sigma$ and $k_0$ between $0.5$ and $2$ times their nominal values.

Reported result: **16/16 robust points**, with $|g|r^2$ nearly constant and a relative deviation from $M_{\mathrm{tot}}$ on the order of $0.1\%$ in the reproducible toy model.

The methodological conclusion is important: recovery of the asymptote is not solely tied to a one-off tuning of the tested parameters.

**Status: 🟢 numerical robustness of the localization mechanism in the tested model.**

### 48.4 Tests 43–44 — torus–cone integration and dynamic exponent

The working geometry was then organized into three regimes:

1. central/torus region;
2. transition/cone region;
3. gentle slope and asymptotic return.

The radii used in Test 43 were:

$$R_{\mathrm{trans}}=0.61\ \mathrm{kpc},\qquad R_{\mathrm{gentle}}=1.31\ \mathrm{kpc}.$$

The ratio $\simeq2.15$ between these radii remains a geometric input and has not yet been derived.

Test 43 preserves the Newtonian asymptote with a coefficient of variation of about $0.005\%$ and a relative deviation of about $-0.004\%$ in the reported calculation.

To make $4/3$ compatible with this constraint, a dynamic interpolation was tested:

$$s(r)=\frac{C(r)-C_c}{C_{\max}-C_c},
\qquad
\alpha(s)=1+\frac{s}{3}.$$

Thus:

$$s\rightarrow0\Rightarrow\alpha\rightarrow1,$$

$$s\rightarrow1\Rightarrow\alpha\rightarrow\frac43.$$

In Test 44, the cone zone gave approximately $1.21\lesssim\alpha\lesssim1.28$, with an average close to $1.25$. The value $4/3$ was therefore not reached everywhere: it appears as a **saturation limit**, not as a global constant imposed at all radii.

**Status: 🟢 numerical consistency of the tested matching; 🟡 fundamental origin of $4/3$ still open.**

### 48.5 Candidate form of localized correction

A working expression compatible with the previous results is:

$$\rho_{\mathrm{eff}}(r)=\rho_b(r)\left[1+k_0\left(\frac{r}{r_t}\right)^{4/3}\mathrm{sech}^2\left(\frac{r-r_t}{\sigma}\right)\right].$$

This expression is not yet a fundamental law. It only encodes three numerical constraints:

- weak correction outside the transition zone;
- $4/3$ scaling in the active zone;
- extinction of the correction at large $r$.

---

## 49. Search for the dimensional origin of $4/3$, $3/4$, and $1/4$

The model is now explicitly fixed at $3+1$ dimensions: $d=3$.

A simple dimensional family gives:

$$\alpha=\frac{d+1}{d}=\frac43,$$

$$\beta=\frac d{d+1}=\frac34,$$

with:

$$\alpha\beta=1.$$

Another candidate relation gives:

$$\eta=\frac1{d+1}=\frac14.$$

With the definition used for the angle:

$$\theta=2\arcsin\left(\frac{C_c}{1-C_c}\right),$$

the value $C_c=0.2=1/5$ yields exactly:

$$\frac{C_c}{1-C_c}=\frac14,$$

then:

$$\theta=2\arcsin\left(\frac14\right)\approx28.955^\circ.$$

One can also write the candidate relation:

$$C_c=\frac1{d+2}.$$

For $d=3$:

$$C_c=\frac15,$$

and therefore:

$$\frac{C_c}{1-C_c}=\frac1{d+1}=\frac14.$$

### 49.1 What is actually demonstrated

The numerical identities are exact:

$$0.2=\frac15,\qquad\frac{0.2}{0.8}=\frac14,$$

$$2\arcsin(1/4)\approx28.955^\circ,$$

$$\frac{d+1}{d}=\frac43,\qquad\frac d{d+1}=\frac34\quad(d=3).$$

### 49.2 What is not derived

Tests 49–50 showed that the minimal dynamics of $C$ and the simple feedback loops tested do not spontaneously select $C_c=1/5$.

With:

$$Z\Box C-V'(C)=0,$$

a quadratic potential relaxes to whatever value was placed in the potential. Likewise, the tested feedback loops of the type $\sigma(C)$ produced markedly more coherent attractors, roughly $0.72$ to $0.91$, with no attractor in the window $[0.16;0.24]$.

**Conclusion:** $C_c=1/5$ remains an **input of the gravitational model**, while $4/3$, $3/4$, and $1/4$ form an elegant and consistent dimensional structure **conditional on this input**. No fundamental physical derivation of $C_c=1/5$ is currently established.

---

## 50. Collective dynamics tests: from $Q_i$ to $C$

### 50.1 Computation chain

The numerical program is organized along the chain:

$$Q_i\rightarrow E_i\rightarrow\theta_i\rightarrow C,$$

with:

$$E_i=Q_i^2,$$

$$w_{ij}=\exp\left[-\frac{(E_i-E_j)^2}{2\sigma^2}\right].$$

The goal is to determine whether a collective structure produces a privileged value of $C$, or only a continuous transition between incoherence and synchronization.

### 50.2 Test 50 — blind feedback of $C$ onto $\sigma$

Two families with no targeting of $0.2$ were tested:

$$\sigma(C)=\sigma_0(1-C),$$

and

$$\sigma(C)=\frac{\sigma_0}{1+\kappa C}.$$

The reported attractors were approximately:

| Form | Parameters | $C^*$ |
|---|---|---:|
| linear | $\sigma_0=0.5$ | 0.778 |
| linear | $\sigma_0=1.0$ | 0.818 |
| linear | $\sigma_0=1.5$ | 0.913 |
| inverse | $\sigma_0=0.8,\kappa=1$ | 0.836 |
| inverse | $\sigma_0=0.8,\kappa=2$ | 0.893 |
| inverse | $\sigma_0=1.2,\kappa=1.5$ | 0.914 |
| inverse | $\sigma_0=1.0,\kappa=3$ | 0.722 |

No attractor appeared in $[0.16;0.24]$.

**Verdict: 🔴 these simple feedback loops do not select $C_c\simeq0.2$.**

### 50.3 Test 51 — blind search for a collective transition

Test 51 then abandoned all artificial feedback and directly searched for a transition in the weighted system:

$$\dot\theta_i=\frac KN\sum_jw_{ij}\sin(\theta_j-\theta_i).$$

The protocol notably uses:

$$N\in\{200,400,800,1600\},$$

a scan over $K$ and $\sigma$, several independent seeds, and a sufficiently long integration time.

The planned observables are:

$$\chi_C=N\left(\langle C^2\rangle-\langle C\rangle^2\right),$$

as well as a Binder cumulant used as a secondary indicator, and the relaxation time.

The first reported 2D scan, with $N=200,400$, $K\in\{0.5,1,1.5,2\}$, and $\sigma\in\{8,12,16,20\}$, shows:

- an incoherent regime at low $K$, with $C$ close to the $1/N$ scale;
- a continuous rise of $C$ with $K$;
- point-wise values close to $0.2$;
- no robust critical line that universally fixes $C\simeq0.2$.

For example, values close to $0.2$ appear around $C\approx0.218$ and $C\approx0.169$ for certain $(K,\sigma)$ pairs, but they shift when the parameters or $N$ change.

**Test 51 verdict:**

$$\boxed{\text{the weighted model has a synchronization transition, but does not universally select }C_{\mathrm{crit}}\approx0.2.}$$

Thus, $C=0.2$ is currently better described as a **parametric crossing point** of the model than as a fundamental attractor or critical point.

---

## 51. Physical consequences and current limits

### 51.1 What the numerical campaigns actually establish

| Element | Status |
|---|---|
| 3+1 dimensional structure | 🟢 Fixed structural hypothesis |
| $C=|Z|^2$ as a phase invariant | 🟢 Confirmed as a robust toy-model observable |
| Incoherent state $C\sim1/N$ | 🟢 Confirmed statistical reference |
| Localized correction | 🟢 Tested with Newtonian non-regression |
| Robustness of the asymptote under $\sigma,k_0$ variation | 🟢 Tested in the toy model |
| Torus–cone integration | 🟢 Numerically consistent within the tested framework |
| $\alpha(s)\to4/3$ at saturation | 🟢 Consistent dynamic formulation; fundamental origin open |
| Global $4/3$ | 🔴 Abandoned: divergence at large $r$ |
| $3/4$ | 🟡 Inverse relation consistent with $4/3$, not an independent derivation |
| $C_c=1/5$ | 🟡 Input parameter; not dynamically selected |
| $1/4$ | 🟡 Identity conditional on $C_c=1/5$; not independently derived |
| $\theta\approx28.955^\circ$ | 🟢 Mathematical consequence of $C_c=0.2$ in the current formula |
| $E=mc^2$ | 🔴 No independent validation; any definition of $m$ via $c^2$ would be circular |
| $c_{\mathrm{eff}}\approx\sqrt2$ | 🟡 To be audited separately; no fundamental origin established here |
| Emergent spatial $r$ | 🔴 Not derived from correlations |
| $D_{\mathrm{eff}}=3/4$ or $4/3$ as an emergent geometric dimension | 🔴 Not established |
| Quantitative resolution of $10^{120}$ | 🔴 Not obtained; the tested toy models give a much smaller suppression |
| Derivation of Einstein's equations | 🔴 Not obtained |

### 51.2 The essential point on singularities

The regularized profile shows that it is mathematically possible to construct a source whose density remains finite at the center and whose total mass converges to $M$ at large distance. A reference metric of the Hayward type, for example, has:

$$m(r)=M\frac{r^3}{r^3+a^3},$$

and asymptotically recovers the Schwarzschild form.

This demonstrates a **regularization property**, not that the field $C$ actually generates this geometric mass.

### 51.3 The essential point on antigravitation

In the current version, the candidate tensor is quadratic in gradients of $C$, and the bound $C\le1$ prevents a trivial extrapolation beyond saturation. This excludes certain repulsive behaviors **in this particular model**, under its hypotheses.

This is not a proof that antigravitation is impossible in any physical theory.

### 51.4 Proper time and emergent time

The question remains open: if a quasi-classical history $H_i$ has a metric $g_{\mu\nu}^{(i)}$, its proper time could be defined by:

$$\tau_i=\int\sqrt{-g_{\mu\nu}^{(i)}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}}\,d\lambda.$$

The heuristic hierarchy:

$$\tau_{\mathrm{micro}}\ll\tau_{\mathrm{corr}}\ll\tau_{\mathrm{macro}}$$

remains a working hypothesis, not an experimental measurement of three fundamental times.

### 51.5 Next roadmap

The next steps must remain separate and falsifiable:

1. **Audit $c_{\mathrm{eff}}$ term by term**, in particular looking for any square root already present in its definition before interpreting a result close to $\sqrt2$.
2. **Continue the correlation analysis** $\tau_{ij}$ to determine whether differentiated correlation scales really emerge.
3. Construct a distance $d_{ij}$ only if correlations produce a non-trivial structure that is not simply inherited from $E_i$.
4. Then look for an emergent radius $r$, and only then test $N(r)$ and $D_{\mathrm{eff}}(r)$.
5. Test whether the exponent observed in the transition zone is really compatible with $4/3$ without fixing it in advance.
6. Confront the corrected gravitational profile with real observational data, notably rotation curves, without ad hoc per-galaxy recalibration if the goal is predictivity.
7. Keep the question of the microscopic origin of $C_c$ separate: Test 51 closes the specific avenue "energy weighting $\rightarrow C_c=1/5$" for the tested family, but does not close all theoretical possibilities.

---

## 52. General conclusion — status of the research program

The model has crossed an important milestone: certain constructions that diverged have been abandoned, while a **localized correction** has shown a robust recovery of the Newtonian limit in the toy model.

$4/3$ is no longer used as a global law. It is now treated as a **potential transition scaling**, with an interpolation $\alpha(s)$ that tends toward $4/3$ as normalized densification tends toward saturation, $s\to1$.

The structure:

$$\frac43,\qquad\frac34,\qquad\frac14$$

is consistent with $d=3$, but its scientific value still depends on an independent derivation of $C_c=1/5$. Tests 49–51 specifically prevented this relation from being presented as already derived: the tested dynamics do not spontaneously select $1/5$.

The current scientific position can therefore be summarized as:

$$
\boxed{
\text{numerically constrained toy model}
\neq
\text{demonstrated theory of emergent gravity}
}
$$

and by the research chain:

$$
\{Q_i,\theta_i\}
\rightarrow C
\rightarrow\text{correlations}
\rightarrow d_{ij}\ ?
\rightarrow r\ ?
\rightarrow N(r)
\rightarrow D_{\mathrm{eff}}(r)
\rightarrow g_{\mu\nu}^{\mathrm{eff}}
$$

with a non-negotiable constraint:

$$
|g(r)|r^2\rightarrow\mathrm{constant}
\qquad(r\rightarrow\infty).
$$

> **Working principle: we no longer choose the sought-after result; we first look for whether the dynamics produces it, then we keep both successes and failures.**

The program therefore remains open, but it is now more falsifiable, mathematically cleaner, and better separated between **inputs**, **consequences**, **numerical results**, and **fundamental hypotheses**.

---

## Conclusion

> **The gravitational geometry described by general relativity is here studied as a possible emergent macroscopic description of a collective quantum structure. Current numerical results do not demonstrate this emergence, but they already allow certain unstable constructions to be ruled out and precise constraints to be identified for the future.**

The central scientific problem remains:

> **Does a microscopic dynamics exist that is precise enough to simultaneously produce coherence $C$, an emergent metric structure, the Newtonian limit, Einstein's equations, and the observed cosmological parameters, without imposing them in advance?**

*Personal reflection and open-science document — to be confronted with the scientific literature and independent validation.*


---

## 53. Critical update — campaigns 68–70: audit of the threshold, symmetries, and falsification protocol

> **Status: major methodological update.**
> This section preserves the record of results, corrections, and open questions that arose after campaigns 68–69e. It should be read as an audit of the toy model, not as a validation of the theory of emergent gravity.

### 53.1 Starting point: the gap $v_c(\alpha=0)\simeq2.92$ versus $v_c^{\rm th}=2u=2.0$

The campaign 68–69e report gave a numerical extrapolation:

$$
v_c(\alpha=0)\simeq2.92
$$

while the analysis of the symmetric model gave:

$$
v_c^{\rm th}=2u.
$$

For $u=1$,

$$
v_c^{\rm th}=2.
$$

This gap of about $46\%$ was identified as a methodological anomaly to be resolved **before any new interpretive campaign**.

The working principle is:

$$
\boxed{
\text{numerical artifact}
\;\rightarrow\;
\text{finite }T,N\text{ limits}
\;\rightarrow\;
\text{missing physical term}
}
$$

and not the reverse.

---

### 53.2 Important correction of the energy audit in report 70A

An additional algebraic check showed that report 70A contained an error in the evaluation of the minima.

The potential is:

$$
F=
-r\sum_a|\psi_a|^2
+
u\sum_a|\psi_a|^4
+
v\sum_{a<b}|\psi_a|^2|\psi_b|^2,
\qquad r>0,\;u>0,\;v>0.
$$

#### Rank 1

For a single active component:

$$
F_1(\rho)=-r\rho^2+u\rho^4.
$$

The stationarity condition gives:

$$
-2r\rho+4u\rho^3=0
$$

and thus, for the non-trivial minimum,

$$
\boxed{\rho_1^2=\frac{r}{2u}}.
$$

The corresponding energy is:

$$
F_1
=
-r\frac{r}{2u}
+
u\frac{r^2}{4u^2}
=
-\frac{r^2}{4u}.
$$

Thus:

$$
\boxed{F_1=-\frac{r^2}{4u}}.
$$

For $r=u=1$,

$$
\boxed{F_1=-0.25}.
$$

> **Explicit correction:** $F_1$ is not equal to $0$. The quadratic and quartic terms do not cancel at the minimum; together they give $-r^2/(4u)$.

#### Symmetric rank 3

For:

$$
\psi_1=\psi_2=\psi_3=\rho,
$$

one obtains:

$$
F_3(\rho)
=
-3r\rho^2+3(u+v)\rho^4.
$$

Stationarity gives:

$$
\boxed{
\rho_3^2=\frac{r}{2(u+v)}
}.
$$

Thus:

$$
\boxed{
F_3=-\frac{3r^2}{4(u+v)}
}.
$$

For $r=u=1$ and $v=0$,

$$
\boxed{F_3=-0.75}.
$$

Report 70A gave $-0.5625$, a value consistent with an incorrect amplitude substitution.

---

### 53.3 The energy crossing is not at $v\simeq0.86$

With the correct expressions:

$$
F_1=-\frac{r^2}{4u},
\qquad
F_3=-\frac{3r^2}{4(u+v)}.
$$

The condition $F_1=F_3$ gives:

$$
\frac1u=\frac3{u+v},
$$

thus:

$$
u+v=3u
$$

and finally:

$$
\boxed{v=2u}.
$$

For $u=1$:

$$
\boxed{v_c^{\rm energy}=2}.
$$

The energy threshold and the local stability threshold therefore coincide in this symmetric model:

$$
\boxed{
v_c^{\rm energy}
=
v_c^{\rm stability}
=
2u
}.
$$

There is therefore **no** distinct thermodynamic window,

$$
0.86<v<2
$$

in this precise symmetric quartic potential, such that rank 1 would be globally favored while rank 3 remains metastable.

The alleged threshold $v\simeq0.86$ from report 70A should be classified as an **algebraic artifact**, not a second physical threshold.

---

### 53.4 General formula for $k$ active components

For $k$ components of equal amplitude $\rho$:

$$
F_k(\rho)
=
-kr\rho^2
+
\left[
ku+\frac{k(k-1)}2v
\right]\rho^4.
$$

The stationarity condition gives:

$$
\rho_k^2
=
\frac{r}
{2u+(k-1)v}.
$$

Thus:

$$
\boxed{
\rho_k
=
\sqrt{\frac{r}{2u+(k-1)v}}
}.
$$

This formula corrects an important ambiguity present in earlier versions: the amplitude itself carries a square root.

The minimum energy becomes:

$$
\boxed{
F_k^{\min}
=
-\frac{k r^2}
{2\,[2u+(k-1)v]}
}.
$$

For $k=1$:

$$
F_1^{\min}=-\frac{r^2}{4u}.
$$

For $k=3$:

$$
F_3^{\min}=-\frac{3r^2}{4(u+v)}.
$$

Comparing $F_1^{\min}=F_3^{\min}$ indeed gives back:

$$
\boxed{v=2u}.
$$

---

### 53.5 Consequence: the modal-competition mechanism remains plausible, but the interpretation must be cleaned up

The minimal model:

$$
F=
-r\sum_a|\psi_a|^2
+
u\sum_a|\psi_a|^4
+
v\sum_{a<b}|\psi_a|^2|\psi_b|^2
$$

therefore has, for $u>0$ and $r>0$, a natural threshold:

$$
\boxed{v_c=2u}.
$$

This result does not depend on a numerical tuning of the threshold.

However, it is not enough to explain why a given simulation might produce an apparent threshold around $2.9$. This question remains distinct:

$$
\boxed{
v_c^{\rm apparent}\neq v_c^{\rm theoretical}
}
$$

as long as finite-time effects, finite-size effects, the operational definition of the threshold, and any possible model reduction have not been separated out.

---

## 53.6 Formalization 70S — exact nature of the dynamics

The collective dynamics studied in Tests 9–46 is a gradient flow:

$$
\boxed{
\dot\psi_a
=
-\frac{\partial F}{\partial\psi_a^*}
}
$$

that is, in the general case:

$$
\boxed{
\dot\psi_a
=
r\psi_a
-
2u|\psi_a|^2\psi_a
-
\left(
\sum_{b\neq a}v_{ab}|\psi_b|^2
\right)\psi_a
}.
$$

### Symmetry of the potential

When the potential depends only on the moduli:

$$
F=F(|\psi_1|^2,|\psi_2|^2,|\psi_3|^2),
$$

it is invariant under:

$$
\psi_a\rightarrow e^{i\varphi_a}\psi_a,
$$

with three independent phases.

Hence:

$$
\boxed{G_F=U(1)^3}.
$$

### Symmetry of the flow

The gradient flow is then equivariant under the same action:

$$
\boxed{G_{\rm flow}=U(1)^3}.
$$

The symmetry of the potential and that of the flow must not, however, be confused with the conservation of a Noether charge.

### Polar variables

Writing:

$$
\psi_a=\sqrt{\rho_a}\,e^{i\theta_a},
$$

the flow considered here gives:

$$
\dot\rho_a=2\lambda_a(\rho)\rho_a,
$$

with $\lambda_a$ real, and:

$$
\boxed{\dot\theta_a=0}
$$

for this **specific reduced dynamics**.

The amplitudes can therefore decay to zero while the phases remain frozen.

> **Essential methodological point:** $\dot\theta_a=0$ is not a consequence of $U(1)^3$ alone. It is a consequence of the combination "phase-invariant potential + choice of gradient flow."

---

## 53.7 Do not automatically extrapolate this property to the microscopic level

The original microscopic dynamics, notably the Kuramoto-type oscillators studied elsewhere in the program, has an active phase dynamics:

$$
\dot\theta_i
=
\frac KN
\sum_j
w_{ij}
\sin(\theta_j-\theta_i).
$$

There are therefore two distinct levels:

$$
\boxed{
\text{microscopic dynamics}
\neq
\text{reduced modal dynamics}
}
$$

The property $\dot\theta_a=0$ of the reduced Landau model should not be presented as a demonstrated property of the microscopic dynamics until an explicit reduction has been derived.

This is now a priority question for 70S:

> **Is the frozen phase dynamics of the modal variables derived from the microscopic dynamics, or introduced by the phenomenological reduction?**

---

# 54. Diagnostic protocol 70A–70D

## 54.1 70A — testing the $\alpha\rightarrow0$ extrapolation

### Hypothesis tested

The $2.92$ value could stem from an inadequate linear extrapolation rather than from a genuine threshold at $\alpha=0$.

We start from the measurements:

$$
\{(\alpha_i,v_c(\alpha_i))\}_{i=1}^{M}.
$$

Compare, at minimum, two models:

$$
v_c(\alpha)=a_0+a_1\alpha
$$

and:

$$
v_c(\alpha)=b_0+b_1\alpha+b_2\alpha^2.
$$

The result to compare is respectively:

$$
v_c^{\rm lin}(0)=a_0,
\qquad
v_c^{\rm quad}(0)=b_0.
$$

### Fixed parameters

- exact dynamics;
- $N$;
- $u,r$;
- integrator;
- $dt$;
- operational definition of $v_c$;
- seeds;
- definition of $\alpha$.

### Variable parameter

Only:

$$
\alpha.
$$

### Criterion defined before the result

**Success:**

$$
|v_c^{\rm extrap}-2|
$$

decreases substantially with a non-linear model.

**Failure:**

$$
v_c^{\rm lin}(0)\simeq v_c^{\rm quad}(0)\simeq2.92
$$

with uncertainties small enough to exclude $2$.

> **Essential condition:** the raw data points $v_c(\alpha)$ must be preserved. An extrapolation must not be reconstructed from its final formula alone.

---

## 54.2 70B — temporal convergence, then size convergence

The two effects must be separated.

### 70B-1 — Time

Fix:

$$
N=N_0
$$

and vary only:

$$
T_1<T_2<T_3<T_4.
$$

Measure:

$$
v_c(T)
$$

and, where possible, the relaxation time:

$$
\tau_{\rm rel}(v).
$$

**Criterion:**

$$
v_c(T)\rightarrow2
$$

indicates a finite-time effect.

If:

$$
v_c(T)\rightarrow2.92,
$$

finite time does not explain the gap.

### 70B-2 — Size

Once $T$ is sufficiently converged:

$$
T=T_{\rm converged},
$$

vary:

$$
N=N_1,N_2,N_3,N_4.
$$

Measure:

$$
v_c(N).
$$

A possible extrapolation is:

$$
v_c(N)=v_c(\infty)+AN^{-\beta}.
$$

**Criterion:**

$$
v_c(N)\rightarrow2
$$

indicates a finite-size effect.

Otherwise, finite size does not explain the gap.

### Non-negotiable rule

Never vary $T$ and $N$ simultaneously in a test intended to causally attribute a shift of the threshold.

---

## 54.3 70C — missing term, only if 70A and 70B fail

The starting potential remains:

$$
F_0=
-r\sum_a|\psi_a|^2
+
u\sum_a|\psi_a|^4
+
v\sum_{a<b}|\psi_a|^2|\psi_b|^2.
$$

Only one additional term should be introduced at a time.

### Phase-coupled candidate

For example:

$$
F_3=
w(\psi_1\psi_2\psi_3+\mathrm{c.c.}).
$$

But this term should only be retained if the microscopic symmetries allow it.

Other couplings are possible, for example:

$$
w_{12}(\psi_1^*\psi_2+\mathrm{c.c.}),
$$

which selects a different combination of phases.

It is therefore no longer correct to present the cubic term as "the" a priori preferred missing term.

### Spatial candidate

If the $\psi_a$ variables are genuinely spatial fields, one can test:

$$
F_\nabla
=
\sum_a\kappa_a|\nabla\psi_a|^2
+
\sum_{a<b}\kappa_{ab}
\nabla\psi_a\cdot\nabla\psi_b.
$$

But this extension changes the nature of the model: it introduces spatial degrees of freedom that do not exist in the homogeneous 0D model.

### Causality criterion

An additional term is only explanatory if:

1. it is allowed by the symmetries;
2. its coefficient is measurable or microscopically derivable;
3. it is introduced before knowing its effect on $v_c$;
4. its magnitude is physically plausible;
5. it improves the prediction without arbitrary tuning.

The strong condition sought is:

$$
\boxed{
\text{micro-dynamics}
\rightarrow
\text{effective coefficient}
\rightarrow
v_c\simeq2.92
}
$$

and not:

$$
\text{choice of }w
\rightarrow
v_c\simeq2.92.
$$

---

## 54.4 70D — direct reconstruction of the effective potential

Starting from the microscopic trajectories:

$$
Q_i(t),
$$

define the modal variables $\psi_a(t)$, then estimate their stationary distribution:

$$
P(\psi_1,\psi_2,\psi_3).
$$

One can then reconstruct, under appropriate assumptions:

$$
\boxed{
F_{\rm eff}
=
-k_BT_{\rm eff}\ln P
}
$$

or, in reduced units:

$$
\boxed{
F_{\rm eff}=-\ln P+C.
}
$$

The reconstructed potential can then be compared to:

$$
F_{\rm eff}
=
-r_{\rm eff}\sum_a|\psi_a|^2
+
u_{\rm eff}\sum_a|\psi_a|^4
+
\sum_{a<b}
v_{ab}^{\rm eff}|\psi_a|^2|\psi_b|^2
+\cdots
$$

The goal is to determine whether the $v_{ab}$, the anisotropies, and any phase or gradient terms appear **in the data**, rather than being introduced to reproduce a result.

> **Caveat:** the inversion $F_{\rm eff}=-\ln P$ is interpretable as a standard thermodynamic potential only if the necessary statistical and equilibrium conditions are satisfied. For an out-of-equilibrium dynamics, it is first an effective statistical potential, not automatically a thermodynamic energy.

---

# 55. Intermediate result of independent reconstruction

An independent reconstruction attempt, using a transparent and explicit parametrization (in the absence of access to the raw data points of campaigns 68–69d), gave:

$$
v_c(\alpha=0)\approx2.118,
$$

to be compared with $v_c^{\rm apparent}\approx2.92$ and $v_c^{\rm th}=2.0$.

This is neither a confirmation of $2.92$ nor of $2.0$: it is a **partial, non-conclusive** independent reconstruction, obtained with a different operational threshold definition than that of campaigns 68–69d.

This leads to a strict rule:

$$
\boxed{
2.118\ \text{is not a validation; it is a non-reproducibility signal to be investigated.}
}
$$

The raw data and exact protocol must therefore be obtained before any conclusion about the origin of the $2.92$ value.

---

# 56. Correction of the external report 70A–70B

The external report 70A–70B had interpreted:

$$
v\simeq0.86
$$

as a distinct energy threshold, then introduced a metastability window between $0.86$ and $2.0$.

The algebraic audit shows that this interpretation is invalid for the symmetric quartic potential defined here.

The correct threshold is:

$$
\boxed{v_c=2u}.
$$

The value $0.86$ should therefore be kept in the journal only as a **historically erroneous result**, accompanied by the mathematical correction.

This distinction is important to prevent a false value from later reappearing as a "previous prediction."

---

# 57. Consolidated decision tree

```text
                  apparent v_c ≈ 2.92
                           │
                           ▼
              70A — α → 0 extrapolation
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
             → 2.0              stays ≈ 2.92
                 │                   │
          α artifact                 ▼
                              70B — convergence
                               T then N separately
                                      │
                           ┌──────────┴──────────┐
                           ▼                     ▼
                        → 2.0              stays ≈ 2.92
                           │                     │
                     finite-size effect          ▼
                                           70C — additional
                                                term
                                                 │
                                                 ▼
                                      microscopic validation
                                                 │
                                                 ▼
                                           70D — direct
                                      F_eff reconstruction
```

A step 70S must be considered **transversal and prior** to physical interpretation:

$$
\boxed{
70S:\quad
\text{precisely identify the class of dynamics}
}
$$

notably:

- gradient dynamics;
- Hamiltonian/conservative dynamics;
- out-of-equilibrium dissipative dynamics;
- Kuramoto-type microscopic dynamics;
- a modal reduction explicitly linking these levels.

---

# 58. Final scientific criterion

The program must now explicitly distinguish:

$$
\boxed{
\text{numerical reproduction}
\neq
\text{physical explanation}
}
$$

A complete predictive explanation should ideally follow the chain:

$$
\boxed{
S_{\rm micro}
\rightarrow
P(\psi)
\rightarrow
F_{\rm eff}
\rightarrow
v_{ab}^{\rm eff}
\rightarrow
v_c
\rightarrow
\gamma_2,\gamma_3
}
$$

without choosing the effective parameters specifically to reproduce the last observable.

This requirement is particularly important for the ratio:

$$
\frac{\gamma_3}{\gamma_2}\approx1.37
$$

obtained with anisotropy, since fitting several $v_{ab}$ to a single target does not by itself constitute a causal demonstration.

---

# 59. Questions remaining open after the audit

1. What is the exact operational definition of $v_c$ in campaigns 68–69e?
2. What are the raw data points $(\alpha_i,v_c(\alpha_i))$?
3. What is the sensitivity of $v_c$ to the duration $T$?
4. What is its convergence in $N$ once $T$ has converged?
5. Can the microscopic reduction to $\psi_a$ be explicitly derived?
6. Does the freezing $\dot\theta_a=0$ exist at the microscopic level, or is it created by the reduction?
7. Which phase couplings are actually allowed by the microscopic symmetries?
8. Can the coefficients $v_{ab}$ be reconstructed directly from the trajectories?
9. Are the anisotropies $v_{12}<v_{13}<v_{23}$ explicitly imposed, or do they emerge?
10. Is the homogeneous 0D model sufficient, or must a spatial structure be introduced?

---

# 60. Principle of conservation of the research thread

> **Do not erase historical errors: keep them, label them, and correct them.**

The current status should be read as follows:

- $v_c=2u$: **analytical result for the symmetric quartic potential**;
- $v\simeq0.86$: **identified algebraic artifact**;
- $v_c\simeq2.92$: **historical observation/extrapolation to be reproduced and audited**, not an established theoretical value;
- $v_c\simeq2.118$: **partial independent reconstruction**, inconclusive;
- $U(1)^3$: **symmetry of the potential and of the reduced flow** in the model considered;
- $\dot\theta_a=0$: **property of the reduced gradient flow**, not yet derived from the microscopic dynamics;
- $v_{ab}$: **effective parameters not yet microscopically derived**;
- 70A–70D: **falsification protocol**, not definitive results;
- 70S: **audit of the class of dynamics and of the micro → modal link**.

The guiding rule remains:

$$
\boxed{
\text{we no longer choose the sought result; we first look for whether the dynamics produces it.}
}
$$
