# drg2txt

Mapper for DRG/MDC numeric codes to their text description.
Uses  [MS-DRG v38.1](https://www.cms.gov/icd10m/version38-1-fullcode-cms/fullcode_cms/P0001.html).

## Installation

`pip install drg2txt`


## Examples

```python
import drg2txt

[drg2txt.get_drg_description(i) for i in [1, 10, 100, 'WOLOLO']]
>>>
['Heart transplant or implant of heart assist system with MCC',
 'Pancreas transplant',
 'Seizures with MCC',
 None]


[drg2txt.get_drg_mdc_description(i) for i in [1, 10, 100, 'WOLOLO']]
>>>
['Has no MDC', 'Has no MDC', 'Diseases and disorders of the nervous system', None]


[drg2txt.get_mdc_code(i) for i in [1, 10, 100, 'WOLOLO']]
[-1, -1, 1, None]
```

Look on original dicts: `from drg2txt import drg_descr, drg_mdc, mdc_descr`
