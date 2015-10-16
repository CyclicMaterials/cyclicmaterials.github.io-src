Title: CSS
Date: 2015-10-14 14:53
Authors: Frederik Krautwald
Slug: cyclic-materials-css-naming-conventions

# Cyclic Materials CSS Naming Conventions

> Cyclic Materials CSS relies on *structural class names* and *meaningful
hyphens*, i.e., not using hyphens merely to separate words. This helps to work
around the current limits of applying CSS to the DOM, and to better communicate
the relationships between classes.
>
> The primary architectural division is between the patterns **[atom](#Atoms)**, 
**[molecule](#Molecules)**, and **[organism](#Organisms)**.

#### Table of Contents

- [Components](#Components)
- [pattern](#pattern)
- [ComponentName](#ComponentName)
- [ComponentName--modifierName](#ComponentName--modifierName)
- [ComponentName_descendentName](#ComponentName_descendentName)
- [ComponentName.is-stateOfComponent](#is-stateOfComponent)

<a name="Component"></a>
## Components

> The CSS responsible for component-specific styling.

**Syntax:** `<pattern>-<ComponentName>[--modifierName|_descendentName]`

This has several benefits when reading and writing HTML and CSS:

- it helps to distinguish between classes for the root of the component, 
  descendent elements, and modifications,
- it keeps the specificity of selectors low, and
- it helps to decouple presentation semantics from document semantics.

<a name="pattern"></a>
### Pattern

Components are prefixed with a pattern, which borrows from atomic design 
principles.

```css
.atom-AutogrowTextarea { /* ... */ }
.molecule-Input { /* ... */ }
```

This makes it clear, when reading the HTML, which components
are part of each pattern.

There are three distinct patterns:

<a name="Atoms"></a>
#### Atoms

Atom components are a set of **basic visual and non-visual utility components.**
They include components for working with layout, user input, selection and 
scaffolding apps. They include abstract components like color palettes, fonts, 
and animations.

<a name="Molecules"></a>
#### Molecules

Molecule components are a set of visual components that implement
Material Design. They are **groups of components that function together
as a unit**.

<a name="Organisms"></a>
#### Organisms

Organisms are **groups of molecules (and atoms) joined together to form 
a distinct section of an interface**. Organisms can consist of similar or
disparate molecule types.

<a name="ComponentName"></a>
### ComponentName

The component’s name is written in pascal case. Nothing else in HTML/CSS uses
pascal case.

```css
.molecule-InputCharCounter { /* ... */ }
```

```html
<div class="molecule-InputCharCounter">
  ...
</div>
```

<a name="ComponentName--modifierName"></a>
### ComponentName--modifierName

A component modifier is a class that modifies the presentation of the base
component in some form, e.g., for a certain configuration of the component.
Modifier names are written in camel case and is separated from the component
by two hyphens. A modifier class always extends the base class and inherits
all base declarations, of which some may be overridden.

```css
/* Core flex layout */
.atom-FlexLayout { /* ... */ }
/* Vertical flex layout */
.atom-FlexLayout--vertical { /* ... */ }
```

```html
<div class="atom-Flexlayout--vertical">...</div>
```

<a name="ComponentName_descendentName"></a>
### ComponentName_descendentName

A component descendent is a class that is attached to the descendent node
of a component. It’s responsible for applying presentation directly
to the descendent on behalf of a particular component. Descendent names
are written in camel case.

```html
<div class="atom-AutogrowTextarea">
  <div class="atom-AutogrowTextarea_mirrorText">...</div>
  <div class="atom-AutogrowTextarea_container">
    <textarea class="atom-AutogrowTextarea_textarea"></textarea>
  </div>
</div>
```

<a name="is-stateOfComponent"></a>
### ComponentName.is-stateOfComponent

`is-stateOfComponent` is used to reflect changes to a component’s state.
The state name is camel case. **These classes are never styled directly;
they should be and are always used as an adjoining class.**

This means that the same state names are used in multiple contexts, but every
component defines its own styles for the state, as they are scoped
to the component.

```css
.molecule-InputContainer { /* ... */ }
.molecule-InputContainer.is-Highlighted { /* ... */ }
```

```html
<div class="molecule-InputContainer is-Highlighted">
  ...
</div>
```
