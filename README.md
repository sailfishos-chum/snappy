# pkg-snappy
RPM packaging of snappy for Sailfish

To get the sources, run download.sh

To build and install:

```
export SFARCH=armv7hl
cd snappy-1.1.3
mb2 -t SailfishOS-$SFARCH -s ../rpm/snappy.spec build
sb2 -t SailfishOS-$SFARCH -m sdk-install -R rpm -Uvh ../../rpms/devel/snappy-devel*$SFARCH.rpm
```

