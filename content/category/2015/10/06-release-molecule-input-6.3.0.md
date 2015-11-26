Title: Release: molecule-input version 6.3.0
Date: 2015-10-06 16:08:26
Authors: Frederik Krautwald
Category: Releases
Tags: release, minor, molecule, input
Slug: release-molecule-input-6.3.0
Summary: MINOR RELEASE: molecule-input version 6.3.0

[molecule-input version 6.3.0][1] has just been released. This release includes
[new features and performance improvements][2].

Head over to the repository to [download this release][1]. You can also obtain it
through *npm* by issuing the following command in your terminal:

```shell
$ npm i @cyclic/molecule-input@6.3.0
```

New features in this release:

- contracts for properties. If a property set on a component
  is not of the correct type, a `TypeError` will be thrown.

Steps have also been taken to improve performance:

- internally, `Rx.Observable` combinations have been optimized
  with `distinctUntilChanged()`.

[See the full changelog][2].

[1]: https://github.com/CyclicMaterials/molecule-input/releases/tag/v6.3.0
[2]: https://github.com/CyclicMaterials/molecule-input/blob/master/CHANGELOG.md#v630-2015-10-06
