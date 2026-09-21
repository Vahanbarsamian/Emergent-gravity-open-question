# Émergence Géométrique, Champ de Cohérence et Gravité Effective — H2C
## README — Version de référence scientifique reconstruite

> **Statut : document de référence reconstruit après audit du README(21).**  
> Cette version sépare explicitement les résultats établis, les validations numériques du solveur, les hypothèses de travail, les branches historiques abandonnées et les questions encore ouvertes.
>
> **Règle de conservation scientifique :** les anciennes erreurs et les anciennes campagnes ne sont pas effacées ; elles sont conservées comme historique et accompagnées de leur statut corrigé.

---

## 0. Statut général

Ce projet étudie, de manière exploratoire et falsifiable, l'hypothèse selon laquelle la géométrie gravitationnelle classique pourrait émerger d'un degré de liberté collectif décrit par un champ complexe de cohérence.

Le programme **ne constitue pas actuellement une théorie démontrée de la gravité émergente**.

La chaîne de recherche visée est :

```text
degrés de liberté microscopiques
        ↓
corrélations / cohérence
        ↓
champ complexe Φ
        ↓
C = |Φ|²
        ↓
structure métrique effective g_eff
        ↓
géodésiques / dynamique gravitationnelle
        ↓
observables astrophysiques
```

La difficulté centrale reste la fermeture du pont :

```text
Φ → C → g_eff
```

avec une définition covariante, dimensionnellement cohérente et indépendante des données à expliquer.

---

# 1. Point de départ théorique

La relativité générale est décrite par :

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}.
$$

où :

- $g_{\mu\nu}$ est la métrique ;
- $G_{\mu\nu}=R_{\mu\nu}-\frac12 Rg_{\mu\nu}$ est le tenseur d'Einstein ;
- $R^\rho{}_{\sigma\mu\nu}$ est le tenseur de Riemann complet ;
- $T_{\mu\nu}$ est le tenseur énergie-impulsion.

La question du projet est :

> **La métrique $g_{\mu\nu}$ pourrait-elle être une variable collective émergente d'une structure microscopique plus fondamentale ?**

Une écriture générale de travail est :

$$
\mathcal Q[
\langle\hat\Phi_i\hat\Phi_j\rangle,
\langle\hat\Phi_i\hat\Phi_j\hat\Phi_k\rangle,\ldots]
\longrightarrow
g_{\mu\nu}
\longrightarrow
G_{\mu\nu}.
$$

Cette relation est un **objectif de formalisation**, pas une dérivation acquise.

---

# 2. Gravité induite : motivation, pas preuve

L'idée de gravité induite, notamment associée historiquement à Sakharov, fournit une motivation conceptuelle :

$$
S_{\rm eff}[g]
=
\int d^4x\sqrt{-g}
\left[
\frac{c^3}{16\pi G_{\rm eff}}(R-2\Lambda_{\rm eff})
+aR^2+bR_{\mu\nu}R^{\mu\nu}+\cdots
\right].
$$

Une relation schématique du type

$$
\frac1{G_{\rm eff}}
\sim
\sum_i c_iN_i\Lambda_i^2
$$

peut apparaître dans certains cadres effectifs.

Elle ne constitue pas une dérivation de la constante $G$ à partir du contenu quantique réel de l'Univers.

---

# 3. Hypothèse centrale du projet

Le programme explore un champ complexe :

$$
\Phi(x)=R(x)e^{i\theta(x)}
$$

et l'invariant :

$$
C(x)=|\Phi(x)|^2=R^2+I^2.
$$

Le modèle est fixé en **3+1 dimensions** :

$$
d=3,\qquad D=4.
$$

La dimension spatiale n'est pas un paramètre libre du modèle.

---

# 4. Logique d'émergence

Deux formulations ont été distinguées.

## 4.1 Logique A — relaxation

Une représentation historique était :

$$
\mathcal Q_0\rightarrow
\mathcal Q_1\rightarrow\cdots\rightarrow
\mathcal Q_{\rm stable}.
$$

Elle peut servir d'analogie pour une dynamique dissipative, mais n'est plus la formulation fondamentale privilégiée.

## 4.2 Logique B — somme sur les configurations

La formulation conceptuelle privilégiée est :

$$
\Psi[G]
=
\int_{\mathcal C(G)}
\mathcal D\Phi\,
e^{iS_{\rm micro}[\Phi]/\hbar}.
$$

