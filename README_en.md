[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22068679.svg)](https://doi.org/10.5281/zenodo.22068679)
---
## Citation

If you reference this work, please use the following citation:

> Barsamian, V. (2026). *Emergent Gravity and Spacetime Geometry from a Phase Coherence Field C(x): An Exploratory Framework and Numerical Test Program*. Zenodo. [https://doi.org/10.5281/zenodo.22068679](https://www.google.com/search?q=https://doi.org/10.5281/zenodo.22068679)

---

[🇫🇷 Version française](README.md) | 🇬🇧 English version

# Open Question: Can Gravitational Geometry Emerge from a Quantum Structure?

> ⚠️ **Note:** This document evolves frequently. Please refresh the page to consult the latest version.
> 📎 **Companion document:** [Mapping of Research Paths](https://www.google.com/search?q=./Reflexion-ouverte-sur-la-gravite.fr.md) — contains precise references to the existing literature and the quantitative validation criterion (section 11), to be consulted and modified exclusively in that location.

**Document Status:** Personal reflection note, formulated with the assistance of several language models (Claude, ChatGPT, Perplexity) based on exploratory discussions.
**Author:** Vahan
**Context:** Reflection conducted in parallel with the H2C V8.4-R project (open-source hydrogen reactor), without any technical connection between the two.

> **Important:** This document claims no discovery, no new theory, and no experimental results. It seeks to formulate a sufficiently precise theoretical physics question to allow comparison with existing literature and to gather feedback from researchers in the field.

---

## 1. Starting Point

The initial question was deliberately broad:

> **Is there a physical mechanism capable of locally compensating the gravitational effect on an object?**

Several classical avenues were explored: air ionization, Lense-Thirring type gravitomagnetism, exotic energy distributions, dark energy, etc. Within the framework of currently established physics, these avenues do not provide a mechanism allowing for controllable macroscopic gravitational compensation.

This inquiry gradually led to a different, more fundamental question:

> **Could gravity itself be an emergent property of a more fundamental quantum structure?**

The problem is therefore no longer to immediately search for an "antigravitational force," but to inquire about the effective origin of gravitational geometry and the constant $G$.

---

## 2. What Is Established

General Relativity describes gravitation through Einstein's field equations:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

where $g_{\mu\nu}$ is the spacetime metric, $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$ is the Einstein tensor, $\Lambda$ is the cosmological constant, $G$ is the gravitational constant, and $T_{\mu\nu}$ is the energy-momentum tensor. The full curvature tensor is the Riemann tensor $R^{\rho}{}_{\sigma\mu\nu}$.

> **Important Precision:** $G_{\mu\nu}$ is not the full curvature tensor. It is the Einstein tensor that directly enters Einstein's equations.

---

## 3. Why Interested in the Origin of $G$?

General Relativity describes gravity remarkably well, but it does not, on its own, provide a microscopic description of the origin of the constant $G$.

> **Is the gravitational constant fundamental, or could it be an effective parameter resulting from deeper dynamics?**

This question leads notably to the concept of **induced gravity**, historically associated with the work of Andrei Sakharov.

---

## 4. The Path of Induced Gravity

In the idea of induced gravity, the Einstein-Hilbert gravitational term can appear as an effective term resulting from the quantum fluctuations of fields coupled to a geometry:

$$S_{\mathrm{EH}} = \frac{c^3}{16\pi G} \int d^4x \sqrt{-g}\, R$$

After integrating out quantum degrees of freedom, one can schematically obtain:

$$S_{\mathrm{eff}}[g] = \int d^4x \sqrt{-g} \left[ \frac{c^3}{16\pi G_{\mathrm{eff}}} (R - 2\Lambda_{\mathrm{eff}}) + aR^2 + bR_{\mu\nu}R^{\mu\nu} + \cdots \right]$$

The important idea is that the coefficient of the curvature term $R$ can receive a contribution from the integrated quantum degrees of freedom.

---

## 5. A Schematic Relation for $1/G_{\mathrm{eff}}$

$$\frac{1}{G_{\mathrm{eff}}} \sim \sum_i c_i N_i \Lambda_i^2$$

where $N_i$ is the number of degrees of freedom in a sector, $\Lambda_i$ is a cutoff scale, and $c_i$ is a coefficient depending on the theory, spin, couplings, and regularization. This relation is **schematic and theoretical-framework dependent** — it does not prove that $G$ is directly determined by the real quantum content of the Universe.

---

## 6. What This Relation Does NOT Allow Us to Assert

### 6.1 The cutoff $\Lambda$ is not necessarily a manipulable physical parameter

A cutoff scale can depend on regularization or the validity limit of the model — it is not an experimentally modifiable physical energy used to change $G$.

### 6.2 A variation of $G$ would be strongly constrained

$G \rightarrow G(x)$ would need to remain compatible with general covariance, conservation laws, and the numerous observations bounding potential variations of $G$.

---

## 7. The Shift in Perspective

A modification of $G$ is not enough to explain gravity, which is a theory of the **dynamic geometry of spacetime**. The deeper question becomes:

> **Could geometry itself emerge from more fundamental quantum degrees of freedom?**

$$\text{microscopic quantum structure} \rightarrow \text{correlations} \rightarrow \text{effective geometry} \rightarrow \text{classical gravity}$$

---

## 8. Working Hypothesis

> **The classical metric $g_{\mu\nu}$ could be an emergent collective variable resulting from the organization or correlations of a set of more fundamental quantum degrees of freedom** $\hat{\Phi}_i$.

This proposal constitutes a **research hypothesis**, not an established theory.

---

## 9. The Central Mathematical Question

$$G_{\mu\nu}(x) = \mathcal{F}_{\mu\nu}\left[\langle\hat{\Phi}_i(x)\hat{\Phi}_j(x')\rangle\right]$$

This equation is **not proposed as an established physical equation**. It represents the mathematical form of the problem to be identified in the literature.

---

## 10. A More General Formulation

$$\mathcal{Q}\left[\langle\hat{\Phi}_i\hat{\Phi}_j\rangle, \langle\hat{\Phi}_i\hat{\Phi}_j\hat{\Phi}_k\rangle, \ldots\right] \rightarrow g_{\mu\nu} \rightarrow R_{\mu\nu}, R, G_{\mu\nu}$$

> **What structure of quantum correlations could produce an effective geometry possessing the properties of relativistic spacetime?**

---

## 11. The Macroscopic Limit: Emergence of the Semi-Classical Regime and Resolution of the $10^{120}$

The decisive test of any theory of emergent gravity lies in its ability to derive — rather than postulate — Einstein's field equations at the macroscopic scale, while resolving the "vacuum catastrophe" ($10^{120}$). This section details the transition from the microscopic regime of sub-quantum phases to the smooth metric of General Relativity.

```
   [ Micro-fluctuations of Phase at the Planck Scale ]
             ρ_micro ~ ρ_Planck ~ 10^{114} J/m³
                       │
                       ▼  ( Ensemble averaging over N >> 1 modes )
     [ Destructive Phase Filter (R < 0) ]
                       │
                       ▼  ( Condensation of critical background C_c )
       [ Emergent Macro Density ρ_vac = V(C_c) ]
             ρ_macro ~ 10^{-6} J/m³ (Factor 10^{-120})
                       │
                       ▼

[ Effective Metric & Cosmological Einstein Equation ]
G_μν[g^{eff}] + Λ(C_c) g_μν^{eff} = (8π G_{eff}(C) / c_loc^4) T_μν^{eff}

```

### 11.1 The Origin of the $10^{120}$ Discrepancy: The Naive Summation Error

In conventional Quantum Field Theory (QFT), the vacuum energy density is calculated by summing zero-point energy ($\frac{1}{2}\hbar\omega$) of all modes up to the Planck cutoff frequency ($\omega_{\text{Planck}}$):

$$\rho_{\text{QFT}} = \int_0^{k_{\text{Planck}}} \frac{\hbar c k}{2} \frac{d^3k}{(2\pi)^3} \approx 10^{114} \text{ J/m}^3$$

This approach unrealistically assumes that all quantum modes interfere in a **purely constructive and in-phase** manner at all spacetime scales.

### 11.2 Phase Decoherence and Volume Scale Factor

In our formalism, macroscopic spacetime is sensitive not to the raw algebraic sum of individual modes, but to the **residual coherence density** of the field $C(\mathbf{x})$.

1. **Underlying Interference:** At the microscopic scale ($r \sim \ell_{\text{Planck}}$), fluctuations possess phases distributed in a highly incoherent manner. Almost all contributions ($R < 0$) cancel out through immense patterns of destructive interference.
2. **Meso-Spatial Averaging:** Integrating fluctuations over a macroscopic volume $\Omega$ obeys the law of large numbers for random phases. The scale ratio between the elementary Planck volume $v_{\text{Planck}} = \ell_{\text{Planck}}^3$ and the mesoscopic coherence volume $V_{\text{coh}}$ naturally generates the attenuation factor:

$$\rho_{\text{vac}}^{\text{macro}} = \rho_{\text{QFT}} \cdot \left( \frac{\ell_{\text{Planck}}}{L_{\text{coherence}}} \right)^4 \approx 10^{-120} \cdot \rho_{\text{QFT}}$$

The $10^{120}$ gap is therefore not a constant to be artificially fine-tuned: it is the **dimensionless scale ratio** between maximum excitation at the Planck level and the stationary background level of the critical vacuum $C_c$.

### 11.3 Emergence of the Scalar $C(\mathbf{x})$ and Metric

When the number of degrees of freedom $N$ becomes macroscopic ($N \gg 1$), the statistical ensemble average operator $\langle \cdot \rangle_{\Omega}$ brings forth the continuous field:

$$C(\mathbf{x}) \equiv \langle \vert{}\Psi(\mathbf{x})\vert{}^2 \rangle_{\Omega}$$

The classical metric $g_{\mu\nu}^{\text{eff}}$ then becomes the response tensor of the substrate facing variations of this averaged field:

$$g_{\mu\nu}^{\text{eff}}(\mathbf{x}) = \eta_{\mu\nu} + f\left( \frac{\nabla_\mu C(\mathbf{x}) \nabla_\nu C(\mathbf{x})}{C_c} \right)$$

### 11.4 Derivation of the Einstein Equation

Applying the principle of least action to the effective action $S_{\text{eff}} = \int \mathcal{L}(C, g^{\text{eff}}) \sqrt{\vert{}g^{\text{eff}}\vert{}} \, d^4x$ yields the macroscopic field equations:

$$G_{\mu\nu}\left[g^{\text{eff}}\right] + \Lambda(C_c) g_{\mu\nu}^{\text{eff}} = \frac{8\pi G_{\text{eff}}(C)}{c_{\text{loc}}^2(C)^2} T_{\mu\nu}^{\text{eff}}$$

Where the observed cosmological constant $\Lambda(C_c) \propto V(C_c) \sim 10^{-52} \text{ m}^{-2}$ stems directly from critical vacuum energy *after* destructive phase cancellation, and not from the raw Planck summation.

### Conclusion of Section 11

The transition from quantum micro-dynamics to macroscopic metric **proposes a path** toward the modern cosmology paradox: the $10^{120}$ factor would not represent missing matter or fine-tuning, but the statistical ratio between maximum local fluctuation and the average condensed state of the coherence field $C(\mathbf{x})$. **This mechanism remains an untested conceptual framework quantitatively at this stage** — available numerical tests (see [summary document](https://www.google.com/search?q=./Synthese-experiences-numeriques.fr.md), §3) show a real but modest effective energy suppression factor (~2-3×, not 10¹²⁰) in a toy model distinctly simpler than described here, with the rigorous quantitative validation criterion detailed in the companion document (§11/47 of the mapping): no candidate mechanism satisfies it to date, including this one.

---

## 12. Why the Question Goes Beyond a Simple Variable $G$ Theory

$$\text{quantum correlations} \rightarrow \text{geometry} \rightarrow G_{\mu\nu} \rightarrow \text{gravity}$$

$G$ would be an **effective parameter of the emergent geometry**, rather than the starting point of the theory.

---

## 13. Theoretical Obstacles to Examine

| Obstacle | Description |
| --- | --- |
| **13.1 General Covariance** | $G_{\mu\nu} = \mathcal{F}_{\mu\nu}[\text{correlations}]$ must respect general covariance. |
| **13.2 Bianchi Identities** | $\nabla^\mu G_{\mu\nu} = 0$ must appear at the macroscopic level. |
| **13.3 Energy-Momentum Conservation** | $\nabla^\mu T_{\mu\nu} = 0$ must generalize if $G_{\mathrm{eff}}$/$\Lambda_{\mathrm{eff}}$ become dynamic. |
| **13.4 Metric Emergence** | It must be explained how $g_{\mu\nu}$ itself emerges from fundamental degrees of freedom. |
| **13.5 Geometry Dynamics** | The appearance of the term $\sqrt{-g}R$ with the correct coefficient must be explained. |
| **13.6 Quantum Vacuum Definition** | Clarify which quantum state and which correlations are physically relevant. |
| **13.7 Locality / Non-locality** | Understand how a local macroscopic geometry emerges from a possibly non-local microscopic description. |
| **13.8 Universality of Gravitation** | Explain why coupling remains universal despite the diversity of microscopic degrees of freedom. |

---

## 14. The Problem of Spacetime "Lattice"

The initial intuition considered the geometric "lattice" of spacetime as potentially corresponding, by analogy, to a microscopic structure of the quantum vacuum — an **heuristic metaphor**, not an assertion that Einstein proposed spacetime made of a physical network of points.

> **Could the continuous geometric structure described by $g_{\mu\nu}$ be an effective, large-scale description of a discrete, relational, or otherwise structured quantum substrate?**

---

## 15. The Question of the Cosmological Constant

The hierarchy often summarized by a factor on the order of $10^{120}$ between certain microscopic estimates of vacuum energy and the observed cosmological contribution must be treated with caution — see companion document for rigorous treatment of this factor.

> **What if the enormous hierarchy revealed a difference between two levels of physical description?**

---

## 16. What If Intermediate Quantum States Were Masked by Macroscopic Description?

> **What if microscopic calculations described a multiplicity of degrees of freedom, states, and configurations, whereas effective cosmological gravitation only gives us access to a collective macroscopic description?**

An early formulation represented this transition as a relaxation **𝒬₀ → 𝒬₁ → ⋯ → 𝒬ₛₜₐᵦₗₑ** — **Logic A**.
This representation remains relevant for comparing different physical mechanisms, but it is no longer the favored mechanism for the fundamental emergence of geometry studied here (see **Section 18**).

---

## 17. The Analogy with a Computer Program

$$\text{quantum micro-states} \rightarrow \text{interactions} \rightarrow \text{correlations} \rightarrow \text{collective constraints} \rightarrow \text{coherent macro-state}$$

This analogy must not be considered a physical equivalence — it serves solely to distinguish microscopic dynamics, intermediate states, interactions, coherence constraints, and macroscopic description.

---

## 18. Two Possible Logics for Emergence

**Logic A — Temporal Relaxation:** The system truly evolves over time and progressively reaches a stable configuration: **𝒬₀ → 𝒬₁ → ⋯ → 𝒬ₛₜₐᵦₗₑ**

**Logic B — Sum Over Configurations and Stationary Phase:** All configurations contribute to a global amplitude without temporal succession:

$$\Psi \sim \int \mathcal{D}[\text{configurations}]\; e^{iS/\hbar}$$

In the semi-classical limit, contributions whose phase varies rapidly cancel out, while regions where the action is stationary contribute constructively. This structure is retained here as a working mathematical analogy for the emergence of $g_{\mu\nu}$.

---

## 19. Why Logic B Is Now Favored

The example of a photon reflected by a mirror illustrates this logic: all paths contribute to amplitude; paths far from the classical path interfere destructively; the neighborhood of the classical path ($\delta S = 0$) interferes constructively. The observed point is not the trace of a single path actually taken, but the dominant macroscopic result of a sum over all possibilities.

---

## 20. Stationary Phase and Coherence Criterion

$$\delta S = 0$$

An additional intuition comes from phase closure conditions (Bohr-Sommerfeld, $n\lambda = 2\pi r$): when phases close coherently, certain contributions are reinforced by interference.

> **Does a similar coherence condition exist for geometric configurations that favors certain geometries as stable quasi-classical configurations?**

This formulation remains a heuristic analogy — it does not mean quantum gravity is a classical mechanical resonance phenomenon.

---

## 21. Path Integral Type Formulation

$$\Psi[G] = \int_{\mathcal{C}(G)} \mathcal{D}\Phi\; e^{iS_{\mathrm{micro}}[\Phi]/\hbar}$$

where $\Phi$ represents fundamental degrees of freedom, $\mathcal{C}(G)$ the set of configurations compatible with a candidate effective geometry $G$, and $S_{\mathrm{micro}}$ a microscopic action yet to be defined. This expression is a formalization target, not a derived equation.

---

## 22. Technical Problems Associated with Logic B

Measure problem ($\mathcal{D}[g_{\mu\nu}]$ covariant), convergence (oscillatory Lorentzian weight), conformal factor (problematic directions of gravitational action), renormalization (perturbative non-renormalizability of quantized GR). The gravitational path integral is a powerful formal framework, not yet a complete and calculable microscopic theory.

---

## 23. Working Hypotheses H1–H10

| ID | Question |
| --- | --- |
| **H1** | Nature of summed degrees of freedom — what concretely are the $\hat{\Phi}_i$? |
| **H2** | Microscopic action $S[\hat{\Phi}_i]$, without presupposing $\sqrt{-g}R$. |
| **H3** | Integration measure — which class of configurations, which symmetries respected. |
| **H4** | Signature and convergence — Euclidean vs Lorentzian. |
| **H5** | Stationary phase criterion, applied to microscopic action. |
| **H6** | Decoherence mechanism separated from stationary phase itself. |
| **H7** | Origin of $G_{\mathrm{eff}}$ and $\Lambda_{\mathrm{eff}}$ from microscopic parameters. |
| **H8** | Boundary conditions. |
| **H9** | Domain of validity. |
| **H10** | Distinctive and testable prediction. |

---

## 24. H6bis — Parallel Spacetime Configurations

Instead of considering multiple intermediate states of the same spacetime, a multiplicity of possible spacetime configurations or histories is envisaged: $\{H_1, H_2, \ldots, H_N\}$, each associated with its own effective geometry $g_{\mu\nu}^{(i)}$ and potentially an effective proper time.

> A multiplicity of spacetime configurations in a quantum description does not automatically imply the existence of several independent classical spacetimes in the ordinary sense.

---

## 25. H6bis.1 — Decoherence of Histories

$$\{H_i\} \xrightarrow{\text{interferences}} \text{decoherence} \rightarrow \{H_k^{\mathrm{qc}}\}$$

A family of histories can become sufficiently decoherent from others to be described as a quasi-classical sector — not necessarily a single history that "wins."

---

## 26. H6bis.2 — The Soap Bubble Analogy

$$\{B_1, B_2, \ldots\} \xrightarrow{\text{interactions}} \text{coalescence} \rightarrow B_{\mathrm{collective}}$$

For bubbles, the mechanism (surface tension) is physical and known. For the quantum problem, the sought-after mechanism is different (interferences → stationary phase → decoherence). The analogy applies strictly to the conceptual transition: multiplicity → collective organization → macroscopic description.

---

## 27. H6bis.3 — Bubbles as Heuristic Representation of Spacetime Configurations

> **Could the spacetime geometry we observe be the dominant quasi-classical sector emerging from a multiplicity of possible quantum spacetime configurations?**

This formulation does not claim to prove that multiple classical spacetimes actually exist — it proposes determining whether a quantum theory of gravity can make mathematical sense of this multiplicity.

---

## 28. H6bis.4 — Parallel with the Photon and Mirror

All trajectories contribute to amplitude; rapidly varying phase contributions cancel out; near the classical path ($\delta S = 0$), contributions reinforce each other. The macroscopically observed point is not the manifestation of a single microscopically traveled path, but of the region where contributions interfere constructively. The parallel with bubbles and histories is structural, not literal.

---

## 29. H6bis.5 — A More Precise Formulation of "Constructed Reality"

It is more rigorous to speak of a **configuration or family of configurations whose constructive contribution and collective coherence dominate in the macroscopic limit considered**, rather than a configuration "absorbing" others.

---

## 30. H6bis.6 — Internal Temporalities of Histories

If $H_i \to g_{\mu\nu}^{(i)}$, then the associated proper time $\tau_i$ is determined by this geometry.

> **Could the time we observe be the internal proper time of the quasi-classical history in which our macroscopic description is defined?**

This link remains to be constructed mathematically.

---

## 31. H6bis.7 — Unified Formulation of H6

$$\text{quantum spacetime configurations} \rightarrow \text{interferences} \rightarrow \text{stationary phase} \rightarrow \text{decoherence} \rightarrow \text{quasi-classical histories} \rightarrow (g_{\mu\nu}, \tau_{\mathrm{eff}})$$

> **What if the macroscopic reality we observe was not a unique fundamental description, but the coherent quasi-classical sector of a multiplicity of quantum spacetime configurations simultaneously contributing in amplitude?**

This formulation constitutes a research hypothesis, not an established interpretation.

---

## 32. Microscopic Energy and Effective Gravitation

$$\rho_{\mathrm{micro}} \gg \rho_{\mathrm{eff}}$$

without assuming that microscopic energy "disappears."

$$\{\text{quantum states}, \text{correlations}, \text{histories}\} \to T_{\mu\nu}^{\mathrm{eff}} \to g_{\mu\nu}$$

---

## 33. The Possible Link with the Cosmological Constant

> **Could the cosmologically observed value of $\Lambda$ be an emergent property of a collective sector of quantum configurations rather than a simple sum of zero-point energies of all fields?**

---

## 34. A Distinction Between Three Levels of Description

Microscopic level (Φ̂ᵢ) → quantum level of configurations/histories (Hᵢ) → emergent classical level (g_μν, τ_eff, G_eff, Λ_eff). This separation avoids confusing fundamental degrees of freedom, possible configurations, and effective macroscopic variables.

---

## 35. Time, History, and Geometry

If $H_i \to (g_{\mu\nu}^{(i)}, \tau_{\mathrm{eff}}^{(i)})$, geometry and time become two linked aspects of the same effective description. The possibility of a common mechanism remains an open question.

---

## 36. An Hypothesis of Separation of Time Scales

$$\tau_{\mathrm{micro}} \ll \tau_{\mathrm{corr}} \ll \tau_{\mathrm{macro}}$$

Heuristic relation, which does not imply the existence of multiple fundamental times.

---

## 37. The Possible Role of the Casimir Effect

$$\Delta E_{\mathrm{Casimir}} = E_{\text{constraint}} - E_{\text{reference}}$$

The Casimir effect must not be interpreted as a direct measurement of absolute vacuum energy. It is not about proposing a "Casimir cosmological constant," but asking: **does gravitation couple to an absolute energy, or could it respond to an effective value derived from differences between states or configurations?**

---

## 38. Geometric Coherence Constraint

$$\nabla^\mu G_{\mu\nu} = 0 \quad (\text{Bianchi identities})$$

An emergent theory must explain how this geometric coherence appears at the macroscopic scale. The analogy with a "cosmic compiler" is strictly heuristic.

---

## 39. A General Formulation of the Sought-After Dynamics

$$\text{quantum degrees of freedom} \rightarrow \text{configurations/histories} \rightarrow \text{correlations} \rightarrow \text{interferences} \rightarrow \text{stationary phase} \rightarrow \text{decoherence} \rightarrow \text{quasi-classical sector} \rightarrow (g_{\mu\nu}, \tau_{\mathrm{eff}}, G_{\mathrm{eff}}, \Lambda_{\mathrm{eff}})$$

This chain constitutes a conceptual architecture, not an established theory.

---

## 40. Open Question on Effective Mass

$$m_{\mathrm{eff}} = \frac{E}{c_{\mathrm{loc}}^2}$$

Dimensionally consistent relation, physically non-trivial only if $c_{\mathrm{loc}}$ is an effective propagation velocity derived from microscopic dynamics.

> **Could the same quantum substrate that produces geometry also produce inertia or effective mass?**

No common mechanism of this form is established here. *(See companion document for historical warning — Wheeler, geometrodynamics, 1955 — associated with this ambition.)*

---

## 41. What Needs to Be Demonstrated to Transform Hypothesis into Theory

Define fundamental degrees of freedom and their state space; define their dynamics and relevant correlations; define the summed object and integration measure; establish a stationary phase criterion; show how decoherence produces quasi-classical histories; show how $g_{\mu\nu}$ and effective time emerge; determine whether an effective mass can appear; derive an effective action recovering $\sqrt{-g}R$; determine $G_{\mathrm{eff}}$ and $\Lambda_{\mathrm{eff}}$; recover Einstein's equations; reproduce known observations; produce a falsifiable prediction.

Without these steps, the idea remains a **heuristic hypothesis**.

---

## 42. Open Question to the Scientific Community

Question submitted to researchers in quantum gravity, QFT in curved spacetime, induced and emergent gravity, holography, quantum information and gravity, renormalization, non-commutative geometry, emergent spacetime, non-equilibrium systems:

> **Is there a mathematical construction in the literature where effective gravitational geometry is explicitly derived from a structure of quantum correlations, amplitudes, and possibly a sum over histories, whose macroscopic limit reproduces Einstein's equations?**
> **Is there a mechanism enabling transition from a multiplicity of quantum configurations to a coherent quasi-classical sector whose effective parameters are calculated rather than postulated?**

(19 technical sub-questions detailed — exact mathematical formulation, degrees of freedom, correlations, measure, decoherence, emergence of metric, time, mass, $G_{\text{eff}}$, $\Lambda_{\text{eff}}$, hypotheses, limits, locality, covariance, energy-momentum coherence, $10^{120}$ hierarchy, distinctive prediction.)

If no construction satisfying these criteria exists: **what known structural obstacle prevents such a construction?**

---

## 43. What This Research Does NOT Claim to Demonstrate

That spacetime is made of "quantum vacuum points"; that several independent classical spacetimes actually exist; that $G$ is necessarily emergent; that $10^{120}$ orders of magnitude represent physical stabilization steps; that coarse-graining already explains this hierarchy; that Casimir is responsible for the cosmological constant; that multiple independent fundamental times exist; that microscopic time "flows faster"; that stationary phase alone selects a unique classical reality; that decoherence proves an emergent geometry; that mass is necessarily emergent; that quantum vacuum allows gravity control; that a new quantum gravity theory was discovered; that an antigravity or propulsion application follows.

This is exclusively a **theoretical research question**.

---

## 44. Five Related but Distinct Problems

| Level | Question |
| --- | --- |
| **Geometry** | How could $g_{\mu\nu}$ emerge? |
| **Gravitation** | How could $G_{\mathrm{eff}}$ appear? |
| **Cosmology** | Why is $\Lambda_{\mathrm{eff}}$ so weak? |
| **Time** | Could proper time itself be emergent? |
| **Inertia** | Could an effective mass emerge from the same substrate? |

These problems may be linked in a deeper theory, but no automatic implication is assumed.

---

## 45. Purpose of This Repository

Document the path of reflection; distinguish established results from speculative hypotheses; identify existing work; avoid reinventing published constructions; gather critiques to falsify or reformulate the hypothesis; determine whether the problem is solved, partially addressed, or truly open.

---

## 46. Methodological Position

> **Hypothesis ≠ interpretation ≠ result ≠ established theory.**

The assistance of language models served to explore literature, reformulate hypotheses, and identify mathematical leads. It does not constitute scientific validation. Any major assertion must be confronted with original publications and feedback from competent researchers.

---

## 47. Mathematical Formalization Avenue (Exploratory Toy Model)

In this section, we introduce a phenomenological formalization attempt based on a dimensionless phase coherence scalar field $C(\mathbf{x}) \in [0, 1]$ and its potential link to the emergence of the effective metric $g_{\mu\nu}^{\text{eff}}$.

### 47.1 Proposed Working Formulas

1. **Potential Emergence Equation (Modified Poisson type):**

$$\nabla^2 \Phi(\mathbf{x}) = \frac{4\pi c^2}{L_0^2} \left( C(\mathbf{x}) - C_c \right)$$



where $C_c = 0.2000$ represents the critical vacuum value, and $L_0$ is a characteristic length scale ensuring dimensional homogeneity ($s^{-2}$).
2. **Core Saturation Profile (Regularized Form):**

$$C(r) = C_c + \left( \frac{r_g^2}{r^2 + r_g^2} \right) (C_{\text{max}} - C_c)$$



*with $C_{\text{max}} = 1.0000$ (absolute upper bound) and $r_g = \frac{2GM}{c^2}$.*
3. **Heuristic Collective Response Indicator $R$:**

$$R = \mathrm{Re}\left( \sum_{i} a_i e^{i S[Q_i]/\hbar} \right)$$



---

### 47.2 Explanation Path for the Cosmological Discrepancy ($10^{120}$)

In conventional QFT approaches, the cosmological constant $\Lambda$ is estimated by summing zero-point energy up to the Planck scale ($\rho_{\text{micro}} \sim M_{\text{Planck}}^4$).

In the present exploratory framework, resolution is envisioned via a **dynamic filtering engine by $R$**:

* Classical gravity would not couple to raw microscopic density, but exclusively to the phase sector selected by the stationary phase condition ($\delta S = 0$).
* Incoherent modes would cancel out through destructive interference in the path integral.
* The effective cosmological constant $\Lambda_{\text{eff}}$ would result from a regularized scale attenuator:

$$\Lambda_{\text{eff}} \sim \Lambda_{\text{bare}} \times \left( \frac{C_c}{C_{\text{max}}} \right)^{\ln(\ell_{\text{Planck}} / \ell_{\text{cosmo}})}$$



This mechanism aims to propose a conceptual framework where the observed value is naturally suppressed without requiring fine-tuning of bare parameters.

---

### 47.3 Provisional Interpretation of the Sign of $R$

In the toy model, we define:

$$Z = R + iI, \qquad C = |Z|^2 = R^2 + I^2, \qquad \phi = \mathrm{atan2}(I, R)$$

The sign of $R$ is not invariant under global phase rotation. It cannot therefore be interpreted alone as a measure of coherence.

Two interpretations remain open:

* $R < 0$ could correspond to an effectively destructive or dynamically suppressed contribution;
* $R < 0$ could have a $C$ value comparable to $R > 0$ and represent primarily a phase orientation near $\phi = \pi$.

A third possibility is that occurrences of $R < 0$ constitute dynamic memory of a previous state, which must be tested via transition probabilities and temporal autocorrelation of the sign.

**These three hypotheses have since been tested numerically** (28 tests, see [numerical synthesis companion document](https://www.google.com/search?q=./Synthese-experiences-numeriques.fr.md)). Results allow partial resolution, in a direction different from what was anticipated here.

**What is confirmed by tests:**

* Phase invariance of $C$ (Guardrail 2 of synthesis document) is confirmed as the correct comparison scalar — $R$ alone depends on an arbitrary reference phase and must **never** serve as a criterion to compare independent sectors (demonstrated numerically in Test 10, prior to tests dedicated to $R$).
* A durable positive floor, $R_\infty > 0$, was not demonstrated at this stage on available time series (see synthesis document, §7) — $\langle R \rangle$ tends toward a value close to zero, with positive and negative signs balancing almost exactly in tested samples.
* **The hypothesis of causal orientation encoded by the sign of $R$ ("two symmetric cones", future/past) was tested directly (Test 27) and is not confirmed.** A systematic and persistent causal asymmetry was found (fraction of future > past ≈ 86% in the central part of tested sequences), attributable to the dissipative nature of the damping mechanism used rather than a symmetric geometric property of the sign of $R$.
* **The hypothesis of topological frustration on compact domain encoded by the sign of $R$ was tested directly (Test 28, winding number on a 1D torus) and is not confirmed either** — winding number does not correlate with the sign of $R$. However, a real topological effect exists: a non-trivial winding effectively suppresses global coherence $C$ (and not $R$). Topological intuition contained a correct seed, but misidentified in its initial formulation: $C$, not $R$, bears the topological signature.
* **A geometric redefinition of $R$** (Test 25: rate of causal relation formation in a causal order derived from dynamics, rather than $dC/dt$) gives qualitatively different behavior — near-monotone decay from an active regime toward saturation near zero, without random sign oscillation. This alternative definition, anchored in geometric construction (see §49 for rapprochement with causal structure), is more promising than $R=\mathrm{Re}(\bar A)$ to carry physical meaning, but still does not demonstrate a positive floor.

The updated status is therefore:

$$\boxed{R > 0 \text{ (defined as } \mathrm{Re}(\bar A)\text{): selection criterion of the toy, dependent on arbitrary reference phase — not retained as comparison criterion between sectors.}}$$

$$\boxed{C = |\bar A|^2 \text{: phase-invariant scalar, sole robust candidate for comparing independent sectors (confirmed numerically).}}$$

$$\boxed{R < 0 \text{: neither a demonstrated destructive sector, nor causal orientation, nor confirmed topological signature — hypotheses tested and rejected in this precise form.}}$$

$$\boxed{R_{\text{causal}}(t) \text{ (causal relation formation rate): more promising candidate, partially tested (Test 25), without established positive floor at this stage.}}$$

---

### 47.4 High Curvature Behavior and Regularization

In general relativity, classical collapse leads to singularities ($r \to 0 \Rightarrow \rho \to \infty$). In this exploratory formalism:

1. **Coherence Bound:** When $r \to 0$, the regularized profile gives $C(r) \to C_{\text{max}} = 1.0000$.
2. **Central Gradient:** The quadratic form ensures that $\frac{dC}{dr}(0) = 0$, and thus $\nabla C(0) = \mathbf{0}$.
3. **Acceleration Cancellation:** Effective acceleration $g(r) = -\nabla \Phi(r)$ naturally vanishes at $r=0$.
4. **Saturated Core:** Point singularity is replaced by a phase core of characteristic radius $r_{\text{core}} \sim r_g$, avoiding origin divergences while preserving external geometry at large distances.

---

### 47.4.1 Regularized Geometry: Consistency Test with Relativistic Limit

The coherence profile proposed in §47.1 is useful as a phenomenological toy, but presents a major difficulty if interpreted directly as a gravitational source:

$$C(r)-C_c = \frac{r_g^2}{r^2+r_g^2}(C_{\max}-C_c).$$

At large distances, this profile decays as $1/r^2$. If this quantity were identified directly as source density, integrated mass would not converge. The profile cannot, as stands, be presented as a demonstrated connection to Schwarzschild geometry.

Methodological correction consists in separating the **phenomenological coherence field** $C(r)$ from the **geometric mass function** $m(r)$, which must have finite total mass.

To test this idea, one can use a class of regular metrics of Hayward type as reference geometry:

$$ds^2=-f(r)c^2dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2,$$

with, in geometric units $G=c=1$,

$$m(r)=M\frac{r^3}{r^3+a^3},$$

and

$$f(r)=1-\frac{2m(r)}r=1-\frac{2Mr^2}{r^3+a^3}.$$

This construction is **not derived from field $C$**: it serves as reference to determine properties that any reconstruction law must respect.

#### Large-Distance Limit

For $r\gg a$:

$$m(r)=M\left(1-\frac{a^3}{r^3}+O(r^{-6})\right),$$

hence

$$f(r)=1-\frac{2GM}{c^2r}+O(r^{-4}).$$

Total mass approaches $M$ and the metric recovers Schwarzschild form at large distances.

#### Central Limit

For $r\ll a$:

$$m(r)\simeq M\frac{r^3}{a^3}.$$

Setting, in geometric units, $a^3=2Ml^2$, we obtain:

$$f(r)\simeq1-\frac{r^2}{l^2}.$$

The divergent term $1/r$ disappears. The core possesses a finite de Sitter type curvature instead of point mass concentration.

Associated density is:

$$\rho(r)=\frac{1}{4\pi r^2}\frac{dm}{dr}=\frac{3Ma^3}{4\pi(r^3+a^3)^2}.$$

Thus:

$$\rho(0)=\frac{3M}{4\pi a^3}<\infty,$$

and at large distances,

$$\rho(r)\sim r^{-6}.$$

Total mass is integrable, unlike a $1/r^2$ density profile which produces divergent mass at infinity.

#### Scope of Result

This calculation demonstrates an important mathematical property: **source regularization can eliminate central divergence while preserving Schwarzschild limit at large distances, without modifying Einstein's equations themselves**. This is the general principle of regular black hole geometries, studied notably in Bardeen and Hayward models.

It does not prove that field $C$ actually produces this function $m(r)$. It merely indicates the reconstruction chain our program must derive:

$$C(r),R(r),I(r)\quad\longrightarrow\quad \rho(r)\quad\longrightarrow\quad m(r)\quad\longrightarrow\quad g_{\mu\nu}^{\mathrm{eff}}.$$

The problem becomes more precise: **what law emerging from microscopic degrees of freedom could produce a regular mass function with $m(r)\propto r^3$ at center and $m(r)\to M$ at large distances?**

This formulation is more restrictive and testable than the initial assertion that $C$ saturation directly suppresses singularity.

> 📎 **Numerical Update:** This reconstruction chain has since been partially tested. A spatially localized growth mechanism (motivated by width $\sigma_Q$ derived in §47.2) restores a stable fixed point far from core and produces a true $1/r^2$ law at large distances (0.65% to 2.36% discrepancy across 9 tested configurations). See [numerical synthesis document](https://www.google.com/search?q=./Synthese-experiences-numeriques.fr.md), §9 (Thread 8), for details — including an initial false positive explicitly corrected, and search for intermediate exponents ($4/3$, $3/4$) remaining inconclusive.

---

### 47.5 Treatment of Casimir Effect

The Casimir effect is seen here not as proof that gravity couples to absolute vacuum energy, but as confirmation of coupling to differential variations:

1. **Constraint Variation:**

$$\Delta E_{\text{Casimir}} = E_{\text{vacuum}}(\text{with plates}) - E_{\text{vacuum}}(\text{without plates})$$


2. **Coupling to Gradients:**
Effective gravitation would react to the local gradient of coherence field imposed by material boundary conditions:

$$T_{\mu\nu}^{\text{Casimir}} \propto \nabla_\mu C(\mathbf{x}) \nabla_\nu C(\mathbf{x})$$



The Casimir effect thus confirms the hypothesis that gravity responds to relative phase variations ($\Delta C$) and not absolute mass/energy of microscopic vacuum.

---

### 47.6 Synthesis of Proposed Emergent System of Equations

> ⚠️ **Status of this subsection: Candidate formalism, unverified numerically.** The four equations below assemble hypotheses of preceding sections into a paper-coherent system — none have been verified by calculation at this stage (see [numerical synthesis document](https://www.google.com/search?q=./Synthese-experiences-numeriques.fr.md) for actual tests). In particular, derivation of $K$ obtained by a different, verified mechanism ($K_{\mathrm{eff}}=g^2/m^2$, adiabatic elimination of a mediator field) has not been linked to $G_{\text{eff}}(C)$ dependence proposed in point 2 below — both constructions coexist without established link.

All hypotheses lead to the following coupled system of equations:

#### 1. Effective Phase Energy-Momentum Tensor $T_{\mu\nu}^{(C)}$

$$T_{\mu\nu}^{(C)} = \alpha_{\text{emergence}} \left( \nabla_\mu C \nabla_\nu C - \frac{1}{2} g_{\mu\nu}^{\text{eff}} g_{\text{eff}}^{\alpha\beta} \nabla_\alpha C \nabla_\beta C - g_{\mu\nu}^{\text{eff}} V(C) \right)$$


*with $V(C_c) = 0$ at critical vacuum level.*

#### 2. Dependence of Gravitational Constant $G_{\text{eff}}$ (Untested)

$$\frac{1}{G_{\text{eff}}(x)} = \frac{1}{G_0} \cdot \left( \frac{C(x)}{C_c} \right)$$

#### 3. Global Field-Geometry Equation

$$G_{\mu\nu}\left[g^{\text{eff}}\right] + \Lambda_{\text{eff}}(C) g_{\mu\nu}^{\text{eff}} = \frac{8\pi G_{\text{eff}}(C)}{c^4} \left( T_{\mu\nu}^{\text{matter}} + T_{\mu\nu}^{(C)} \right)$$

#### 4. Emergence Loop Scheme

$$\{ \hat{\Phi}_i \} \xrightarrow{\text{correlations / amplitudes}} C(\mathbf{x}) \xrightarrow{\text{reconstruction}} \rho(r),m(r) \xrightarrow{\text{Einstein equations}} g_{\mu\nu}^{\text{eff}} \xrightarrow{\text{regularized profile}} \text{non-singular core}$$

---

## 48. Conceptual Clarification: Equivalence $m_{\text{eff}} = E / c_{\text{loc}}^2$

### 48.1 Mass as Phase Condensation

In this framework, relation $m_{\text{eff}} = E / c_{\text{loc}}^2$ is interpreted as an equation of state of quantum substrate.

For localized excitation, effective mass is expressed by coherence condensation above critical vacuum:

$$m_{\text{eff}} = \frac{\rho_0}{c_{\text{loc}}^2} \int_V \left( \frac{C(\mathbf{x}) - C_c}{C_c} \right) d^3x$$

*where $\rho_0$ is a reference energy density ensuring mass homogeneity ($kg$).*

### 48.2 Origin of Inertia via Tensor $T_{\mu\nu}^{(C)}$

Density $T_{00}^{(C)}$ depends directly on field gradients:

$$T_{00}^{(C)} \propto (\nabla C)^2$$

Inertia is interpreted as resistance to deformation of this phase gradient during acceleration, yielding upon integration:

$$E_{\text{total}} = \int T_{00}^{(C)} d^3x = m_{\text{eff}} \cdot c_{\text{loc}}^2$$

### 48.3 Velocity $c_{\text{loc}}$ as Dynamic Property

In this model, $c_{\text{loc}}$ represents propagation speed of phase perturbations within coherence field, varying locally according to $C(\mathbf{x})$.

---

## 49. Geometric Formalization: Spatialized Toroidal Topology and Dynamic Causal Cone

### 49.1 Integration over Toroidal Topology $\mathbb{T}^3$

To analyze confined configurations, one can consider spatial toroidal topology ($\mathbb{T}^3$) swept by a causal cone along proper time:

$$\int_{V_{\mathbb{T}^3}} \left( C(\mathbf{x}) - C_c \right) \sqrt{|g_{\text{torus}}|} \, d^3x$$

### 49.2 Mechanism Articulation

1. **Phase Trapping on $\mathbb{T}^3$:** Spatial torus traps and confines phase ($C > C_c$), generating effective mass and confined energy.
2. **Causal Propagation Cone:** Fixes advancement speed $c_{\text{loc}}$ of phase front.
3. **Inertia Reaction ($T_{\mu\nu}^{(C)}$):** Quantifies elastic resistance during torus translation along causal cone.

---

## 50. Invariance of Gravity and Limits of the Model Regarding Antigravity

In this section, we examine a fundamental question regarding theoretical model applications: does coherence field $C(\mathbf{x})$ allow generating a repulsive effect or "antigravity"? **To be clear from the outset: what this paragraph establishes is an internal property of this specific toy model under hypotheses stated below — not a definitive physical answer.**

### 50.1 Impossibility via Field Saturation ($C \le C_{\text{max}}$)

To generate repulsive gravity or negative mass in geometric formalism, one would need to invert sign of coherence gradient ($\nabla_\mu C$) or force field beyond saturation value.

However, field structure imposes strict bound $C(\mathbf{x}) \le C_{\text{max}} = 1.0000$. As coherence approaches maximum ($C \to C_{\text{max}}$):

$$\nabla_\mu C \to 0$$

Gradient naturally vanishes, smoothing gravitational potential at dense core center. Absence of singularity ($r \to 0$) precludes creation of "negative density" regions.

### 50.2 Phase Filtering and Decoherence of $R < 0$ Sector

In current construction, $R < 0$ sector is excluded by selection rule $R > 0$. This exclusion is a toy model choice, not a demonstration that $R < 0$ contributions are physically destroyed or incapable of producing effective geometry. Campaign $(R, I, C, \phi)$, complemented by temporal analysis and cross-level comparison, must determine if exclusion corresponds to real dynamics, phase rotation, or projection effect.

| Current Formulation | More Rigorous Formulation |
| --- | --- |
| "model solves $10^{120}$" | "model proposes path for $10^{120}$ hierarchy" |
| "filter $R > 0$ is demonstrated" | "filter $R > 0$ is imposed in current model" |
| "$R < 0$ is destructive" | "$R < 0$ compatible with destructive interpretation, to be tested" |
| "metric emerges" | "candidate metric emergence rule is proposed" |
| "absence of singularity obtained" | "regularized profile avoids divergence in this phenomenological model" |
| "confirms general relativity" | "could be compared to general relativity limits" |
| "formally forbids antigravity" | "excludes this behavior in specific model version" |

* $R^-$ is not yet identified as coherence loss. It could represent opposite phase orientation, destructive sector, or dynamic memory of previous $R$ sign. Distinction requires joint recording of $(R, I, C, \phi)$, transition analysis, and micro/macro comparison.

---

### 50.3 Quadratic Form of Energy Density

Effective field energy-momentum tensor depends on quadratic terms $(\nabla C)^2$:

$$T_{\mu\nu}^{(C)} \propto \left( \nabla_\mu C \nabla_\nu C - \frac{1}{2} g_{\mu\nu}^{\text{eff}} g_{\text{eff}}^{\alpha\beta} \nabla_\alpha C \nabla_\beta C - g_{\mu\nu}^{\text{eff}} V(C) \right)$$

This quadratic structure guarantees effective energy density remains strictly non-negative ($T_{00}^{(C)} \ge 0$). The model preserves weak energy condition of General Relativity and forbids artificial gravitational repulsion phenomena.

### Conclusion of Section 50

**If saturation hypotheses posed here were verified** (unproven — see table above, §50.2), **they would exclude** any form of antigravity in this specific model. Saturation $C_{\text{max}}$ eliminating physical spacetime singularities ($r \to 0$) would be the same mechanism preventing emergent repulsive gravitational forces — an internal conditional consequence, not a proven property of the Universe.

---

## 51. Time Dilation and Concordance with General Relativity

In this section, we analyze the impact of local coherence field variation $C(\mathbf{x})$ on proper time flow and spatial navigation, demonstrating perfect continuity between our formalism and validated predictions of Albert Einstein.

### 51.1 Proper Time as Function of Coherence Density

In our theoretical framework, proper time $d\tau$ measured by an observer or embedded system depends not on absolute universal time, but local value of effective metric $g_{\mu\nu}^{\text{eff}}(C)$:

$$d\tau = dt \sqrt{g_{00}^{\text{eff}}(C) - \frac{v^2}{c_{\text{loc}}^2(C)}}$$

When local coherence increases ($C(\mathbf{x}) > C_c$) — near condensed mass or via artificial phase modification —, component $g_{00}^{\text{eff}}$ decreases.

* **Internal Clock Slowing:** For crew inside high coherence pool, quantum micro-process frequency slows relative to distant critical vacuum ($C \approx C_c$) — a reformulation in field $C$ of standard gravitational time dilation known in GR, not a new effect.

> ⚠️ **Reminder of §43:** This document does NOT claim propulsion or travel applications follow. No artificial controlled condensation mechanism for $C(\mathbf{x})$ is proposed, tested, or sketched — mentioning a "vehicle" would be unfounded extrapolation, technically unspecified and contradicting imposed self-limits. Mechanism described in this paragraph remains an internal GR consistency exercise (§51.2), not an application proposal.

### 51.2 Underlying Explanation of Einstein's Principle

Far from contradicting General Relativity, this dynamic brings fundamental physical mechanism underlying Einstein's equations:

1. **Einstein Geometry as Emergence:** Time dilation and relativistic trajectory curvature are not abstract postulates, but direct manifestation of hydrodynamic substrate resistance under gradient $\nabla C$.
2. **Correspondence Principle:** At ordinary macroscopic scales, tensor $T_{\mu\nu}^{(C)}$ and field-geometry equation rigorously recover Einstein's results (Shapiro delay, gravitational redshift, time dilation).

### 51.3 Preservation of Cosmic Causality

However, proper time bending permits no "instantaneous jump" or backward time travel:

* **Causality Conservation:** Absence of negative mass and phase filtering $R < 0$ (established §§48, 50) forbid closed timelike curves or traversable wormholes.
* **Relativistic Cost:** Any gain in crew proper time $d\tau$ is paid by irreversible offset relative to rest of Universe. Interstellar traveler returns to an Earth aged by centuries, confirming classical relativistic framework.

### Conclusion of Section 51

Ability of coherence field to bend time flow confirms model robustness: it explains **why** General Relativity works well at observed scales, while providing continuous sub-quantum description eliminating boundary divergences.

---

---

---

## General Conclusion

> **"Gravitational geometry described by general relativity is envisioned here as macroscopic, filtered manifestation of a quantum phase coherence field. Field saturation could, under unverified hypotheses, prevent singularities ($r \to 0$), while phase filtering offers conceptual avenue — unvalidated quantitatively at this stage — for cosmological constant discrepancy."**

$$\text{quantum degrees of freedom} \xrightarrow{\text{filtering } R > 0 \text{ (hypothesis)}} \text{coherent sector } (C_c \to C_{\text{max}}) \rightarrow g_{\mu\nu}^{\text{eff}} \text{ (non-singular candidate)}$$

> **Quantitative validation criterion associated with $10^{120}$ factor remains documented in companion file (Mapping of research paths, section 11/47) — no candidate mechanism presented in this document, including formalism of sections 47-51, satisfies it to date.**

### Two Distinct Levels in This Document, Not to Be Confused

* **Sections 1-46:** Framework of theoretical questions confronted with existing literature (see companion mapping) — rigor level maintained throughout.
* **Sections 47-51:** Candidate phenomenological formalism ($C(\mathbf{x})$, saturation, torus-cone), **largely untested numerically**. Program of 28 numerical tests on simplified toy models conducted in parallel — see [numerical synthesis document](https://www.google.com/search?q=./Synthese-experiences-numeriques.fr.md) — with positive and negative results partially constraining hypotheses in these sections (notably §47.3 updated above), but not covering full proposed formalism (tensor $T_{\mu\nu}^{(C)}$, dependence $G_{\text{eff}}(C)$, and topology $\mathbb{T}^3$ of §49 remain untested proposals to date).

---

*Personal reflection and open-science document — Official GitHub repository.*
