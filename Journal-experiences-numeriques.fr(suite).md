# Journal de laboratoire — modèles jouets

## Mécanisme de filtrage, rappel collectif et localisation par courbure

> **Statut.** Journal de laboratoire personnel. Les calculs décrits ici concernent des modèles jouets numériques. Ils ne constituent ni une théorie de la gravité, ni une dérivation de la métrique, de la constante gravitationnelle ou de la constante cosmologique.
>
> Les interprétations physiques restent hypothétiques. Les résultats numériques sont reproductibles à partir des équations et du code fournis, sous réserve des conventions numériques indiquées.

## 1. Objectif général

Le projet explore une question de travail : une variable collective de type géométrique pourrait-elle émerger d'une multiplicité de configurations microscopiques, par interférences, sélection de phase et dynamique de cohérence ?

La chaîne conceptuelle étudiée est :

\[
\text{degrés de liberté}
\rightarrow \text{configurations}
\rightarrow \text{amplitudes}
\rightarrow \text{interférences}
\rightarrow \text{cohérence collective}
\rightarrow \text{secteur quasi-classique}.
\]

Le présent journal ne franchit pas encore le passage vers une métrique effective \(g_{\mu\nu}\). Il teste uniquement des mécanismes intermédiaires.

## 2. Garde-fous méthodologiques

### 2.1 Statut de \(C\) et \(R\)

On utilise :

\[
A_i=e^{i\theta_i},
\qquad
C=\left|\frac1N\sum_i A_i\right|^2.
\]

\(C\) mesure la cohérence collective des phases. Il est invariant sous une rotation globale \(A_i\mapsto e^{i\varphi}A_i\).

Dans les premiers tests, on a aussi utilisé un résidu de type :

\[
R=\operatorname{Re}\left(\frac1N\sum_i A_i\right).
\]

Mais \(R\) dépend de la phase de référence globale. Deux secteurs peuvent avoir le même \(C\) et des valeurs très différentes de \(R\). Par conséquent :

- \(C\) est l'indicateur privilégié pour comparer des secteurs indépendants ;
- \(R\) peut être utilisé comme diagnostic relatif à l'intérieur d'un secteur dont la référence de phase est fixée ;
- \(R\) ne doit pas être interprété comme une énergie gravitationnelle, une densité d'énergie ou une force physique.

### 2.2 Aucun résultat ne dérive encore la gravité

Les quantités \(C\), \(R\), \(K\), \(\sigma\), \(\delta Q\) et les noyaux de couplage appartiennent au modèle jouet. Leur pertinence pour une théorie fondamentale reste à démontrer.

## 3. Formulation mathématique minimale

Une formulation plus précise de la question est :

\[
\Psi[g,\tau,E]
=
\int \mathcal D\Phi\,
\delta[g-\mathcal G(\Phi)]
\delta[\tau-\mathcal T(\Phi)]
\delta[E-\mathcal E(\Phi)]
\exp\left(\frac{iS_{\mathrm{micro}}[\Phi]}{\hbar}\right).
\]

Ici :

- \(\Phi\) représente les degrés de liberté microscopiques ;
- \(\mathcal G(\Phi)\) est une règle de reconstruction d'une géométrie candidate ;
- \(\mathcal T(\Phi)\) est une règle de reconstruction d'un temps effectif ;
- \(\mathcal E(\Phi)\) est une observable énergétique ;
- \(S_{\mathrm{micro}}\) est une action microscopique à définir.

Cette formule est un cadre de travail, pas une équation établie.

## 4. Test 8 — rappel imposé

On introduit directement une dynamique qui favorise la cohérence :

\[
\dot Q_i\propto \nabla_{Q_i}C.
\]

### Observation

Après une perturbation, \(C\) augmente sous cette dynamique.

### Limite

Le résultat est construit dans la définition du modèle : une dynamique qui maximise \(C\) tend nécessairement à augmenter \(C\). Ce test ne démontre donc pas l'existence d'un rappel physique.

### Statut

Test de référence uniquement. Il fournit une signature attendue pour comparer un mécanisme non imposé.

## 5. Test 9 — rappel dérivé des amplitudes

On remplace le rappel explicite par un couplage de phase :

\[
\dot\theta_i
=
\frac{K}{N}\sum_j\sin(\theta_j-\theta_i).
\]

Ce terme est lié aux amplitudes car :