Dans une limite semi-classique :

$$
\delta S=0
$$

sélectionne les contributions stationnaires.

Cette écriture est un **objectif de formalisation**. L'action microscopique $S_{\rm micro}$ et la mesure complète ne sont pas encore dérivées.

---

# 5. Ce qui a été abandonné

## 5.1 Loi globale $4/3$

Une loi globale imposant un scaling $4/3$ a été testée puis abandonnée car elle divergeait ou dégradait l'asymptote newtonienne.

**Statut : 🔴 abandonné.**

## 5.2 Modèles de réfraction scalaires V9.1-R

Une branche scalaire utilisait notamment une normalisation galaxie par galaxie, un $v_{\rm flat}$ directement extrait des observations et une correction empirique.

L'audit aveugle a montré que cette branche n'est pas prédictive dans son état actuel.

**Statut : 🔴 branche fermée comme modèle gravitationnel prédictif.**

Cette fermeture ne réfute pas une formulation tensorielle générale $C\rightarrow g_{\mu\nu}^{\rm eff}$.

## 5.3 Branche MOND/AQUAL historique

Le README historique contient une branche de type :

$$
\nabla\cdot[\mu(\cdots)\nabla\Phi]
=
4\pi G\rho_b.
$$

Elle a été utile comme étape exploratoire, mais ne doit pas être présentée comme une dérivation indépendante de MOND depuis H2C.

**Statut : 🟠 historique / non fondamental.**

Toute fonction d'interpolation $\nu(y)$ ou $\mu(y)$ choisie pour reproduire les courbes observées est interdite dans le protocole prédictif actuel.

---

# 6. Résultats robustes du modèle jouet

## 6.1 Invariant de cohérence

$$
C=|Z|^2
$$

est un observable robuste dans les jouets numériques étudiés.

**Statut : 🟢 propriété du modèle jouet.**

Cela ne démontre pas que $C$ est un champ gravitationnel.

## 6.2 Correction localisée et asymptote

Les Tests 41–44 ont étudié une correction localisée capable de préserver :

$$
|g(r)|\,r^2\rightarrow {\rm constante}
\qquad(r\rightarrow\infty).
$$

Le Test 42 a rapporté une robustesse sur une grille de paramètres $(\sigma,k_0)$.

**Statut : 🟢 robustesse numérique dans le modèle jouet.**

Les rayons de transition utilisés, notamment :

$$
R_{\rm trans}=0.61\ {\rm kpc},
\qquad
R_{\rm gentle}=1.31\ {\rm kpc},
$$

restent des entrées géométriques dans ces expériences et ne sont pas dérivés.

---

# 7. Seuil $C_c=1/5$

Le programme utilise :

$$
C_c=0.2000=\frac15.
$$

Les identités :

$$
\frac{C_c}{1-C_c}=\frac14,
$$

et, avec la définition angulaire utilisée,

$$
\theta=2\arcsin\left(\frac14\right)
\simeq28.955^\circ
$$

sont des conséquences mathématiques conditionnelles à $C_c=1/5$.

En revanche, les tests aveugles de rétroaction et les recherches de transition collective n'ont pas sélectionné spontanément $C_c=0.2$.

Des attracteurs autour de $0.72$–$0.91$ ont été obtenus dans certaines rétroactions testées, et le balayage collectif n'a pas produit de ligne critique universelle à $C\simeq0.2$.

**Conclusion :**

> $C_c=1/5$ est actuellement une **entrée du modèle**, pas une constante dérivée.

---

# 8. Structure $3/4$, $4/3$, $1/4$

En $d=3$ :

$$
\frac{d}{d+1}=\frac34,
\qquad
\frac{d+1}{d}=\frac43.
$$

Ces relations sont mathématiquement cohérentes et réciproques.

De même :

$$
\frac1{d+1}=\frac14.
$$

Mais aucune de ces identités ne constitue à elle seule une dérivation physique.

Le lien entre ces nombres et une éventuelle géométrie émergente reste ouvert.

**Statut : 🟡 structure mathématique intéressante, non dérivation physique.**

---

# 9. Régularisation et géométrie de référence

Une géométrie régulière de type Hayward peut servir de référence :

$$
m(r)=M\frac{r^3}{r^3+a^3},
$$

avec une fonction métrique de type :

$$
f(r)=1-\frac{2m(r)}r.
$$

