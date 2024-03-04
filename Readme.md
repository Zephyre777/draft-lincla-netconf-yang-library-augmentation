# Augmentation to ietf-yang-library

This repo contains the draft for the next version of
[draft-lincla-netconf-yang-library-augmentation](https://datatracker.ietf.org/doc/draft-lincla-netconf-yang-library-augmentation/)

## Diff between the current working draft and latest ietf version

RUN ```rfcdiff [CURRENT VERSION] [PREVIOUS VERSION]```  

The .html file will be generated under the main directory.

## Modifying the draft

### Quick way

The text of the draft can be modified in [builder/draft-lincla-netconf-yang-library-augmentation.xml](builder/draft-lincla-netconf-yang-library-augmentation.xml)

For the current draft version that the user is working on, execute the ```make``` to generate .xml and .txt file for the draft.
Modify the .xml corresponding to the current version. Make sure to 
commit the corresponding .txt so that diff with current version is correct.

### Automated way (Preferred if YANG modules are modified)

#### Dependencies

 * python3
 * pyang
 * make
 * xml2rfc
 * iddiff
 * pip

The YANG modules are in the [yang_augment_RFC7895] and the [yang_augment_RFC85435] directories, each contains one set of modules that augment different version of ietf-yang-library.






