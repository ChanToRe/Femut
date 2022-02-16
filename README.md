```
   ___                    _   
  / __\__ _ __ ___  _   _| |_ 
 / _\/ _ \ '_ ` _ \| | | | __|
/ / |  __/ | | | | | |_| | |_ 
\/   \___|_| |_| |_|\__,_|\__|

```
### Introduction
 * It is a package that allows you to estimate the height of the owner of the femur using the femur length.
 * In 2019, I reorganized the code I wrote as a hobby while learning Python.
---
### Installation
```python
#pip
pip install Femut
```

```bash
#github
git clone https://github.com/ChanToRe/Femut.git
```
---
### Docs
 * The package contains a CUI program.
 * This project use 'pandas'
 * Formula
   * Pearson
    - Male : T = 81.306 + 1.880 * x
    - Female : T = 72.844 + 1.945 * x
   * Huzii
    - Male : T = (2.47 * (Length*10) + 549.01)/10
    - Female : T = (2.24 * (Length*10) + 610.43)/10
   * Trotter&Glaser(Only Male)
    - T = 2.15 * x + 72.57

### Instructions
```python
#Pearson
pearson(Length, Sex='Male or Female')

#Trotter&Glaser
tng(Length)

#Huzii
huzii(Length, Sex='Male or Female')
```