Près du centre :

$$
f(r)\simeq1-\frac{r^2}{\ell^2},
$$

et à grande distance :

$$
f(r)\simeq1-\frac{2M}{r}.
$$

Cela démontre qu'une géométrie régulière avec limite asymptotiquement schwarzschildienne peut être construite.

Cela **ne démontre pas** que $C$ engendre cette géométrie.

Les objets suivants doivent rester séparés :

```text
C(r)
source phénoménologique ρ(r)
masse intégrée m(r)
métrique g_μν
courbure
```

---

# 10. Audit du modèle de Landau à trois modes

Le potentiel étudié est :

$$
F=
-r\sum_a\rho_a
+u\sum_a\rho_a^2
+v\sum_{a<b}\rho_a\rho_b,
\qquad
\rho_a=|\psi_a|^2.
$$

Pour $k$ composantes actives :

$$
\rho_k=
\frac{r}{2u+(k-1)v}
$$

et

$$
F_k^{\min}
=
-\frac{k r^2}
{2[2u+(k-1)v]}.
$$

Ainsi :

$$
F_1=-\frac{r^2}{4u},
$$

$$
F_2=-\frac{r^2}{2(2u+v)},
$$

$$
F_3=-\frac{3r^2}{4(u+v)}.
$$

Le croisement $F_1=F_3$ donne :

$$
v=2u.
$$

Le seuil de stabilité locale du mode symétrique donne également :

$$
v_c=2u.
$$

Pour $u=1$ :

$$
v_c=2.
$$

### Correction historique

Une ancienne valeur proche de $v\simeq0.86$ provenait d'une erreur algébrique dans l'évaluation des minima.

**Statut :**

- $v_c=2u$ : 🟢 résultat analytique du potentiel quartique symétrique ;
- $v\simeq0.86$ : 🔴 artefact historique corrigé ;
- une valeur numérique différente doit être reproduite et auditée avant interprétation.

---

# 11. Symétries et dynamique de phase

Lorsque le potentiel dépend uniquement des modules :

$$
F=F(|\psi_1|^2,|\psi_2|^2,|\psi_3|^2),
$$

la symétrie est :

$$
U(1)^3.
$$

Pour le flot de gradient :

$$
\dot\psi_a=-\frac{\partial F}{\partial\psi_a^*},
$$

les phases restent figées dans la réduction modale considérée :

$$
\dot\theta_a=0.
$$

Cette propriété vient de la combinaison :

```text
potentiel invariant en phase
+
flot de gradient
```

et non de la seule symétrie $U(1)^3$.

Elle ne doit pas être extrapolée automatiquement à la dynamique microscopique de type Kuramoto :

$$
\dot\theta_i=
\frac KN\sum_jw_{ij}\sin(\theta_j-\theta_i).
$$

Une réduction explicite micro → modes est encore nécessaire.

---

# 12. Termes de couplage de phase

Un terme comme :

$$
w(\psi_1\psi_2\psi_3+\mathrm{c.c.})
$$

impose :

$$
\theta_1+\theta_2+\theta_3
=
0\pmod{2\pi},
$$

et laisse typiquement une symétrie $U(1)^2$.

D'autres couplages, par exemple :

$$
w_{12}(\psi_1^*\psi_2+\mathrm{c.c.}),
$$

sélectionnent d'autres combinaisons de phases.

Aucun terme de ce type ne doit être présenté comme « le terme manquant » sans dérivation à partir des symétries microscopiques.

---

# 13. Passage au champ complexe covariant — V1.2

La branche actuellement privilégiée introduit un champ complexe covariant :

$$
\Phi(x)=R(x)e^{i\theta(x)}.
$$

Une formulation effective de travail est :

$$
\mathcal L_\Phi
=
-\frac12
K^{\mu\nu}
\nabla_\mu\Phi^*
\nabla_\nu\Phi
-
V(|\Phi|^2),
$$

avec :

$$
K^{\mu\nu}
=
g^{\mu\nu}
+
\beta u^\mu u^\nu.
$$

La signature adoptée est :

$$
(-,+,+,+).
$$

Le vecteur temporel unitaire vérifie :

$$
u^\mu u_\mu=-1.
$$

### Point de covariance

Si $u^\mu$ est externe, le secteur effectif introduit une structure privilégiée.

