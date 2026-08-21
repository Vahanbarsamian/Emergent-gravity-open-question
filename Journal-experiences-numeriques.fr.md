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

## Test 11 — Critère H10a/b/c sur le mécanisme de rappel validé (Test 9)

**Protocole :** N=300 configurations, $E_i = Q_i^2$ (énergie microscopique), $\theta_i = sE_i \bmod 2\pi$, couplage de Kuramoto uniforme (Test 9), $K=0{,}4$. $\rho_{\mathrm{micro}} = \langle E_i \rangle$ sur toute la population. Secteur cohérent = configurations dont la phase finale est proche de la phase moyenne finale.

**Résultat : échec net.** Quelle que soit la tolérance de phase (5° à 60°), les 300 configurations sur 300 finissent dans le secteur cohérent, avec $\rho_{\mathrm{eff}}/\rho_{\mathrm{micro}} = 1{,}000$ exactement. **Aucune suppression.**

**Diagnostic :** le couplage de Kuramoto uniforme (celui qui explique le retour à la cohérence au Test 9) n'a aucune notion de distance entre configurations dans l'espace des énergies — toutes les paires interfèrent identiquement, donc toute la population se synchronise sans aucun tri. Le mécanisme qui explique le retour à la cohérence après perturbation (Test 9) **n'est pas**, en l'état, celui qui pourrait expliquer une suppression d'énergie effective (H10). Ce sont deux propriétés distinctes ; le modèle n'a pour l'instant que la première. Résultat négatif informatif, conforme aux critères de falsification (section 19 du document source).

---

## Test 12-13 — Couplage localisé en énergie

**Modification :** le couplage est pondéré par la proximité d'énergie entre configurations, $w_{ij} = \exp\left(-\frac{(E_i-E_j)^2}{2\sigma^2}\right)$ — cohérent avec le principe d'interférence réelle ($\cos((S_i-S_j)/\hbar)$ ne contribue significativement que si $S_i \approx S_j$).

**Résultat (8 graines indépendantes, N=300, K=0,4, tolérance 15°) :**

| $\sigma$ | $C$ moyen | $\rho_{\mathrm{eff}}/\rho_{\mathrm{micro}}$ moyen | écart-type | Taille secteur moyenne |
|---|---|---|---|---|
| 30 | 0,773 | 0,800 | 0,100 | 202,6 |
| 20 | 0,438 | 0,638 | 0,177 | 129,9 |
| 15 | 0,282 | 0,444 | 0,178 | 123,0 |
| 12 | 0,212 | 0,458 | 0,210 | 100,1 |
| 10 | 0,167 | 0,398 | 0,308 | 98,9 |
| 8 | 0,117 | 0,449 | 0,381 | 89,4 |
| 6 | 0,077 | 0,573 | 0,406 | 60,5 |
| 5 | 0,063 | 0,519 | 0,209 | 55,4 |

**Ce que ça montre :** un effet de suppression réel et directionnellement correct — $\rho_{\mathrm{eff}}/\rho_{\mathrm{micro}}$ passe de $1{,}000$ (couplage uniforme, Test 11) à $\approx 0{,}4$–$0{,}6$ pour $\sigma \in [8,15]$, avec un secteur cohérent substantiel (60 à 200 configurations sur 300 — pas un artefact de bruit).

**Ce qu'il ne faut PAS en conclure :**
- Écarts-types importants (jusqu'à 0,4) — tendance robuste sur 8 graines, pas encore un résultat précis.
- Facteur de suppression obtenu (~2-3×) sans commune mesure avec le critère $10^{120}$ (section 11/47 du readme cartographie) — attendu pour un modèle jouet à $N=300$, mais à ne jamais laisser croire que ce test s'en approche.
- En dessous de $\sigma \approx 6$, le secteur redevient trop petit et $C$ trop faible — le mécanisme cesse de fonctionner : ceci délimite un **domaine de validité** du modèle actuel (pertinent pour H9).

**Verdict H10a/b/c :** H10a (suppression) partiellement satisfait, modeste et bruité. H10b (signe positif) satisfait sur toute la plage testée. H10c (calculé, non ajusté) **non satisfait** — $\sigma$ reste un paramètre libre, pas dérivé de $S_{\mathrm{micro}}$.

---

## H22 — Origine de $\sigma$ (paramètre de localisation)

$$\mathbf{H22}: \quad \sigma \text{ doit être dérivé de } S_{\mathrm{micro}}[\hat\Phi_i] \text{ (H2), pas postulé comme largeur de couplage externe}$$

Piste à tester ensuite : $\sigma$ pourrait naturellement émerger comme l'échelle sur laquelle $\cos((S_i-S_j)/\hbar)$ décroît significativement — c'est-à-dire être une conséquence directe de l'action microscopique elle-même plutôt qu'un paramètre ajouté à la main pour obtenir la localisation. Si c'est le cas, le couplage localisé du Test 12 ne serait pas une modification ad hoc du modèle, mais une propriété déjà contenue dans $A_i = e^{iS_i/\hbar}$ qu'on aurait simplement rendue explicite en pondérant par $|A_i^* A_j|$-like plutôt que par un $\sigma$ gaussien externe.

---

## Code (Tests 11-13, reproductible)

```python
import numpy as np

def local_kuramoto_evolve(theta0, E, K, sigma, N, steps=3000, dt=0.01):
    theta = theta0.copy()
    dE = E[None,:] - E[:,None]
    weight = np.exp(-(dE**2)/(2*sigma**2))  # sigma=None -> couplage uniforme (Test 11)
    for t in range(steps):
        diff = theta[None,:] - theta[:,None]
        force = (K/N) * np.sum(weight * np.sin(diff), axis=1)
        theta = theta + dt*force
    return theta

# Test 11 : weight = 1 partout (pas de ponderation) -> rho_eff/rho_micro = 1.000 (echec)
# Test 12-13 : weight gaussien en (E_i-E_j) -> voir tableau ci-dessus
```

---

## Prochaine étape proposée (mise à jour)

Tester H22 : essayer de dériver $\sigma$ directement à partir de $|A_i^* A_j| = |e^{i(S_i-S_j)/\hbar}|$-type de pondération sans paramètre gaussien externe, et vérifier si un $\sigma$ effectif émerge naturellement de cette construction plutôt que d'être choisi à la main. Si oui, refaire le Test 10 (universalité entre secteurs indépendants) avec ce couplage localisé dérivé, pour vérifier si l'universalité de $C$ tient aussi pour $\rho_{\mathrm{eff}}$.



---
*Journal de travail — résultats numériques réels, interprétation physique non établie.*
