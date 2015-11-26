Title: Release: molecule-input version 6.2.0
Date: 2015-09-30 14:29:56
Authors: Frederik Krautwald
Category: Releases
Tags: release, minor, molecule, input
Slug: release-molecule-input-6.2.0
Summary: MINOR RELEASE: molecule-input version 6.2.0

[molecule-input version 6.2.0][1] has just been released. This release includes
[bug fixes and new features][2].

Head over to the repository to [download this release][1]. You can also obtain it
through *npm* by issuing the following command in your terminal:

```shell
$ npm i @cyclic/molecule-input@6.2.0
```

Bug fixes in this release:

- **InputContainer:** keep `.is-highlighted` CSS class when invalid
  and still focused.

New features in this release:

- it is now possible to set the initial value through properties. Currently,
  only **Input** supports this. **Textarea** will support this when
  **atom-autogrow-textarea** has implemented support.

[See the full changelog][2].

[1]: https://github.com/CyclicMaterials/molecule-input/releases/tag/v6.2.0
[2]: https://github.com/CyclicMaterials/molecule-input/blob/master/CHANGELOG.md#v620-2015-09-30