Pour une théorie fondamentalement covariante, $u^\mu$ doit donc idéalement être un degré de liberté dynamique avec contrainte :

$$
u^\mu u_\mu=-1.
$$

---

# 14. Équation du champ

L'équation générale est de la forme :

$$
\nabla_\mu
\left(
K^{\mu\nu}\nabla_\nu\Phi
\right)
-
\frac{\partial V}{\partial\Phi^*}
=
0,
$$

avec un facteur numérique dépendant de la convention de normalisation du potentiel.

Pour :

$$
V(C)=-\mu^2C+\lambda C^2,
\qquad C=|\Phi|^2,
$$

on obtient :

$$
\frac{\partial V}{\partial\Phi^*}
=
-\mu^2\Phi
+
2\lambda|\Phi|^2\Phi.
$$

Le minimum non nul vérifie :

$$
C_0=\frac{\mu^2}{2\lambda}.
$$

Donc, si l'on impose :

$$
\phi_0=1,
$$

il faut avoir :

$$
\mu^2=2\lambda.
$$

Cette relation doit être respectée dans toute version finale du modèle.

---

# 15. Correction dimensionnelle obligatoire

Si $\Phi$ est dimensionnellement normalisé pour être sans dimension :

$$
[\Phi]=1,
$$

alors :

$$
[\Box\Phi]=L^{-2}.
$$

Le terme de potentiel dans l'équation du champ doit donc avoir la dimension :

$$
[\mu^2]=[\lambda]=L^{-2}.
$$

Une proposition antérieure :

$$
\lambda=
\frac{c^4}{4a_0^2L_c^2}
$$

était dimensionnellement sans dimension et ne pouvait donc pas être utilisée telle quelle dans l'équation précédente.

Une normalisation cohérente possible est :

$$
\ell_0=\frac{c^2}{a_0},
$$

puis :

$$
\lambda=\ell_0^{-2}
=
\frac{a_0^2}{c^4},
$$

et, pour conserver $\phi_0=1$ avec le potentiel $-\mu^2C+\lambda C^2$ :

$$
\mu^2=2\ell_0^{-2}
=
\frac{2a_0^2}{c^4}.
$$

L'équation devient alors :

$$
\boxed{
\Box\Phi
-
\frac{2a_0^2}{c^4}\Phi
+
\frac{2a_0^2}{c^4}
|\Phi|^2\Phi
=
\kappa T_{\rm bar}
}
$$

avec :

$$
\kappa=\frac{8\pi G}{c^4}.
$$

**Statut : 🟡 normalisation cohérente proposée, à intégrer explicitement dans la prochaine version du modèle.**

Elle ne constitue pas encore une dérivation fondamentale de $a_0$.

---

# 16. Courant de Noether

Pour la symétrie globale :

$$
\Phi\rightarrow e^{i\alpha}\Phi,
$$

le courant est :

$$
j^\mu
=
\frac{i}{2}
K^{\mu\nu}
\left(
\Phi^*\nabla_\nu\Phi
-
\Phi\nabla_\nu\Phi^*
\right).
$$

Lorsque les équations du mouvement sont satisfaites :

$$
\nabla_\mu j^\mu=0.
$$

La charge totale est conservée sous les conditions aux limites appropriées.

Point méthodologique :

> une symétrie du potentiel ne suffit pas à elle seule à établir une conservation dans une dynamique dissipative ; la structure dynamique complète doit être examinée.

---

# 17. Décomposition amplitude / phase

Avec :

$$
\Phi=Re^{i\theta},
$$

on obtient :

$$
|\nabla\Phi|_K^2
=
K^{\mu\nu}
\left(
\nabla_\mu R\nabla_\nu R
+
R^2\nabla_\mu\theta\nabla_\nu\theta
\right).
$$

Cette identité a été vérifiée analytiquement dans la campagne V1.1.

Pour les diagnostics numériques, il faut éviter de dériver spectralement une phase déroulée $\theta=\mathrm{unwrap}(\arg\Phi)$ sur un domaine périodique.

Un diagnostic robuste de gradient de phase utilise plutôt :

$$
\nabla_\mu\theta
=
\frac{\operatorname{Im}
(\Phi^*\nabla_\mu\Phi)}
{|\Phi|^2},
$$

lorsque $|\Phi|$ ne s'annule pas.

---

# 18. Propagation et métrique optique effective

Pour une configuration homogène et :

$$
u^\mu=(1,0,0,0),
$$

