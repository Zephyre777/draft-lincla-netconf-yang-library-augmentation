# Augmentation to ietf-yang-library

This repo contains the draft for the next version of
[draft-lincla-netconf-yang-library-augmentedby](https://datatracker.ietf.org/doc/draft-lincla-netconf-yang-library-augmentedby/)

## Diff between the current working draft and latest ietf version

RUN ```rfcdiff [CURRENT VERSION] [PREVIOUS VERSION]```  

The .html file will be generated under the main directory.

## Modifying the draft

### Quick way

The text of the draft can be modified in [builder/draft-lincla-netconf-yang-library-augmentedby.xml](builder/draft-lincla-netconf-yang-library-augmentedby.xml)

Before generating a new draft version, user can go to [/builder/build_yanglib_augment_draft.py](/builder/build_yanglib_augment_draft.py) end of Line 79 to change the version identifier. (e.g. draft-lincla-netconf-yang-library-augmentedby-<strong>00</strong> => draft-lincla-netconf-yang-library-augmentedby-<strong>01</strong>) 

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

The YANG modules are in the [yang_augment_RFC7895](./yang_augment_RFC7895/) and the [yang_augment_RFC85435](./yang_augment_RFC8525/) directories, each containining a set of modules that augment different version of ietf-yang-library.

## Docker image instruction
### build docker image
```
./build_docker_image.sh
```

### Manually configuration for netopeer2
```
cd netopeer2/scripts

export NP2_MODULE_DIR=/usr/share/yang/modules/netopeer2
export NP2_MODULE_PERMS=600
export LN2_MODULE_DIR=/usr/share/yang/modules/libnetconf2/

./setup.sh
./merge_hostkey.sh
./merge_config.sh
```

### Run netopeer2 docker container  
```
docker run -dit --name [your_container_name] -p [port_from_your_machine]:830 -it netopeer2_ietf120
```

### Configure password for the docker container
```
docker exec -itu 0 [your_container_name] pass_wd
```  
Then type in your new password, which is later going to be used as the netopeer2-cli ssh connection password. 

### Run netopeer2-server
```
netopeer2-server
```

### RUN netopeer2-cli
```
netopeer2-cli

> connect
```
Type in the password you set to connect as the root user for n





