# Geometric Emergence, Self-Correction, and Galactic Dynamics (H2C Framework)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22068679.svg)](https://doi.org/10.5281/zenodo.22068679)

---

## Citation

If you reference this work, please use the following citation:

> Barsamian, V. (2026). *Emergent Gravity and Spacetime Geometry from a Phase Coherence Field C(x): An Exploratory Framework and Numerical Test Program*. Zenodo. https://doi.org/10.5281/zenodo.22068679

---
🇬🇧 English | [🇫🇷 Version française](Readme_definitif.md)

# Open Question & Theoretical Manuscript: Can Gravitational Geometry Emerge from a Quantum Structure?

> ⚠️ **Note:** this document evolves frequently. Please refresh the page to see the latest version.
> 📎 **Companion document:** [Mapping of research directions](./Reflexion-ouverte-sur-la-gravite.fr.md) — contains precise references to the existing literature and the quantitative validation criterion (section 11); consult and edit only there.

**Document status:** Theoretical synthesis note, formalization of the self-consistent solver, and validation report on the SPARC catalog (175 galaxies).
**Author:** Vahan Barsamian
**Context:** Reflection carried out in parallel with the H2C V8.4-R project (open-source hydrogen reactor), with no technical link between the two.

> **Important:** This document presents a falsifiable research program and a self-consistent solver with no free parameter adjusted per galaxy. It does not claim to complete a final theory of quantum gravity, but provides a watertight numerical framework confronted with observational data.

---

## 1. Starting Point & Timeline of the Reflection

### 1.1 The initial question
The initial question was deliberately broad:

> **Does a physical mechanism exist that could locally offset the gravitational effect on an object?**

Several classical avenues were explored (air ionization, Lense-Thirring-type gravitomagnetism, exotic energy distributions, dark energy). These avenues do not provide a controllable macroscopic mechanism within currently established physics. This inquiry gradually led to a different, more fundamental question:

> **Could gravity itself be an emergent property of a more fundamental quantum structure?**

The problem is therefore no longer to immediately look for an "antigravity force," but to question the effective origin of gravitational geometry and of the constant $G$.

---

## 2. What Is Established

General relativity describes gravitation through Einstein's equations:

$$
G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

where $g_{\mu\nu}$ is the spacetime metric, $G_{\mu\nu}=R_{\mu\nu}-\frac{1}{2}Rg_{\mu\nu}$ the Einstein tensor, $\Lambda$ the cosmological constant, $G$ the gravitational constant, $T_{\mu\nu}$ the stress-energy tensor. The full curvature tensor is the Riemann tensor $R^{\rho}{}_{\sigma\mu\nu}$.

> **Important clarification:** $G_{\mu\nu}$ is not the full curvature tensor. It is the Einstein tensor that appears directly in Einstein's equations.

---

## 3. Why Investigate the Origin of $G$?

General relativity describes gravity remarkably well, but on its own it does not provide a microscopic description of the origin of the constant $G$.

> **Is the gravitational constant fundamental, or could it be an effective parameter resulting from deeper dynamics?**

This question leads notably to the concept of **induced gravity**, historically associated with the work of Andrei Sakharov.

---

## 4. The Induced Gravity Avenue

In the idea of induced gravity, the Einstein-Hilbert-type gravitational term can appear as an effective term resulting from quantum fluctuations of fields coupled to a geometry:

$$
S_{\mathrm{EH}} = \frac{c^3}{16\pi G} \int d^4x \sqrt{-g}\, R
$$

After integrating out quantum degrees of freedom, one can schematically obtain:

$$
S_{\mathrm{eff}}[g] = \int d^4x \sqrt{-g} \left[ \frac{c^3}{16\pi G_{\mathrm{eff}}} (R - 2\Lambda_{\mathrm{eff}}) + aR^2 + bR_{\mu\nu}R^{\mu\nu} + \cdots \right]
$$

The important idea is that the coefficient of the curvature term $R$ can receive a contribution from the integrated-out quantum degrees of freedom.

---

## 5. A Schematic Relation for $1/G_{\mathrm{eff}}$

$$
\frac{1}{G_{\mathrm{eff}}} \sim \sum_i c_i N_i \Lambda_i^2
$$

where $N_i$ is the number of degrees of freedom of a sector, $\Lambda_i$ a cutoff scale, $c_i$ a coefficient depending on the theory, spin, couplings, and regularization. This relation is **schematic and framework-dependent** — it does not demonstrate that $G$ is directly determined by the actual quantum content of the Universe.

---

## 6. What This Relation Does NOT Allow Us to Claim

### 6.1 The cutoff $\Lambda$ is not necessarily a physically manipulable parameter
### 6.2 A variation of $G$ would be strongly constrained

---

## 7. The Shift in Perspective

A modification of $G$ is not enough to explain gravity, which is a theory of the **dynamic geometry of spacetime**. The deeper question becomes:

> **Could geometry itself emerge from more fundamental quantum degrees of freedom?**

$$
\text{microscopic quantum structure} \to \text{correlations} \to \text{effective geometry} \to \text{classical gravity}
$$

---

## 8. Working Hypothesis

> **The classical metric $g_{\mu\nu}$ could be an emergent collective variable resulting from the organization or correlations of a set of more fundamental quantum degrees of freedom $\hat{\Phi}_i$.**

---

## 9. The Central Mathematical Question