on obtient :

$$
K^{00}=-(1-\beta).
$$

La dispersion massless est :

$$
\omega^2
=
\frac{k^2}{1-\beta}.
$$

La vitesse de groupe correspondante est :

$$
v_g=\frac1{\sqrt{1-\beta}}.
$$

La condition numérique de signe impose notamment :

$$
\beta<1
$$

pour éviter le changement de signe problématique du terme temporel.

On peut définir formellement un cône optique effectif à partir de :

$$
K^{\mu\nu}k_\mu k_\nu=0.
$$

Cela permet de parler d'une **métrique optique effective**.

Attention :

> cette métrique optique n'est pas encore une métrique gravitationnelle émergente.

---

# 19. Qualification numérique du solveur — B1 à D4

Les campagnes B1, B2, D1, D2, D3 et D4 qualifient le solveur pour les configurations testées.

Elles ne valident pas encore la physique gravitationnelle.

## B1 — vérification directe de l'opérateur

Après correction de deux dérivées analytiques, le résidu numérique était :

```text
N=8    8.877445e-16
N=12   3.190417e-15
N=16   4.753851e-15
N=32   2.036517e-14
N=64   1.073979e-13
N=128  4.148550e-13
```

**Statut : 🟢 PASS — vérification de l'opérateur dans le cas analytique testé.**

## B2 — Manufactured Solution Test

Le terme source a été construit indépendamment à partir de :

$$
S_{\rm exact}=L[\Phi_{\rm exact}].
$$

Le mode nul a été traité explicitement.

Résultats L2 :

```text
N=8    1.31e-13
N=12   1.57e-13
N=16   3.07e-13
N=32   3.90e-13
N=64   7.01e-13
```

**Statut : 🟢 PASS — validation MMS pour la configuration testée.**

L'erreur ne doit pas être présentée comme une convergence vers zéro indépendante de la tolérance du solveur.

## D1 — K homogène

Pour :

$$
\beta=0.2,\qquad k_x=k_y=1,
$$

la dispersion analytique est :

$$
\omega=
\frac{\sqrt2}{\sqrt{0.8}}
\simeq1.58113883.
$$

La diminution de $dt$ a donné :

```text
dt       dérive Q       dérive H
1e-2     2.17e-10       2.17e-10
5e-3     6.78e-12       6.78e-12
2.5e-3   2.11e-13       2.11e-13
1.25e-3  5.89e-15       5.77e-15
```

**Statut : 🟢 PASS.**

## D2 — K spatialement inhomogène et stationnaire

```text
dt       dérive Q       dérive H
1e-2     2.34e-10       2.61e-10
5e-3     7.32e-12       8.16e-12
2.5e-3   2.29e-13       2.55e-13
1.25e-3  6.78e-15       7.17e-15
```

**Statut : 🟢 PASS.**

## D3 — K dépendant du temps

La charge reste conservée numériquement :

```text
dt       dérive Q
1e-2     2.24e-10
5e-3     7.00e-12
2.5e-3   2.19e-13
1.25e-3  6.45e-15
```

La variation énergétique est :

$$
\Delta H/H\simeq3.3135\%.
$$

Elle reste pratiquement indépendante de $dt$.

**Interprétation :** il s'agit d'un effet lié au coefficient temporel du problème testé, pas d'une dérive numérique de l'intégrateur.

**Statut : 🟢 PASS pour le bilan dynamique testé.**

## D4 — bilan énergétique local

Le résidu du bilan énergétique atteint :

```text
dt=1e-2     4.25e-11
dt=5e-3     2.32e-12
dt=2.5e-3   1.76e-13
dt=1.25e-3  1.58e-13
```

**Statut : 🟢 PASS — bilan local vérifié à la précision atteinte par ce protocole.**

### Conclusion B1–D4

> La discrétisation et l'intégrateur de la formulation covariante testée sont qualifiés pour les configurations B1–D4.

Cela qualifie **l'instrument numérique**, pas la théorie gravitationnelle.

---

# 20. SPARC — protocole prédictif strict

Le protocole actuel est séparé des anciennes branches SPARC.

## 20.1 Données

Le catalogue officiel SPARC contient 175 galaxies.

Les entrées baryoniques doivent provenir exclusivement des données officielles :

