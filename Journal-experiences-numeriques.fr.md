🇫🇷 Journal de laboratoire — modèles jouets

# Journal d'expériences numériques — mécanisme de filtrage par cohérence

> **Statut :** journal de laboratoire personnel. Contrairement au [document compagnon sourcé](./Reflexion-ouverte-sur-la-gravite.fr.md), ce fichier documente des expériences numériques sur des modèles jouets sans équivalent direct établi dans la littérature. Les résultats numériques sont réels (calculés, reproductibles avec le code fourni) ; leur interprétation physique reste entièrement hypothétique.
> **Renvoi :** pour le cadre théorique complet, voir le [document source](./Question-ouverte-gravite-source.fr.md).

---

## ⚠️ Deux garde-fous à ne jamais confondre

### Garde-fou 1 — Statut épistémique de $R$ (ne pas relâcher)
$R$ (et $C$) sont des **critères de filtrage internes au modèle jouet**. Ils ne doivent à aucun moment être présentés comme des grandeurs gravitationnelles physiques. Leur pertinence pour un modèle physique plus fondamental reste entièrement à démontrer — ce n'est acquis à aucune étape de ce journal.

### Garde-fou 2 — Défaut mathématique spécifique de $R$ (indépendant du garde-fou 1)
Même en restant strictement à l'intérieur du modèle jouet, sans aucune prétention physique, $R = \mathrm{Re}(\bar{A})$ dépend d'une **phase de référence globale arbitraire**. Deux secteurs peuvent être également cohérents ($C$ élevé) tout en ayant des $R$ complètement différents, simplement parce qu'ils ont verrouillé sur des phases différentes. **$R$ ne doit donc pas être utilisé comme critère de comparaison entre secteurs indépendants — $C = |\bar{A}|^2$, invariant de phase, doit être utilisé à sa place pour toute question d'universalité entre secteurs.** $R$ reste utilisable *à l'intérieur* d'un seul secteur, où la phase de référence ne varie pas.

---

## Test 8 — Rappel imposé à la main (Modèle B)

Rappel défini directement comme $\dot Q_i \propto \nabla_{Q_i} C$.

**Résultat :** $C$ augmente après perturbation, comme attendu — mais **ceci est une conséquence mathématique automatique de la définition**, pas une découverte physique. Un système construit pour maximiser $C$ voit $C$ augmenter par construction. Ce test seul ne valide rien ; il sert uniquement de référence de comparaison pour le Test 9.

---

## Test 9 — Rappel dérivé uniquement des amplitudes (Modèle C)

Dynamique non circulaire, dérivée du couplage de phase $\mathrm{Im}(A_i^* A_j) \propto \sin(\theta_j - \theta_i)$ (couplage de Kuramoto), **sans jamais écrire $\nabla_Q C$ à la main**.

$$\dot\theta_i = \frac{K}{N}\sum_j \sin(\theta_j - \theta_i)$$

**Résultat numérique (N=200, code ci-dessous) :**

| État | R | C |
|---|---|---|
| Initial | 0,221 | 0,118 |
| Après perturbation | 0,112 | 0,019 |
| K=0 (pas de couplage) | 0,112 | 0,019 (bloqué) |
| K≥0,5 | 0,757 | 1,000 (retour complet) |

**Seuil critique identifié** entre $K \approx 0{,}14$ et $K \approx 0{,}36$ (transition progressive) — comportement de transition de phase du modèle de Kuramoto, cité et documenté dans la littérature : Strogatz, *From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators*, Physica D 143, 1 (2000).

**Conclusion Test 9 :** un mécanisme de rappel dérivé uniquement de l'interférence des amplitudes, sans postulat direct sur $C$, reproduit spontanément le retour à la cohérence. Le résultat n'est pas construit pour l'occasion — c'est un phénomène de synchronisation connu, retrouvé ici numériquement.

---

## Test 10 — Universalité entre secteurs indépendants (H21)

**Protocole enregistré avant calcul :** deux populations de configurations, graines aléatoires totalement indépendantes, aucun couplage entre elles, même $S(Q) = sQ^2$, même mécanisme de rappel (Modèle C, K=0,4). Prédiction : les distributions macroscopiques de $C$ doivent devenir statistiquement indiscernables malgré une divergence totale configuration par configuration.

**Résultat numérique (25 tirages indépendants par secteur) :**

| Secteur | R (moyenne ± écart-type) | C (moyenne ± écart-type) |
|---|---|---|
| A | 0,144 ± 0,744 | 0,994 ± 0,018 |
| B | 0,212 ± 0,721 | 0,996 ± 0,008 |

Test t : $C$ → $p = 0{,}696$ (indiscernables). $R$ → dispersion trop large pour être un indicateur exploitable entre secteurs (conforme au Garde-fou 2).

**Conclusion Test 10 :** l'hypothèse H21 (universalité de la cohérence macroscopique entre secteurs isolés, sans couplage causal) **n'est pas réfutée** par ce test, à condition d'utiliser $C$ et non $R$ comme critère de comparaison.

---

## H21 — Formalisation

$$D[H_i, H_j] \to 0 \ (i \neq j) \ \text{et} \ S[\hat\Phi_i] \text{ universelle} \implies \text{secteurs isolés, } C^{(i)} \approx C^{(j)} \text{ (statistiquement)}$$

Reste à tester : est-ce que $G_{\mathrm{eff}}$ et $\Lambda_{\mathrm{eff}}$ (pas seulement $C$) montrent la même universalité, une fois qu'un mécanisme de reconstruction géométrique $g_{\mu\nu}^{\mathrm{eff}}$ sera défini (étape non encore franchie — voir section 13 du README_REPRISE).

---

## Code (reproductible)

```python
import numpy as np

def R_C(theta):
    A = np.exp(1j*theta)
    z = np.mean(A)
    return z.real, abs(z)**2

def kuramoto_step(theta, K, N, dt):
    diff = theta[None,:] - theta[:,None]
    force = (K/N) * np.sum(np.sin(diff), axis=1)
    return theta + dt*force

def evolve(theta0, K, N, steps=3000, dt=0.01):
    theta = theta0.copy()
    for t in range(steps):
        theta = kuramoto_step(theta, K, N, dt)
    return theta

# Test 9 : voir texte ci-dessus pour le protocole complet
# Test 10 : deux secteurs, graines indépendantes (1000+trial) et (5000+trial),
# même s, même K, aucun couplage croisé, comparaison des distributions de C.
```

---

## Prochaine étape proposée

Définir la reconstruction géométrique $g_{\mu\nu}^{\mathrm{eff}} = \sum_i w_i g_{\mu\nu}^{(i)}$ (section 13, README_REPRISE) avec des poids $w_i$ dérivés du même mécanisme non circulaire (Modèle C), puis tester si $G_{\mathrm{eff}}$ et $\Lambda_{\mathrm{eff}}$ calculés à partir de deux secteurs indépendants montrent la même universalité que $C$ dans le Test 10 — c'est le test qui rapprocherait vraiment H21 d'une hypothèse cosmologique plutôt que d'un résultat de synchronisation générique.

---
*Journal de travail — résultats numériques réels, interprétation physique non établie.*
