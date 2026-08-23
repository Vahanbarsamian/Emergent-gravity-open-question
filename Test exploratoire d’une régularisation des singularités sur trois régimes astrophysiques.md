# Potentiel Gravitationnel Émergent et Résolution des Singularités via un Champ de Cohérence de Phase Borné

**Auteur :** Vahan Barsamian  
**Date :** Août 2026  
**Dépôt :** [H2C-Open-Project / Theoretical Physics Notes]  
**Licence :** MIT / CC-BY-4.0  

---

## Résumé

Nous proposons un modèle de gravité à champ scalaire émergent où le potentiel gravitationnel $\Phi(r)$ découle de déformations locales d'un champ de cohérence de phase $C(\mathbf{x})$. En imposant une borne supérieure absolue $C_{\text{max}} = 1,0$ et une ligne de base de cohérence du vide critique $C_c = 0,2000$, le modèle résout naturellement les infinités gravitationnelles aux petites échelles spatiales tout en retrouvant les comportements newtoniens et einsteiniens standards dans les limites de champ faible et fort. Appliqué aux données astrophysiques d'observation, le modèle rend compte avec précision des courbes de rotation plates des galaxies spirales (testé sur la galaxie d'Andromède M31) sans recourir aux halos de matière noire, concorde avec les observations de décalage vers le rouge gravitationnel (étoile S2 près de Sgr A*), et prédit un diamètre d'ombre pour les trous noirs supermassifs (M87*) conforme aux mesures de l'Event Horizon Telescope (EHT), tout en éliminant la singularité centrale ($r \to 0$).

---

## 1. Formulation Mathématique

Nous définissons la cohérence de phase locale $C(\mathbf{x}) \in [0, 1]$. Dans le vide, $C(\mathbf{x}) = C_c = 0,2000$. Les sources de matière déforment le champ de cohérence, générant un déficit ou un excès de cohérence $\Delta C(\mathbf{x}) = C(\mathbf{x}) - C_c$.

Le potentiel gravitationnel émergent $\Phi(\mathbf{x})$ est régi par une équation de type Poisson modifiée :

$$\nabla^2 \Phi(\mathbf{x}) = 4\pi G \alpha_{\text{émergence}} \left( C(\mathbf{x}) - C_c \right)$$

où $\alpha_{\text{émergence}} \approx \frac{c^2}{G}$ fixe l'échelle de couplage entre la perturbation du champ de cohérence et la densité d'énergie-impulsion effective.

### Mécanisme d'Évitement des Singularités
En Relativité Générale classique, $r \to 0$ conduit à une singularité de courbure ($\rho \to \infty$). Dans ce cadre théorique, lorsque $r \to 0$, $C(r)$ s'approche asymptotiquement de $C_{\text{max}} = 1,0000$. La saturation du champ de cohérence plafonne le gradient spatial $\nabla C(r)$, annulant l'accélération locale effective $g(r) = -\nabla \Phi(r)$ au centre absolu ($g \to 0$), ce qui substitue à la singularité ponctuelle centrale un cœur de phase saturé.

---

## 2. Validation Numérique et Observationnelle

Le modèle a été confronté à trois régimes astrophysiques clés :