- $R$ ;
- $V_{\rm gas}$ ;
- $V_{\rm disk}$ ;
- $V_{\rm bul}$ ;
- incertitudes observationnelles uniquement pour la comparaison finale.

Les facteurs de masse sont fixés globalement :

$$
\Upsilon_{\rm disk}=0.5,
\qquad
\Upsilon_{\rm bul}=0.7.
$$

Aucun paramètre ne doit être ajusté galaxie par galaxie.

## 20.2 Règle de non-fuite observationnelle

Le solveur ne doit pas recevoir :

- $V_{\rm obs}$ ;
- $V_{\rm flat}$ ;
- la RAR ;
- une interpolation MOND ;
- une correction empirique dérivée des résidus ;
- une normalisation utilisant l'observable à prédire.

Les observations ne sont utilisées qu'après résolution.

---

# 21. SPARC-A — chaîne de calcul cible

La chaîne stricte est :

$$
T_{\rm bar}
\rightarrow
\Phi
\rightarrow
C=|\Phi|^2
\rightarrow
g_{\mu\nu}^{\rm eff}
\rightarrow
\text{géodésiques}
\rightarrow
V_c(r)
\rightarrow
V_{\rm obs}(r).
$$

Le protocole vise notamment NGC 3198 comme galaxie de référence avant généralisation aux 175 galaxies.

### Règle fondamentale

> **Aucune observable galactique ne doit entrer dans le solveur avant la prédiction de $V_c(r)$.**

---

# 22. Pont métrique : point encore ouvert

Une proposition de travail est :

$$
g_{\mu\nu}^{\rm eff}
=
\eta_{\mu\nu}
+
h_{\mu\nu}[C,\nabla C].
$$

Une forme candidate historique utilisait :

$$
h_{00}=-\frac{2\Phi_{\rm eff}}{c^2},
\qquad
h_{ij}=-\frac{2\Phi_{\rm eff}}{c^2}\delta_{ij}.
$$

Une autre proposition de travail était :

$$
\Phi_{\rm eff}
=
\Phi_{\rm bar}
+
\frac{c^2}{2}
\ln
\left(
1+\ell_0^2
\frac{|\nabla C|^2}{C^2+\epsilon}
\right).
$$

Cette expression doit être considérée comme **ansatz à tester**, et non comme dérivation.

Le rayon circulaire est ensuite :

$$
V_c^2=r\frac{d\Phi_{\rm eff}}{dr}.
$$

La convention gravitationnelle doit rester :

$$
g_{00}=-
\left(
1+\frac{2\Phi_{\rm eff}}{c^2}
\right),
$$

avec accélération :

$$
\mathbf a=-\nabla\Phi_{\rm eff}.
$$

---

# 23. Audit dimensionnel de la fermeture V1.2

Pour :

$$
\Box\Phi+\frac{\partial V}{\partial\Phi^*}
=
\kappa T_{\rm bar},
$$

avec $\Phi$ sans dimension :

$$
[\Box\Phi]=L^{-2},
\qquad
[\kappa T_{\rm bar}]=L^{-2}.
$$

Il faut donc :

$$
[\mu^2]=[\lambda]=L^{-2}.
$$

Avec :

$$
\ell_0=\frac{c^2}{a_0},
$$

une normalisation cohérente est :

$$
\lambda=\ell_0^{-2},
\qquad
\mu^2=2\ell_0^{-2}
$$

pour le potentiel :

$$
V=-\mu^2|\Phi|^2+\lambda|\Phi|^4
$$

et $\phi_0=1$.

**Cette correction est nécessaire avant de qualifier la fermeture physique du modèle.**

---

# 24. Campagne SPARC historique : pourquoi les anciens chiffres ne sont pas une validation actuelle

Le README historique contient un ancien résultat :

> « 175 galaxies », « gain de 19 % de $\chi^2$ ».

Il contient également un ancien solveur avec :

- $\eta_{\rm curr}$ ;
- variation de $\Upsilon$ ;
- facteur géométrique $\gamma_{\rm geom}$ ;
- correction empirique.

Ce solveur ne respecte pas le protocole SPARC-A actuel.

Un audit ultérieur a également rencontré un problème de correspondance Master/Rotmod :

```text
Galaxies appariées : 0
```

avant correction déterministe du nommage.

Il est donc interdit de réutiliser le « gain de 19 % » comme résultat scientifique actuel sans reprendre l'audit complet avec :

