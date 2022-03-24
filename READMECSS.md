# Classes CSS utilisables

## Colors

### Couleurs de fond

Utiliser la classe `.bg-${color}` où color est parmi les variables suivantes :

![#f03c15](https://via.placeholder.com/15/fd8061/000000?text=+) `accent`

![#f03c15](https://via.placeholder.com/15/fff/000000?text=+) `white`

![#f03c15](https://via.placeholder.com/15/fec0a0/000000?text=+) `color-accent-middle`

![#f03c15](https://via.placeholder.com/15/fbd5d0/000000?text=+) `color-accent-light`

![#f03c15](https://via.placeholder.com/15/a7c8fd/000000?text=+) `blue`

![#f03c15](https://via.placeholder.com/15/fffbf1/000000?text=+) `color-bg-shade`

![#f03c15](https://via.placeholder.com/15/24997f/000000?text=+) `color-primary`

![#f03c15](https://via.placeholder.com/15/fff/000000?text=+) `transparent`

### Couleurs de texte

Utiliser la classe `.txt-${color}` où color est parmi les variables suivantes :

![#f03c15](https://via.placeholder.com/15/2e2f37/000000?text=+) `black`

![#f03c15](https://via.placeholder.com/15/fd8061/000000?text=+) `accent`

![#f03c15](https://via.placeholder.com/15/24997f/000000?text=+) `color-primary`

![#f03c15](https://via.placeholder.com/15/fbd5d0/000000?text=+) `color-accent-light`

![#f03c15](https://via.placeholder.com/15/fec0a0/000000?text=+) `color-accent-middle`

![#f03c15](https://via.placeholder.com/15/fffbf1/000000?text=+) `color-bg-shade`

![#f03c15](https://via.placeholder.com/15/59dbb7/000000?text=+) `green`

![#f03c15](https://via.placeholder.com/15/ee4062/000000?text=+) `red`

## Font

TODO DOC

## Margin / Padding

TODO DOC

## Sizing

TODO DOC

## Shadows

TODOCSS

## Display

TODO DOC

## Les boutons

Les balises boutons, les éléments avec la classe `.button` sont stylisés de la façon suivante :

- Ajouter la classe `.primary` pour avec le bouton de base
- Ajouter la classe `.secondary`pour le bouton secondaire
- Ajouter la classe `.no-style` pour un bouton sans style

## Les tags

Utiliser la classe `.tag` puis la couleur du tag que vous souhaitez avec `.primary` ou `.green` ou `.blue` ou `.accent` ou `.accent-middle`

## Messages

Utiliser les classes `.error-message` et `success-message` pour vos messages d'erreurs et de success

## Inputs

Pour vos formulaires, merci d'utiliser les classes suivantes :

```

<div class="input__label">{{ form.username.label }}</div>
<div class="input__field">{{ form.username }}</div>
```

## Utiliser flexbox

Utiliser flexbox en ajoutant la classe `.d-${breakpoint?}-flex` où `breakpoint` pour être vide ou avoir les valeurs suivantes : ` xs, sm, md, lg, xl`

Exemples : `.d-flex`, `.d-md-flex`

Puis les classes suivantes sont à votre dispositions :

```
      .flex#{$breakpoint}-column
      .flex#{$breakpoint}-row-reverse
      .flex#{$breakpoint}-column-reverse

      .flex#{$breakpoint}-wrap
      .flex#{$breakpoint}-nowrap
      .flex#{$breakpoint}-wrap-reverse+
      .flex#{$breakpoint}-fill
      .flex#{$breakpoint}-grow-0
      .flex#{$breakpoint}-grow-1
      .flex#{$breakpoint}-grow-2
      .flex#{$breakpoint}-shrink-0
      .flex#{$breakpoint}-shrink-1

      .justify-content#{$breakpoint}-start
      .justify-content#{$breakpoint}-end
      .justify-content#{$breakpoint}-center
      .justify-content#{$breakpoint}-between
      .justify-content#{$breakpoint}-around

      .align-items#{$breakpoint}-start
      .align-items#{$breakpoint}-end
      .align-items#{$breakpoint}-center
      .align-items#{$breakpoint}-baseline
      .align-items#{$breakpoint}-stretch

      .align-content#{$breakpoint}-start
      .align-content#{$breakpoint}-end
      .align-content#{$breakpoint}-center
      .align-content#{$breakpoint}-between
      .align-content#{$breakpoint}-around
      .align-content#{$breakpoint}-stretch

      .align-self#{$breakpoint}-auto
      .align-self#{$breakpoint}-start
      .align-self#{$breakpoint}-end
      .align-self#{$breakpoint}-center
      .align-self#{$breakpoint}-baseline
      .align-self#{$breakpoint}-stretch

```

où `breakpoints` pour être vide ou avoir les valeurs suivantes : ` xs, sm, md, lg, xl`

Exemples : `.justify-content-xl-start` , `.justify-content-start`

## Utiliser grid

Utiliser grid en mettant une classe de ce type : `.grid-${breakpoint?}-column${nbDeColumn}` ou `.grid-${breakpoint}-row${nbDeRows}` où `nbDeColumn ou nbDeRows` peut aller de 1 à 5 et `breakpoint` pour être vide ou avoir les valeurs suivantes : ` xs, sm, md, lg, xl`

Exemples : `.grid-column2`, `.grid-sm-row1`

## Non fait

- Les bordures
