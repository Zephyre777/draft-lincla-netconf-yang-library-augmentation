# Yanglint Validation of the YANG module in the draft

## Introduction
This is a YANG validation that user can try with **yanglint** by typing the following commands.  
It is mainly used to prove the syntax correctness of the propsed YANG module. In the YANG module, the augmented list 'augmented-by' has a leafref ```'../../yanglib:module/yanglib:name'```. Only modules under the same module-set can augment each other, or the validation will fail. 
This targets the situation when vendors are grouping the modules in multiple module-sets.

## Example
There are three examples of ietf-yang-library data provided. Run them with:  
```bash
cd demo/yang-validation
yanglint EXAMPLE_FILE_PATH ../../yang_augment_RFC8525/ietf-yang-library@2019-01-04.yang ../../yang_augment_RFC8525/ietf-yang-library-augmentedby@2023-10-27.yang
```
Expected Output:
* example_valid_no_augment.xml: no(success) 
* example_valid: no(success) 
* example_invalid: 
```
libyang err : Invalid leafref value "module2" - no target instance "../../yanglib:module/yanglib:name" with the same value. (Data location "/ietf-yang-library:yang-library/module-set[name='ms1']/module[name='module1']/ietf-yang-library-augmentedby:augmented-by[2]".)
YANGLINT[E]: Failed to parse input data file "example_invalid.xml".
```

In the invalid example, there is one module ```module2``` defined in module-set ``ms2`` and is augmenting the ``module1`` in module-set ``ms1``. It cannot be found on ``ms1`` so the validation fails.