\[
\operatorname{Im}(A_i^*A_j)
=
\sin(\theta_j-\theta_i).
\]

### Résultat enregistré

Pour une réalisation avec \(N=200\) :

| État | \(R\) | \(C\) |
|---|---:|---:|
| Initial | 0,221 | 0,118 |
| Après perturbation | 0,112 | 0,019 |
| \(K=0\) | 0,112 | 0,019 |
| \(K\geq0,5\) | 0,757 | 1,000 |

Un seuil progressif a été observé dans cette réalisation entre environ \(K=0,14\) et \(K=0,36\).

### Conclusion limitée

Une dynamique construite à partir des différences de phase peut restaurer la cohérence sans contenir explicitement \(\nabla C\). Cela reproduit une synchronisation collective connue dans les modèles d'oscillateurs couplés.

Cela ne démontre pas que la nature utilise ce mécanisme, ni que cette cohérence constitue une géométrie.

## 6. Test 10 — comparaison entre secteurs indépendants

Deux populations indépendantes ont été générées avec des graines distinctes et le même mécanisme de couplage.

### Résultat enregistré

| Secteur | \(R\) moyen ± écart-type | \(C\) moyen ± écart-type |
|---|---:|---:|
| A | 0,144 ± 0,744 | 0,994 ± 0,018 |
| B | 0,212 ± 0,721 | 0,996 ± 0,008 |

Le test statistique enregistré donne \(p=0,696\) pour la comparaison de \(C\). La dispersion de \(R\) est trop importante pour en faire un indicateur inter-sectoriel.

### Conclusion

L'universalité statistique de la cohérence n'est pas réfutée dans cette réalisation. Cette observation doit être formulée avec \(C\), et non avec \(R\).

## 7. Test 11 — couplage uniforme et énergie effective

On prend :

\[
E_i=Q_i^2,
\qquad
\theta_i=sE_i\bmod 2\pi.
\]

Le secteur cohérent est défini par une proximité angulaire autour de la phase moyenne finale.

### Résultat

Avec un couplage uniforme, toute la population se synchronise :

\[
N_{\mathrm{coh}}=N,
\qquad
\frac{\rho_{\mathrm{eff}}}{\rho_{\mathrm{micro}}}=1.
\]

### Diagnostic

Le rappel de cohérence uniforme ne sélectionne aucune région énergétique. Il explique au mieux une synchronisation globale, pas une suppression de l'énergie effective.

\[
\text{rappel de cohérence}
\neq
\text{sélection énergétique}.
\]

## 8. Tests 12–13 — couplage localisé en énergie

On introduit :

\[
w_{ij}
=
\exp\left[-\frac{(E_i-E_j)^2}{2\sigma^2}\right].
\]

### Résultats enregistrés

Pour \(N=300\), plusieurs graines et différentes valeurs de \(\sigma\), la réduction observée est de l'ordre de :

\[
\frac{\rho_{\mathrm{eff}}}{\rho_{\mathrm{micro}}}
\approx 0,4\text{--}0,6
\]

dans une zone intermédiaire de \(\sigma\).

### Limites

- Les écarts-types sont importants ;
- le facteur de suppression reste modeste ;
- il est sans rapport avec \(10^{120}\) ;
- \(\sigma\) est un paramètre libre ;
- la condition H10c, qui exige une valeur calculée et non ajustée, n'est pas satisfaite.

### Conclusion

La localisation énergétique peut produire une suppression partielle dans le modèle, mais son origine n'est pas encore dérivée de l'action microscopique.

## 9. Diagnostic du repliement des phases

Le noyau :

\[
w_{ij}=\frac{1+\cos(\theta_i-\theta_j)}2
\]

utilise une phase modulo \(2\pi\). Deux énergies éloignées peuvent donc produire des phases voisines après plusieurs tours.

Ce noyau mesure une distance sur le cercle des phases, mais pas une distance métrique dans l'espace des configurations ou des énergies.

Il est adapté à la synchronisation de phase, mais insuffisant pour représenter une localité configurationnelle.

## 10. Courbure de l'action et largeur de cohérence

Pour :

\[
S(Q)=sQ^2,
\]

on a :

\[
S''(Q)=2s.
\]

Autour d'un point stationnaire \(Q_c\) :

\[
S(Q_c+\delta Q)
\simeq
S(Q_c)+\frac12S''(Q_c)(\delta Q)^2.
\]