1. correspondance bijective 175/175 ;
2. fichiers officiels uniquement ;
3. paramètres globaux verrouillés ;
4. aucune fuite de $V_{\rm obs}$ ;
5. comparaison a posteriori seulement.

---

# 25. Dimensions et paramètres fondamentaux

Le projet doit distinguer strictement :

| Élément | Statut |
|---|---|
| $d=3$, $D=4$ | 🟢 hypothèse structurelle fixée |
| $C=|\Phi|^2$ | 🟢 invariant du champ complexe / observable du jouet |
| $C_c=0.2$ | 🟡 entrée du modèle |
| $4/3$ global | 🔴 abandonné |
| $4/3$ comme limite de transition | 🟡 hypothèse / résultat de construction numérique |
| $3/4$ | 🟡 relation inverse, non dérivation indépendante |
| $1/4$ | 🟡 conséquence conditionnelle de $C_c=1/5$ |
| $\theta\simeq28.955^\circ$ | 🟢 conséquence mathématique conditionnelle |
| $r$ spatial émergent | 🔴 non dérivé |
| $D_{\rm eff}=3/4$ ou $4/3$ | 🔴 non établi |
| suppression $10^{120}$ | 🔴 non obtenue |
| équations d'Einstein émergentes | 🔴 non dérivées |
| $g_{\mu\nu}^{\rm eff}[C,\nabla C]$ | 🟡 pont à fermer |
| solveur B1–D4 | 🟢 qualifié pour les tests numériques effectués |
| validation astrophysique SPARC-A | 🟡 protocole défini, validation finale à effectuer |

---

# 26. Hypothèse sur le temps émergent

Une histoire quasi-classique $H_i$ pourrait posséder une métrique $g_{\mu\nu}^{(i)}$ et un temps propre :

$$
\tau_i
=
\int
\sqrt{
-g_{\mu\nu}^{(i)}
\frac{dx^\mu}{d\lambda}
\frac{dx^\nu}{d\lambda}
}
\,d\lambda.
$$

Une hiérarchie heuristique :

$$
\tau_{\rm micro}
\ll
\tau_{\rm corr}
\ll
\tau_{\rm macro}
$$

reste une hypothèse de travail.

Elle ne constitue pas une mesure expérimentale de trois temps fondamentaux.

---

# 27. Hypothèse morphologique « condensation S² »

Une hypothèse de travail plus spéculative envisage qu'une condensation collective puisse être associée à une transition morphologique :

```text
sphérique → oblate → disque
```

avec éventuellement une modification effective du champ gravitationnel et des courbes de rotation.

Cette idée est **non démontrée**.

Elle ne doit être testée qu'après les campagnes de robustesse fondamentales et ne doit pas être utilisée comme justification a posteriori d'un profil galactique.

---

# 28. Ce que le programme établit réellement

Le programme a permis de :

- éliminer plusieurs constructions divergentes ;
- montrer la robustesse de certains invariants du modèle jouet ;
- tester une correction localisée conservant une asymptote newtonienne ;
- corriger des erreurs algébriques du modèle de Landau ;
- montrer que les rétroactions simples testées ne sélectionnent pas $C_c=0.2$ ;
- qualifier numériquement le solveur covariant pour B1–D4 ;
- identifier précisément le pont manquant entre champ et métrique ;
- définir un protocole SPARC sans fuite observationnelle.

Il n'a pas encore démontré :

- l'émergence d'une métrique 3+1 depuis les corrélations ;
- la dérivation de $G$ ;
- la dérivation de $C_c=1/5$ ;
- la dérivation fondamentale de $4/3$ ;
- la résolution du problème de la constante cosmologique ;
- la dérivation des équations d'Einstein ;
- une explication complète des courbes de rotation SPARC ;
- une validation indépendante par lentillage gravitationnel ;
- une théorie complète de gravité quantique.

---

# 29. Arbre décisionnel scientifique actuel

```text
                 Champ complexe covariant Φ
                           │
                           ▼
                      C = |Φ|²
                           │
                           ▼
                 Corrélations de C / Φ
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
          structure spatiale ?   pas de structure
                 │                   │
                 ▼                   ▼
          distance émergente ?    branche ouverte
                 │
                 ▼
            r émergent ?
                 │
                 ▼
          métrique effective
                 │
                 ▼
       géodésiques / V_c(r)
                 │
                 ▼
        comparaison SPARC
```

