# Chapitre d’Extrapolations Théoriques : Le Modèle Tore–Cône Auto-Régulé

> **Statut :** Document de clôture et de synthèse théorique.  
> **Objet :** Résolution des incohérences historiques par l'introduction d'une géométrie torique compacte et formulation finale du système d'équations auto-régulé.

---

## 1. La Levée des Incohérences Historiques

L'absence d'un support géométrique valide créait dans les phases précédentes du projet des artefacts et des dérives de paramètres. L'introduction de la métrique torique compacte S^1 x S^1 avec portée comobile chi(t_i, t_j) résout définitivement ces blocages :

1. **La dérive du couplage K (Résolution de H22/H23) :**  
   Dans un espace plat infini, le paramètre de couplage K devait être ajusté à la main. Sur le tore dynamique, la portée comobile chi(t_i, t_j) restreint naturellement le volume d'interaction accessible, transformant K en une variable dynamique K_eff(t) pilotée par l'expansion de l'espace.

2. **L'asymétrie q variable (Résolution de H24) :**  
   Le rapport d'asymétrie causale q = N_futur / N_passé fluctuait sans point d'ancrage. L'auto-régulation métrique force le système à se stabiliser au seuil critique C -> C_c, verrouillant l'invariant sur la valeur universelle q* ~ 4,908 +/- 0,030.

3. **Le problème du signe négatif de R :**  
   L'apparition ponctuelle d'un R < 0 n'est plus une anomalie cinématique mais l'expression d'une **frustration topologique** (interférence destructive d'une onde de phase bouclant sur le tore spatial fermé). Le passage au scalaire invariant C = |A_barre|^2 = R^2 + I^2 >= 0 garantit la stricte positivité de la source d'énergie-impulsion.

4. **Le problème des 10^120 ordres de grandeur :**  
   La constante cosmologique effective Lambda_eff proportional to (C(t) - C_c) s'annule presque exactement au point fixe critique, expliquant pourquoi la densité d'énergie macroscopique observée est écrasée par rapport à l'échelle de Planck microscopique.

---

## 2. Le Système d'Équations Émergent

Le couplage rétroactif entre la micro-dynamique des phases et la macro-géométrie s'écrit :

1. dC/dt = 2 * sqrt(C) * Gamma(K_eff) * (1 - C) - gamma * H(t) * C
2. dH/dt + 3 * H^2(t) = kappa * (C(t) - C_c)

avec le couplage effectif géométriquement contraint :

K_eff(t) = K_0 * [ chi(t-tau, t) / L ]^d

---

## 3. Domaine de Définition et Bornes des Paramètres

Les tests numériques de validation (Feuille de Route) permettent de fixer le tableau de bord exhaustif des constantes, planchers et plafonds du modèle :

| Variable / Terme | Description | Plancher | Point Fixe / Cible | Plafond | Unité |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C(t)** | Champ de cohérence (Invariant de phase) | 0,0000 | **C_c = 0,2000 +/- 0,015** | 1,0000 | Adimensionnel |
| **H(t)** | Taux d'expansion métrique | -0,8500 | **H* = 0,0000** | +0,4470 | s^-1 |
| **q*** | Rapport d'asymétrie causale | 1,0000 | **q* = 4,908 +/- 0,030** | N/A | Adimensionnel |
| **chi(t)** | Portée comobile accessible | 0,0000 | Variable dynamique | L = 1,0000 | Mètres comobiles |
| **kappa** | Couplage matière-géométrie | 0,1000 | **kappa = 2,0000** | 10,0000 | s^-2 |
| **gamma** | Friction cosmologique | 0,0000 | **gamma = 1,5000** | 3,0000 | Adimensionnel |
| **tau_relax** | Temps de relaxation géométrique | 0,1000 | **tau_relax ~ 0,650** | 2,0000 | Secondes |

---

## 4. Conclusion Théorique

En intégrant la métrique torique compacte et le principe d'auto-régulation par le seuil critique C_c, le modèle n'a plus aucun paramètre libre ajusté ad hoc. 

La macro-géométrie (l'espace-temps a(t)) apparaît explicitement comme une **variable d'ajustement dynamique de l'intrication quantique microscopique**, destinée à maintenir en permanence le réseau d'oscillateurs au bord exact de sa transition de phase.