Une variation de phase d'ordre unité conduit à la largeur locale :

\[
\delta Q_{\mathrm{coh}}
\sim
\sqrt{\frac{\hbar}{|S''(Q_c)|}}
\]

à un facteur conventionnel près. Une autre convention donne \(\sqrt{2\hbar/|S''|}\).

Cette largeur est calculée à partir de la courbure de l'action et n'est pas une largeur énergétique ajoutée indépendamment.

Dans plusieurs dimensions, avec la hessienne :

\[
H_{ab}
=
\frac{\partial^2S}{\partial Q^a\partial Q^b},
\]

les largeurs propres sont :

\[
\delta Q_a
\sim
\sqrt{\frac{\hbar}{|\lambda_a|}}.
\]

## 11. Test 14 — noyau localisé par courbure

### Protocole

Paramètres principaux :

\[
N=300,
\qquad
s=0,3,
\qquad
\hbar=1,
\qquad
S''=0,6.
\]

Deux largeurs ont été comparées :

\[
\delta Q_1=\sqrt{\frac{\hbar}{|S''|}}\approx1,291,
\]

\[
\delta Q_2=\sqrt{\frac{2\hbar}{|S''|}}\approx1,826.
\]

Le noyau utilisé est :

\[
w_{ij}^{(\mathrm{curv})}
=
\exp\left[-\frac{(Q_i-Q_j)^2}{2\delta Q_{\mathrm{coh}}^2}\right].
\]

La dynamique de phase reste :

\[
\dot\theta_i
=
K\sum_jw_{ij}\sin(\theta_j-\theta_i).
\]

### Test de robustesse

Le calcul a été répété sur quatre graines indépendantes et trois valeurs de \(K\). Les résultats suivants sont des moyennes sur les graines.

| Largeur | \(K\) | \(C\) moyen | \(\rho_{\mathrm{eff}}/\rho_{\mathrm{micro}}\), 15° | Secteur moyen |
|---|---:|---:|---:|---:|
| \(\delta Q_1\) | 0,2 | 0,305 | 0,546 | 73 |
| \(\delta Q_1\) | 0,4 | 0,674 | 0,729 | 103 |
| \(\delta Q_1\) | 0,8 | 0,916 | 0,638 | 256 |
| \(\delta Q_2\) | 0,2 | 0,392 | 0,556 | 92 |
| \(\delta Q_2\) | 0,4 | 0,818 | 0,540 | 232 |
| \(\delta Q_2\) | 0,8 | 0,986 | 0,866 | 286 |

### Observations

Dans toutes les séries testées :

\[
C>0,
\qquad
0<\frac{\rho_{\mathrm{eff}}}{\rho_{\mathrm{micro}}}<1.
\]

Le noyau dérivé de la courbure produit donc une cohérence collective et une sélection énergétique partielle.

### Conclusion limitée

Le résultat soutient, dans ce modèle jouet, la chaîne :

