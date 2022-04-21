# reorient-nii

Load and reorient nifti images

[![PyPI](https://img.shields.io/pypi/v/reorient-nii)](https://pypi.org/project/reorient-nii/)

## Installation

`pip install reorient-nii`

## Understanding Orientation

- The image voxel orientation indicates how the image array data is stored.
- The voxel orientation is represented by three axes: Left/Right, Anterior/Posterior, and Inferior/Superior.
- The orientation is a string of three letters representing the order and increasing direction of the axes.
    - For example, `"RAS"` orientation corresponds to the first axis being ordered from Left to Right, the second axis from Posterior to Anterior and the third axis from Inferior to Superior.
    - This orientation is also sometimes referred to as RAS+ to more clearly convey that the letters represent the increasing direction.

## Usage

`reorient-nii` exposes three functions
- `reorient`
- `load`
- `get_orientation`

**`reorient`** will reorient a nifti image to the desired voxel orientation by flipping and / or reordering the voxel axes. The orientation can be provided as a string of three characters or a length three tuple of strings reflecting the desired positive end of the voxel axes. For example, if the desired orientation is RAS+ the orientation can be specified as `"RAS"` or `('R', 'A', 'S')`. The orientation must have a single character for each of the voxel axes indicating the positive direction of the voxel axis. This means the orientation must consist of "R" or "L", "A" or "P", "I" or "S", in any order. For example, the orientation `"RLP"` is not valid since "R" and "L" are directions for the same voxel axis and only one can indicate the positive direction. The reoriented nifti image will have voxel axes that match the directions in `orientation`. Note, this function does not resample, register or de-oblique an image, it only flips and / or reorders the voxel axes, chaning the storage of the image array data. The following are valid orientations and can also be specified as a tuple as described above instead of a single string.

`orientation: ('RAS' or 'RAI' or 'RPS' or 'RPI' or 'LAS' or 'LAI' or
         'LPS' or 'LPI' or 'RSA' or 'RSP' or 'RIA' or 'RIP' or 'LSA' or
         'LSP' or 'LIA' or 'LIP' or 'ARS' or 'ARI' or 'ALS' or 'ALI' or
         'PRS' or 'PRI' or 'PLS' or 'PLI' or 'ASR' or 'ASL' or 'AIR' or
         'AIL' or 'PSR' or 'PSL' or 'PIR' or 'PIL' or 'SRA' or 'SRP' or
         'SLA' or 'SLP' or 'IRA' or 'IRP' or 'ILA' or 'ILP' or 'SAR' or
         'SAL' or 'SPR' or 'SPL' or 'IAR' or 'IAL' or 'IPR' or 'IPL',
         default value: RAS)`

**`load`** will load the nifti image and reorient it to the desired orientation (default="RAS").

**`get_orientation`** will get the orientation of a nifti image as a tuple of 3 strings indicating the labels for the positive end of the voxel axes.

## API

```python
# src/reorient_nii.py

def reorient(
    nii: nib.Nifti1Image,
    orientation: str | tuple[str, str, str] = "RAS",
) -> nib.Nifti1Image:
    """Reorients a nifti image to specified orientation. Orientation string or tuple
    must consist of "R" or "L", "A" or "P", and "I" or "S" in any order."""

def load(
    filepath: str | Path,
    orientation: str | tuple[str, str, str] = "RAS",
) -> nib.Nifti1Image:
    """Loads and reorients a nifti image. Orientation string or tuple must consist of
    "R" or "L", "A" or "P", and "I" or "S" in any order."""

def get_orientation(
    nii: nib.Nifti1Image,
) -> tuple[str, str, str]:
    """Gets the orientation of a nifti image."""

```


## License
The `reorient` function is a light weight version of Nipype's [Reorient function](https://github.com/nipy/nipype/blob/ecd5871b6/nipype/interfaces/image.py#L122-L223), copyright 2009-2016, Nipype developers, licensed under Apache 2.0 license. This project's `reorient` function removes several elements from the source code. The function is not a class method for a Nipype interface, it does not compute or save the affine transform, it does not save the reoriented image and it does not support backwards compatibility for Nibabel version < "2.4.0". See [LICENSE](LICENSE) for full license info.


## Contributing

1. Have or install a recent version of poetry (version >= 1.1)
1. Fork the repo
1. Setup a virtual environment (however you prefer)
1. Run poetry install
1. Run pre-commit install
1. Add your changes (adding/updating tests is always nice too)
1. Commit your changes + push to your fork
1. Open a PR
