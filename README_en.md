# 🛠️ H2C SOFTWARE DOWNLOADS
- [🚀 **Pro Version (Python)** : H2C_Universal_Cockpit.py](./H2C_Universal_Cockpit.py) (Full scientific features)
- [🪟 **Windows Version (Builder)** : H2C_Windows_Builder.py](./H2C_Windows_Builder.py) (Generates a standalone .exe)

> **💡 How to generate the Windows executable (.exe) :**
> 1. Download the two files above (`H2C_Universal_Cockpit.py` and `H2C_Windows_Builder.py`).
> 2. Place them in the same folder on your computer.
> 3. Open a terminal and run the builder: `python H2C_Windows_Builder.py`.
> 4. Your standalone application will be created in the `dist/` folder.

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22068679.svg)](https://doi.org/10.5281/zenodo.22068679)
---
## Citation

If you reference this work, please use the following citation:

> Barsamian, V. (2026). *Emergent Gravity and Spacetime Geometry from a Phase Coherence Field C(x): An Exploratory Framework and Numerical Test Program*. Zenodo. https://doi.org/10.5281/zenodo.22064401
---
[🇫🇷 Français](README.md) | 🇬🇧 English version
# Open Question: Can gravitational geometry emerge from a quantum structure?

> ⚠️ **Note:** this document evolves frequently. Remember to refresh the page to consult the latest version.
> 📎 **Companion document:** [Cartography of research paths](./Reflexion-ouverte-sur-la-gravite.fr.md) — contains precise references to existing literature and the quantitative validation criterion (section 11), to be consulted and modified only there.

**Document status:** personal reflection note, formulated with the assistance of several language models (Claude, ChatGPT, Perplexity) from exploratory exchanges.
**Author:** Vahan
**Context:** reflection conducted in parallel with the H2C V8.4-R project (open-source hydrogen reactor), with no technical link between the two.

> **Important:** this document does not claim any discovery, any new theory, or any experimental result. It seeks to formulate a question of theoretical physics precise enough to allow its confrontation with the existing literature and to gather the opinions of researchers in the field.

---

## 1. Starting Point

The initial question was deliberately broad:

> **Is there a physical mechanism capable of locally compensating for the gravitational effect on an object?**

Several classical paths were explored: air ionization, Lense-Thirring type gravitomagnetism, exotic energy distributions, dark energy, etc. These paths do not provide, within the framework of currently established physics, a mechanism allowing the production of a controllable macroscopic gravitational compensation.

This research gradually led to a different, more fundamental question:

> **Could gravity itself be an emergent property of a more fundamental quantum structure?**

The problem is therefore no longer to immediately seek an "anti-gravitational force", but to wonder about the effective origin of gravitational geometry and the constant $G$.

---

## 2. What is Established

General relativity describes gravitation by Einstein's equations:

$$
G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

where $g_{\mu\nu}$ is the spacetime metric, $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$ the Einstein tensor, $\Lambda$ the cosmological constant, $G$ the gravitational constant, $T_{\mu\nu}$ the energy-momentum tensor. The full curvature tensor is the Riemann tensor $R^{\rho}{}_{\sigma\mu\nu}$.

> **Important precision:** $G_{\mu\nu} $ is not the full curvature tensor. It is the Einstein tensor that intervenes directly in Einstein's equations.

---

## 3. Why Interest in the Origin of $G$?

General relativity describes gravity remarkably well, but it does not, by itself, provide a microscopic description of the origin of the constant $G$.

> **Is the gravitational constant fundamental, or could it be an effective parameter resulting from deeper dynamics?**

This question leads notably to the concept of **induced gravity**, historically associated with the work of Andrei Sakharov.

---

## 4. The Induced Gravity Path

In the idea of induced gravity, the Einstein-Hilbert type gravitational term can appear as an effective term resulting from quantum fluctuations of fields coupled to a geometry:

$$
S_{\mathrm{EH}} = \frac{c^3}{16\pi G} \int d^4x \sqrt{-g}\, R
$$

After integrating quantum degrees of freedom, one can schematically obtain:

$$
S_{\mathrm{eff}}[g] = \int d^4x \sqrt{-g} \left[ \frac{c^3}{16\pi G_{\mathrm{eff}}} (R - 2\Lambda_{\mathrm{eff}}) + aR^2 + bR_{\mu\nu}R^{\mu\nu} + \cdots \right]
$$

The important idea is that the coefficient of the curvature term $R$ can receive a contribution from integrated quantum degrees of freedom.

---

## 5. A Schematic Relation for $1/G_{\mathrm{eff}}$

$$
\frac{1}{G_{\mathrm{eff}}} \sim \sum_i c_i N_i \Lambda_i^2
$$

where $N_i$ is the number of degrees of freedom of a sector, $\Lambda_i$ a cutoff scale, $c_i$ a coefficient depending on the theory, spin, couplings and regularization. This relation is **schematic and dependent on the theoretical framework** — it does not demonstrate that $G$ is directly determined by the actual quantum content of the Universe.

---

## 6. What this Relation does NOT allow to Assert

### 6.1 The cutoff $\Lambda$ is not necessarily a manipulable physical parameter
A cutoff scale can depend on the regularization or the limit of validity of the model — it is not a physical energy that can be experimentally modified to change $G$.

### 6.2 A variation of $G$ would be strongly constrained
A variation $G \rightarrow G(x)$ would have to remain compatible with general covariance, conservation laws, and the numerous observations that bound eventual variations of $G$.

---

## 7. The Change of Perspective

A modification of $G$ is not enough to explain gravity, which is a theory of the **dynamic geometry of spacetime**. The deeper question becomes:

> **Could geometry itself emerge from more fundamental quantum degrees of freedom?**

$$
\text{microscopic quantum structure} \rightarrow \text{correlations} \rightarrow \text{effective geometry} \rightarrow \text{classical gravity}
$$

---

## 8. Working Hypothesis

> **The classical metric $g_{\mu\nu}$ could be an emergent collective variable resulting from the organization or correlations of a set of more fundamental quantum degrees of freedom** $\hat{\Phi}_i$.

This proposition constitutes a **research hypothesis**, and not an established theory.

---

## 9. The Central Mathematical Question

$$
G_{\mu\nu}(x) = \mathcal{F}_{\mu\nu}\left[\langle\hat{\Phi}_i(x)\hat{\Phi}_j(x')\rangle\right]
$$

This equation is **not proposed as an established physical equation**. It represents the mathematical form of the problem to be identified in the literature.

---

## 10. A more General Formulation

$$
\mathcal{Q}\left[\langle\hat{\Phi}_i\hat{\Phi}_j\rangle, \langle\hat{\Phi}_i\hat{\Phi}_j\hat{\Phi}_k\rangle, \ldots\right] \rightarrow g_{\mu\nu} \rightarrow R_{\mu\nu}, R, G_{\mu\nu}
$$

> **What structure of quantum correlations could produce an effective geometry possessing the properties of relativistic spacetime?**

---

## 11. The Macroscopic Limit: The Emergence of the Semi-Classical Regime and the Resolution of the $10^{120}$

The decisive test of any theory of emergent gravity lies in its ability to deduce — and not to postulate — Einstein's field equations at the macroscopic scale, while resolving the "vacuum catastrophe" ($10^{120}$). This section details the transition from the microscopic regime of sub-quantum phases to the smooth metric of General Relativity.

```text
   [ Phase Micro-fluctuations at the Planck Scale ]
                 ρ_micro ~ ρ_Planck ~ 10^{114} J/m³
                           │
                           ▼  ( Ensemble averaging over N >> 1 modes )
         [ Destructive Phase Filter (R < 0) ]
                           │
                           ▼  ( Condensation of the critical background C_c )
           [ Emergent Macro Density ρ_vac = V(C_c) ]
                 ρ_macro ~ 10^{-6} J/m³ (Factor 10^{-120})
                           │
                           ▼
[ Effective Metric & Cosmological Einstein Equation ]
G_μν[g^{eff}] + Λ(C_c) g_μν^{eff} = (8π G_{eff}(C) / c_loc^4) T_μν^{eff}
```

### 11.1 The Origin of the $10^{120}$ Discrepancy: The Naive Summation Error
In conventional quantum field theory (QFT), the vacuum energy density is calculated by summing the zero-point energy ($\frac{1}{2}\hbar\omega$) of all modes up to the Planck cutoff frequency ($\omega_{\text{Planck}}$):

$$
\rho_{\text{QFT}} = \int_0^{k_{\text{Planck}}} \frac{\hbar c k}{2} \frac{d^3k}{(2\pi)^3} \approx 10^{114} \text{ J/m}^3
$$

This approach unrealistically assumes that all quantum modes interfere in a **purely constructive and in-phase** manner at all spacetime scales.

### 11.2 Phase Decoherence and the Volume Scale Factor
In our formalism, the macroscopic spacetime is not sensitive to the raw algebraic sum of individual modes, but to the **residual coherence density** of the field $C(\mathbf{x})$.

1. **Underlying interference:** At the microscopic scale ($r \sim \ell_{\text{Planck}}$), fluctuations have phases distributed in a highly incoherent manner. Almost all contributions ($R < 0$) cancel out through immense patterns of destructive interference.
2. **Meso-spatial averaging:** Integrating fluctuations over a macroscopic volume $\Omega$ obeys the law of large numbers for random phases. The scale ratio between the elementary Planck volume $v_{\text{Planck}} = \ell_{\text{Planck}}^3$ and the meso-spatial coherence volume $V_{\text{coh}}$ naturally generates the attenuation factor:

$$
\rho_{\text{vac}}^{\text{macro}} = \rho_{\text{QFT}} \cdot \left( \frac{\ell_{\text{Planck}}}{L_{\text{coherence}}} \right)^4 \approx 10^{-120} \cdot \rho_{\text{QFT}}
$$

The discrepancy of $10^{120}$ is therefore not a constant to be artificially adjusted: it is the **dimensionless scale ratio** between the maximum excitation at the Planck level and the stationary background level of the critical vacuum $C_c$.

### 11.3 The Emergence of the Scalar $C(\mathbf{x})$ and the Metric
When the number of degrees of freedom $N$ becomes macroscopic ($N \gg 1$), the statistical ensemble average operator $\langle \cdot \rangle_{\Omega}$ brings forth the continuous field:

$$
C(\mathbf{x}) \equiv \langle |\Psi(\mathbf{x})|^2 \rangle_{\Omega}
$$

The classical metric $g_{\mu\nu}^{\text{eff}}$ then becomes the response tensor of the substrate to the variations of this averaged field:

$$
g_{\mu\nu}^{\text{eff}}(\mathbf{x}) = \eta_{\mu\nu} + f\left( \frac{\nabla_\mu C(\mathbf{x}) \nabla_\nu C(\mathbf{x})}{C_c} \right)
$$

### 11.4 The Deduction of Einstein's Equation
Applying the principle of least action to the effective action $S_{\text{eff}} = \int \mathcal{L}(C, g^{\text{eff}}) \sqrt{|g^{\text{eff}}|} \, d^4x$ brings forth the macroscopic field equations:

$$
G_{\mu\nu}\left[g^{\text{eff}}\right] + \Lambda(C_c) g_{\mu\nu}^{\text{eff}} = \frac{8\pi G_{\text{eff}}(C)}{c_{\text{loc}}^2(C)^2} T_{\mu\nu}^{\text{eff}}
$$

Where the observed cosmological constant $\Lambda(C_c) \propto V(C_c) \sim 10^{-52} \text{ m}^{-2}$ flows directly from the critical vacuum energy *after* destructive phase cancellation, and not from the raw Planck sum.

### Conclusion of Section 11
The transition from quantum micro-dynamics to the macroscopic metric **proposes a path** for the paradox of modern cosmology: the $10^{120}$ would not represent missing matter or fine-tuning, but the statistical ratio between the maximum local fluctuation and the average condensed state of the coherence field $C(\mathbf{x})$. **This mechanism remains an untested conceptual framework quantitatively at this stage** — the available numerical tests (see the [summary document](./Synthese-experiences-numeriques.fr.md), §3) show a real but modest effective energy suppression (factor ~2-3×, not 10¹²⁰) in a toy model significantly simpler than the one described here, with the rigorous quantitative validation criterion detailed in the companion document (§11/47 of the cartography): no candidate mechanism satisfies it to date, including this one.

---

## 12. Why the Question Goes Beyond a Simple Variable $G$ Theory

$$
\text{quantum correlations} \rightarrow \text{geometry} \rightarrow G_{\mu\nu} \rightarrow \text{gravity}
$$

$G$ would be an **effective parameter of the emergent geometry**, rather than the starting point of the theory.

---

## 13. Theoretical Obstacles to Examine

| Obstacle | Description |
|---|---|
| **13.1 General covariance** | $G_{\mu\nu} = \mathcal{F}_{\mu\nu}[\text{correlations}]$ must respect general covariance. |
| **13.2 Bianchi identities** | $\nabla^\mu G_{\mu\nu} = 0$ must appear at the macroscopic level. |
| **13.3 Energy-momentum conservation** | $\nabla^\mu T_{\mu\nu} = 0$ must generalize if $G_{\mathrm{eff}}$/$\Lambda_{\mathrm{eff}}$ become dynamic. |
| **13.4 Emergence of the metric** | It must be explained how $g_{\mu\nu}$ itself emerges from fundamental degrees of freedom. |
| **13.5 Dynamics of geometry** | It must be explained how the term $\sqrt{-g}R$ appears with the right coefficient. |
| **13.6 Definition of the quantum vacuum** | Specify which quantum state and which correlations are physically relevant. |
| **13.7 Locality / non-locality** | Understand how a local macroscopic geometry emerges from an eventually non-local microscopic description. |
| **13.8 Universality of gravitation** | Explain why the coupling remains universal despite the diversity of microscopic degrees of freedom. |

---

## 14. The Problem of the "Meshing" of Spacetime

The initial intuition considered the geometric "meshing" of spacetime as being able to correspond, by analogy, to a microscopic structure of the quantum vacuum — a **heuristic metaphor**, not an assertion that Einstein would have proposed a spacetime made of a physical network of points.

> **Could the continuous geometric structure described by $g_{\mu\nu}$ be an effective description, at large scale, of a discrete, relational or otherwise structured quantum substrate?**

---

## 15. The Question of the Cosmological Constant

The hierarchy often summarized by a factor of the order of $10^{120}$ between certain microscopic estimations of the vacuum energy and the observed cosmological contribution must be treated with caution — see the companion document for the rigorous treatment of this factor.

> **What if the huge hierarchy revealed a difference between two levels of physical description?**

---

## 16. What if Intermediate Quantum States Were Masked by the Macroscopic Description?

> **What if microscopic calculations described a multiplicity of degrees of freedom, states, and configurations, while effective cosmological gravitation only gave us access to a macroscopic collective description?**

A first formulation represented this transition as a relaxation **𝒬₀ → 𝒬₁ → ⋯ → 𝒬ₛₜₐᵦₗₑ** — **Logic A**.
This representation remains relevant for comparing different physical mechanisms, but it is no longer the preferred mechanism for the fundamental emergence of the geometry studied here (see **section 18**).

---

## 17. The Analogy with a Computer Program

$$
\text{quantum micro-states} \rightarrow \text{interactions} \rightarrow \text{correlations} \rightarrow \text{collective constraints} \rightarrow \text{coherent macroscopic state}
$$

This analogy should not be considered a physical equivalence — it only serves to distinguish microscopic dynamics, intermediate states, interactions, coherence constraints, and macroscopic description.

---

## 18. Two Possible Logics for Emergence

**Logic A — Temporal relaxation:** the system actually evolves in time and progressively reaches a stable configuration: **𝒬₀ → 𝒬₁ → ⋯ → 𝒬ₛₜₐᵦₗₑ**

**Logic B — Sum over configurations and stationary phase:** all configurations contribute to a global amplitude without temporal succession:

$$
\Psi \sim \int \mathcal{D}[\text{configurations}]\; e^{iS/\hbar}
$$

In the semi-classical limit, contributions whose phase varies rapidly cancel out, while regions where the action is stationary contribute constructively. It is this structure that is retained here as a working mathematical analogy for the emergence of $g_{\mu\nu}$.

---

## 19. Why Logic B is Now Preferred

The example of a photon reflected by a mirror illustrates this logic: all trajectories contribute to the amplitude; paths far from the classical path interfere destructively; the neighborhood of the classical path ($\delta S = 0$) interferes constructively. The observed point is therefore not the trace of a single path actually taken, but the dominant macroscopic result of a sum over all possibilities.

---

## 20. Stationary Phase and Coherence Criterion

$$
\delta S = 0
$$

An additional intuition comes from phase closure conditions (Bohr-Sommerfeld, $n\lambda = 2\pi r$): when phases close coherently, certain contributions are reinforced by interference.

> **Is there, for geometric configurations, an analogous coherence condition that favors certain geometries as stable quasi-classical configurations?**

This formulation remains a heuristic analogy — it does not mean that quantum gravity is a classical mechanical resonance phenomenon.

---

## 21. A Path Integral Type Formulation

$$
\Psi[G] = \int_{\mathcal{C}(G)} \mathcal{D}\Phi\; e^{iS_{\mathrm{micro}}[\Phi]/\hbar}
$$

where $\Phi$ represents the fundamental degrees of freedom, $\mathcal{C}(G)$ the set of configurations compatible with a candidate effective geometry $G$, and $S_{\mathrm{micro}}$ a microscopic action yet to be defined. This writing is an objective of formalization, not an equation already derived.

---

## 22. Technical Problems Associated with Logic B

Measure problem ($\mathcal{D}[g_{\mu\nu}]$ covariant), convergence (oscillating Lorentzian weight), conformal factor (problematic directions of the gravitational action), renormalization (perturbative non-renormalizability of quantized GR). The gravitational path integral is a powerful formal framework, not yet a complete and calculable microscopic theory.

---

## 23. Working Hypotheses H1–H10

| ID | Question |
|---|---|
| **H1** | Nature of the summed degrees of freedom — what concretely are the $\hat{\Phi}_i$? |
| **H2** | Microscopic action $S[\hat{\Phi}_i]$, without assuming $\sqrt{-g}R$. |
| **H3** | Integration measure — what class of configurations, what symmetries respected. |
| **H4** | Signature and convergence — Euclidean vs Lorentzian. |
| **H5** | Stationary phase criterion, applied to the microscopic action. |
| **H6** | Decoherence mechanism separated from the stationary phase itself. |
| **H7** | Origin of $G_{\mathrm{eff}}$ and $\Lambda_{\mathrm{eff}}$ from microscopic parameters. |
| **H8** | Boundary conditions. |
| **H9** | Domain of validity. |
| **H10**| Distinctive and testable prediction. |

---

## 24. H6bis — Parallel Spatiotemporal Configurations

Instead of considering several intermediate states of the same spacetime, we envisage a multiplicity of possible spatiotemporal configurations or histories: $\{H_1, H_2, \ldots, H_N\}$, each associated with its own effective geometry $g_{\mu\nu}^{(i)}$ and eventually an effective proper time.

> A multiplicity of spatiotemporal configurations in a quantum description does not automatically mean the existence of several independent classical spacetimes in the ordinary sense.

---

## 25. H6bis.1 — The Decoherence of Histories

$$
\{H_i\} \xrightarrow{\text{interferences}} \text{decoherence} \rightarrow \{H_k^{\mathrm{qc}}\}
$$

A family of histories can become sufficiently decoherent from the others to be described as a quasi-classical sector — not necessarily a single history that "wins".

---

## 26. H6bis.2 — The Soap Bubbles Analogy

$$
\{B_1, B_2, \ldots\} \xrightarrow{\text{interactions}} \text{coalescence} \rightarrow B_{\mathrm{collective}}
$$

For bubbles, the mechanism (surface tension) is physical and known. For the quantum problem, the sought mechanism is different (interferences → stationary phase → decoherence). The analogy relates solely to the conceptual transition: multiplicity → collective organization → macroscopic description.

---

## 27. H6bis.3 — Bubbles as a Heuristic Representation of Spatiotemporal Configurations

> **Could the geometry of spacetime we observe be the dominant quasi-classical sector flowing from a multiplicity of possible quantum spatiotemporal configurations?**

This formulation does not claim to demonstrate that several classical spacetimes actually exist — it proposes to determine if a quantum theory of gravitation can give a mathematical meaning to this multiplicity.

---

## 28. H6bis.4 — The Parallel with the Photon and the Mirror

All trajectories contribute to the amplitude; contributions with rapidly varying phase cancel out; near the classical path ($\delta S = 0$), contributions reinforce each other. The macroscopically observed point is not the manifestation of a single microscopic path actually taken, but of the region where contributions interfere constructively. The parallel with bubbles and with histories is structural, not literal.

---

## 29. H6bis.5 — A More Precise Formulation of "Constructed Reality"

It is more rigorous to speak of a **configuration or family of configurations whose constructive contribution and collective coherence dominate in the considered macroscopic limit**, rather than a configuration that would "absorb" the others.

---

## 30. H6bis.6 — Internal Temporalities of Histories

If $H_i \to g_{\mu\nu}^{(i)}$, then the associated proper time $\tau_i$ is determined by this geometry.

> **Could the time we observe be the internal proper time of the quasi-classical history in which our macroscopic description is defined?**

This link remains to be constructed mathematically.

---

## 31. H6bis.7 — Unified Formulation of H6

$$
\text{quantum spatiotemporal configurations} \rightarrow \text{interferences} \rightarrow \text{stationary phase} \rightarrow \text{decoherence} \rightarrow \text{quasi-classical histories} \rightarrow (g_{\mu\nu}, \tau_{\mathrm{eff}})
$$

> **What if the macroscopic reality we observe was not a unique fundamental description, but the coherent quasi-classical sector of a multiplicity of simultaneously contributing quantum spatiotemporal configurations in the amplitude?**

This formulation constitutes a research hypothesis, not an established interpretation.

---

## 32. Microscopic Energy and Effective Gravitation

$$
\rho_{\mathrm{micro}} \gg \rho_{\mathrm{eff}}
$$

without assuming that microscopic energy "disappears".

$$
\{\text{quantum states}, \text{correlations}, \text{histories}\} \rightarrow T_{\mu\nu}^{\mathrm{eff}} \rightarrow g_{\mu\nu}
$$

---

## 33. The Possible Link with the Cosmological Constant

> **Could the cosmologically observed value of $\Lambda$ be an emergent property of a collective sector of quantum configurations rather than a simple sum of the zero-point energies of all fields?**

---

## 34. A Distinction Between Three Levels of Description
Microscopic level (Φ̂ᵢ) → quantum level of configurations/histories (Hᵢ) → emergent classical level (g_μν, τ_eff, G_eff, Λ_eff). This separation avoids confusing fundamental degrees of freedom, possible configurations, and effective macroscopic variables.

---

## 35. Time, History and Geometry

If $H_i \to (g_{\mu\nu}^{(i)}, \tau_{\mathrm{eff}}^{(i)})$, geometry and time become two linked aspects of the same effective description. The possibility of a common mechanism remains an open question.

---

## 36. A Time-Scale Separation Hypothesis

$$
\tau_{\mathrm{micro}} \ll \tau_{\mathrm{corr}} \ll \tau_{\mathrm{macro}}
$$

Heuristic relationship, which does not mean the existence of several fundamental times.

---

## 37. The Possible Role of the Casimir Effect

$$
\Delta E_{\mathrm{Casimir}} = E_{\text{constraint}} - E_{\text{reference}}
$$

The Casimir effect should not be interpreted as a direct measure of the absolute vacuum energy. It is not about proposing a "Casimir cosmological constant", but about asking: **does gravitation couple to an absolute energy, or could it respond to an effective quantity flowing from differences between states or configurations?**

---

## 38. A Geometric Coherence Constraint

$$
\nabla^\mu G_{\mu\nu} = 0 \quad (\text{Bianchi identities})
$$

An emergent theory must explain how this geometric coherence appears at the macroscopic scale. The analogy with a "cosmic compiler" is solely heuristic.

---

## 39. A General Formulation of the Sought Dynamics

$$
\text{quantum degrees of freedom} \rightarrow \text{configurations/histories} \rightarrow \text{correlations} \rightarrow \text{interferences} \rightarrow \text{stationary phase} \rightarrow \text{decoherence} \rightarrow \text{quasi-classical sector} \rightarrow (g_{\mu\nu}, \tau_{\mathrm{eff}}, G_{\mathrm{eff}}, \Lambda_{\mathrm{eff}})
$$

This chain constitutes a conceptual architecture, not an established theory.

---

## 40. Open Question on Effective Mass

$$
m_{\mathrm{eff}} = \frac{E}{c_{\mathrm{loc}}^2}
$$

Dimensionally coherent relationship, physically non-trivial only if $c_{\mathrm{loc}}$ is an effective propagation speed derived from microscopic dynamics.

> **Could the same quantum substrate that would eventually produce geometry also produce inertia or effective mass?**

No common mechanism of this form is established here. *(See the companion document for the historical warning — Wheeler, geometrodynamics, 1955 — associated with this ambition.)*

---

## 41. What Would Need to Be Demonstrated to Transform the Hypothesis into a Theory

Define the fundamental degrees of freedom and their state space; define their dynamics and the relevant correlations; define the summed object and the integration measure; establish a stationary phase criterion; show how decoherence produces quasi-classical histories; show how $g_{\mu\nu}$ and effective time emerge; determine if an effective mass can appear; derive an effective action recovering $\sqrt{-g}R$; determine $G_{\mathrm{eff}}$ and $\Lambda_{\mathrm{eff}}$; find Einstein's equations; reproduce known observations; produce a falsifiable prediction.

Without these steps, the idea remains a **heuristic hypothesis**.

---

## 42. Open Question to the Scientific Community

Question submitted to researchers in quantum gravity, QFT in curved spacetime, induced and emergent gravity, holography, quantum information and gravity, renormalization, non-commutative geometry, emergent spacetime, out-of-equilibrium systems:

> **Is there in the literature a mathematical construction where the effective gravitational geometry is explicitly derived from a structure of quantum correlations, amplitudes, and eventually a sum over histories, whose macroscopic limit reproduces Einstein's equations?**
>
> **Is there a mechanism allowing the transition from a multiplicity of quantum configurations to a coherent quasi-classical sector whose effective parameters are calculated rather than postulated?**

(19 detailed technical sub-questions — exact mathematical formulation, degrees of freedom, correlations, measure, decoherence, emergence of the metric, of time, of mass, of $G_{\text{eff}}$, of $\Lambda_{\text{eff}}$, hypotheses, limits, locality, covariance, energy-momentum coherence, $10^{120}$ hierarchy, distinctive prediction.)

If no construction satisfying these criteria exists: **what known structural obstacle prevents such a construction?**

---

## 43. What this Research does NOT Claim to Demonstrate

That spacetime is made of "quantum vacuum points"; that several independent classical spacetimes actually exist; that $G$ is necessarily emergent; that the $10^{120}$ orders of magnitude represent physical steps of stabilization; that coarse-graining already explains this hierarchy; that Casimir is responsible for the cosmological constant; that several independent fundamental times exist; that microscopic time "flows faster"; that the stationary phase selects by itself a unique classical reality; that decoherence proves an emergent geometry; that mass is necessarily emergent; that the quantum vacuum allows gravity control; that a new theory of quantum gravity has been discovered; that an antigravity or propulsion application flows from it.

It is solely a **theoretical research question**.

---

## 44. Five Linked but Distinct Problems

| Level | Question |
|---|---|
| **Geometry** | How could $g_{\mu\nu}$ emerge? |
| **Gravitation** | How could $G_{\mathrm{eff}}$ appear? |
| **Cosmology** | Why is $\Lambda_{\mathrm{eff}}$ so small? |
| **Time** | Could proper time itself be emergent? |
| **Inertia** | Could an effective mass emerge from the same substrate? |

These problems may be linked in a deeper theory, but no automatic implication is assumed.

---

## 45. Objective of this Repository

Document the progress of the reflection; distinguish established results and speculative hypotheses; identify existing works; avoid rediscovering an already published construction; gather criticisms allowing to falsify or reformulate the hypothesis; determine if the problem is already resolved, partially treated, or truly open.

---

## 46. Methodological Position

> **Hypothesis ≠ interpretation ≠ result ≠ established theory.**

The assistance of language models served to explore the literature, reformulate hypotheses, and identify mathematical paths. It does not constitute a scientific validation. Any important assertion must be confronted with the original publications and the opinion of competent researchers.

---

---

## 47. Mathematical Formalization and Toy Model: Consolidated State

This section gathers the phenomenological formalism and the numerical results obtained after successive campaigns. It must be read as a **falsifiable research program**, and not as an established derivation of general relativity.

### 47.1 Coherence Field and Fundamental Variables

We consider a scalar phase coherence field:

$$
C(\mathbf{x})\in[0,1].
$$

In collective dynamics models, it is represented by the order parameter:

$$
Z=\frac{1}{N}\sum_{j=1}^{N}e^{i\theta_j},\qquad C=|Z|^2.
$$

This definition presents an important property: $C$ is invariant under a global rotation of phases, unlike $R=\mathrm{Re}(Z)$. Previous campaigns have therefore led to retaining $C$ as a robust coherence observable.

The structural framework remains fixed in **3+1 dimensions**:

$$
d=3\quad\text{space dimensions},\qquad D=d+1=4.
$$

### 47.2 Potential Equation and Regularized Profile

The working model retains a modified Poisson-type equation:

$$
\nabla^2\Phi(\mathbf{x})=\frac{4\pi c^2}{L_0^2}\left[C(\mathbf{x})-C_c\right].
$$

The regularized profile used as a reference is:

$$
C(r)=C_c+\frac{r_g^2}{r^2+r_g^2}(C_{\max}-C_c),
$$

with $C_{\max}=1$ and $r_g=2GM/c^2$.

This profile possesses a useful property:

$$
C(0)=C_{\max},\qquad C'(0)=0.
$$

But it must not be identified directly with a mass density: its asymptotic behavior in $1/r^2$ would make the integrated mass divergent. The reconstruction must therefore remain separate:

$$
C(r)\rightarrow\rho(r)\rightarrow m(r)\rightarrow g(r)\rightarrow g_{\mu\nu}^{\mathrm{eff}}.
$$

### 47.3 Tested Collective Dynamics

The weighted Kuramoto dynamics used in Tests 12–13 and the campaign of Test 51 is:

$$
E_i=Q_i^2,
$$

$$
w_{ij}=\exp\left[-\frac{(E_i-E_j)^2}{2\sigma^2}\right],
$$

$$
\dot\theta_i=\frac{K}{N}\sum_jw_{ij}\sin(\theta_j-\theta_i).
$$

The order parameter is then:

$$
C=|Z|^2,\qquad Z=\frac1N\sum_j e^{i\theta_j}.
$$

This dynamics allows distinguishing an incoherent state ($C\sim1/N$) from a collectively coherent state ($C\gg1/N$).

For uniform independent phases:

$$
\mathbb E[C]=\frac1N,
$$

which provides an indispensable reference for interpreting small $C$ at finite size.

### 47.4 Status of $R$
The sign of $R=\mathrm{Re}(Z)$ is not invariant under global phase rotation. Previous tests have therefore discarded its use as an absolute coherence criterion or as proof of a causal orientation.

The following specific hypotheses were not confirmed in their initial form:

- $R<0$ as a necessarily destructive sector;
- $R$ as a direct code of a future/past causal cone;
- correlation between the sign of $R$ and a topological winding.

An alternative causal indicator $R_{\mathrm{causal}}$ remains a path, but without a demonstrated positive floor.

---

### 47.5 Derivation of $K$: From a Postulated Parameter to a Derived Coupling Constant

The dynamics described in 47.3 uses a coupling constant $K$ which, until now, was an external parameter adjusted by hand. Two results establish that it can be reformulated, then partly derived.

**Step 1 — $K$ is already, structurally, a coupling constant.** The dynamics $\dot\theta_i=\frac{K}{N}\sum_j w_{ij}\sin(\theta_j-\theta_i)$ is exactly the descending gradient flow of the potential:

$$
V[\theta]=-\frac{K}{2N}\sum_{i,j}w_{ij}\cos(\theta_i-\theta_j)
$$

verified numerically at machine precision ($\sim10^{-11}$) — $K$ is therefore not an arbitrarily added force, but the coupling constant of an XY-type interaction term.

**Step 2 — derivation by adiabatic elimination of a mediator field.** By coupling each phase $\theta_i$ to a complex mediator field $\psi$ (Hubbard-Stratonovich type technique, formal analogue to Sakharov's induced gravity, §4-5):

$$
\dot\psi = \mathrm{rate}\cdot(-m^2\psi+g\,\bar Z),\qquad \bar Z=\frac{1}{N}\sum_j e^{i\theta_j}
$$

the adiabatic elimination of $\psi$ (fast relaxation towards its equilibrium $\psi_{\mathrm{eq}}=(g/m^2)\bar Z$) reproduces the reduced Kuramoto dynamics with:

$$
\boxed{K_{\mathrm{eff}}=\frac{g^2}{m^2}}
$$

Numerically verified: the full system with explicit mediator reproduces the reduced dynamics to within the 3rd-4th decimal place, across five tested coupling values $g$ (from $g=0.05$ to $g=1.0$).

**Scope and limit.** This is the first non-circular derivation of a parameter of this model, rather than an adjustment — but $g$ (coupling to the mediator) and $m$ (mass of the mediator) remain themselves un-derived external parameters. The problem is pushed back a step, not resolved.

> ⚠️ **Vigilance point on test numbering.** Several independent working threads (this one, and the companion digital journal) each have their own numbering of "Test N", which do not coincide term-by-term — for example, "Test 43" of section 48.4 below (radii $R_{\mathrm{trans}}$, $R_{\mathrm{gentle}}$) is not the same calculation as "Test 43" of the [digital experience journal](./Journal-experiences-numeriques.fr.md) (search for exponents on the radial solution). Refer to the content of each test, not just its number, in case of doubt.

---

## 48. Regularized Geometry and Recovery of the Newtonian Limit

### 48.1 Why the Global $4/3$ Was Abandonned

The first versions used a global scaling of the type $r\sim N^{4/3}$. Tests 39–40 showed that this unbounded growth cannot be maintained until infinity: it destroys the Newtonian limit.

The physical constraint therefore becomes:

$$
\text{central/intermediate regime: possible correction}
$$

$$
\text{Large } r :\qquad |g(r)| \propto \frac{1}{r^2}.
$$

### 48.2 Test 41 — Success of Localized Correction

Test 41 corrected a sign error: $g(r)$ is negative by convention, while $M_{\mathrm{tot}}>0$. The correct comparison therefore relates to the magnitudes $|g(r)|r^2$.

Reported values:

| $r$ (kpc) | $|g(r)|r^2$ |
|---:|---:|
| 15 | 1183.9 |
| 20 | 1183.0 |
| 30 | 1182.0 |

The average is around $1183$, with a coefficient of variation of about $0.07\%$, and the relative deviation to $M_{\mathrm{tot}}=1196.7$ is about $1.15\%$.

The result establishes in this toy model a very clean recovery of the law:

$$
|g(r)|r^2\rightarrow\mathrm{constante}.
$$

**Status: 🟢 numerical result of non-regression in the toy model.** It does not constitute an observational validation of emergent gravity.

### 48.3 Test 42 — Robustness of Localized Correction

A $4\times4$ grid was explored by independently varying $\sigma$ and $k_0$ between $0.5$ and $2$ times their nominal values.

Reported result: **16/16 robust points**, with $|g|r^2$ quasi-constant and a relative deviation to $M_{\mathrm{tot}}$ of the order of $0.1\%$ in the reproducible toy.

The methodological conclusion is important: the recovery of the asymptote is not solely linked to a punctual adjustment of the tested parameters.

**Status: 🟢 numerical robustness of the localization mechanism in the tested model.**

### 48.4 Tests 43–44 — Torus–Cone Integration and Dynamic Exponent

The working geometry was then organized into three regimes:

1. central region/torus;
2. transition region/cone;
3. gentle slope and asymptotic return.

The radii used in Test 43 were:

$$
R_{\mathrm{trans}}=0.61\ \mathrm{kpc},\qquad R_{\mathrm{gentle}}=1.31\ \mathrm{kpc}.
$$

The ratio $\delta \simeq 2.15$ between these radii remains a geometric input and is not yet derived.

Test 43 retains the Newtonian asymptote with a coefficient of variation of about $0.005\%$ and a relative deviation of about $-0.004\%$ in the reported calculation.

To make the $4/3$ compatible with this constraint, a dynamic interpolation was tested:

$$
s(r)=\frac{C(r)-C_c}{C_{\max}-C_c},
\qquad
\alpha(s)=1+\frac{s}{3}.
$$

Thus:

$$
s\rightarrow0\Rightarrow\alpha\rightarrow1,
$$

$$
s\rightarrow1\Rightarrow\alpha\rightarrow\frac43.
$$

In Test 44, the cone zone gave approximately $1.21\lesssim\alpha\lesssim1.28$, with an average close to $1.25$. The value $4/3$ was therefore not reached everywhere: it appears as a **saturation limit**, not as a global constant imposed on all radii.

**Status: 🟢 numerical coherence of the tested connection; 🟡 fundamental origin of $4/3$ still open.**

### 48.5 Candidate Form of Localized Correction

A working expression compatible with previous results is:

$$
\rho_{\mathrm{eff}}(r)=\rho_b(r)\left[1+k_0\left(\frac{r}{r_t}\right)^{4/3}\mathrm{sech}^2\left(\frac{r-r_t}{\sigma}\right)\right].
$$

This expression is not yet a fundamental law. It only encodes the three numerical constraints:

- weak correction out of the transition zone;
- $4/3$ scaling in the active zone;
- extinction of the correction at large $r$.

---

## 49. Search for the Dimensional Origin of $4/3$, $3/4$ and $1/4$
The model is now explicitly fixed in $3+1$ dimensions: $d=3$.

A simple dimensional family gives:

$$
\alpha=\frac{d+1}{d}=\frac43,
$$

$$
\beta=\frac d{d+1}=\frac34,
$$

with:

$$
\alpha\beta=1.
$$

Another candidate relation gives:

$$
\eta=\frac1{d+1}=\frac14.
$$

With the definition used for the angle:

$$
\theta=2\arcsin\left(\frac{C_c}{1-C_c}\right),
$$

the value $C_c=0.2=1/5$ entails exactly:

$$
\frac{C_c}{1-C_c}=\frac14,
$$

then:

$$
\theta=2\arcsin\left(\frac14\right)\approx28.955^\circ.
$$

One can also write the candidate relation:

$$
C_c=\frac1{d+2}.
$$

For $d=3$:

$$
C_c=\frac15,
$$

and therefore:

$$
\frac{C_c}{1-C_c}=\frac1{d+1}=\frac14.
$$

### 49.1 What Is Really Demonstrated

The numerical identities are exact:

$$
0.2=\frac15,\qquad\frac{0.2}{0.8}=\frac14,
$$

$$
2\arcsin(1/4)\approx28.955^\circ,
$$

$$
\frac{d+1}{d}=\frac43,\qquad\frac d{d+1}=\frac34\quad(d=3).
$$

### 49.2 What Is Not Derived

Tests 49–50 showed that the minimal dynamics of $C$ and the simple tested feedbacks do not spontaneously select $C_c=1/5$.

With:

$$
Z\Box C-V'(C)=0,
$$

a quadratic potential relaxes towards the value placed in the potential. Similarly, the tested feedbacks of type $\sigma(C)$ produced significantly more coherent attractors, around $0.72$ to $0.91$, with no attractor in the window $[0.16; 0.24]$.

**Conclusion:** $C_c=1/5$ remains an **input of the gravitational model**, while $4/3$, $3/4$ and $1/4$ form an elegant and coherent dimensional structure **conditional on this input**. No fundamental physical derivation of $C_c=1/5$ is currently established.

---

## 50. Collective Dynamics Tests: From $Q_i$ to $C$

### 50.1 Calculation Chain

The numerical program is organized according to the chain:

$$
Q_i\rightarrow E_i\rightarrow\theta_i\rightarrow C,
$$

with:

$$
E_i=Q_i^2,
$$

$$
w_{ij}=\exp\left[-\frac{(E_i-E_j)^2}{2\sigma^2}\right].
$$

The objective is to determine if a collective structure produces a privileged value of $C$ or solely a continuous transition between incoherence and synchronization.

### 50.2 Test 50 — Blind Feedbacks of $C$ on $\sigma$
Two families without targeting $0.2$ were tested:

$$
\sigma(C)=\sigma_0(1-C),
$$

and

$$
\sigma(C)=\frac{\sigma_0}{1+\kappa C}.
$$

The reported attractors were approximately:

| Form | Parameters | $C^*$ |
|---|---|---:|
| linear | $\sigma_0=0.5$ | 0.778 |
| linear | $\sigma_0=1.0$ | 0.818 |
| linear | $\sigma_0=1.5$ | 0.913 |
| inverse | $\sigma_0=0.8, \kappa=1$ | 0.836 |
| inverse | $\sigma_0=0.8, \kappa=2$ | 0.893 |
| inverse | $\sigma_0=1.2, \kappa=1.5$ | 0.914 |
| inverse | $\sigma_0=1.0, \kappa=3$ | 0.722 |

No attractor appeared in $[0.16; 0.24]$.

**Verdict: 🔴 these simple feedbacks do not select $C_c\simeq0.2$.**

### 50.3 Test 51 — Blind Search for a Collective Transition

Test 51 then abandoned all artificial feedback and searched directly for a transition in the weighted system:

$$
\dot\theta_i=\frac KN\sum_jw_{ij}\sin(\theta_j-\theta_i).
$$

The protocol uses notably:

$$
N\in\{200,400,800,1600\},
$$

a sweep of $K$ and $\sigma$, several independent seeds, and a sufficiently long integration time.

The planned observables are:

$$
\chi_C=N\left(\langle C^2\rangle-\langle C\rangle^2\right),
$$

as well as a Binder cumulant treated as a secondary indicator, and the relaxation time.

The first reported 2D scan, with $N=200,400$, $K\in\{0.5, 1, 1.5, 2\}$ and $\sigma\in\{8,12,16,20\}$, shows:

- an incoherent regime at low $K$, with $C$ close to the $1/N$ scale;
- a continuous rise of $C$ with $K$;
- punctual values close to $0.2$;
- no robust critical line that universally fixes $C\simeq0.2$.

For example, values close to $0.2$ appear around $C\approx0.218$ and $C\approx0.169$ for certain pairs $(K,\sigma)$, but they shift when parameters or $N$ change.

**Verdict of Test 51:**

$$
\boxed{\text{the weighted model has a synchronization transition, but does not select }C_{\mathrm{crit}}\approx0.2\text{ universally}.}
$$

Thus, $C=0.2$ is currently better described as a **parametric waypoint** of the model than as a fundamental attractor or critical point.

---

## 51. Physical Consequences and Current Limits

### 51.1 What Numerical Campaigns Actually Establish

| Element | Status |
|---|---|
| 3+1 dimensional structure | 🟢 Fixed structural hypothesis |
| $C=|Z|^2$ as phase invariant | 🟢 Confirmed as robust toy observable |
| Incoherent state $C\sim1/N$ | 🟢 Confirmed statistical reference |
| Localized correction | 🟢 Tested with Newtonian non-regression |
| Robustness of the asymptote under variation $\sigma,k_0$ | 🟢 Tested in the toy |
| Torus–cone integration | 🟢 Numerically coherent within the tested framework |
| $\alpha(s)\to4/3$ at saturation | 🟢 Coherent dynamic formulation; fundamental origin open |
| Global $4/3$ | 🔴 Abandoned: divergence at large $r$ |
| $3/4$ | 🟡 Inverse relation coherent with $4/3$, not independent derivation |
| $C_c=1/5$ | 🟡 Input parameter; not dynamically selected |
| $1/4$ | 🟡 Identity conditional on $C_c=1/5$; not independently derived |
| $\theta\approx28.955^\circ$ | 🟢 Mathematical consequence of $C_c=0.2$ in current formula |
| $E=mc^2$ | 🔴 No independent validation; any definition of $m$ via $c^2$ would be circular |
| $c_{\mathrm{eff}}\approx\sqrt2$ | 🟡 To be audited separately; no fundamental origin established here |
| Emergent spatial $r$ | 🔴 Not derived from correlations |
| $D_{\mathrm{eff}}=3/4$ or $4/3$ as emergent geometric dimension | 🔴 Not established |
| Quantitative resolution of $10^{120}$ | 🔴 Not obtained; tested toys give much lower suppression |
| Derivation of Einstein's equations | 🔴 Not obtained |

### 51.2 The Essential Point on Singularities

The regularized profile shows that it is mathematically possible to construct a source whose density remains finite at the center and whose total mass converges to $M$ at large distance. A reference metric of Hayward type possesses for example:

$$
m(r)=M\frac{r^3}{r^3+a^3},
$$

and asymptotically recovers the Schwarzschild form.

This demonstrates a **regularization property**, not that the field $C$ effectively generates this geometric mass.

### 51.3 The Essential Point on Antigravitation

In the current version, the candidate tensor is quadratic in gradients of $C$ and the bound $C\le1$ prevents a trivial extrapolation beyond saturation. This excludes certain repulsive behaviors **in this particular model**, under its hypotheses.

This is not a proof that antigravitation is impossible in any physical theory.

### 51.4 Proper Time and Emergent Time

The question remains open: if a quasi-classical history $H_i$ possesses a metric $g_{\mu\nu}^{(i)}$, its proper time could be defined by:

$$
\tau_i= \int\sqrt{-g_{\mu\nu}^{(i)}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}}\,d\lambda.
$$

The heuristic hierarchy:

$$
\tau_{\mathrm{micro}}\ll\tau_{\mathrm{corr}}\ll\tau_{\mathrm{macro}}
$$

remains a working hypothesis and not an experimental measurement of three fundamental times.

### 51.5 Next Roadmap

The next steps must remain separate and falsifiable:

1. **Audit $c_{\mathrm{eff}}$ term-by-term**, notably looking for any square root already present in its definition before interpreting a result close to $\sqrt2$.
2. **Pursue the analysis of correlations** $\tau_{ij}$ to determine if differentiated correlation scales actually emerge.
3. Construct a distance $d_{ij}$ only if the correlations produce a non-trivial structure that is not simply inherited from $E_i$.
4. Then seek an emergent radius $r$ and only then test $N(r)$ and $D_{\mathrm{eff}}(r)$.
5. Test if the exponent observed in the transition zone is truly compatible with $4/3$ without fixing it in advance.
6. Confront the corrected gravitational profile with actual observational data, notably rotation curves, without ad hoc recalibration per galaxy if the goal is predictivity.
7. Retain separately the question of the microscopic origin of $C_c$: Test 51 closes the precise path "energy weighting $\rightarrow C_c=1/5$" under the tested family, but does not close all theoretical possibilities.

---

## 52. General Conclusion — State of the Research Program

The model has crossed an important step: certain constructions that diverged have been abandoned, while a **localized correction** showed a robust recovery of the Newtonian limit in the toy model.

The $4/3$ is no longer used as a global law. It is now treated as a **potential transition scaling**, with an interpolation $\alpha(s)$ that tends towards $4/3$ when the normalized densification tends towards saturation $s\to1$.

The structure:

$$
\frac43,\qquad\frac34,\qquad\frac14
$$

is coherent with $d=3$, but its scientific value still depends on an independent derivation of $C_c=1/5$. Tests 49–51 precisely prevented presenting this relationship as already derived: the tested dynamics do not select $1/5$ spontaneously.

The current scientific position can therefore be summarized by:

$$
\boxed{
\text{numerically constrained toy model}
\neq
\text{demonstrated emergent gravity theory}
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
|g(r)|r^2\rightarrow\mathrm{constante}
\qquad(r\rightarrow\infty).
$$

> **Working principle: we no longer choose the sought result; we first seek if the dynamics produces it, then we keep both successes and failures.**

The program therefore remains open, but it is now more falsifiable, cleaner mathematically, and better separated between **inputs**, **consequences**, **numerical results** and **fundamental hypotheses**.

---

## Conclusion

> **The gravitational geometry described by general relativity is here studied as an eventual emergent macroscopic description of a collective quantum structure. Current numerical results do not demonstrate this emergence, but they already allow eliminating certain unstable constructions and identifying precise constraints for the future.**

The central scientific problem remains:

> **Is there a microscopic dynamics precise enough to simultaneously produce the coherence $C$, an emergent metric structure, the Newtonian limit, Einstein's equations and the observed cosmological parameters without imposing them in advance?**

*Document of personal reflection and open science — to be confronted with scientific literature and independent validations.*

---

## 53. Critical Update — Campaigns 68–70: Threshold Audit, Symmetries and Falsification Protocol

> **Status: major methodological update.**
> This section preserves the trace of results, corrections, and open questions that appeared after campaigns 68–69e. It must be read as an audit of the toy model, and not as a validation of the gravitational emergence theory.

### 53.1 Starting Point: The Deviation $v_c(\alpha=0)\simeq2.92$ Against $v_c^{\rm th}=2u=2.0$

The report of campaigns 68–69e reported a numerical extrapolation:

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

This deviation of the order of $46\%$ was identified as a methodological anomaly to be resolved **before any new interpretative campaign**.

The working principle is:

$$
\boxed{
\text{numerical artifact}
\;\rightarrow\;
\text{limits }T,N
\;\rightarrow\;
\text{missing physical term}
}
$$

and not the inverse.

---

### 53.2 Important Correction of the Energy Audit of Report 70A

An additional algebraic check showed that report 70A contained an error in evaluating the minima.

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

and therefore, for the non-trivial minimum,

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

The:

$$
\boxed{F_1=-\frac{r^2}{4u}}.
$$

For $r=u=1$,

$$
\boxed{F_1=-0.25}.
$$

> **Explicit correction:** $F_1$ is not equal to $0$. The quadratic term and the quartic term do not cancel at the minimum; together they give $-r^2/(4u)$.

#### Symmetric Rank 3

For:

$$
\psi_1=\psi_2=\psi_3=\rho,
$$

we get:

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

So:

$$
\boxed{
F_3=-\frac{3r^2}{4(u+v)}
}.
$$

For $r=u=1$ and $v=0$,

$$
\boxed{F_3=-0.75}.
$$

Report 70A gave $-0.5625$, a value compatible with a bad substitution of the amplitude.

---

### 53.3 The Energy Crossing Is Not at $v\simeq0.86$

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

so:

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

There is therefore **no** distinct thermodynamic window in this precise symmetric quartic potential

$$
0.86<v<2
$$

such that rank 1 would be globally favored while rank 3 would remain metastable.

The alleged threshold $v\simeq0.86$ of report 70A must be classified as an **algebraic artifact**, and not as a second physical threshold.

---

### 53.4 General Formula for $k$ Active Components

For $k$ components of same amplitude $\rho$:

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

This formula corrects an important ambiguity present in previous versions: the amplitude itself carries a square root.

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

The comparison $F_1^{\min}=F_3^{\min}$ gives back indeed:

$$
\boxed{v=2u}.
$$

---

### 53.5 Consequence: The Modal Competition Mechanism Remains Plausible, but the Interpretation Must Be Cleaned Up

The minimal model:

$$
F=
-r\sum_a|\psi_a|^2
+
u\sum_a|\psi_a|^4
+
v\sum_{a<b}|\psi_a|^2|\psi_b|^2
$$

possesses therefore, for $u>0$ and $r>0$, a natural threshold:

$$
\boxed{v_c=2u}.
$$

This result does not depend on a numerical adjustment of the threshold.

On the other hand, it is not enough to explain why a given simulation could produce an apparent threshold around $2.9$. This question remains distinct:

$$
\boxed{
v_c^{\rm apparent}\neq v_c^{\rm theoretical}
}
$$

as long as the effects of finite time, finite size, operational definition of the threshold, and eventual reduction of the model have not been separated.

---

## 53.6 Formalization 70S — Exact Nature of the Dynamics

The collective dynamics studied in Tests 9–46 is a gradient flow:

$$
\boxed{
\dot\psi_a
=
-\frac{\partial F}{\partial\psi_a*}
}
$$

either, in the general case:

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

### Potential Symmetry

When the potential only depends on modules:

$$
F=F(|\psi_1|^2,|\psi_2|^2,|\psi_3|^2),
$$

it is invariant under:

$$
\psi_a\rightarrow e^{i\varphi_a}\psi_a,
$$

with three independent phases.

So:

$$
\boxed{G_F=U(1)^3}.
$$

### Flow Symmetry

The gradient flow is then equivariant under the same action:

$$
\boxed{G_{\rm flow}=U(1)^3}.
$$

The symmetry of the potential and that of the flow must not however be confused with a conservation law of a Noether charge.

### Polar Variables

By writing:

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

for this **precise reduced dynamics**.

The amplitudes can therefore decrease to zero while the phases remain frozen.

> **Essential methodological point:** $\dot\theta_a=0$ is not a consequence of $U(1)^3$ alone. It is a consequence of the combination "phase-invariant potential + choice of gradient flow".

---

## 53.7 Do Not Automatically Extrapolate This Property to the Microscopic Level

The original microscopic dynamics, notably the Kuramoto-type oscillators studied elsewhere in the program, possesses an active phase dynamics:

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

The property $\dot\theta_a=0$ of the reduced Landau model must not be presented as a demonstrated property of microscopic dynamics until an explicit reduction has been derived.

This is now a priority question for 70S:

> **Is the frozen phase dynamics of modal variables derived from microscopic dynamics, or introduced by phenomenological reduction?**

---

# 54. Diagnostic Protocol 70A–70D

## 54.1 70A — Test the Extrapolation $\alpha\rightarrow0$

### Tested Hypothesis

The $2.92$ could come from an inadequate linear extrapolation rather than a true threshold at $\alpha=0$.

We start from the measurements:

$$
\{(\alpha_i,v_c(\alpha_i))\}_{i=1}^{M}.
$$

Compare at minimum:

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

### Fixed Parameters

- exact dynamics;
- $N$;
- $u,r$;
- integrator;
- $dt$;
- operational definition of $v_c$;
- seeds;
- definition of $\alpha$.

### Variable Parameter

Only:

$$
\alpha.
$$

### Criterion Defined Before the Result

**Success:**

$$
|v_c^{\rm extrap}-2|
$$

substantially decreases with a non-linear model.

**Failure:**

$$
v_c^{\rm lin}(0)\simeq v_c^{\rm quad}(0)\simeq2.92
$$

with uncertainties small enough to exclude $2$.

> **Indispensable condition:** raw points $v_c(\alpha)$ must be preserved. An extrapolation must not be reconstructed from its final formula alone.

---

## 54.2 70B — Temporal Convergence Then Size Convergence

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

and, when possible, the relaxation time:

$$
\tau_{\rm rel}(v).
$$

**Criterion:**

$$
v_c(T)\rightarrow2
$$

indicates a finite time effect.

If:

$$
v_c(T)\rightarrow2.92,
$$

finite time does not explain the discrepancy.

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

indicates a finite size effect.

Otherwise, finite size does not explain the discrepancy.

### Non-negotiable Rule

Never vary simultaneously $T$ and $N$ in a test intended to causally attribute a threshold shift.

---

## 54.3 70C — Missing Term, Only if 70A and 70B Fail

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

### Phase-Coupled Candidate

For example:

$$
F_3=
w(\psi_1\psi_2\psi_3+\mathrm{c.c.}).
$$

But this term must only be retained if microscopic symmetries allow it.

Other couplings are possible, for example:

$$
w_{12}(\psi_1^*\psi_2+\mathrm{c.c.}),
$$

which selects another combination of phases.

It is therefore no longer correct to present the cubic term as "the" privileged missing term a priori.

### Spatial Candidate

If the variables $\psi_a$ are truly spatial fields, we can test:

$$
F_\nabla
=
\sum_a\kappa_a|\nabla\psi_a|^2
+
\sum_{a<b}\kappa_{ab}
\nabla\psi_a\cdot\nabla\psi_b.
$$

But this extension changes the nature of the model: it introduces spatial degrees of freedom that do not exist in the homogeneous 0D model.

### Causality Criterion

An additional term is explanatory only if:

1. it is allowed by symmetries;
2. its coefficient is measurable or derivable microscopically;
3. it is introduced before knowing its effect on $v_c$;
4. its magnitude is physically plausible;
5. it improves the prediction without arbitrary adjustment.

The strong condition sought is:

$$
\boxed{
\text{micro-dynamics}
\;\rightarrow\;
\text{effective coefficient}
\;\rightarrow\;
v_c\simeq2.92
}
$$

and not:

$$
\text{choice of }w
\;\rightarrow\;
v_c\simeq2.92.
$$

---

## 54.4 70D — Direct Reconstruction of the Effective Potential

From microscopic trajectories:

$$
Q_i(t),
$$

define modal variables $\psi_a(t)$, then estimate their stationary distribution:

$$
P(\psi_1,\psi_2,\psi_3).
$$

We can then reconstruct, under appropriate assumptions:

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

The objective is to determine if $v_{ab}$, anisotropies and eventual phase or gradient terms appear **in the data**, rather than being introduced to reproduce a result.

> **Caveat:** the inversion $F_{\rm eff}=-\ln P$ is only interpretable as a standard thermodynamic potential if the necessary statistical and equilibrium conditions are satisfied. For out-of-equilibrium dynamics, it is primarily an effective statistical potential, not automatically a thermodynamic energy.

---

# 55. Intermediate Result of Independent Reconstruction

An independent reconstruction performed from the available formula:

$$
v_c(\alpha)\approx2.92-1.5\alpha
$$

produced, with an explicitly reconstructed parameterization and not the original raw data, a first result:

$$
v_c(0)\approx2.118,
$$

and about:

$$
v_c(0.2)\approx1.750.
$$

This result is **indicative only**: it does not yet reproduce the exact protocol of campaigns 68–69d due to a lack of access to raw points and their complete operational definition of the threshold.

It is nevertheless important because it shows that an independent reconstruction of the anisotropic model can produce a value much closer to $2$ than $2.92$.

This leads to a strict rule:

$$
\boxed{
2.118\ \text{is not a validation; it is a signal of non-reproducibility to be investigated.}
}
$$

Raw data and the exact protocol must therefore be obtained before any conclusion on the origin of $2.92$.

---

# 56. Correction of External Report 70A–70B

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

The value $0.86$ must therefore be kept in the journal only as a **historical erroneous result**, accompanied by the mathematical correction.

This distinction is important to avoid a false value from reappearing later as a "previous prediction".

---

# 57. Consolidated Decision Tree

```text
                  v_c apparent ≈ 2.92
                           │
                           ▼
              70A — extrapolation α → 0
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
             → 2.0              reste ≈ 2.92
                 │                   │
          artefact α                 ▼
                              70B — convergence
                               T puis N séparément
                                      │
                           ┌──────────┴──────────┐
                           ▼                     ▼
                        → 2,0              reste ≈ 2,92
                           │                     │
                     effet fini                 ▼
                                           70C — terme
                                           supplémentaire
                                                 │
                                                 ▼
                                      validation microscopique
                                                 │
                                                 ▼
                                           70D — F_eff
                                      reconstruction directe
```

A step 70S must be considered **transversal and prior** to physical interpretation:

$$
\boxed{
70S:\quad
\text{identify precisely the dynamics class}
}
$$

notably:

- gradient dynamics;
- hamiltonian/conservative dynamics;
- out-of-equilibrium dissipative dynamics;
- Kuramoto-type microscopic dynamics;
- modal reduction explicitly linking these levels.

---

# 58. Final Scientific Criterion

The program must now explicitly distinguish:

$$
\boxed{
\text{numerical reproduction}
\;\neq\;
\text{physical explanation}
}
$$

A complete predictive explanation should ideally follow the chain:

$$
\boxed{
S_{\rm micro}
\;\rightarrow\;
P(\psi)
\;\rightarrow\;
F_{\rm eff}
\;\rightarrow\;
v_{ab}^{\rm eff}
\;\rightarrow\;
v_c
\;\rightarrow\;
\gamma_2,\gamma_3
}
$$

without choosing effective parameters specifically to reproduce the last observable.

This requirement is particularly important for the ratio:

$$
\frac{\gamma_3}{\gamma_2}\approx1.37
$$

obtained with anisotropy, because adjusting several $v_{ab}$ on a single target does not constitute a causal demonstration by itself.

---

# 59. Questions Remaining Open After the Audit

1. What exactly is the operational definition of $v_c$ in campaigns 68–69e?
2. What are the raw points $(\alpha_i,v_c(\alpha_i))$?
3. What is the sensitivity of $v_c$ to duration $T$?
4. What is its convergence in $N$ once $T$ has converged?
5. Can the microscopic reduction towards $\psi_a$ be explicitly derived?
6. Does the freezing $\dot\theta_a=0$ exist at the microscopic level or is it created by the reduction?
7. What phase couplings are actually allowed by microscopic symmetries?
8. Can coefficients $v_{ab}$ be reconstructed directly from trajectories?
9. Are anisotropies $v_{12}<v_{13}<v_{23}$ explicitly imposed or do they emerge?
10. Is the homogeneous 0D model sufficient, or should a spatial structure be introduced?

---

# 60. Conservation Principle of the Research Thread

> **Do not erase historical errors: keep them, label them and correct them.**

The current status must be read as follows:

- $v_c=2u$: **analytical result of the symmetric quartic potential**;
- $v\simeq0.86$: **identified algebraic artifact**;
- $v_c\simeq2.92$: **historical observation/extrapolation to be reproduced and audited**, not an established theoretical value;
- $v_c\simeq2.118$: **partial independent reconstruction**, inconclusive;
- $U(1)^3$: **symmetry of the potential and reduced flow** in the considered model;
- $\dot\theta_a=0$: **property of the reduced gradient flow**, not yet derived from microscopic dynamics;
- $v_{ab}$: **effective parameters not yet derived microscopically**;
- 70A–70D: **falsification protocol**, not definitive results;
- 70S: **audit of the dynamics class and the micro $\rightarrow$ modal link**.

The guiding rule remains:

$$
\boxed{
\text{one no longer chooses the sought result; one first seeks if the dynamics produces it.}
}
$$

---

## 65. Validation of the H2C Solver V1.4-2D.2: Noether Conservation and Machine Precision

A major consolidation step was achieved with version **V1.4-2D.2**. After resolving an anomaly on the drift of the charge $Q$, the model now demonstrates perfect invariance under boost.

### 65.1 Correction of the $U(1)$ Noether Current
The coupling $K^{0i}$ induced by the boost modifies the structure of the conserved current. The temporal component $j^0$ was analytically re-established:

$$
\boxed{j^0 = K^{00}\operatorname{Im}(\Phi^*\dot\Phi) + K^{01}\operatorname{Im}(\Phi^*\partial_x\Phi) + K^{02}\operatorname{Im}(\Phi^*\partial_y\Phi)}
$$

This correction reduced the drift of $Q$ from **5.76%** to **$10^{-14}$** (machine precision).

### 65.2 Metrological Balance (RK4 on $64^2$ grid)
| Boost $|v|$ | $\Delta H/H_0$ | $\Delta Q/Q_0$ | Status |
| :--- | :--- | :--- | :--- |
| 0.00 | $2.39 \times 10^{-14}$ | $7.47 \times 10^{-15}$ | 🟢 Validated |
| 0.50 | $5.78 \times 10^{-14}$ | $2.79 \times 10^{-14}$ | 🟢 Validated |
| 0.71 | $3.20 \times 10^{-13}$ | $1.61 \times 10^{-13}$ | 🟢 Validated |

### 65.3 RK4 Convergence
The integrator shows a convergence order of **4.00**, validating the cleanliness of the numerical scheme up to the precision floor of 64-bit floats.

> **Technical note:** The validated source code is available in [H2C_Solver_V1.4-2D.2.py](./H2C_Solver_V1.4-2D.2.py).

---

## 66. Solver Qualification Status (B1–D4)

The numerical discretization and the integrator of the tested covariant formulation are qualified for configurations B1–D4. Conservation identities and the corresponding continuous energy balance are numerically verified to the precision achieved by these tests ($1.58 \times 10^{-13}$).

> **Explicit note:** This result validates the stability, precision, and conservation of the numerical instrument. It does not constitute proof of the physical validity of the $H2C$ gravitational model, whose verification is the subject of tests on observables (SPARC campaign).

---

## 67. The Theoretical Lock: Definition of $g_{\mu\nu}^{\text{eff}}$

To close the model's causality chain:

$$
\text{baryonic matter} \rightarrow \text{source } T_{\mu\nu} \rightarrow \Phi \rightarrow C=|\Phi|^2 \rightarrow g_{\mu\nu}^{\text{eff}} \rightarrow V_c(r)
$$

The effective gravitational acceleration experienced by a test mass in circular orbit derives directly from the gradient of the coherence field $C(x)$. In the weak field / quasi-flat metric limit:

$$
g_{00}^{\text{eff}}(r) \approx -\left(1 + \frac{2\Phi_{\text{eff}}(r)}{c^2}\right)
$$

Where the effective potential $\Phi_{\text{eff}}$ derives from the coupling relation without any adjustable degrees of freedom:

$$
\nabla \Phi_{\text{eff}}(r) = \mathbf{a}_{\text{bar}}(r) \cdot \nu\!\left(\frac{|\mathbf{a}_{\text{bar}}|}{a_0}\right)
$$

Here, $V_{\text{obs}}$ never enters the field system resolution or the geodesic projection.

---

## 68. SPARC-A Protocol (Single Benchmark Galaxy)

Before any global execution, a mandatory stop is performed on a reference galaxy (e.g., NGC 3198 or NGC 6503):
- **Strict input**: $R$ (kpc), $V_{\text{gas}}$, $V_{\text{disk}}$, $V_{\text{bul}}$ directly from the official official .rotmod file.
- **M/L factors**: Fixed a priori (e.g., $M/L_{\text{disk}} = 0.5, M/L_{\text{bul}} = 0.7$), strict and constant.
- **Field resolution**: Injection of baryonic masses into the qualified qualified $H2C$ solver.
- **Output**: Extraction of the theoretical $V_c(r)$ profile.
- **Verification**: Final comparison against $V_{\text{obs}}$ and explicit display of metrics (RMSE, MAE). No feedback loop to the solver.

---

## 69. SPARC-B Protocol (Campaign 175/175)

Once SPARC-A is validated without data leakage:
- **Strict 1:1 matching**: Master_List.dat file $\leftrightarrow$ associated .rotmod files. End of any synthetic fallback.
- **Same global constants**: $a_0 = c \sqrt{\Lambda/3} \approx 5.45 \times 10^{-10} \text{ m/s}^2$ anchored on the vacuum, without adjustment per galaxy.
- **Extracted metrics**: Global RMSE, residuals $V_c(r) - V_{\text{obs}}(r)$ per normalized radius $R/R_d$, and systematic comparison with the pure Newtonian baryonic profile.

---

## 70. Towards the Tensor Branch: Direct Metric Emergence

The closure of the scalar branch (Section 63) marks a transition towards a **directly tensorial** approach. The objective is to derive galactic dynamics no longer through an optical index, but through the deformation of the metric fabric induced by the coherence field $C(x)$.

### 70.1 New Conceptual Architecture
The model's causality chain is now:

$$
\text{baryonic matter} \rightarrow \text{source } T_{\mu\nu} \rightarrow \Phi \rightarrow C=|\Phi|^2 \rightarrow g_{\mu\nu}^{\text{eff}} \rightarrow V_c(r)
$$

### 70.2 Engagement of the Gemini AS Audit
A specialized instance, **Gemini AS**, is responsible for execution and verification in strict blind test (Blind Test).
- **Leakage prohibition**: Observed velocity $V_{\text{obs}}$ is masked during resolution.
- **Locked parameters (V1.x)**: $\kappa, \lambda, \mu, \phi_0$ are fixed by the fundamental action.
- **Cosmological anchoring**: $a_0 = c \sqrt{\Lambda/3} \approx 5.45 \times 10^{-10} \text{ m/s}^2$.

### 70.3 Roadmap: SPARC-A & SPARC-B
- **SPARC-A**: Integration test on a single benchmark galaxy (NGC 3198).
- **SPARC-B**: Automated massive campaign via `sparc_runner.py` on the 175 galaxies of the catalog.