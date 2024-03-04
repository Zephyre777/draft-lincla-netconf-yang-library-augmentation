# This is a demo instruction to the draft

## Introduction

The demo is ran based on netopeer2. It updated libyang and sysrepo to add the augmentation list

## Requirement
sysrepo(https://github.com/Zephyre777/sysrepo.git)
libyang(https://github.com/Zephyre777/libyang.git)
libnetconf2

## How to run
```
mkdir build; cd build  
cmake ..  
make  
make install  
```

## Augmentation list
By running a netopeer2 server and client, send the query ```get --filter-xpath /ietf-yang-library:yang-library/module-set/module/augmentation``` and the augmentation information of each module will be printed. See the picture attached.
 