Title: Release: molecule-input version 6.0.1
Date: 2015-09-25 00:33:19
Authors: Frederik Krautwald
Category: Releases
Tags: release, patch, molecule, input
Slug: release-molecule-input-6.0.1
Summary: PATCH RELEASE: molecule-input version 6.0.1

[molecule-input version 6.0.1][1] has just been released. This release is a
correction to v6.0.0 that somehow were released without essential commits.
The [breaking changes][2] in this release actually belongs to the former
version; hence no major version bump again.

Head over to the repository to [download this release][1]. You can also obtain
it through *npm* by issuing the following command in your terminal:

```shell
$ npm i @cyclic/molecule-input@6.0.1
```

**Breaking Changes:**

Rename components.
Component functions and directories are capitalized.

Before:

- `moleculeInput`
- `moleculeInputCharCounter`
- `moleculeInputContainer`
- `moleculeInputError`
- `moleculeInputTextarea`

After:

- `Input`
- `InputCharCounter`
- `InputContainer`
- `InputError`
- `InputTextarea`

Rename `noLabelFloat` property to `disableLabelFloat`.

`InputCharCounter` and `InputError` no longer accepts `className` property.

[1]: https://github.com/CyclicMaterials/molecule-input/releases/tag/v6.0.1
[2]: https://github.com/CyclicMaterials/molecule-input/blob/master/CHANGELOG.md#v601-2015-09-25
