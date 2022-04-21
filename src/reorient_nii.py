from __future__ import annotations

from pathlib import Path

import nibabel as nib
from nibabel.orientations import axcodes2ornt
from nibabel.orientations import ornt_transform


__version__ = "0.1.0"


def reorient(
    nii: nib.Nifti1Image,
    orientation: str | tuple[str, str, str] = "RAS",
) -> nib.Nifti1Image:
    """Reorients a nifti image to specified orientation. Orientation string or tuple
    must consist of "R" or "L", "A" or "P", and "I" or "S" in any order."""
    orig_ornt = nib.io_orientation(nii.affine)
    targ_ornt = axcodes2ornt(orientation)
    transform = ornt_transform(orig_ornt, targ_ornt)
    reoriented_nii = nii.as_reoriented(transform)
    return reoriented_nii


def load(
    filepath: str | Path,
    orientation: str | tuple[str, str, str] = "RAS",
) -> nib.Nifti1Image:
    """Loads and reorients a nifti image. Orientation string or tuple must consist of
    "R" or "L", "A" or "P", and "I" or "S" in any order."""
    nii = nib.load(filepath)
    reoriented_nii = reorient(nii, orientation=orientation)
    return reoriented_nii


def get_orientation(nii: nib.Nifti1Image) -> tuple[str, str, str]:
    """Gets the orientation of a nifti image."""
    orientation = nib.aff2axcodes(nii.affine)
    return orientation
