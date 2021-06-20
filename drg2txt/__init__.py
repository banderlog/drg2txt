import pickle
import importlib.resources


package_name = __name__.split(".")[0]
# load weights from JSON
with importlib.resources.path(package_name, "data.pickle") as f_path:
    with open(f_path, 'rb') as f:
        drg_descr, drg_mdc, mdc_descr = pickle.load(f)


def get_drg_description(drg: int) -> str:
    return drg_descr.get(drg)


def get_mdc_code(drg: int) -> int:
    return drg_mdc.get(drg)


def get_mdc_description(mdc: int) -> str:
    return mdc_descr.get(mdc)


def get_drg_mdc_description(drg: int) -> str:
    return mdc_descr.get(drg_mdc.get(drg))
