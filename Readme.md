# Augmentation to ietf-yang-library

This repo contains the draft for the next version of
[draft-lincla-netconf-yang-library-augmentation](https://datatracker.ietf.org/doc/draft-lincla-netconf-yang-library-augmentation/)


## Modifying the draft

### Quick way

Modify the .xml corresponding to the current version. Make sure to 
commit the corresponding .txt so that diff with current version is correct.

### Automated way (Preferred if YANG modules are modified)

#### Dependencies

 * python3
 * make
 * xml2rfc
 * rfcdiff
 * pip

#### Modifying and building

The text of the draft can be modified in [builder/draft-lincla-netconf-yang-library-augmentation-00.xml](builder/draft-lincla-netconf-yang-library-augmentation-00.xml)

The YANG modules are in the [yang_??] directory.

Use `make` to build the .xml and .txt of the draft.