Aucune flèche n'est considérée comme démontrée simplement parce qu'elle est écrite dans le schéma.

---

# 30. Critère de falsifiabilité

Une version scientifique fermée devra suivre :

$$
S_{\rm micro}
\rightarrow
P(\Phi)
\rightarrow
\mathcal L_{\rm eff}
\rightarrow
g_{\mu\nu}^{\rm eff}
\rightarrow
V_c(r)
\rightarrow
\text{observables}.
$$

Les paramètres effectifs doivent être :

1. dérivés ;
2. mesurables indépendamment ;
3. ou fixés par des constantes universelles explicitement justifiées.

Ils ne doivent pas être choisis pour reproduire l'observable finale.

---

# 31. Règles non négociables du programme

### Règle 1 — pas de dimension spatiale variable

$$
d=3.
$$

### Règle 2 — pas de recalibrage par galaxie

Les constantes fondamentales doivent être communes.

### Règle 3 — pas de fuite observationnelle

$V_{\rm obs}$ et $V_{\rm flat}$ ne doivent pas entrer dans le solveur.

### Règle 4 — pas de fonction MOND injectée

Aucune $\mu(y)$ ou $\nu(y)$ empirique ne doit être ajoutée pour améliorer artificiellement l'ajustement.

### Règle 5 — distinguer entrée et conséquence

Une valeur fixée dans le modèle ne devient pas une prédiction.

### Règle 6 — conserver les échecs

Les branches abandonnées restent dans le journal, mais avec leur statut explicite.

### Règle 7 — distinguer qualification numérique et validation physique

```text
solveur validé
≠
théorie physique validée.
```

### Règle 8 — aucun résultat observationnel ne doit être interprété avant l'audit du pipeline

En particulier, aucune comparaison SPARC ne doit être considérée comme probante tant que le mapping 175/175 n'est pas vérifié.

---

# 32. Synthèse finale

La position scientifique actuelle peut être résumée ainsi :

> **Le programme H2C possède désormais une formulation covariante de champ complexe suffisamment précise pour être testée numériquement, et un solveur qualifié sur plusieurs tests analytiques et de conservation. En revanche, le pont entre le champ de cohérence et une métrique gravitationnelle effective reste une hypothèse à fermer, et aucune validation astrophysique définitive n'est encore acquise.**

La chaîne de travail actuelle est :

$$
\boxed{
\Phi
\rightarrow
C=|\Phi|^2
\rightarrow
g_{\mu\nu}^{\rm eff}[C,\nabla C]
\rightarrow
V_c(r)
\rightarrow
\mathrm{SPARC}
}
$$

avec deux contraintes centrales :

$$
\boxed{
\text{aucune fuite observationnelle}
}
$$

et

$$
\boxed{
\text{aucune constante présentée comme dérivée si elle est encore imposée}
}
$$

Le problème scientifique central reste :

> **Existe-t-il une dynamique microscopique suffisamment précise pour produire simultanément la cohérence $C$, une structure métrique émergente, la limite newtonienne, les équations d'Einstein et les paramètres cosmologiques observés sans les imposer à l'avance ?**

---

## Annexe A — Historique des branches fermées

Les campagnes suivantes restent archivées comme historique :

- 61H-10A : inversion/régularisation de phase — résultat de jouet ;
- 61H-13 : branche MOND-like — historique, non fondamentale ;
- tests 39–45 : exploration de scaling et correction localisée ;
- tests 49–51 : recherche de sélection dynamique de $C_c$ ;
- Landau 68–70 : audit analytique du seuil $v_c=2u$ ;
- V9.1-R : branche de réfraction scalaire fermée comme modèle prédictif.

Aucune de ces branches ne doit être présentée comme une preuve de gravité émergente.

---

## Annexe B — Référentiel des statuts

- 🟢 **Établi / vérifié dans le cadre indiqué**
- 🟡 **Hypothèse, construction ou résultat conditionnel**
- 🟠 **Historique / branche exploratoire**
- 🔴 **Échec, abandon ou non-démontré**
- ⚪ **Question ouverte**

---

## Annexe C — Principe directeur

> **On ne choisit plus le résultat recherché. On cherche d'abord si la dynamique le produit, puis on conserve aussi bien les succès que les échecs.**

Document de réflexion personnelle et d'open science — à confronter à la littérature scientifique, aux données officielles et à des validations indépendantes.