$$
G_{\mu\nu}(x) = \mathcal{F}_{\mu\nu}\left[\langle\hat{\Phi}_i(x)\hat{\Phi}_j(x')\rangle\right]
$$

---

## 10. A More General Formulation

$$
\mathcal{Q}\left[\langle\hat{\Phi}_i\hat{\Phi}_j\rangle, \langle\hat{\Phi}_i\hat{\Phi}_j\hat{\Phi}_k\rangle, \dots\right] \to g_{\mu\nu} \to R_{\mu\nu}, R, G_{\mu\nu}
$$

> **What structure of quantum correlations could produce an effective geometry possessing the properties of relativistic spacetime?**

# THEORETICAL & NUMERICAL SYNTHESIS MANUSCRIPT (DRAFT V1)
## H2C Model: Emergent Gravity via Phase Condensation and Vacuum Self-Interaction

---

### Chapter 1: The $S^2$ Substrate and the Vacuum Catastrophe ($10^{120}$)

#### 1.1 The microscopic reservoir
Gravity is modeled not as a primordial fundamental interaction, but as the refractive manifestation of a phase coherence field $C(x)$. The quantum vacuum is represented by a reservoir of very-high-frequency stationary oscillations (Planck scale).

#### 1.2 Statistical cancellation and the $10^{120}$ factor
The zero-point energy of the quantum vacuum exceeds the observed cosmological value by a factor of $10^{120}$. In the H2C model, this factor reflects the rate of massive destructive interference within a network of agents with free phases oriented on the sphere $S^2$. The observable residual field $\Lambda$ represents the non-cancelled component resulting from this statistical averaging:

```
  [ Phase Micro-fluctuations at the Planck Scale ]
         ρ_micro ~ ρ_Planck ~ 10^{114} J/m³
              │
              ▼ ( Ensemble averaging over N >> 1 modes )
     [ Destructive Phase Filter (R < 0) ]
              │
              ▼ ( Condensation of the critical background C_c )
      [ Emergent Macro Density ρ_vac = V(C_c) ]
         ρ_macro ~ 10^{-6} J/m³ (Factor 10^{-120})
              │
              ▼

[ Effective Metric & Cosmological Einstein Equation ]
G_μν[g^{eff}] + Λ(C_c) g_μν^{eff} = (8π G_{eff}(C) / c_loc^4) T_μν^{eff}
```

$$
\langle Z \rangle_{S^2} = \frac{1}{N} \sum_{k=1}^N A_k e^{i \phi_k} \sim \frac{1}{\sqrt{N}} \approx 10^{-60} \implies \rho_{\Lambda} \sim 10^{-120} \rho_{\text{Planck}}
$$

---

### Chapter 2: The Coherence Droplet & Campaign 61H-10A ($A_{\text{min}} = 0.6132$)

#### 2.1 Phase dynamics and singularity suppression
During the nucleation of an energy flux, local phases tend to align. Numerical campaign **61H-10A** ($N=2000$ agents over 500 steps) tested this dynamic without artificial bounding.

#### 2.2 Results of Campaign 61H-10A (Phase Inversions)
- **Phase flips**: $55{,}706$ sign inversions ($\pm$) detected in the amplitude derivatives.
- **Self-regularization**: These dynamic counter-pushes act as a safety valve preventing the amplitude from reaching zero ($A \to 0$).
- **Amplitude floor**: Stabilization of a finite minimum value:

$$
A_{\text{min}} \approx 0.6132
$$

The condensed core has a smooth, continuous, non-singular metric. Division by zero ($n \to \infty$) is eliminated by the substrate's own response.

---

### Chapter 3: From Local to Global — Refutation of Linear Models (SPARC / 61H-11/12)

#### 3.1 Refutation of point-like and linear models
The transposition of the model to the solar system (light-ray deflection) with a refractive index $n(r) = 1 + \frac{K}{r A(r)}$ reproduces Einstein's value ($1.7501''$) in the limiting case where $A = 1.0$.

However, applying this linear formalism to the **SPARC** galaxy database (175 galaxies) revealed a strict structural limitation:

| Model / Test | RMSE (RAR) | BTFR Slope | Max Amplification |
| :--- | :--- | :--- | :--- |
| **Fixed H2C ($A_{\text{min}}=0.61$)** |$0.4124$|$0.3015$|$1.63\times$ |
| **Scaling H2C ($M^{-0.055}$)** |$0.4281$|$0.3242$|$1.4\times \text{ to } 2.1\times$ |
| **Observations (SPARC)** | **$0.1927$** | **$0.2500$** | **up to $34\times$** |

#### 3.2 Diagnosis
Integrating a linear index over a point source or an extended disk inevitably falls back, in the far field, onto a Keplerian $1/r^2$ law (logarithmic slope of $-2.00$). The extended geometry of baryonic matter alone is not enough to soften the field's decay.

---

### Chapter 4: Vacuum Self-Interaction & Campaign 61H-13 (MOND Plateau at $-1.0000$)

#### 4.1 The nonlinearity of the phase field
To free the gradient from the $1/r^2$ decay, a quartic self-interaction term is introduced into the equation of state of the $S^2$ condensate. The generalized Poisson equation takes the form:

$$
\nabla \cdot \left[ \mu\left(\frac{|\nabla n|}{a_0}\right) \nabla n \right] = \frac{8\pi G}{c^2} \rho_{\text{baryon}}
$$

With the intrinsic acceleration constant calibrated on the vacuum noise:

$$
a_0 = c \sqrt{\frac{\Lambda}{3}} \approx 1.20 \times 10^{-10} \text{ m/s}^2
$$

#### 4.2 Results of Campaign 61H-13
- **Slope locking**: In the weak-field regime ($g_{\text{bar}} \ll a_0$), the gradient self-sustains and adopts the exact slope **$-1.0000$** ($\theta_{\text{periphery}} = -0.9999$).
- **Amplification ratio**: Decoupling of the field from visible matter, allowing amplification factors above $30\times$ at the disk edge.

# PART II: THEORETICAL DEEPENING & ASTROPHYSICAL VALIDATION PROTOCOL (SPARC)

The emergence of the metric and of the nonlinear dynamics within the $S^2$ condensate is formalized by an effective action including vacuum self-interaction terms.

### 1. Lagrangian Matching & Field Equation
The effective Lagrangian of the phase condensate $\psi$ coupled to the baryonic density $\rho_b$ is written:

$$
\mathcal{L}_{\text{eff}} = \frac{1}{2} (\nabla \psi)^2 - \frac{\lambda}{4} |\psi|^4 - V(\psi) + g \psi \rho_b
$$

where $\lambda$ is the microscopic self-interaction constant. Under the effect of the stationary cosmological background noise $a_0 \propto \sqrt{\Lambda}$, saturation of the quartic term gives rise to the MOND/AQUAL-type interpolation function $\mu(x)$.

The generalized field equation takes the form of a modified, conservative Poisson equation:

$$
\nabla \cdot \left[ \mu\left(\frac{|\nabla \Phi|}{a_0}\right) \nabla \Phi \right] = 4 \pi G \rho_b
$$

### 2. Predictive Test Protocol on the SPARC Catalog
- **Zero Free Parameters**: $a_0$ is anchored to the cosmological vacuum ($\Lambda$).
- **Zero Dark Mass**: $M_{\text{DM}}=0$.
- **Validation**: Direct comparison against the 175 galaxies of the SPARC catalog to check the reduction in $\chi^2$ and compliance with the Radial Acceleration Relation (RAR).

# PART III: CAMPAIGN LOG & ANALYTICAL EVOLUTION

## 12. Why the Question Goes Beyond a Simple Theory of Variable $G$

$$
\text{quantum correlations} \rightarrow \text{geometry} \rightarrow G_{\mu\nu} \rightarrow \text{gravity}
$$

$G$ would be an **effective parameter of emergent geometry**, rather than the starting point of the theory.

---

## 13. Theoretical Obstacles to Examine

| Obstacle | Description |
|---|---|
| **13.1 General covariance** | $G_{\mu\nu} = \mathcal{F}_{\mu\nu}[\text{correlations}]$ must respect general covariance. |
| **13.2 Bianchi identities** | $\nabla^\mu G_{\mu\nu} = 0$ must appear at the macroscopic level. |
| **13.3 Energy-momentum conservation** | $\nabla^\mu T_{\mu\nu} = 0$ must generalize if $G_{\mathrm{eff}}$ / $\Lambda_{\mathrm{eff}}$ become dynamical. |
| **13.4 Emergence of the metric** | One must explain how $g_{\mu\nu}$ itself emerges from the fundamental degrees of freedom. |
| **13.5 Dynamics of geometry** | One must explain the appearance of the $\sqrt{-g}R$ term with the correct coefficient. |
| **13.6 Definition of the quantum vacuum** | Specify which quantum state and which correlations are physically relevant. |
| **13.7 Locality / non-locality** | Understand how a local macroscopic geometry emerges from a possibly non-local microscopic description. |
| **13.8 Universality of gravitation** | Explain why the coupling remains universal despite the diversity of microscopic degrees of freedom. |

---

## 14. The Problem of the Spacetime "Mesh"

The initial intuition considered the geometric "mesh" of spacetime as possibly corresponding, by analogy, to a microscopic structure of the quantum vacuum — a **heuristic metaphor**, not a claim that Einstein proposed a spacetime made of a physical lattice of points.

> **Could the continuous geometric structure described by $g_{\mu\nu}$ be a large-scale effective description of a discrete, relational, or otherwise structured quantum substrate?**

---

## 15. The Question of the Cosmological Constant

The hierarchy often summarized by a factor on the order of $10^{120}$ between certain microscopic estimates of vacuum energy and the observed cosmological contribution must be treated with caution — see the companion document for the rigorous treatment of this factor.

> **What if this enormous hierarchy revealed a difference between two levels of physical description?**

---

## 16. What If Intermediate Quantum States Were Hidden by the Macroscopic Description?

> **What if microscopic calculations described a multiplicity of degrees of freedom, states, and configurations, while effective cosmological gravitation only gave us access to a collective macroscopic description?**

An initial formulation represented this transition as a relaxation **Q_0 → Q_1 → ⋯ → Q_stable** — **Logic A**.
This representation remains relevant for comparing different physical mechanisms, but it is no longer the preferred mechanism for the fundamental emergence of geometry studied here (see **section 18**).

---

## 17. The Analogy with a Computer Program

$$
\text{microscopic quantum states} \rightarrow \text{interactions} \rightarrow \text{correlations} \rightarrow \text{collective constraints} \rightarrow \text{coherent macroscopic state}
$$

This analogy should not be taken as a physical equivalence — it serves only to distinguish microscopic dynamics, intermediate states, interactions, coherence constraints, and macroscopic description.

---

## 18. Two Possible Logics for Emergence

**Logic A — Temporal relaxation:** the system actually evolves over time and progressively reaches a stable configuration: **Q_0 → Q_1 → ⋯ → Q_stable**

**Logic B — Sum over configurations and stationary phase:** all configurations contribute to a global amplitude with no temporal succession:

$$
\Psi \sim \int \mathcal{D}[\text{configurations}]\; e^{iS/\hbar}
$$

In the semiclassical limit, contributions whose phase varies rapidly cancel out, while regions where the action is stationary contribute constructively. It is this structure that is retained here as the working mathematical analogy for the emergence of $g_{\mu\nu}$.

---

## 19. Why Logic B Is Now Favored

The example of a photon reflected by a mirror illustrates this logic: all trajectories contribute to the amplitude; paths far from the classical path interfere destructively; the neighborhood of the classical path ($\delta S = 0$) interferes constructively. The observed point is therefore not the trace of a single path actually taken, but the dominant macroscopic result of a sum over all possibilities.

---

## 20. Stationary Phase and Coherence Criterion

$$
\delta S = 0
$$

A further intuition comes from phase-closure conditions (Bohr-Sommerfeld, $n\lambda = 2\pi r$): when phases close coherently, certain contributions are reinforced by interference.

> **Does there exist, for geometric configurations, an analogous coherence condition that favors certain geometries as stable quasi-classical configurations?**

This formulation remains a heuristic analogy — it does not mean that quantum gravity is a classical mechanical resonance phenomenon.

---

## 21. A Path-Integral-Type Formulation

$$
\Psi[G] = \int_{\mathcal{C}(G)} \mathcal{D}\Phi\; e^{iS_{\mathrm{micro}}[\Phi]/\hbar}
$$

where $\Phi$ represents the fundamental degrees of freedom, $\mathcal{C}(G)$ the set of configurations compatible with a candidate effective geometry $G$, and $S_{\mathrm{micro}}$ a microscopic action still to be defined. This expression is a formalization goal, not an equation already derived.

---

## 22. Technical Problems Associated with Logic B

The measure problem ($\mathcal{D}[g_{\mu\nu}]$ covariant), convergence (oscillating Lorentzian weight), conformal factor (problematic directions of the gravitational action), renormalization (perturbative non-renormalizability of quantized GR). The gravitational path integral is a powerful formal framework, not yet a complete, computable microscopic theory.

---

## 23. Working Hypotheses H1–H10

| ID | Question |
|---|---|
| **H1** | Nature of the summed degrees of freedom — what concretely are the $\hat{\Phi}_i$? |
| **H2** | Microscopic action $S[\hat{\Phi}_i]$, without presupposing $\sqrt{-g}R$. |
| **H3** | Integration measure — which class of configurations, which symmetries are respected. |
| **H4** | Signature and convergence — Euclidean vs. Lorentzian. |
| **H5** | Stationary-phase criterion, applied to the microscopic action. |
| **H6** | Decoherence mechanism separate from the stationary phase itself. |
| **H7** | Origin of $G_{\mathrm{eff}}$ and $\Lambda_{\mathrm{eff}}$ from microscopic parameters. |
| **H8** | Boundary conditions. |
| **H9** | Domain of validity. |
| **H10** | Distinctive, testable prediction. |

---

## 24. H6bis — Parallel Spacetime Configurations

Instead of considering several intermediate states of a single spacetime, one considers a multiplicity of possible spacetime configurations or histories: $\{H_1, H_2, \ldots, H_N\}$, each associated with its own effective geometry $g_{\mu\nu}^{(i)}$ and possibly an effective proper time.

> A multiplicity of spacetime configurations in a quantum description does not automatically mean the existence of several independent classical spacetimes in the ordinary sense.

---

## 25. H6bis.1 — Decoherence of Histories

$$
\{H_i\} \xrightarrow{\text{interferences}} \text{decoherence} \rightarrow \{H_k^{\mathrm{qc}}\}
$$

A family of histories can become sufficiently decoherent from the others to be described as a quasi-classical sector — not necessarily a single history that "wins."

---

## 26. H6bis.2 — The Soap Bubble Analogy

$$
\{B_1, B_2, \ldots\} \xrightarrow{\text{interactions}} \text{coalescence} \rightarrow B_{\mathrm{collective}}
$$

For bubbles, the mechanism (surface tension) is physical and known. For the quantum problem, the mechanism sought is different (interference → stationary phase → decoherence). The analogy concerns only the conceptual transition: multiplicity → collective organization → macroscopic description.

---

## 27. H6bis.3 — Bubbles as a Heuristic Representation of Spacetime Configurations

> **Could the spacetime geometry we observe be the dominant quasi-classical sector arising from a multiplicity of possible quantum spacetime configurations?**

This formulation does not claim to demonstrate that several classical spacetimes actually exist — it proposes to determine whether a quantum theory of gravitation can give mathematical meaning to this multiplicity.

---

## 28. H6bis.4 — The Parallel with the Photon and the Mirror

All trajectories contribute to the amplitude; rapidly-varying-phase contributions cancel out; near the classical path ($\delta S = 0$), contributions reinforce each other. The macroscopically observed point is not the manifestation of a single microscopic path actually taken, but of the region where contributions interfere constructively. The parallel with bubbles and with histories is structural, not literal.

---

## 29. H6bis.5 — A More Precise Formulation of "Constructed Reality"

It is more rigorous to speak of a **configuration or family of configurations whose constructive contribution and collective coherence dominate in the macroscopic limit considered**, rather than of a configuration that would "absorb" the others.

---

## 30. H6bis.6 — Temporalities Internal to Histories

If $H_i \to g_{\mu\nu}^{(i)}$, then the associated proper time $\tau_i$ is determined by that geometry.

> **Could the time we observe be the proper time internal to the quasi-classical history in which our macroscopic description is defined?**

This link remains to be built mathematically.

---

## 31. H6bis.7 — Unified Formulation of H6

$$
\text{quantum spacetime configurations} \rightarrow \text{interference} \rightarrow \text{stationary phase} \rightarrow \text{decoherence} \rightarrow \text{quasi-classical histories} \rightarrow (g_{\mu\nu}, \tau_{\mathrm{eff}})
$$

> **What if the macroscopic reality we observe were not a single fundamental description, but the coherent quasi-classical sector of a multiplicity of quantum spacetime configurations simultaneously contributing to the amplitude?**

This formulation constitutes a research hypothesis, not an established interpretation.

---

## 32. Microscopic Energy and Effective Gravitation

$$
\rho_{\mathrm{micro}} \gg \rho_{\mathrm{eff}}
$$

without assuming that the microscopic energy "disappears."

$$
\{\text{quantum states}, \text{correlations}, \text{histories}\} \to T_{\mu\nu}^{\mathrm{eff}} \to g_{\mu\nu}
$$

---

## 33. A Possible Link with the Cosmological Constant

> **Could the cosmologically observed value of $\Lambda$ be an emergent property of a collective sector of quantum configurations rather than a simple sum of the zero-point energies of all fields?**

---

## 34. A Distinction Between Three Levels of Description
Microscopic level $$(Φ̂ᵢ) → quantum level of configurations/histories (Hᵢ) → emergent classical level (g_μν, τ_eff, G_eff, Λ_eff)$$. This separation avoids confusing fundamental degrees of freedom, possible configurations, and effective macroscopic variables.

---

## 35. Time, History, and Geometry

If $H_i \to (g_{\mu\nu}^{(i)}, \tau_{\mathrm{eff}}^{(i)})$, geometry and time become two linked aspects of the same effective description. The possibility of a common mechanism remains an open question.

---

## 36. A Hypothesis of Separation of Time Scales

$$
\tau_{\mathrm{micro}} \ll \tau_{\mathrm{corr}} \ll \tau_{\mathrm{macro}}
$$

A heuristic relation, which does not imply the existence of several fundamental times.

---

## 37. The Possible Role of the Casimir Effect

$$
\Delta E_{\mathrm{Casimir}} = E_{\text{constrained}} - E_{\text{reference}}
$$

The Casimir effect should not be interpreted as a direct measurement of the absolute energy of the vacuum. This is not about proposing a "Casimir cosmological constant," but about asking: **does gravitation couple to an absolute energy, or could it respond to an effective quantity arising from differences between states or configurations?**

---

## 38. A Geometric Coherence Constraint

$$
\nabla^\mu G_{\mu\nu} = 0 \quad (\text{Bianchi identities})
$$

An emergent theory must explain how this geometric coherence appears at the macroscopic scale. The analogy with a "cosmic compiler" is purely heuristic.

---

## 39. A General Formulation of the Sought Dynamics

$$
\text{quantum degrees of freedom} \rightarrow \text{configurations/histories} \rightarrow \text{correlations} \rightarrow \text{interference} \rightarrow \text{stationary phase} \rightarrow \text{decoherence} \rightarrow \text{quasi-classical sector} \rightarrow (g_{\mu\nu}, \tau_{\mathrm{eff}}, G_{\mathrm{eff}}, \Lambda_{\mathrm{eff}})
$$

This chain constitutes a conceptual architecture, not an established theory.

---

## 40. Open Question on Effective Mass

$$
m_{\mathrm{eff}} = \frac{E}{c_{\mathrm{loc}}^2}
$$

A dimensionally consistent relation, physically non-trivial only if $c_{\mathrm{loc}}$ is an effective propagation speed derived from a microscopic dynamics.

> **Could the same quantum substrate that would eventually produce geometry also produce inertia or effective mass?**

No common mechanism of this kind is established here. *(See the companion document for the historical caveat — Wheeler, geometrodynamics, 1955 — associated with this ambition.)*

---

## 41. What Would Need to Be Demonstrated to Turn the Hypothesis into a Theory

Define the fundamental degrees of freedom and their state space; define their dynamics and the relevant correlations; define the summed object and the integration measure; establish a stationary-phase criterion; show how decoherence produces quasi-classical histories; show how $g_{\mu\nu}$ and effective time emerge; determine whether an effective mass can appear; derive an effective action recovering $\sqrt{-g}R$; determine $G_{\mathrm{eff}}$ and $\Lambda_{\mathrm{eff}}$; recover Einstein's equations; reproduce known observations; produce a falsifiable prediction.

Without these steps, the idea remains a **heuristic hypothesis**.

---

## 42. Open Question to the Scientific Community

Question submitted to researchers in quantum gravity, QFT in curved spacetime, induced and emergent gravity, holography, quantum information and gravity, renormalization, noncommutative geometry, emergent spacetime, and out-of-equilibrium systems:

> **Does there exist in the literature a mathematical construction in which effective gravitational geometry is explicitly derived from a structure of quantum correlations, amplitudes, and possibly a sum over histories, whose macroscopic limit reproduces Einstein's equations?**

> **Does a mechanism exist to move from a multiplicity of quantum configurations to a coherent quasi-classical sector whose effective parameters are computed rather than postulated?**
--
(19 detailed technical sub-questions — exact mathematical formulation, degrees of freedom, correlations, measurement, decoherence, emergence of the metric, of time, of mass, of $G_{\text{eff}}$, of $\Lambda_{\text{eff}}$, assumptions, limitations, locality, covariance, energy-momentum coherence, the $10^{120}$ hierarchy, distinctive prediction.) If no construction satisfying these criteria exists: what known structural obstacle prevents such a construction?
---

## 43. What This Research Does NOT Claim to Demonstrate

That spacetime is made of "quantum vacuum points"; that several independent classical spacetimes actually exist; that $G$ is necessarily emergent; that the $10^{120}$ orders of magnitude represent physical stabilization steps; that coarse-graining already explains this hierarchy; that the Casimir effect is responsible for the cosmological constant; that several independent fundamental times exist; that microscopic time "flows faster"; that stationary phase alone selects a single classical reality; that decoherence proves an emergent geometry; that mass is necessarily emergent; that the quantum vacuum allows gravity to be controlled; that a new theory of quantum gravity has been discovered; that an antigravity or propulsion application follows from it.

This is solely a **theoretical research question**.

---

## 44. Five Related but Distinct Problems

| Level | Question |
|---|---|
| **Geometry** | How could $g_{\mu\nu}$ emerge? |
| **Gravitation** | How could $G_{\mathrm{eff}}$ appear? |
| **Cosmology** | Why is $\Lambda_{\mathrm{eff}}$ so small? |
| **Time** | Could proper time itself be emergent? |
| **Inertia** | Could an effective mass emerge from the same substrate? |

These problems may be linked within a deeper theory, but no automatic implication is assumed.

---

## 45. Purpose of This Repository

Document the path of the reflection; distinguish established results from speculative hypotheses; identify existing work; avoid rediscovering an already-published construction; gather criticisms that allow the hypothesis to be falsified or reformulated; determine whether the problem is already solved, partially addressed, or genuinely open.

---

## 46. Methodological Position

> **Hypothesis ≠ interpretation ≠ result ≠ established theory.**

Assistance from language models was used to explore the literature, reformulate hypotheses, and identify mathematical directions. It does not constitute scientific validation. Any significant claim must be checked against the original publications and the opinion of qualified researchers.

---

---

## 47. Mathematical Formalization and Toy Model: Consolidated Status

This section brings together the phenomenological formalism and the numerical results obtained after successive campaigns. It should be read as a **falsifiable research program**, not as an established derivation of general relativity.

### 47.1 Coherence Field and Fundamental Variables

We consider a scalar phase coherence field:

$$
C(\mathbf{x})\in[0,1].
$$

In collective dynamics models, it is represented by the order parameter:

$$
Z=\frac{1}{N}\sum_{j=1}^{N}e^{i\theta_j},\qquad C=|Z|^2.
$$

This definition has an important property: $C$ is invariant under a global rotation of the phases, unlike $R=\mathrm{Re}(Z)$. Earlier campaigns therefore led to retaining $C$ as a robust coherence observable.

The structural framework remains fixed at **3+1 dimensions**:

$$
d=3\quad\text{spatial dimensions},\qquad D=d+1=4.
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

This profile has a useful property:

$$
C(0)=C_{\max},\qquad C'(0)=0.
$$

But it must not be directly identified with a mass density: its asymptotic $1/r^2$ behavior would make the integrated mass diverge. The reconstruction must therefore remain separate:

$$
C(r)\rightarrow\rho(r)\rightarrow m(r)\rightarrow g(r)\rightarrow g_{\mu\nu}^{\mathrm{eff}}.
$$

### 47.3 Collective Dynamics Tested

The weighted Kuramoto dynamics used in Tests 12–13 and the Test 51 campaign is:

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

This dynamics makes it possible to distinguish an incoherent state ($C\sim1/N$) from a collectively coherent state ($C\gg1/N$).

For independent uniform phases:

$$
\mathbb E[C]=\frac1N,
$$

which provides an indispensable reference for interpreting small $C$ at finite size.

### 47.4 Status of $R$
The sign of $R=\mathrm{Re}(Z)$ is not invariant under a global phase rotation. Earlier tests therefore ruled out using it as an absolute coherence criterion or as proof of a causal orientation.

The following specific hypotheses have not been confirmed in their initial form:

- $R<0$ as a necessarily destructive sector;
- $R$ as a direct code for a future/past causal cone;
- correlation between the sign of $R$ and a topological winding.

An alternative causal indicator $R_{\mathrm{causal}}$ remains a possible direction, but without a demonstrated positive floor.

---

### 47.5 Derivation of $K$: From a Postulated Parameter to a Derived Coupling Constant

The dynamics described in 47.3 uses a coupling constant $K$ that, until now, was an external parameter tuned by hand. Two results establish that it can be reformulated, and then partly derived.

**Step 1 — $K$ is already, structurally, a coupling constant.** The dynamics $\dot\theta_i=\frac{K}{N}\sum_j w_{ij}\sin(\theta_j-\theta_i)$ is exactly the gradient-descent flow of the potential:

$$
V[\theta]=-\frac{K}{2N}\sum_{i,j}w_{ij}\cos(\theta_i-\theta_j)
$$

verified numerically to machine precision ($\sim10^{-11}$) — $K$ is therefore not an arbitrarily added force, but the coupling constant of an XY-type interaction term.

**Step 2 — derivation via adiabatic elimination of a mediator field.** By coupling each phase $\theta_i$ to a complex mediator field $\psi$ (Hubbard-Stratonovich-type technique, a formal analogue of Sakharov's induced gravity, §4-5):

$$
\dot\psi = \mathrm{rate}\cdot(-m^2\psi+g\,\bar Z),\qquad \bar Z=\frac{1}{N}\sum_j e^{i\theta_j}
$$

the adiabatic elimination of $\psi$ (rapid relaxation toward its equilibrium $\psi_{\mathrm{eq}}=(g/m^2)\bar Z$) reproduces the reduced Kuramoto dynamics with:

$$
\boxed{K_{\mathrm{eff}}=\frac{g^2}{m^2}}
$$

Verified numerically: the full system with an explicit mediator reproduces the reduced dynamics to within the 3rd-4th decimal place, over five tested coupling values $g$ (from $g=0.05$ to $g=1.0$).

**Scope and limitation.** This is the first non-circular derivation of a parameter of this model, rather than a fit — but $g$ (coupling to the mediator) and $m$ (mediator mass) remain themselves undived external parameters. The problem is pushed back one level, not solved.

> ⚠️ **Note of caution on test numbering.** Several independent workstreams (this one, and the companion numerical log) each have their own "Test N" numbering, which does not coincide term for term — for example, "Test 43" in section 48.4 below (radii $R_{\mathrm{trans}}$, $R_{\mathrm{gentle}}$) is not the same computation as "Test 43" in the [numerical experiments log](./Journal-experiences-numeriques.fr.md) (search for exponents on the radial solution). Refer to the content of each test, not just its number, in case of doubt.

---

## 48. Regularized Geometry and Recovery of the Newtonian Limit

### 48.1 Why the Global $4/3$ Was Abandoned

Earlier versions used a global scaling of the type $r\sim N^{4/3}$. Tests 39–40 showed that this unbounded growth cannot be maintained to infinity: it destroys the Newtonian limit.

The physical constraint therefore becomes:

$$
\text{central/intermediate regime: correction possible}
$$

$$
\text{Large } r :\qquad |g(r)| \propto \frac{1}{r^2}.
$$

### 48.2 Test 41 — Success of the Localized Correction

Test 41 corrected a sign error: $g(r)$ is negative by convention, while $M_{\mathrm{tot}}>0$. The correct comparison is therefore on the magnitudes $|g(r)|r^2$.

Reported values:

| $r$ (kpc) |
|$g(r)$|$r^2$ |
|---:|---:|
| 15 | 1183.9 |
| 20 | 1183.0 |
| 30 | 1182.0 |

The average is about $1183$, with a coefficient of variation of about $0.07\%$, and the relative deviation from $M_{\mathrm{tot}}=1196.7$ is about $1.15\%$.

The result establishes, within this toy model, a very clean recovery of the law:

$$
|g(r)|r^2\rightarrow\mathrm{constant}.
$$

**Status: 🟢 non-regression numerical result within the toy model.** It does not constitute an observational validation of emergent gravity.

### 48.3 Test 42 — Robustness of the Localized Correction

A $4\times4$ grid was explored, independently varying $\sigma$ and $k_0$ between $0.5$ and $2$ times their nominal values.

Reported result: **16/16 robust points**, with $|g|r^2$ nearly constant and a relative deviation from $M_{\mathrm{tot}}$ on the order of $0.1\%$ in the reproducible toy model.

The methodological conclusion is important: recovery of the asymptote is not solely tied to a specific tuning of the tested parameters.

**Status: 🟢 numerical robustness of the localization mechanism within the tested model.**

### 48.4 Tests 43–44 — Torus-Cone Integration and Dynamic Exponent

The working geometry was then organized into three regimes:

1. central/torus region;
2. transition/cone region;
3. gentle slope and asymptotic return.

The radii used in Test 43 were:

$$
R_{\mathrm{trans}}=0.61\ \mathrm{kpc},\qquad R_{\mathrm{gentle}}=1.31\ \mathrm{kpc}.
$$

The ratio $\simeq2.15$ between these radii remains a geometric input and has not yet been derived.

Test 43 preserves the Newtonian asymptote with a coefficient of variation of about $0.005\%$ and a relative deviation of about $-0.004\%$ in the reported calculation.

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

In Test 44, the cone zone gave approximately $1.21\lesssim\alpha\lesssim1.28$, with an average close to $1.25$. The value $4/3$ was therefore not reached everywhere: it appears as a **saturation limit**, not as a global constant imposed at all radii.

**Status: 🟢 numerical consistency of the tested matching; 🟡 fundamental origin of $4/3$ still open.**

### 48.5 Candidate Form of the Localized Correction

A working expression consistent with the previous results is:

$$
\rho_{\mathrm{eff}}(r)=\rho_b(r)\left[1+k_0\left(\frac{r}{r_t}\right)^{4/3}\mathrm{sech}^2\left(\frac{r-r_t}{\sigma}\right)\right].
$$

This expression is not yet a fundamental law. It only encodes the three numerical constraints:

- weak correction outside the transition zone;
- $4/3$ scaling in the active zone;
- extinction of the correction at large $r$.

---

## 49. Search for the Dimensional Origin of $4/3$, $3/4$, and $1/4$
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

the value $C_c=0.2=1/5$ leads exactly to:

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

### 49.1 What Is Actually Demonstrated

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

Tests 49–50 showed that the minimal dynamics of $C$ and the simple feedbacks tested do not spontaneously select $C_c=1/5$.

With:

$$
Z\Box C-V'(C)=0,
$$

a quadratic potential relaxes toward the value placed in the potential. Similarly, the tested feedbacks of the $\sigma(C)$ type produced clearly more coherent attractors, roughly $0.72$ to $0.91$, with no attractor in the window $[0.16;0.24]$.

**Conclusion:** $C_c=1/5$ remains a **gravitational-model input**, while $4/3$, $3/4$, and $1/4$ form an elegant and consistent dimensional structure **conditional on this input**. No fundamental physical derivation of $C_c=1/5$ is currently established.

---

## 50. Collective Dynamics Tests: From $Q_i$ to $C$

### 50.1 Computation Chain

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

The goal is to determine whether a collective structure produces a preferred value of $C$ or merely a continuous transition between incoherence and synchronization.

### 50.2 Test 50 — Blind Feedbacks of $C$ on $\sigma$
Two families with no targeting of $0.2$ were tested:

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
| inverse | $\sigma_0=0.8,\kappa=1$ | 0.836 |
| inverse | $\sigma_0=0.8,\kappa=2$ | 0.893 |
| inverse | $\sigma_0=1.2,\kappa=1.5$ | 0.914 |
| inverse | $\sigma_0=1.0,\kappa=3$ | 0.722 |

No attractor appeared in $[0.16;0.24]$.

**Verdict: 🔴 these simple feedbacks do not select $C_c\simeq0.2$.**

### 50.3 Test 51 — Blind Search for a Collective Transition

Test 51 then dropped all artificial feedback and directly searched for a transition in the weighted system:

$$
\dot\theta_i=\frac KN\sum_jw_{ij}\sin(\theta_j-\theta_i).
$$

The protocol notably uses:

$$
N\in\{200,400,800,1600\},
$$

a sweep of $K$ and $\sigma$, several independent seeds, and a sufficiently long integration time.

The planned observables are:

$$
\chi_C=N\left(\langle C^2\rangle-\langle C\rangle^2\right),
$$

as well as a Binder cumulant treated as a secondary indicator, and the relaxation time.

The first reported 2D scan, with $N=200,400$, $K\in\{0.5,1,1.5,2\}$, and $\sigma\in\{8,12,16,20\}$, shows:

- an incoherent regime at low $K$, with $C$ close to the $1/N$ scale;
- a continuous rise of $C$ with $K$;
- point values close to $0.2$;
- no robust critical line that universally fixes $C\simeq0.2$.

For example, values close to $0.2$ appear around $C\approx0.218$ and $C\approx0.169$ for certain $(K,\sigma)$ pairs, but they shift as the parameters or $N$ change.

**Verdict of Test 51:**

$$
\boxed{\text{the weighted model has a synchronization transition, but does not select }C_{\mathrm{crit}}\approx0.2\text{ universally}.}
$$

Thus, $C=0.2$ is currently better described as a **parametric crossing point** of the model than as a fundamental attractor or critical point.

---

## 51. Physical Consequences and Current Limitations

### 51.1 What the Numerical Campaigns Actually Establish

| Element | Status |
|---|---|
| 3+1 dimensional structure | 🟢 Fixed structural hypothesis |
| $C=|Z|^2$ as a phase invariant | 🟢 Confirmed as a robust toy observable |
| Incoherent state $C\sim1/N$ | 🟢 Confirmed statistical reference |
| Localized correction | 🟢 Tested with Newtonian non-regression |
| Robustness of the asymptote under $\sigma,k_0$ variation | 🟢 Tested in the toy model |
| Torus-cone integration | 🟢 Numerically consistent within the tested framework |
| $\alpha(s)\to4/3$ at saturation | 🟢 Consistent dynamic formulation; fundamental origin open |
| Global $4/3$ | 🔴 Abandoned: diverges at large $r$ |
| $3/4$ | 🟡 Inverse relation consistent with $4/3$, not an independent derivation |
| $C_c=1/5$ | 🟡 Input parameter; not dynamically selected |
| $1/4$ | 🟡 Identity conditional on $C_c=1/5$; not independently derived |
| $\theta\approx28.955^\circ$ | 🟢 Mathematical consequence of $C_c=0.2$ in the current formula |
| $E=mc^2$ | 🔴 No independent validation; any definition of $m$ via $c^2$ would be circular |
| $c_{\mathrm{eff}}\approx\sqrt2$ | 🟡 To be audited separately; no fundamental origin established here |
| emergent spatial $r$ | 🔴 Not derived from correlations |
| $D_{\mathrm{eff}}=3/4$ or $4/3$ as an emergent geometric dimension | 🔴 Not established |
| quantitative resolution of $10^{120}$ | 🔴 Not obtained; the tested toys give a much lower suppression |
| derivation of Einstein's equations | 🔴 Not obtained |

### 51.2 The Essential Point on Singularities

The regularized profile shows that it is mathematically possible to construct a source whose density remains finite at the center and whose total mass converges to $M$ at large distance. A Hayward-type reference metric, for instance, has:

$$
m(r)=M\frac{r^3}{r^3+a^3},
$$

and asymptotically recovers the Schwarzschild form.

This demonstrates a **regularization property**, not that the field $C$ actually generates this geometric mass.

### 51.3 The Essential Point on Antigravity

In the current version, the candidate tensor is quadratic in the gradients of $C$, and the bound $C\le1$ prevents a trivial extrapolation beyond saturation. This rules out certain repulsive behaviors **within this particular model**, under its assumptions.

This is not a proof that antigravity is impossible in any physical theory.

### 51.4 Proper Time and Emergent Time

The question remains open: if a quasi-classical history $H_i$ has a metric $g_{\mu\nu}^{(i)}$, its proper time could be defined by:

$$
\tau_i=\int\sqrt{-g_{\mu\nu}^{(i)}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}}\,d\lambda.
$$

The heuristic hierarchy:

$$
\tau_{\mathrm{micro}}\ll\tau_{\mathrm{corr}}\ll\tau_{\mathrm{macro}}
$$

remains a working hypothesis and not an experimental measurement of three fundamental times.

### 51.5 Next Roadmap

The next steps must remain separate and falsifiable:

1. **Audit $c_{\mathrm{eff}}$ term by term**, in particular looking for any square root already present in its definition before interpreting a result close to $\sqrt2$.
2. **Continue the analysis of correlations** $\tau_{ij}$ to determine whether differentiated correlation scales actually emerge.
3. Construct a distance $d_{ij}$ only if the correlations produce a nontrivial structure that is not simply inherited from $E_i$.
4. Then look for an emergent radius $r$, and only then test $N(r)$ and $D_{\mathrm{eff}}(r)$.
5. Test whether the exponent observed in the transition zone is actually compatible with $4/3$ without fixing it in advance.
6. Compare the corrected gravitational profile with real observational data, notably rotation curves, without ad hoc per-galaxy recalibration if the goal is predictivity.
7. Keep the question of the microscopic origin of $C_c$ separate: Test 51 closes the specific avenue "energy weighting $\rightarrow C_c=1/5$" for the tested family, but does not close all theoretical possibilities.

---

## 52. General Conclusion — Status of the Research Program

The model has crossed an important milestone: certain constructions that diverged were abandoned, while a **localized correction** showed a robust recovery of the Newtonian limit in the toy model.

$4/3$ is no longer used as a global law. It is now treated as a **potential transition scaling**, with an interpolation $\alpha(s)$ that tends toward $4/3$ as the normalized densification tends toward saturation $s\to1$.

The structure:

$$
\frac43,\qquad\frac34,\qquad\frac14
$$

is consistent with $d=3$, but its scientific value still depends on an independent derivation of $C_c=1/5$. Tests 49–51 specifically prevented this relation from being presented as already derived: the tested dynamics do not spontaneously select $1/5$.

The current scientific position can thus be summarized by:

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
|g(r)|r^2\rightarrow\mathrm{constant}
\qquad(r\rightarrow\infty).
$$

> **Working principle: we no longer choose the sought-after result; we first look at whether the dynamics produces it, then we keep both successes and failures.**

The program therefore remains open, but it is now more falsifiable, mathematically cleaner, and better separated between **inputs**, **consequences**, **numerical results**, and **fundamental hypotheses**.

---

## Conclusion

> **The gravitational geometry described by general relativity is studied here as a possible emergent macroscopic description of a collective quantum structure. The current numerical results do not demonstrate this emergence, but they already allow certain unstable constructions to be ruled out and precise constraints for future work to be identified.**

The central scientific problem remains:

> **Does a microscopic dynamics exist that is precise enough to simultaneously produce the coherence $C$, an emergent metric structure, the Newtonian limit, Einstein's equations, and the observed cosmological parameters without imposing them in advance?**

*Personal reflection and open-science document — to be checked against the scientific literature and independent validation.*

---

## 53. Critical Update — Campaigns 68–70: Threshold Audit, Symmetries, and Falsification Protocol

> **Status: major methodological update.**
> This section keeps track of the results, corrections, and open questions that arose after campaigns 68–69e. It should be read as an audit of the toy model, not as a validation of the theory of gravitational emergence.

### 53.1 Starting Point: The Gap $v_c(\alpha=0)\simeq2.92$ vs. $v_c^{\rm th}=2u=2.0$

The 68–69e campaign report gave a numerical extrapolation:

$$
v_c(\alpha=0)\simeq2.92
$$

whereas analysis of the symmetric model gave:

$$
v_c^{\rm th}=2u.
$$

For $u=1$,

$$
v_c^{\rm th}=2.
$$

This gap of about $46\%$ was identified as a methodological anomaly to resolve **before any new interpretive campaign**.

The working principle is:

$\boxed{
\text{numerical artifact}
\;\rightarrow\;
\text{limits }T,N
\;\rightarrow\;
\text{missing physical term}
}$

and not the reverse.

---

### 53.2 Important Correction to the Energy Audit of Report 70A

An additional algebraic check showed that report 70A contained an error in the evaluation of the minima.

The potential is:
$$F=-r\sum_a|\psi_a|^2+
u\sum_a|\psi_a|^4+
v\sum_{a<b}|\psi_a|^2|\psi_b|^2,
\qquad r>0,\;u>0,\;v>0.$$

#### Rank 1
For a single active component:
$F_1(\rho)=-r\rho^2+u\rho^4.$
The stationarity condition gives:
$-2r\rho+4u\rho^3=0$
and thus, for the nontrivial minimum,
$\boxed{\rho_1^2=\frac{r}{2u}}.$
The corresponding energy is:
$$F_1=-r\frac{r}{2u}+u\frac{r^2}{4u^2}=-\frac{r^2}{4u}.$$
Thus:
$\boxed{F_1=-\frac{r^2}{4u}}.$
For $r=u=1$,
$\boxed{F_1=-0.25}.$
> **Explicit correction:** $F_1$ is not equal to $0$. The quadratic and quartic terms do not cancel at the minimum; together they give $-r^2/(4u)$.

#### Symmetric Rank 3
For:
$$\psi_1=\psi_2=\psi_3=\rho,$$
we obtain:
$$F_3(\rho)=-3r\rho^2+3(u+v)\rho^4.$$
Stationarity gives:
$$\boxed{
\rho_3^2=\frac{r}{2(u+v)}}.$$
So:
$\boxed{F_3=-\frac{3r^2}{4(u+v)}}.$
For $r=u=1$ and $v=0$, $\boxed{F_3=-0.75}$.
Report 70A gave $-0.5625$, a value consistent with an incorrect amplitude substitution.

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

$\boxed{v=2u}.$

For $u=1$:

$\boxed{v_c^{\rm energy}=2}.$

The energetic threshold and the local-stability threshold therefore coincide in this symmetric model:

$\boxed{v_c^{\rm energy}=v_c^{\rm stability}=2u}.$

There is therefore **no**, in this specific symmetric quartic potential, a distinct thermodynamic window

$$
0.86<v<2
$$

in which rank 1 would be globally favored while rank 3 would remain metastable.

The alleged threshold $v\simeq0.86$ from report 70A must be classified as an **algebraic artifact**, not as a second physical threshold.

---

### 53.4 General Formula for $k$ Active Components

For $k$ components of the same amplitude $\rho$:

$$F_k(\rho)=-kr\rho^2+\left[ku+\frac{k(k-1)}2v\right]\rho^4.$$

The stationarity condition gives:

$$\rho_k^2=\frac{r}{2u+(k-1)v}.$$

Thus:

$\boxed{\rho_k=\sqrt{\frac{r}{2u+(k-1)v}}}.$

This formula corrects an important ambiguity present in earlier versions: the amplitude itself carries a square root.

The minimum energy becomes:

$\boxed{F_k^{\min}=-\frac{k r^2}{2\,[2u+(k-1)v]}}.$

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

### 53.5 Consequence: The Modal Competition Mechanism Remains Plausible, but the Interpretation Must Be Cleaned Up

The minimal model:
$F=-r\sum_a|\psi_a|^2+u\sum_a|\psi_a|^4+v\sum_{a<b}|\psi_a|^2|\psi_b|^2$

therefore has, for $u>0$ and $r>0$, a natural threshold:

$\boxed{v_c=2u}.$

This result does not depend on a numerical tuning of the threshold.

However, it is not enough to explain why a given simulation might produce an apparent threshold around $2.9$. This question remains distinct:

$\boxed{v_c^{\rm apparent}\neq v_c^{\rm theoretical}}$

as long as finite-time effects, finite-size effects, the operational definition of the threshold, and any model reduction have not been separated out.

---

## 53.6 Formalization 70S — Exact Nature of the Dynamics

The collective dynamics studied in Tests 9–46 is a gradient flow:

$\boxed{\dot\psi_a=-\frac{\partial F}{\partial\psi_a^*}}$

that is, in the general case:

$\boxed{\dot\psi_a=r\psi_a-2u|\psi_a|^2\psi_a-\left(\sum_{b\neq a}v_{ab}|\psi_b|^2\right)\psi_a}.$

### Symmetry of the Potential

When the potential depends only on the moduli:

$$
F=F(|\psi_1|^2,|\psi_2|^2,|\psi_3|^2),
$$

it is invariant under:

$$
\psi_a\rightarrow e^{i\varphi_a}\psi_a,
$$

with three independent phases.

So:

$\boxed{G_F=U(1)^3}.$

### Symmetry of the Flow

The gradient flow is then equivariant under the same action:

$\boxed{G_{\rm flow}=U(1)^3}.$

The symmetry of the potential and that of the flow should not, however, be confused with a conservation law for a Noether charge.

### Polar Variables

Writing:

$$
\psi_a=\sqrt{\rho_a}\,e^{i\theta_a},
$$

the flow considered here gives:

$$
\dot\rho_a=2\lambda_a(\rho)\rho_a,
$$

with $\lambda_a$ real, and:

$\boxed{\dot\theta_a=0}$

for this **precise reduced dynamics**.

The amplitudes can therefore decay to zero while the phases remain frozen.

> **Essential methodological point:** $\dot\theta_a=0$ is not a consequence of $U(1)^3$ alone. It is a consequence of the combination "phase-invariant potential + choice of gradient flow."

---

## 53.7 Do Not Automatically Extrapolate This Property to the Microscopic Level

The original microscopic dynamics, notably the Kuramoto-type oscillators studied elsewhere in the program, has an active phase dynamics:

$$
\dot\theta_i=\frac KN\sum_jw_{ij}\sin(\theta_j-\theta_i).
$$

There are therefore two distinct levels:

$\boxed{\text{microscopic dynamics}\neq\text{reduced modal dynamics}}$

The property $\dot\theta_a=0$ of the reduced Landau model must not be presented as a demonstrated property of the microscopic dynamics as long as an explicit reduction has not been derived.

This is now a priority question for 70S:

> **Is the frozen phase dynamics of the modal variables derived from the microscopic dynamics, or introduced by the phenomenological reduction?**

---

# 54. Diagnostic Protocol 70A–70D

## 54.1 70A — Testing the $\alpha\rightarrow0$ Extrapolation

### Tested Hypothesis

The $2.92$ value might come from an inadequate linear extrapolation rather than a genuine threshold at $\alpha=0$.

We start from the measurements:

$$
\{(\alpha_i,v_c(\alpha_i))\}_{i=1}^{M}.
$$

Compare at least:

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

decreases substantially with a nonlinear model.

**Failure:**

$$
v_c^{\rm lin}(0)\simeq v_c^{\rm quad}(0)\simeq2.92
$$

with uncertainties small enough to exclude $2$.

> **Indispensable condition:** the raw points $v_c(\alpha)$ must be kept. An extrapolation must not be reconstructed from its final formula alone.

---

## 54.2 70B — Time Convergence, Then Size Convergence

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

### Non-Negotiable Rule

Never vary $T$ and $N$ simultaneously in a test intended to causally attribute a threshold shift.

---

## 54.3 70C — Missing Term, Only If 70A and 70B Fail

The starting potential remains:

$F_0=-r\sum_a|\psi_a|^2+u\sum_a|\psi_a|^4+v\sum_{a<b}|\psi_a|^2|\psi_b|^2.$

Only one additional term should be introduced at a time.

### Phase-Coupled Candidate

For example:

$F_3=w(\psi_1\psi_2\psi_3+\mathrm{c.c.}).$

But this term should only be kept if the microscopic symmetries allow it.

Other couplings are possible, for example:

$w_{12}(\psi_1^*\psi_2+\mathrm{c.c.}),$

which selects a different combination of phases.

It is therefore no longer correct to present the cubic term as "the" a priori preferred missing term.

### Spatial Candidate

If the variables $\psi_a$ are actually spatial fields, one can test:
$F_\nabla=\sum_a\kappa_a|\nabla\psi_a|^2+\sum_{a<b}\kappa_{ab}\nabla\psi_a\cdot\nabla\psi_b.$

But this extension changes the nature of the model: it introduces spatial degrees of freedom that do not exist in the homogeneous 0D model.

### Causality Criterion

An additional term is only explanatory if:

1. it is allowed by the symmetries;
2. its coefficient is measurable or microscopically derivable;
3. it is introduced before knowing its effect on $v_c$;
4. its magnitude is physically plausible;
5. it improves the prediction without arbitrary tuning.

The strong condition sought is:

$$
\boxed{\text{micro-dynamics} \to \text{effective coefficient} \to v_c \simeq 2.92}
$$

and not:

$$
\text{choice of }w
\rightarrow
v_c\simeq2.92.
$$

---

## 54.4 70D — Direct Reconstruction of the Effective Potential

Starting from the microscopic trajectories:

$$
Q_i(t),
$$

define the modal variables $\psi_a(t)$, then estimate their stationary distribution:

$$
P(\psi_1,\psi_2,\psi_3).
$$

One can then reconstruct, under the appropriate assumptions:
$\boxed{F_{\rm eff}=-k_BT_{\rm eff}\ln P}$
or, in reduced units:
$\boxed{F_{\rm eff}=-\ln P+C.}$

The reconstructed potential can then be compared to:
$F_{\rm eff}=-r_{\rm eff}\sum_a|\psi_a|^2+u_{\rm eff}\sum_a|\psi_a|^4+\sum_{a<b}v_{ab}^{\rm eff}|\psi_a|^2|\psi_b|^2+\cdots$

The goal is to determine whether the $v_{ab}$, the anisotropies, and any phase or gradient terms appear **in the data**, rather than being introduced to reproduce a result.

> **Caveat:** the inversion $F_{\rm eff}=-\ln P$ is only interpretable as a standard thermodynamic potential if the necessary statistical and equilibrium conditions are satisfied. For an out-of-equilibrium dynamics, it is first an effective statistical potential, not automatically a thermodynamic energy.

---

# 55. Intermediate Result of Independent Reconstruction

An independent reconstruction carried out from the available formula:

$$
v_c(\alpha)\approx2.92-1.5\alpha
$$

produced, with an explicitly reconstructed parametrization and not the original raw data, a first result:

$$
v_c(0)\approx2.118,
$$

and about:

$$
v_c(0.2)\approx1.750.
$$

This result is **indicative only**: it does not yet reproduce the exact protocol of campaigns 68–69d, for lack of access to the raw points and their complete operational definition of the threshold.

It is nonetheless important because it shows that an independent reconstruction of the anisotropic model can produce a value much closer to $2$ than to $2.92$.

This leads to a strict rule:

$$
\boxed{
2.118\ \text{is not a validation; it is a signal of non-reproducibility to be investigated.}
}
$$

The raw data and the exact protocol must therefore be obtained before any conclusion about the origin of the $2.92$.

---

# 56. Correction of the External Report 70A–70B

The external report 70A–70B had interpreted:

$v\simeq0.86$

as a distinct energetic threshold, then introduced a metastability window between $0.86$ and $2.0$.

The algebraic audit shows that this interpretation is invalid for the symmetric quartic potential defined here.

The correct threshold is:

$$
\boxed{v_c=2u}.
$$

The value $0.86$ must therefore be kept in the log only as an **erroneous historical result**, accompanied by the mathematical correction.

This distinction is important to prevent an incorrect value from later reappearing as a "previous prediction."

---

# 57. Consolidated Decision Tree

```text
         apparent v_c ≈ 2.92
              │
              ▼
       70A — extrapolation α → 0
              │
         ┌─────────┴─────────┐
         ▼          ▼
       → 2.0       stays ≈ 2.92
         │          │
     α artifact         ▼
               70B — convergence
                T then N separately
                   │
              ┌──────────┴──────────┐
              ▼           ▼
            → 2.0       stays ≈ 2.92
              │           │
           finite effect         ▼
                      70C — additional
                      term
                         │
                         ▼
                   microscopic validation
                         │
                         ▼
                      70D — F_eff
                   direct reconstruction
```

A 70S step must be considered **transversal and prior** to the physical interpretation:

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
- microscopic Kuramoto-type dynamics;
- modal reduction explicitly linking these levels.

---

# 58. Final Scientific Criterion

The program must now explicitly distinguish:

$\boxed{\text{numerical reproduction}\neq\text{physical explanation}}$

A complete predictive explanation should ideally follow the chain:

$$
\boxed{S_{\rm micro} \to P(\psi) \to F_{\rm eff} \to v_{ab}^{\rm eff} \to v_c \to \gamma_2, \gamma_3}
$$

without choosing the effective parameters specifically to reproduce the last observable.

This requirement is particularly important for the ratio:

$$
\frac{\gamma_3}{\gamma_2}\approx1.37
$$

obtained with anisotropy, since fitting several $v_{ab}$ to a single target does not by itself constitute a causal demonstration.

---

# 59. Questions Still Open After the Audit

1. What exactly is the operational definition of $v_c$ in campaigns 68–69e?
2. What are the raw points $(\alpha_i,v_c(\alpha_i))$?
3. What is the sensitivity of $v_c$ to the duration $T$?
4. What is its convergence in $N$ once $T$ has converged?
5. Can the microscopic reduction to $\psi_a$ be explicitly derived?
6. Does the freeze $\dot\theta_a=0$ exist at the microscopic level, or is it created by the reduction?
7. Which phase couplings are actually allowed by the microscopic symmetries?
8. Can the coefficients $v_{ab}$ be reconstructed directly from the trajectories?
9. Are the anisotropies $v_{12}<v_{13}<v_{23}$ explicitly imposed, or do they emerge?
10. Is the homogeneous 0D model sufficient, or must a spatial structure be introduced?

---

# 60. Principle of Preserving the Research Thread

> **Do not erase historical errors: keep them, label them, and correct them.**

The current status should be read as follows:

- $v_c=2u$: **analytical result of the symmetric quartic potential**;
- $v\simeq0.86$: **identified algebraic artifact**;
- $v_c\simeq2.92$: **historical observation/extrapolation to be reproduced and audited**, not an established theoretical value;
- $v_c\simeq2.118$: **partial independent reconstruction**, inconclusive;
- $U(1)^3$: **symmetry of the potential and of the reduced flow** in the model considered;
- $\dot\theta_a=0$: **property of the reduced gradient flow**, not yet derived from the microscopic dynamics;
- $v_{ab}$: **effective parameters not yet derived microscopically**;
- 70A–70D: **falsification protocol**, not definitive results;
- 70S: **audit of the dynamics class and of the micro → modal link**.

The guiding rule remains:

$$
\boxed{
\text{we no longer choose the sought-after result; we first look at whether the dynamics produces it.}
}
$$

# PART IV: NUMERICAL APPENDICES & PROOF GUIDE

This section archives the critical software building blocks and the reading guide for the raw data validating the model.

---

## 1. Phase Inversion Engine (61H-10A Audit)
Proof of singularity suppression via free phase dynamics.

```python
import numpy as np
def run_phase_inversion_audit(N=2000, max_steps=500, dt=0.01):
  phases = np.random.uniform(0, 2*np.pi, size=N)
  amplitudes = np.random.uniform(0.1, 1.0, size=N)
  for step in range(max_steps):
    interaction = np.mean(np.exp(1j * phases))
    d_phase = np.angle(interaction) - phases
    d_amplitude = np.cos(d_phase) * (1.0 - amplitudes)
    amplitudes += d_amplitude * dt
    phases += np.sin(d_phase) * dt
  return np.min(np.abs(amplitudes)) # ~0.61
```

---

## 2. MOND Emergence Engine (61H-13 Audit)
Analytical validation of the $-1.0000$ slope in the weak-field regime.

```python
import numpy as np
def compute_mond_emergence(a_0=1.2e-10, g_bar_scale=1e-8):
  r = np.linspace(5.0, 50.0, 50)
  g_bar = g_bar_scale / (r**2)
  g_h2c = np.sqrt(g_bar * a_0 + np.sqrt((g_bar * a_0)**2 + 4 * g_bar**2)) / np.sqrt(2)
  return np.polyfit(np.log(r[-15:]), np.log(g_h2c[-15:]), 1)[0] # -0.9999
```

---

## 3. Evidence Reading Guide (`Numerical_Evidence/`)

To ensure full transparency, the raw data files are archived in [Numerical_Evidence/](./Numerical_Evidence).

- **`61H8C_limit_audit.json`**: Proof of substrate regularity ($A_{\text{min}} > 0$).
- **`61H9_convergence_report.json`**: High-resolution scaling report ($N=4000$).
- **`61H12_extended_results.csv`**: Documents the galactic shape effect.
- **`61H11_final_report.json`**: Summary of performance across 175 galaxies ($19\%$ gain in $\chi^2$).

---

## 55. H2C Self-Consistent Solver & SPARC Validation (175 Galaxies)

### 55.1 Complete Source Code (Agg Backend)

```python
import os
import re
import zipfile
import requests
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# UNIVERSAL CONSTANTS & COSMOLOGICAL ANCHORING
C_M_S = 299792458.0
KPC_TO_M = 3.085677581491367e19
KM_S_TO_M_S = 1000.0
LAMBDA_M2 = 1.1056e-52

A0_H2C = (C_M_S**2) * np.sqrt(LAMBDA_M2 / 3.0) # ~5.4546e-10 m/s^2

class H2CSolverCoupledExperimental:
 def __init__(self, r_kpc, v_gas, v_disk, v_bul, max_iter=15, tol=1e-4):
  self.r_kpc = np.array(r_kpc, dtype=float)
  self.r_m = self.r_kpc * KPC_TO_M
  self.v_gas, self.v_disk, self.v_bul = np.array(v_gas), np.array(v_disk), np.array(v_bul)
  self.max_iter = max_iter
  self.tol = tol

 def solve(self):
  v_bar_sq_raw = np.sign(self.v_gas)*(self.v_gas**2) + 0.5*(self.v_disk**2) + 0.7*(self.v_bul**2)
  a_n = (np.maximum(0.0, v_bar_sq_raw) * (KM_S_TO_M_S**2)) / np.maximum(self.r_m, 1.0)
  y_curr = a_n / A0_H2C
  eta_curr = 1.0 - np.exp(-np.sqrt(np.maximum(1e-12, y_curr)))

  for iteration in range(self.max_iter):
   eta_old = eta_curr.copy()
   ml_d = 0.50 * (1.0 + 0.15 * np.exp(-y_curr))
   ml_b = 0.70 * (1.0 + 0.10 * np.exp(-y_curr))
   gamma_geom = 1.0 - 0.15 * eta_curr

   v_bar_sq = (np.sign(self.v_gas)*(self.v_gas**2) + ml_d*(self.v_disk**2) + ml_b*(self.v_bul**2)) * gamma_geom
   a_n_new = (np.maximum(0.0, v_bar_sq) * (KM_S_TO_M_S**2)) / np.maximum(self.r_m, 1.0)
   y_curr = a_n_new / A0_H2C
   eta_curr = 1.0 - np.exp(-np.sqrt(np.maximum(1e-12, y_curr)))

   if np.max(np.abs(eta_curr - eta_old)) < self.tol:
    break

  a_h2c = a_n_new * np.sqrt(0.5 + 0.5 * np.sqrt(1.0 + 4.0 / (y_curr**2 + 1e-12)))
  v_h2c = np.sqrt(a_h2c * self.r_m) / KM_S_TO_M_S

  return {
   "v_bar": np.sqrt(np.maximum(0.0, v_bar_sq)),
   "v_h2c": v_h2c,
   "eta": eta_curr,
   "iterations": iteration + 1
  }
```
