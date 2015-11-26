Title: Release: molecule-input version 6.3.1
Date: 2015-10-09 01:21:58
Authors: Frederik Krautwald
Category: Releases
Tags: release, patch, molecule, input
Slug: release-molecule-input-6.3.1
Summary: PATCH RELEASE: molecule-input version 6.3.1

[molecule-input version 6.3.1][1] has just been released. This release includes
[bug fixes and performance improvements][2].

Head over to the repository to [download this release][1]. You can also obtain it
through *npm* by issuing the following command in your terminal:

```shell
$ npm i @cyclic/molecule-input@6.3.1
```

This release fixes:

- label float synchronization when using the *Textarea* component, and
- overlap between label and placeholder of the *Input* component.

Steps have also been taken to increase performance:

- the *InputContainer* component doesn’t render empty DIVs and excludes
  rendering of `.molecule-InputContainer_floatLabelPlaceholder`, and
- internally, `Rx.Observable` combinations have been optimized.

[See the full changelog][2].

[1]: https://github.com/CyclicMaterials/molecule-input/releases/tag/v6.3.1
[2]: https://github.com/CyclicMaterials/molecule-input/blob/master/CHANGELOG.md#v631-2015-10-09
