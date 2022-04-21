from __future__ import annotations

from os.path import dirname
from os.path import join as pjoin

import nibabel as nib
import pytest

from reorient_nii import get_orientation
from reorient_nii import load
from reorient_nii import reorient


data_path = pjoin(dirname(__file__), "data")


def test_reorient_return_type():
    fname = "tpl-MNI152NLin6Asym_label-RAS_res-01_desc-brain_T1w.nii.gz"
    fpath = pjoin(data_path, fname)
    nii = nib.load(fpath)
    out = reorient(nii)
    assert isinstance(out, nib.nifti1.Nifti1Image)


def test_get_orientation_return_type():
    fname = "tpl-MNI152NLin6Asym_label-RAS_res-01_desc-brain_T1w.nii.gz"
    fpath = pjoin(data_path, fname)
    nii = nib.load(fpath)
    out = get_orientation(nii)
    assert isinstance(out, tuple)


def test_load_return_type():
    fname = "tpl-MNI152NLin6Asym_label-RAS_res-01_desc-brain_T1w.nii.gz"
    fpath = pjoin(data_path, fname)
    out = load(fpath)
    assert isinstance(out, nib.nifti1.Nifti1Image)


@pytest.mark.parametrize(
    "orientation,target_orientation",
    [("RAS", "LAS"), ("LAS", "RAS")],
)
def test_reorient_ras(orientation, target_orientation):
    fname = f"tpl-MNI152NLin6Asym_label-{orientation}_res-01_desc-brain_T1w.nii.gz"
    fpath = pjoin(data_path, fname)
    nii = nib.load(fpath)
    out = reorient(nii, orientation=target_orientation)
    actual = get_orientation(out)
    desired = tuple(target_orientation)
    assert actual == desired


def test_reorient_same_orientation():
    fname = "tpl-MNI152NLin6Asym_label-RAS_res-01_desc-brain_T1w.nii.gz"
    fpath = pjoin(data_path, fname)
    nii = nib.load(fpath)
    out = reorient(nii, orientation="RAS")
    assert out is nii


def test_get_orientation():
    fname = "tpl-MNI152NLin6Asym_label-RAS_res-01_desc-brain_T1w.nii.gz"
    fpath = pjoin(data_path, fname)
    nii = nib.load(fpath)
    actual = get_orientation(nii)
    desired = ("R", "A", "S")
    assert actual == desired