\[
\text{courbure de l'action}
\rightarrow
\text{largeur de cohérence configurationnelle}
\rightarrow
\text{couplage localisé}
\rightarrow
\text{cohérence collective et réduction énergétique partielle}.
\]

Il ne démontre pas encore que cette réduction est universelle, ni qu'elle explique la constante cosmologique.

## 12. Comparaison entre les mécanismes

\[
\text{synchronisation globale}
\neq
\text{localisation configurationnelle}
\neq
\text{suppression énergétique}
\neq
\text{émergence géométrique}.
\]

Le couplage de phase uniforme restaure la cohérence, mais ne sélectionne pas l'énergie. Le noyau localisé par courbure réalise les deux partiellement dans la simulation, mais la dynamique reste encore un modèle effectif.

## 13. Formulation multidimensionnelle proposée

Une généralisation naturelle est :

\[
w_{ij}
=
\exp\left[
-\frac{1}{2\hbar}
(Q_i-Q_j)^T|H_c|(Q_i-Q_j)
\right].
\]

Cette forme utilise la hessienne de l'action au voisinage d'un secteur stationnaire. Elle est anisotrope lorsque les valeurs propres de \(H_c\) sont différentes.

Les directions presque plates, avec \(|\lambda_a|\) petit, donnent des largeurs grandes. Les directions fortement courbées donnent des largeurs petites.

## 14. Énergie effective et condition cosmologique

La contrainte de travail peut être écrite :

\[
0<\rho_{\mathrm{eff}}\ll\rho_{\mathrm{micro}}.
\]

Si l'on cherche un lien avec une contribution de type cosmologique :

\[
\rho_\Lambda=\frac{\Lambda c^2}{8\pi G},
\qquad
\Lambda>0.
\]

Mais aucune relation entre la suppression observée dans le modèle jouet et la constante cosmologique réelle n'est établie.

Pour satisfaire H10c, il faudrait que le noyau de localisation et sa largeur soient calculés à partir de \(S_{\mathrm{micro}}\), sans paramètre libre externe tel que \(\sigma\).

## 15. Hypothèses et statuts

| Hypothèse | Statut |
|---|---|
| La phase modulo \(2\pi\) suffit à définir la localité | Éliminée |
| Une dynamique de phases peut restaurer la cohérence | Soutenue dans le modèle |
| La cohérence seule sélectionne l'énergie | Réfutée par le test 11 |
| Une localisation configurationnelle peut réduire \(\rho_{\mathrm{eff}}\) | Soutenue partiellement |
| La largeur peut être calculée avec la courbure de l'action | Soutenue pour \(S=sQ^2\) |
| La réduction est universelle | Non testée suffisamment |
| \(0<\rho_{\mathrm{eff}}\ll\rho_{\mathrm{micro}}\) sans réglage | Non démontrée |
| Une géométrie effective émerge | Non testée |
| \(G_{\mathrm{eff}}\) et \(\Lambda_{\mathrm{eff}}\) sont calculables | Non testés |
| Les équations d'Einstein sont retrouvées | Non testé |

## 16. Prochaines expériences

### H22 — Origine de la localisation

Remplacer le noyau gaussien par une construction entièrement dérivée des amplitudes et de la courbure :

\[
\mathcal W_{ij}
=
\mathcal W_{ij}
[S_{\mathrm{micro}},A_i,A_j,H_i,H_j].
\]

Objectif : éliminer progressivement les paramètres libres et vérifier si une échelle de localisation émerge spontanément.

### H23 — Correcteurs individuels

Après identification d'un secteur collectif, définir les écarts :

\[
\delta Q_i=Q_i-Q_{\mathrm{collectif}},
\]

et étudier :

\[
\langle\delta Q_i\delta Q_j\rangle,
\qquad
\langle\delta Q_i E_j\rangle,
\qquad
\langle\delta Q_i\delta Q_j\rangle_{\mathrm{coh}}.
\]

L'ordre logique est :

\[
\text{cohérence collective}
\rightarrow
\text{stabilité collective}
\rightarrow
\text{correcteurs individuels et corrélations}.
\]

### H24 — Dynamique des configurations

Jusqu'ici, le noyau agit surtout sur les phases. Il faut ensuite tester une dynamique sur les configurations elles-mêmes :

\[
\dot Q_i=F_i[Q,A,H]+\xi_i,
\]

et mesurer si, après perturbation :

\[
d(Q(t),\mathcal A_{\mathrm{coh}})\rightarrow0.
\]

Ce test permettrait de distinguer une simple synchronisation de phase d'un véritable attracteur dans l'espace des configurations.

### H25 — Reconstruction géométrique

Seulement après les étapes précédentes, définir une application :

\[
\mathcal G:\Phi\mapsto g_{\mu\nu}^{\mathrm{candidate}},
\]

puis tester si une action effective contient :

\[
\sqrt{-g}R.
\]

## Conclusion du palier

Le résultat actuel ne constitue pas une théorie de gravité émergente. Il établit cependant une architecture de test plus précise :

\[
\boxed{
\text{action microscopique}
\rightarrow
\text{courbure locale}
\rightarrow
\text{largeur de cohérence}
\rightarrow
\text{filtrage configurationnel}
\rightarrow
\text{secteur collectif}
\rightarrow
\rho_{\mathrm{eff}}
}
\]

Le mécanisme de rappel peut restaurer la cohérence, mais la sélection énergétique nécessite une localisation supplémentaire. La courbure de l'action fournit une candidate naturelle pour cette localisation, avec un effet positif et non nul dans les tests réalisés.

La prochaine exigence scientifique est de vérifier si ce noyau peut être dérivé sans paramètre externe, puis de rechercher les corrélations individuelles à l'intérieur du secteur collectif.

---

*Journal de laboratoire — résultats numériques de modèles jouets ; interprétation physique non établie.*
