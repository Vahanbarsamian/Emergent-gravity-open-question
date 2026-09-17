# 📑 SYNTHÈSE EXÉCUTIVE H2C : De la V1.2 à la V1.4-2D.2
**Destinataire** : Gemini AS (Relais de ChatGPT)
**Date** : Septembre 2026

## 1. HISTORIQUE ET RECULS ANALYTIQUES

### A. La crise du test Q en V1.4-2D.1 (Le faux négatif)
- **Constat** : L'Hamiltonien $H$ était conservé ($10^{-13}$), mais la charge $Q$ dérivait de $5.76\%$.
- **Erreur initiale** : Imputée à la dispersion spatiale sous boost.
- **Correction théorique** : Le courant de Noether doit intégrer les termes croisés de la métrique effective $K^{\mu\nu}$ induite par le boost. L'ancienne formule $\int \operatorname{Im}(\Phi^* \dot{\Phi})\,d^2x$ était incomplète.

### B. Le vrai courant de Noether sous métrique effective $K^{\mu\nu}$
Pour le Lagrangien :
$$\mathcal{L} = -\frac{1}{2} K^{\mu\nu} \partial_\mu \Phi^* \partial_\nu \Phi - V(|\Phi|^2)$$
La composante temporelle du courant $j^0$ est :
$$\boxed{j^0 = K^{00}\operatorname{Im}(\Phi^*\dot\Phi) + K^{01}\operatorname{Im}(\Phi^*\partial_x\Phi) + K^{02}\operatorname{Im}(\Phi^*\partial_y\Phi)}$$
- **Résultat** : La dérive de $Q$ tombe à l'ordre de la précision machine ($10^{-15} \sim 10^{-13}$).

## 2. RÉSULTATS MÉTROLOGIQUES VALIDÉS (V1.4-2D.2)

| Boost $(v_x, v_y)$ | $|v|$ | $\Delta H/H_0$ | $\Delta Q/Q_0$ | Bilan |
| :--- | :--- | :--- | :--- | :--- |
| $(0.0, 0.0)$ | $0.00$ | $2.39 \times 10^{-14}$ | $7.47 \times 10^{-15}$ | 🟢 Précision machine |
| $(0.3, 0.4)$ | $0.50$ | $5.78 \times 10^{-14}$ | $2.79 \times 10^{-14}$ | 🟢 Précision machine |
| $(0.5, 0.5)$ | $0.71$ | $3.20 \times 10^{-13}$ | $1.61 \times 10^{-13}$ | 🟢 Précision machine |

- **Convergence RK4** : Ordre 4 maintenu jusqu'au plancher Float64.

## 3. FEUILLE DE ROUTE V1.4-2D.3 (Gemini AS)

1.  **Signature et Géométrie (3+1)** : 
    - Vérifier l'invariance de $\det(K)$ sous boost.
    - Étudier la transition $\beta < 1$, $\beta = 1$, $\beta > 1$ (rupture de causalité).
2.  **Anisotropie de dispersion** : Valider $\omega(\mathbf{k})$ par rapport à $\mathbf{u}$.
3.  **Objectif V1.5 (Le Saut Décisif)** : Faire émerger la métrique $g_{\mu\nu}^{\text{eff}}$ de façon **dynamique** à partir des variations du champ $\Phi$.

---
*Ce document sert de base de connaissance pour la poursuite des travaux sur la branche Tensorielle.*
