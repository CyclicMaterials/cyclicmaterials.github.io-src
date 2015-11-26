Title: Release: molecule-input version 6.1.0
Date: 2015-09-26 14:29:56
Authors: Frederik Krautwald
Category: Releases
Tags: release, minor, molecule, input
Slug: release-molecule-input-6.1.0
Summary: MINOR RELEASE: molecule-input version 6.1.0

[molecule-input version 6.1.0][1] has just been released. This release includes
[bug fixes and new features][2].

Head over to the repository to [download this release][1]. You can also obtain it
through *npm* by issuing the following command in your terminal:

```shell
$ npm i @cyclic/molecule-input@6.1.0
```

Bug fixes in this release:

- **Input:** wrong component CSS class name
- **InputContainer:** supply correct argument to `getInputElement()`
- **inputContainer:** remove get `maxLength` if unspecified
- **makeInputContainer:** prevent injected component class names leak

New features in this release:

- **CSS:** add CSS all entry file

[See the full changelog][2].

[1]: https://github.com/CyclicMaterials/molecule-input/releases/tag/v6.1.0
[2]: https://github.com/CyclicMaterials/molecule-input/blob/master/CHANGELOG.md#v610-2015-09-26
